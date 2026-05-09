#!/usr/bin/env python3
"""
Calectra Dashboard Data Processor
Extracts annual generation and LMC data for visualization
"""

import csv
import json
from pathlib import Path
from collections import defaultdict
import sys

# CSV File path
CSV_FILE = Path(__file__).parent / "data" / "Cambium24_allScenarios_annual_gea.csv"

# Renewable energy columns to sum
RENEWABLE_COLS = [
    'distpv_MWh', 'geothermal_MWh', 'hydro_MWh', 'upv_MWh',
    'wind-ons_MWh', 'wind-ofs_MWh', 'biomass_MWh'
]

# Other important columns
OTHER_COLS = ['battery_MWh', 'curtailment_MWh']

def read_csv_data():
    """Read and parse CSV file"""
    data = {
        'scenarios': set(),
        'regions': set(),
        'years': set(),
        'annual_data': defaultdict(dict),  # {(scenario, region, year): {...}}
    }
    
    with open(CSV_FILE, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            if not row or all(v is None or v == '' for v in row.values()):
                continue
            
            scenario = row['scenario']
            region = row['gea']
            year = int(row['t'])
            
            data['scenarios'].add(scenario)
            data['regions'].add(region)
            data['years'].add(year)
            
            # Extract generation and renewable values (MWh -> TWh conversion: /1M)
            gen_mwh = float(row.get('generation', 0) or 0)
            gen_twh = gen_mwh / 1_000_000
            
            # Calculate renewable total
            renewable_twh = 0
            for col in RENEWABLE_COLS:
                val = float(row.get(col, 0) or 0)
                renewable_twh += val / 1_000_000
            
            # Non-renewable = Total - Renewable
            non_renewable_twh = max(0, gen_twh - renewable_twh)
            
            # Extract battery and curtailment
            battery_twh = float(row.get('battery_MWh', 0) or 0) / 1_000_000
            curtailment_twh = float(row.get('curtailment_MWh', 0) or 0) / 1_000_000
            
            key = (scenario, region, year)
            data['annual_data'][key] = {
                'generation_twh': round(gen_twh, 4),
                'renewable_twh': round(renewable_twh, 4),
                'non_renewable_twh': round(non_renewable_twh, 4),
                'battery_twh': round(battery_twh, 4),
                'curtailment_twh': round(curtailment_twh, 4),
                # Store raw for verification
                'generation_mwh': int(gen_mwh),
            }
    
    # Convert sets to sorted lists
    data['scenarios'] = sorted(list(data['scenarios']))
    data['regions'] = sorted(list(data['regions']))
    data['years'] = sorted(list(data['years']))
    
    # Convert defaultdict to regular dict
    data['annual_data'] = {str(k): v for k, v in data['annual_data'].items()}
    
    return data

def verify_caiso_2050():
    """Verify the test case: CAISO, 2050, MidCase"""
    print("Verifying test case...")
    data = read_csv_data()
    
    key = "('MidCase', 'CAISO', 2050)"
    if key in data['annual_data']:
        value = data['annual_data'][key]
        mwh = value['generation_mwh']
        twh = value['generation_twh']
        print(f"✓ CAISO, 2050, MidCase: {mwh:,} MWh = {twh} TWh")
        if mwh == 591425000:
            print("✓ VERIFICATION PASSED")
            return True
        else:
            print(f"✗ Expected 591425000, got {mwh}")
            return False
    else:
        print(f"✗ Key not found: {key}")
        print(f"Available keys: {list(data['annual_data'].keys())[:5]}")
        return False

def export_json():
    """Export processed data as JSON"""
    print("Processing data...")
    data = read_csv_data()
    
    output = {
        'metadata': {
            'scenarios': data['scenarios'],
            'regions': data['regions'],
            'years': data['years'],
            'source': 'Cambium24_allScenarios_annual_gea.csv',
            'units': 'TWh (TerraWatt-hours)',
        },
        'annual_data': data['annual_data'],
    }
    
    # Save JSON
    output_path = Path(__file__).parent / "data" / "energy_data.json"
    with open(output_path, 'w') as f:
        json.dump(output, f, indent=2)
    
    print(f"✓ Exported to {output_path}")
    return output

if __name__ == '__main__':
    if not CSV_FILE.exists():
        print(f"Error: {CSV_FILE} not found")
        sys.exit(1)
    
    # Verify
    verify_caiso_2050()
    print()
    
    # Export
    export_json()
    
    print("\nData processing complete!")
