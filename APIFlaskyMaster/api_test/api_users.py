import requests,json
from requests.structures import CaseInsensitiveDict
from Common_Functions import *

# Get API of api/users
url = "http://127.0.0.1:8080/api/users"
headers = CaseInsensitiveDict()

#Get request from API
resp = requests.get(url, headers=headers)


#Print Response code
respcode=print(resp.status_code)                     #200

#Check Response status code is '200' or not
respcodecheck=responce_check(resp.status_code)
print(respcodecheck)                                 #True

#Print Response of Payload for particular user
json_response=resp.json()
print(json_response)                                  #Payload response data

#Check status is "Success" or 'Failure'
Actualstatus= json_response['status']
result=status_check(Actualstatus)
print('Status check result:',result)                  #True

# Print For all Registered Users
Registered_user=json_response['payload']
print('My Payload is :',Registered_user)
for i in Registered_user:
    print("registered_user is:","'",i,"'")             # Print all Registered User















