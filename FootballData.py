import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context # Ignore SSL certificate errors

def get_data(url):
    team_name = url.split('/')[-1].replace('-Stats', '')
    df = pd.read_html(url, match="Round")[0]  # Automatically selects the first table that contains 'Round'
    df['Team'] = team_name
    df = df[['Date', 'Round', 'Venue', 'Opponent', 'Result', 'GF', 'xG', 'GA', 'xGA', 'Formation', 'Referee']]
    df = df[df['Round'].str.contains('Matchweek', na=False)].dropna()
    print(f"Data fetched successfully for {team_name}")
    return df, team_name  # Return both the DataFrame and the team name

urls = [
    'https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats',
    'https://fbref.com/en/squads/19538871/Manchester-United-Stats'
]

# Fetch data for each URL
for url in urls:
    data, team_name = get_data(url) 
    # Save each team's data to a separate CSV file
    data.to_excel(f"./Programming/Snippets/{team_name}.xlsx", index=False)