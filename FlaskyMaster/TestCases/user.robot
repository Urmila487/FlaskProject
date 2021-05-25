*** Settings ***
Library  SeleniumLibrary
Resource  ../Resources/Resources1.robot
Suite Setup  Open my Browser
Suite Teardown  Close Browser

*** Test Cases ***
UserInformation Test case

    Input User name  ${User}                    #Enter User name
    Input Password  ${Password}                 #Enter Password
    Click Login Button
    UserInformation page should be visible
    User name should be visible
    Firstname should be visible
    Lastname should be visible
    Phone number should be visible
    Click Logout link
