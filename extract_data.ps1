# Read CSV - skip metadata rows
# Skip first 5 rows which are metadata
$lines = @(Get-Content 'data/Cambium24_allScenarios_annual_gea.csv')
$csv = $lines | Select-Object -Skip 5 | ConvertFrom-Csv -ErrorAction SilentlyContinue

if ($csv -eq $null) {
    Write-Host 'Failed to import CSV'
    exit 1
}

# Group by scenario, region, year and create JSON
$data = @{}
$count = 0

foreach ($row in $csv) {
    # Skip empty rows and rows with missing data
    if ([string]::IsNullOrWhiteSpace($row.scenario)) { continue }
    if ($row.scenario -eq 'scenario') { continue }
    if ([string]::IsNullOrWhiteSpace($row.gea)) { continue }
    if ([string]::IsNullOrWhiteSpace($row.t)) { continue }
    
    $scenario = $row.scenario
    $region = $row.gea
    $year = $row.t
    
    # Convert MWh to TWh (divide by 1,000,000)
    $generation_twh = [float]$row.generation / 1000000
    
    # Sum renewable sources: distpv, geothermal, hydro, upv, wind-ons, wind-ofs, biomass
    $distpv = if ([string]::IsNullOrWhiteSpace($row.distpv_MWh)) { 0 } else { [float]$row.distpv_MWh }
    $geo = if ([string]::IsNullOrWhiteSpace($row.geothermal_MWh)) { 0 } else { [float]$row.geothermal_MWh }
    $hydro = if ([string]::IsNullOrWhiteSpace($row.hydro_MWh)) { 0 } else { [float]$row.hydro_MWh }
    $upv = if ([string]::IsNullOrWhiteSpace($row.upv_MWh)) { 0 } else { [float]$row.upv_MWh }
    $wind_ons = if ([string]::IsNullOrWhiteSpace($row.'wind-ons_MWh')) { 0 } else { [float]$row.'wind-ons_MWh' }
    $wind_ofs = if ([string]::IsNullOrWhiteSpace($row.'wind-ofs_MWh')) { 0 } else { [float]$row.'wind-ofs_MWh' }
    $biomass = if ([string]::IsNullOrWhiteSpace($row.biomass_MWh)) { 0 } else { [float]$row.biomass_MWh }
    
    $renewable_twh = ($distpv + $geo + $hydro + $upv + $wind_ons + $wind_ofs + $biomass) / 1000000
    
    # Fossil = Total - Renewable
    $fossil_twh = [math]::Max(0, $generation_twh - $renewable_twh)
    
    # Battery energy capacity (MWh) and curtailment
    $battery_cap_mwh = if ([string]::IsNullOrWhiteSpace($row.'battery_energy_cap_MWh')) { 0 } else { [float]$row.'battery_energy_cap_MWh' }
    $curtailment_mwh = if ([string]::IsNullOrWhiteSpace($row.curtailment_MWh)) { 0 } else { [float]$row.curtailment_MWh }
    $battery_cap_twh = $battery_cap_mwh / 1000000
    $curtailment_twh = $curtailment_mwh / 1000000
    
    # Build nested structure
    if (-not $data[$scenario]) { $data[$scenario] = @{} }
    if (-not $data[$scenario][$region]) { $data[$scenario][$region] = @{} }
    
    $data[$scenario][$region][$year] = @{
        year = [int]$year
        generation = [math]::Round($generation_twh, 4)
        renewable = [math]::Round($renewable_twh, 4)
        fossil = [math]::Round($fossil_twh, 4)
        battery = [math]::Round($battery_cap_twh, 4)
        curtailment = [math]::Round($curtailment_twh, 4)
    }
    
    $count++
}

Write-Host "Processed $count data rows"
Write-Host "Scenarios: $(($data.Keys | Measure-Object).Count)"

# Output as JSON
$json = $data | ConvertTo-Json -Depth 5
Write-Host "JSON length: $($json.Length) characters"

# Save to temp file
$json | Out-File -Encoding UTF8 'data/energy_data.json'
Write-Host "Saved to data/energy_data.json"
