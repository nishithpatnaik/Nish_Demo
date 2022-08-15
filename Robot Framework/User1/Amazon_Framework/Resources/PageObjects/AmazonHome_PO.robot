*** Settings ***
Library    SeleniumLibrary

*** Keywords ***

Open Homepage
    go to   ${URL}
    maximize browser window

Validate Homepage
    wait until page contains    Hello    timeout=3
    wait until page contains    Select your address     timeout=3

Search Item
    input text    id=twotabsearchtextbox    ${SEARCH_ITEM}

Click Search Button
    click button    id=nav-search-submit-button