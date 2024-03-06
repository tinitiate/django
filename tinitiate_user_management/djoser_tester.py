import requests
from requests.auth import HTTPBasicAuth

# Your API endpoint
login_url = "http://127.0.0.1:8000/accounts/token/login"

# Your credentials
data = {
    "username": "admin",
    "password": "Test!2345678"
}

# First, make a request to get the token using basic authentication
response = requests.post(login_url, data=data)
print(str(response.json() ))
# Check if the request was successful
if response.status_code == 200:
    # Extract the token from the response
    token = response.json().get('auth_token')
    
    print("Token",token)
    
    # Use the token in subsequent requests
    headers = {'Authorization': f'Token {token}'}
    url = "http://127.0.0.1:8000/securecontent/securedata"
    response = requests.get(url, headers=headers)

    # Process the response
    print(response.json())
else:
    print("Failed to authenticate")
