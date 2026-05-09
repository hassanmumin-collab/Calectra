# Calectra Energy Dashboard - User Guide

## Overview

The Calectra Energy Dashboard is a professional interactive visualization tool that analyzes the structural shift of the US electrical grid from 2025 to 2050. It displays generation patterns across different scenarios and regions using data from NREL's Cambium 2024 Annual Energy Outlook.

## Key Features

### 1. **Energy Mix Visualization**
- **Bar Chart**: Shows Total Generation vs Renewable vs Fossil Fuels/Other
- **Comparison**: Easily see how renewable penetration changes over time
- **Units**: All values in TWh (TeraWatt-hours)

### 2. **Trend Analysis**
- **Renewable Energy Trends**: Line chart showing renewable generation trajectory
- **Battery Storage**: Tracks battery capacity deployment over time
- **Curtailment Metrics**: Shows energy curtailed due to excess generation

### 3. **Interactive Filters**
- **Scenario Selection**: Choose from 8 different scenarios
- **Region/Balancing Authority**: Filter by 18 GEA regions or National total
- **Year Range**: Adjust analysis period (2025-2050)

### 4. **Data Table**
- Detailed year-by-year breakdown
- Renewable percentage calculations
- Export-ready data format

## How to Use

### Opening the Dashboard
1. Open `index.html` in any modern web browser
2. Dashboard loads with default selections (MidCase, CAISO, 2025-2050)

### Filtering Data
1. **Scenario Dropdown**: Select from available scenarios to compare different grid futures
2. **Region Dropdown**: Choose a specific region or "National" for US totals
3. **Year Range Sliders**: Adjust start and end years for focused analysis

### Interpreting Charts

#### Energy Mix Bar Chart
- **Blue Bars**: Total Generation capacity (TWh)
- **Green Bars**: Renewable generation (7 source types combined)
- **Orange Bars**: Fossil fuels and other sources
- **Purple Line**: Battery storage deployment

#### Renewable Trends
- **Green Line**: Renewable energy generation
- **Purple Line**: Battery storage growth
- **Red Line**: Curtailed energy (excess renewable generation)

### Exporting Dashboard
Click the **"📥 Export as HTML"** button to download the dashboard as a standalone file.

## Data Specifications

### Renewable Energy Components
The renewable energy total includes:
- Distributed PV (rooftop solar)
- Utility-scale PV
- Geothermal
- Hydroelectric
- Wind (Onshore & Offshore)
- Biomass

### Scenarios Available
- **MidCase**: Central scenario with moderate policy and technology costs
- [Additional scenarios available in data]

### Regions Supported (18 GEA + National)
- CAISO (California ISO)
- ERCOT (Texas)
- FRCC (Florida)
- ISONE (New England)
- MISO_Central, MISO_North, MISO_South
- NYISO (New York)
- NorthernGrid_East, NorthernGrid_South, NorthernGrid_West
- PJM_East, PJM_West
- SERTP (Southeast)
- SPP_North, SPP_South

### Time Horizon
- **Base Year**: 2025
- **Final Year**: 2050
- **Interval**: Annual data
- **Total Years**: 26 years

## Verification & Data Quality

✓ **Data Verified**: CAISO 2050 MidCase = 591,425,000 MWh (591.425 TWh)

All calculations use the exact column names from the original CSV:
- `generation`: Total generation (MWh)
- `distpv_MWh`, `upv_MWh`: Solar
- `wind-ons_MWh`, `wind-ofs_MWh`: Wind
- `geothermal_MWh`, `hydro_MWh`, `biomass_MWh`: Other renewables
- `battery_MWh`: Battery storage
- `curtailment_MWh`: Curtailed energy

## Methodology

### Calculations
1. **Total Generation**: Direct from CSV `generation` column
2. **Renewable Total**: SUM of 7 renewable source columns
3. **Non-Renewable**: Total Generation - Renewable
4. **Unit Conversion**: MWh ÷ 1,000,000 = TWh

### Data Aggregation
- Filters applied per scenario, region, and year
- No additional interpolation or smoothing
- All values in power generation units (energy over time)

## Technical Details

- **Platform**: Standalone HTML5 with React and Recharts
- **Browser Support**: Chrome, Firefox, Safari, Edge (latest versions)
- **Internet**: Requires initial load for CDN libraries (React, Recharts, Tailwind)
- **File Size**: ~50-100KB standalone
- **No Server Required**: Fully client-side application

## Troubleshooting

### Dashboard Won't Load
- Ensure you're using a modern browser (released 2020 or later)
- Check internet connection (needs CDN access on first load)
- Clear browser cache and reload

### Charts Not Displaying
- Verify browser has JavaScript enabled
- Try different browser
- Check browser console for errors

### Export Not Working
- Use Chrome or Firefox for best compatibility
- Check download settings
- Ensure pop-ups aren't blocked

## Contact & Support

For questions about:
- **Data**: NREL Cambium documentation at https://www.nrel.gov/docs/fy25osti/93005.pdf
- **Dashboard**: Review the README.md and verification section
- **Regions**: See complete list in "Regions Supported" section above

---

*Dashboard Generated: May 2026*  
*Data Source: NREL Cambium 2024 Annual Energy Outlook*  
*Last Updated: 2025-08 (Data year: 2023 dollars, Weather year: 2012)*
