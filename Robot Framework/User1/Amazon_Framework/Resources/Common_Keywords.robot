*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
#Runs before all of your testcases if called by Suite Setup
Begin Suite Setup
    Log     Suite Setup Begins-Runs at the beggining of Suite
    Insert Testing Data

Insert Testing Data
    log     This is Example of Keyword use inside Suite Setup

Begin Web Testing
    open browser    about:blank   ${BROWSER}

End Web Testing
    close browser
    log     End of Script

#Runs after all of your testcases if called by Suite Teardown
Cleanup Testing Data
    log     End Suite Setup - This runs at the end of Suite

