*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Load Product Details
    wait until page contains element    id=breadcrumb-back-link

Click Add to Cart Button
    click button    id=add-to-cart-button
    sleep    3s
    click button    xpath=//*[@id="attachSiAddCoverage"]/span/input
    sleep    3s

Validate Cart
    wait until page contains    Added to Cart