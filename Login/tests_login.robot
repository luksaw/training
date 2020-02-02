*** Settings ***
Library  SeleniumLibrary
Resource  Keywords/login_keywords.robot
Resource  Variables/login_variables.robot

Documentation  User can login to system X

Test Setup  Open Login Page  ${BROWSER}
Test Teardown  Close All Browsers

*** Test Cases ***
User can login with correct credentials
    Input Username  ${VALID_USERNAME}
    Input Password  ${VALID_PASSWORD}
    Click Login
    Login Successful

User cannot login with correct email and incorrect password
    Input Username  ${VALID_USERNAME}
    Input Password  ${INVALID_PASSWORD}
    Click Login
    Login Error Message Is Displayed

User cannot login with incorrect email and correct password
    Input Username  ${INVALID_USERNAME}
    Input Password  ${VALID_PASSWORD}
    Click Login
    Login Error Message Is Displayed

User cannot login with empty credentials
    Input Username  ${EMPTY}
    Input Password  ${EMPTY}
    Click Login
    Login Error Message Is Displayed

User can login simultaneously on different browsers
    Input Username  ${VALID_USERNAME}
    Input Password  ${VALID_PASSWORD}
    Click Login
    Login Successful
    Open Login Page  firefox
    Input Username  ${VALID_USERNAME}
    Input Password  ${VALID_PASSWORD}
    Click Login
    Login Successful



