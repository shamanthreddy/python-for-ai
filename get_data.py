import requests
from datetime import datetime, timedelta
import pandas as pd
import matplotlib.pyplot as plt
import os

def get_7day_weather(latitude, longitude):
    # Calculate dates
    today = datetime.now()
    week_ago = today - timedelta(days = 7)

    # format dates for API (YYYY-MM-DD)
    start_date = week_ago.strftime("%Y-%m-%d")
    end_date = today.strftime("%Y-%m-%d")

    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

    response = requests.get(url)
    data = response.json()
    return data

paris_daily_data = get_7day_weather(48.85, 2.35)["daily"]

def make_data_frame(daily_data):

    df = pd.DataFrame({
        'date': daily_data['time'],
        'max_temp': daily_data['temperature_2m_max'],
        'min_temp': daily_data['temperature_2m_min']
    }) 

    # Convert date strings to datetime
    df['date'] = pd.to_datetime(df['date'])

    return df

paris_df = make_data_frame(paris_daily_data)

print(paris_df)

def visualize_data(df):

    # Create the plot
    plt.figure(figsize=(10, 6))
    plt.plot(df['date'], df['max_temp'], marker = 'o', label = 'Max Temp')
    plt.plot(df['date'], df['min_temp'], marker = 'o', label = 'Min Temp')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title('Weather - Past 7 Days')
    plt.legend()

    # Rotate x-axis labels for readability
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot
    plt.savefig('weather_chart.png')
    plt.show()
    pass

visualize_data(paris_df)

def save_to_csv(df):
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save to CSV
    df.to_csv('data/weather.csv', index = True)
    print("CSV saved to folder data")
    pass

save_to_csv(paris_df)

