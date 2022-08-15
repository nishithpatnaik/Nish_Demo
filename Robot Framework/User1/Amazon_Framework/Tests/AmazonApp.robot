*** Settings ***
Documentation    This is AmazonApp.robot test file
Resource    ../Resources/AmazonApp_Keywords.robot   #Necessary for Setup & Teardown
Resource    ../Resources/Common_Keywords.robot      #Necessary for lower level keywords in testcases
#Runs at the beginning of Suite
Suite Setup    Common_Keywords.Begin Suite Setup
#Runs at the beginning of each TC
Test Setup      Common_Keywords.Begin Web Testing
#Runs at the end of each TC
Test Teardown    Common_Keywords.End Web Testing
#Runs at the end of Suite
Suite Teardown    Common_Keywords.Cleanup Testing Data

*** Variables ***
${URL} =  http://www.amazon.com
${BROWSER} =  Chrome
${SEARCH_ITEM} =  Ferrari 458

*** Test Cases ***
TC01 - Testcase name1 - Shopping @ Amazon
    [Documentation]    This is testcase documentation for TC01
    [Tags]    Smoke
    AmazonApp_Keywords.Search for Products on Amazon
    AmazonApp_Keywords.Validate Product from Search Results
    AmazonApp_Keywords.Open Product Details
    AmazonApp_Keywords.Add Product into Cart
    AmazonApp_Keywords.Begin Checkout


TC02 - Testcase name2 - Search For Product
    [Documentation]    This is testcase documentation for TC02
    [Tags]    Smoke
    AmazonApp_Keywords.Search for Products on Amazon