*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resources1.robot
Suite Setup  Open my Browser
Suite Teardown  Close Browser


*** Test Cases ***
Login Test Case
    Input User name  ${User}                            #Enter User name
    Input Password  ${Password}                         #Enter Password
    Click Login Button
    UserInformation page should be visible
    Click Logout link
