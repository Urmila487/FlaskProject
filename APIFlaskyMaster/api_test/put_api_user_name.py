import requests
from requests.auth import HTTPBasicAuth
from get_api_users_username import username
from Common_Functions import *

#Get token for particular users
response = requests.get('http://127.0.0.1:8080/api/auth/token', auth=HTTPBasicAuth( 'Urmila123', 'Urmi@123'))
token=response.json()['token']
url = "http://127.0.0.1:8080/api/users/"
headers = {'Content-Type': 'application/json','token': token}


# Update data for Put request
payload= {"firstname":"Urmila","lastname":"Vadi","phone":"40891"}

# Print put Response
response = requests.put(url+username,headers=headers,json=payload)
print(response.text)

#Check put Response status
putresponsestatuscheck=put_response_status_is_check(response)
print(putresponsestatuscheck)