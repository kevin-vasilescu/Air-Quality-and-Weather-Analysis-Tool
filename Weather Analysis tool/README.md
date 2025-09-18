# 🌬️ Air Quality Analysis Project

A Python tool that analyzes PM2.5 air pollution and its relationship with weather conditions.

## ✨ Features
- Real-time air quality data from WAQI API
- Weather correlation analysis  
- Beautiful data visualizations
- CSV export functionality
- Comprehensive error handling

## 🚀 Quick Start

### Install Dependencies
pip install -r requirements.txt
### Run the Analysis
python corrected_pm25_analysis.py

## 📊 What It Does
- Fetches live air quality data for any city
- Analyzes relationships between PM2.5 and weather variables
- Creates correlation charts and time series plots
- Saves results to CSV file

## 📈 Sample Output
The tool generates:
- Scatter plots showing PM2.5 vs temperature, humidity, wind speed
- Correlation heatmap between all variables
- Monthly average PM2.5 trends
- Time series analysis

## 🛠️ Built With
- **Python** 🐍 - Main programming language
- **Pandas** - Data analysis and manipulation
- **Matplotlib & Seaborn** - Data visualization
- **WAQI API** - Real-time air quality data
- **NumPy** - Numerical computations

## 📁 Project Files
- `corrected_pm25_analysis.py` - Main analysis script
- `air_quality_analysis.csv` - Generated dataset  
- `requirements.txt` - Python dependencies
- `README.md` - This documentation

## 🌍 API Information
Uses the free WAQI (World Air Quality Index) API which provides:
- Real-time air quality data worldwide
- No registration required
- Multiple pollutant measurements
- City-based queries

## 🔧 Customization
You can modify the analysis by:
- Changing the city in `fetch_air_quality_data("your_city")`
- Adjusting date ranges in `create_sample_dataset()`
- Adding new visualization types
- Including additional weather variables

## 📊 Understanding Results
**Correlation Values:**
- Close to +1: Strong positive relationship
- Close to -1: Strong negative relationship  
- Close to 0: No relationship

**Typical Findings:**
- Higher temperatures often correlate with higher pollution
- Wind speed usually reduces pollution (negative correlation)
- Humidity effects vary by location and season

## 🚨 Error Handling
The code handles:
- API connection failures
- Missing data columns
- Invalid data formats
- Network timeouts

## 🤝 Contributing
Feel free to fork this project and submit pull requests for improvements!

## 📄 License
This project is open source and available under the MIT License.

---
*Created for environmental data analysis and air quality monitoring*
