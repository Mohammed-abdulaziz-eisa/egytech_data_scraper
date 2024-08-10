import requests
import pandas as pd

API_URL = 'https://api.egytech.fyi/participants'

def fetch_data(api_url):
    """Fetch data from the API."""
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an error for bad status codes
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parse_data(json_data):
    """Parse JSON data to extract participants."""
    try:
        return json_data['results']
    except KeyError as e:
        print(f"Error parsing data: {e}")
        return []

def create_dataframe(data):
    """Create a pandas DataFrame from the parsed data."""
    return pd.DataFrame(data)

def style_dataframe(df):
    """Apply styling to the DataFrame for better readability."""
    styled_df = df.style.set_properties(**{'text-align': 'left'})
    styled_df = styled_df.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    return styled_df

def save_to_csv(df, filepath):
    """Save the DataFrame to a CSV file."""
    try:
        df.to_csv(filepath, index=False)
        print(f"Data saved to {filepath}")
    except Exception as e:
        print(f"Error saving data to CSV: {e}")

def main():
    json_data = fetch_data(API_URL)
    if json_data:
        participants_data = parse_data(json_data)
        df = create_dataframe(participants_data)
        styled_df = style_dataframe(df)
        #display(styled_df)
        # Uncomment the line below to save the DataFrame to a CSV file
        save_to_csv(df, '../data/raw/v0.2/EgyTech_participants_10-8-2024_v0.2.csv')

if __name__ == "__main__":
    main()