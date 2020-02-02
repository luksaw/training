*** Settings ***
Library  SeleniumLibrary

*** Keywords ***

Open login page
    [Arguments]  ${BROWSER}
    Open Browser  ${URL}  ${BROWSER}
    Maximize Browser Window

Input username
    [Arguments]  ${input}
    Input Text  ${USERNAME_INPUT}  ${input}

Input password
    [Arguments]  ${input}
    Input Text  ${PASSWORD_INPUT}  ${input}

Click login
    Wait Until Element is Visible  ${SUBMIT_BUTTON}
    Click Element  ${SUBMIT_BUTTON}

Login successful
    Wait Until Page Contains Element  ${HEADER_AFTER_LOGIN}

Login Error Message Is Displayed
    Wait Until Element is Visible  ${LOGIN_ERROR_MESSAGE}
