import requests
import datetime

def fetch_and_save():
    # Example: Fetching basic crypto data
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        price = data['bpi']['USD']['rate']
        timestamp = datetime.datetime.now().isoformat()
        
        # Append to file
        with open("data.txt", "a") as f:
            f.write(f"{timestamp} | BTC Price: {price}\n")
            
        print(f"Logged at {timestamp}")
        
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    fetch_and_save()
