import requests
BASE_URL = "https://www.cheapshark.com/api/1.0"
import certifi
import time

def mainApicall():
    while(1):
        print(f"\n 1. Display the top Game details\n 2. Search for a game \n 3. Logout\n ")
        n = input("Enter your response: ")
        if n=='1':
            print(f"\n Here are the details of some product listed : ")
            deals = get_deals()
            if deals:
                for deal in deals[:5]:
                    time.sleep(2)
                    deal_link = deal.get('dealLink', 'No deal link available')
                    print(f" \n --------------------\n Title: {deal['title']},\n Price: {deal['salePrice']}, \n Original: {deal['normalPrice']}, \n Savings: {deal['savings']}%, \n Website-Link: {deal_link}\n")
        elif n=='2':
            game_name = input("Enter the game name you want to search for: ")
            if game_name.strip():  # Check if the input is not empty
                print(f"\n Searching for deals on '{game_name}'... \n")
                deals = get_gamedeals(game_name)
                if deals:
                    for deal in deals[:5]:
                        time.sleep(2)  # Simulate delay for better readability
                        deal_link = deal.get('dealLink', 'No deal link available')
                        print(f" \n --------------------\n Title: {deal['title']},\n Price: {deal['salePrice']},\n Original Price: {deal['normalPrice']},\n Savings: {deal['savings']}%,\n Website-Link: {deal_link}\n")
                else:
                    print(f"No deals found for the game '{game_name}'.")
            else:
                print("Game name cannot be empty.")
 
        else:
            return


def get_gamedeals(game_name):
    session = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # The API endpoint
    endpoint = f"{BASE_URL}/deals"
    
    params = {
        "title":game_name,
        "storeID": 1,         
        "upperPrice": 15,
        "sortBy": "Deal Rating" 
    }
    
    try:
        response = session.get(endpoint, params=params, headers=headers,verify=certifi.where())
        
        # Check if the response is successful
        if response.status_code == 200:
            deals = response.json()
            return deals
        else:
            print(f"HTTP Error: {response.status_code}")
            return None
    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL Error: {ssl_error}")
        return None
    except requests.exceptions.RequestException as req_error:
        print(f"Request Error: {req_error}")
        return None




def get_deals():
    session = requests.Session()
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    # The API endpoint
    endpoint = f"{BASE_URL}/deals"
    
    params = {
        "storeID": 1,         
        "upperPrice": 15,
        "sortBy": "Deal Rating" 
    }
    
    try:
        response = session.get(endpoint, params=params, headers=headers,verify=certifi.where())
        
        # Check if the response is successful
        if response.status_code == 200:
            deals = response.json()
            return deals
        else:
            print(f"HTTP Error: {response.status_code}")
            return None
    except requests.exceptions.SSLError as ssl_error:
        print(f"SSL Error: {ssl_error}")
        return None
    except requests.exceptions.RequestException as req_error:
        print(f"Request Error: {req_error}")
        return None

