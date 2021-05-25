import requests, json
from requests.auth import HTTPBasicAuth
from Common_Functions import *


# Basic get api/auth
response = requests.get('http://127.0.0.1:8080/api/auth/token', auth=HTTPBasicAuth('Urmila123', 'Urmi@123'))


#Print Json Response
json_response = response.json()
print(json_response)                                        #status & token


# Print Response status code
responsescode = response.status_code
print(responsescode)                                         #200


# Check Response code is "200" or not
responsecheck=responce_check(responsescode)
print(responsecheck)                                           #True


#Check Response Staus 'Success' or 'Failure'
responsestatus= status_check(json_response['status'])
print(responsestatus)                                           # True
print(json_response['status'])                                  #Success


# Check Response Token is getting or not
responsetoken =response_token_check(json_response['token'])
print(responsetoken)                                              #True


# Print User token
json_status = print(json_response['token'])                       #token




