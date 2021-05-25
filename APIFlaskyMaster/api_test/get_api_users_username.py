import requests
from requests.auth import HTTPBasicAuth
from requests.structures import CaseInsensitiveDict
from Common_Functions import *
import json


#Get token for particular users
response = requests.get('http://127.0.0.1:8080/api/auth/token', auth=HTTPBasicAuth('Urmila123', 'Urmi@123'))
token=response.json()['token']
print("My token is:"+ token)                                       # Print Token

#Check Token is getting or not and Print token "True" or "False"
tokencheck=response_token_check(token)
print(tokencheck)                                                  # "True"


# Get Usersname
url = "http://127.0.0.1:8080/api/users"
headers = CaseInsensitiveDict()
resp = requests.get(url, headers=headers)
json_response=resp.json()
username = (json_response['payload'][1])                                     #Get Username


#Add username is URL for next request
URL1=url +"/"+username

#Get response data and Print for particular user
headers = {'Content-Type': 'application/json','token': token}
realgetrequest = requests.get(URL1, headers=headers)
Actualvalue= json.loads(realgetrequest.text)
print(Actualvalue)                                                          # Print Actual Value


#Check Users Data matched or not
Expectedvalue = {'message': 'retrieval succesful', 'payload': {'firstname': 'Urmila', 'lastname': 'Vadi', 'phone': '408329191'}, 'status': 'SUCCESS'}
checkdatavalue=get_data_is_check(Expectedvalue,Actualvalue)
print(checkdatavalue)                                                       # True

