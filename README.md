# Calectra Dashboard - US Grid Structural Shift Visualization

## Project Overview
Interactive dashboard visualizing the structural shift of the US power grid (2025–2050) using Energy Outlook data and hourly cost dynamics.

## Data Files Required

Place these files in the `data/` directory:

1. **Cambium24_allScenarios_annual_gea.csv**
   - Contains annual generation data by scenario and region
   - Required columns: generation, distpv_MWh, geothermal_MWh, hydro_MWh, upv_MWh, wind-ons_MWh, wind-ofs_MWh, biomass_MWh, battery_MWh, curtailment_MWh
   - Years: 2025-2050

2. **Cambium Workbook24.xlsx**
   - Tab: 'Levelized Cost' (Rows 55-342)
   - Contains 24-hour LMC data with monthly filtering

## Verification Checklist

Before development begins:
- [ ] CAISO, 2050, Mid-case = 591,425,000 MWH
- [ ] 8 scenarios confirmed
- [ ] 18 GEA regions confirmed
- [ ] 7 renewable energy columns verified

## Dashboard Features

### Energy Mix Bar Chart
- Grouped/stacked bar visualization
- Total Generation vs Renewable vs Fossil Fuels/Other
- Years: 2025-2050 (adjustable range)
- Filters: Scenario, Region, Metrics

### Trend Indicators
- Battery storage (MWh → TWh)
- Curtailment (MWh → TWh)

### Hourly Cost Dynamics
- 24-hour LMC line chart
- $20/MWh Gas Benchmark reference
- Monthly filtering

## Tech Stack
- React
- Tailwind CSS
- Recharts
- Single standalone index.html export

## Next Steps
1. Upload data files to `data/` directory
2. Run verification against provided metrics
3. Build interactive components
4. Export as standalone HTML
