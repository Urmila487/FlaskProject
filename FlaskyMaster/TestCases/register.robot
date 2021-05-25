*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resources1.robot
Suite Setup  Open my Browser
Suite Teardown  Close Browser

*** Test Cases ***
Register Test case
    Open Register page                      #Click Register link
    Input User name  ${User}                #Enter User name
    Input Password  ${Password}             #Enter Password
    Input Firstname  ${Firstname}           #Enter First name
    Input Lastname  ${Lastname}             #Enter Last name
    Input Phonenumber  ${Phonenumber}       #Enter Phone name
    Click Register Button













