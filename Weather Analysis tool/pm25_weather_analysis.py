
# Corrected PM2.5 and Weather Analysis Code
# This version handles real API response structures and includes error handling

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import requests
import json
from datetime import datetime, timedelta
import numpy as np

def fetch_air_quality_data(city="paris"):
    """
    Fetch air quality data from WAQI API (World Air Quality Index)
    This API is free and doesn't require registration
    """
    print(f"Fetching air quality data for {city}...")

    # WAQI API endpoint
    url = f"https://api.waqi.info/feed/{city}/?token=demo"

    try:
        resp = requests.get(url)
        if resp.status_code == 200:
            data = resp.json()
            if data.get('status') == 'ok':
                return data.get('data', {})
            else:
                print(f"API Error: {data.get('message', 'Unknown error')}")
                return None
        else:
            print(f"HTTP Error: {resp.status_code}")
            return None
    except Exception as e:
        print(f"Request failed: {e}")
        return None

def create_sample_dataset(n_days=365):
    """
    Create a sample dataset for demonstration purposes
    This simulates the structure of real air quality and weather data
    """
    print("Creating sample dataset for analysis demonstration...")

    # Generate date range
    end_date = datetime.now()
    start_date = end_date - timedelta(days=n_days)
    dates = pd.date_range(start_date, end_date, freq='D')

    # Set random seed for reproducibility
    np.random.seed(42)

    # Generate realistic synthetic data
    n_samples = len(dates)

    # PM2.5 values with seasonal variation
    base_pm25 = 25 + 10 * np.sin(2 * np.pi * np.arange(n_samples) / 365)
    pm25 = base_pm25 + np.random.normal(0, 8, n_samples)
    pm25 = np.clip(pm25, 5, 80)

    # Temperature with seasonal variation
    base_temp = 12 + 15 * np.sin(2 * np.pi * np.arange(n_samples) / 365)
    temperature = base_temp + np.random.normal(0, 5, n_samples)

    # Humidity with some correlation to temperature
    humidity = 70 - 0.5 * temperature + np.random.normal(0, 10, n_samples)
    humidity = np.clip(humidity, 30, 95)

    # Wind speed with seasonal variation
    wind_speed = 3 + 2 * np.sin(2 * np.pi * np.arange(n_samples) / 365 + np.pi/4)
    wind_speed = wind_speed + np.random.exponential(1, n_samples)
    wind_speed = np.clip(wind_speed, 0.5, 12)

    # Create DataFrame
    df = pd.DataFrame({
        'date': dates,
        'pm25': pm25,
        'temperature': temperature,
        'humidity': humidity,
        'wind_speed': wind_speed
    })

    return df

def analyze_air_quality_weather(df):
    """
    Perform analysis on air quality and weather data
    """
    print("Performing air quality and weather analysis...")

    # Calculate correlations
    correlation_cols = ['pm25', 'temperature', 'humidity', 'wind_speed']
    correlation = df[correlation_cols].corr()

    # Monthly averages
    df['month'] = df['date'].dt.month
    monthly_pm25 = df.groupby('month')['pm25'].mean()

    return correlation, monthly_pm25

def create_visualizations(df, correlation, monthly_pm25):
    """
    Create visualizations for the analysis
    """
    print("Creating visualizations...")

    # Set up the plotting style
    plt.style.use('default')
    sns.set_palette("husl")

    # Create figure with subplots
    fig = plt.figure(figsize=(15, 12))

    # 1. Scatter plots: PM2.5 vs weather variables
    plt.subplot(2, 3, 1)
    sns.scatterplot(data=df, x='temperature', y='pm25', alpha=0.6)
    plt.title('PM2.5 vs Temperature')
    plt.xlabel('Temperature (Â°C)')
    plt.ylabel('PM2.5 (Âµg/mÂ³)')

    plt.subplot(2, 3, 2)
    sns.scatterplot(data=df, x='humidity', y='pm25', alpha=0.6)
    plt.title('PM2.5 vs Humidity')
    plt.xlabel('Humidity (%)')
    plt.ylabel('PM2.5 (Âµg/mÂ³)')

    plt.subplot(2, 3, 3)
    sns.scatterplot(data=df, x='wind_speed', y='pm25', alpha=0.6)
    plt.title('PM2.5 vs Wind Speed')
    plt.xlabel('Wind Speed (m/s)')
    plt.ylabel('PM2.5 (Âµg/mÂ³)')

    # 2. Correlation heatmap
    plt.subplot(2, 3, 4)
    sns.heatmap(correlation, annot=True, cmap='RdBu_r', center=0, 
                square=True, fmt='.2f')
    plt.title('Correlation Matrix')

    # 3. Time series plot: Monthly average PM2.5
    plt.subplot(2, 3, 5)
    plt.plot(monthly_pm25.index, monthly_pm25.values, marker='o', linewidth=2)
    plt.title('Monthly Average PM2.5')
    plt.xlabel('Month')
    plt.ylabel('Mean PM2.5 (Âµg/mÂ³)')
    plt.xticks(range(1, 13))
    plt.grid(True, alpha=0.3)

    # 4. Time series of PM2.5 over time
    plt.subplot(2, 3, 6)
    plt.plot(df['date'], df['pm25'], alpha=0.7, linewidth=0.8)
    plt.title('PM2.5 Time Series')
    plt.xlabel('Date')
    plt.ylabel('PM2.5 (Âµg/mÂ³)')
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    return fig

def main():
    """
    Main function to run the analysis
    """
    print("Air Quality and Weather Analysis")
    print("=" * 50)

    # Try to fetch real data first
    real_data = fetch_air_quality_data("paris")

    if real_data:
        print("Successfully fetched real-time data!")
        print(f"Station: {real_data.get('city', {}).get('name', 'Unknown')}")
        print(f"Current AQI: {real_data.get('aqi', 'N/A')}")

        # For real-time data, we would need to collect historical data
        # For this demonstration, we'll use sample data
        print("\nNote: For historical analysis, using sample dataset...")

    # Create sample dataset for analysis
    df = create_sample_dataset(365)
    print(f"\nDataset created with {len(df)} daily observations")
    print(f"Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")

    # Perform analysis
    correlation, monthly_pm25 = analyze_air_quality_weather(df)

    # Create visualizations
    fig = create_visualizations(df, correlation, monthly_pm25)

    # Print findings
    print("\nAnalysis Results:")
    print("=" * 30)
    corr_pm25 = correlation['pm25']
    print(f"Correlation between PM2.5 and Temperature: {corr_pm25['temperature']:.3f}")
    print(f"Correlation between PM2.5 and Humidity: {corr_pm25['humidity']:.3f}")
    print(f"Correlation between PM2.5 and Wind Speed: {corr_pm25['wind_speed']:.3f}")
    print(f"\nMonth with highest average PM2.5: {monthly_pm25.idxmax()} ({monthly_pm25.max():.1f} Âµg/mÂ³)")
    print(f"Month with lowest average PM2.5: {monthly_pm25.idxmin()} ({monthly_pm25.min():.1f} Âµg/mÂ³)")

    # Save results to CSV
    df.to_csv('air_quality_analysis.csv', index=False)
    print(f"\nResults saved to 'air_quality_analysis.csv'")

    return df, correlation, monthly_pm25

# Run the analysis
if __name__ == "__main__":
    df_results, corr_results, monthly_results = main()