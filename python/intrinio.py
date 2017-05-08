# First install the required package via this CLI command:
# pip install requests

import requests

# Setup common variables

api_username = "YOUR_INTRINIO_API_USERNAME"
api_password = "YOUR_INTRINIO_API_PASSWORD"
base_url = "https://api.intrinio.com"

# Get the latest FY Income Statement for AAPL

ticker = "AAPL"
request_url = base_url + "/financials/standardized"
query_params = {
    'ticker': ticker,
    'statement': 'income_statement',
    'type': 'FY'
}

response = requests.get(request_url, params=query_params, auth=(api_username, api_password))
if response.status_code == 401: print("Unauthorized! Check your username and password."); exit()

data = response.json()['data']

for row in data:
    tag = row['tag']
    value = row['value']
    print(tag + ": " + str(value))
