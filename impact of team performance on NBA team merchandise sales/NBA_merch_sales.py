import requests
import pandas as pd
from bs4 import BeautifulSoup

# Function to get merchandise sales data from RunRepeat (example URL)
def get_merchandise_sales():
    url = "https://runrepeat.com/nba-revenue-statistics"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting data from a table (adjust based on actual HTML structure)
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

# Function to get season performance data from Team Rankings
def get_season_performance():
    url = "https://www.teamrankings.com/nba/stat/win-pct-all-games"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting data from a table (adjust based on actual HTML structure)
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

# Function to get All-Stars data from JustAllStar.com
def get_all_stars():
    url = "https://www.justallstar.com/nba-all-star-game/player-lists/rosters/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting data from a table (adjust based on actual HTML structure)
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

# Function to get median state income data from U.S. Census Bureau
def get_median_state_income():
    url = "https://www.census.gov/data/tables/time-series/demo/income-poverty/historical-income-households.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting data from a table (adjust based on actual HTML structure)
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

# Function to get fan attendance data from ESPN
def get_fan_attendance():
    url = "http://www.espn.com/nba/attendance"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Example: Extracting data from a table (adjust based on actual HTML structure)
    table = soup.find('table')
    rows = table.find_all('tr')
    data = []
    for row in rows:
        cols = row.find_all('td')
        cols = [col.text.strip() for col in cols]
        data.append(cols)
    
    df = pd.DataFrame(data[1:], columns=data[0])
    return df

# Main function to gather all data
def main():
    merchandise_sales = get_merchandise_sales()
    season_performance = get_season_performance()
    all_stars = get_all_stars()
    median_state_income = get_median_state_income()
    fan_attendance = get_fan_attendance()
    
    # Save data to CSV files
    merchandise_sales.to_csv('merchandise_sales.csv', index=False)
    season_performance.to_csv('season_performance.csv', index=False)
    all_stars.to_csv('all_stars.csv', index=False)
    median_state_income.to_csv('median_state_income.csv', index=False)
    fan_attendance.to_csv('fan_attendance.csv', index=False)
    
    print("Data collection complete. Check the CSV files for the gathered data.")

if __name__ == "__main__":
    main()
