*** Settings ***
Library  SeleniumLibrary

*** Variables ***
${LOGIN URL}    http://127.0.0.1:8080/login
${BROWSER}      Chrome
${User}  Urmila1234567
${Password}  Urmi@123
${Firstname}  Urmila
${Lastname}  Vadi
${Phonenumber}  408329191

*** Keywords ***
Open my Browser
    open browser  ${LOGIN URL}  ${BROWSER}
    maximize browser window

Close Browser
    close all browsers

Open Register page
    click link  Register

Input User name

    [Arguments]  ${username}
    element should be visible   username
    input text  name:username  ${username}

Input Password

    [Arguments]  ${password}
    element should be visible   password
    input text  name:password  ${password}

Input Firstname

    [Arguments]  ${firstname}
    element should be visible   firstname
    input text  name:firstname  ${firstname}

Input Lastname

    [Arguments]  ${lastname}
    element should be visible   lastname
    input text  name:lastname  ${lastname}

Input Phonenumber

    [Arguments]  ${phonenumber}
    element should be visible   phone
    input text  name:phone  ${phonenumber}

Click Register Button
    click element  xpath://input[@value='Register']

Login page should be visible
    wait until page contains  Log In - Demo App

If User is new Register
    Login page should be visible

If user is already Register error
   page should contain  User ${User} is already registered.
   Open Login page

Open Login page
    go to  ${LOGIN URL}

Click Login Button
    click element  xpath://input[@value='Log In']

Click Logout link
    click link  Log Out

UserInformation page should be visible
    wait until page contains    User Information - Demo App

User name should be visible
    element text should be  //td[normalize-space()='Username']  Username
    ${response}    Get Text    xpath://td[@id='username']
    Should Be Equal As Strings    ${response}    ${User}

Firstname should be visible
    element text should be  //td[normalize-space()='First name']  First name
    ${response}    Get Text    xpath://td[@id='firstname']
    Should Be Equal As Strings    ${response}    ${Firstname}

Lastname should be visible
    element text should be  //td[normalize-space()='Last name']  Last name
    ${response}    Get Text    xpath=//td[@id='lastname']
    Should Be Equal As Strings    ${response}    ${Lastname}

Phone number should be visible
    element text should be  //td[normalize-space()='Phone number']  Phone number
    ${response}    Get Text    xpath=//td[@id='phone']
    Should Be Equal As Strings    ${response}    ${Phonenumber}