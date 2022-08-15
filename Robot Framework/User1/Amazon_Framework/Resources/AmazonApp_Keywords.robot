*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/PageObjects/AmazonHome_PO.robot
Resource    ../Resources/PageObjects/SearchResults_PO.robot
Resource    ../Resources/PageObjects/ProductDetails_PO.robot
Resource    ../Resources/PageObjects/FinalCart_PO.robot


*** Keywords ***
Search for Products on Amazon
    AmazonHome_PO.Open Homepage
    AmazonHome_PO.Validate Homepage
    AmazonHome_PO.Search Item
    AmazonHome_PO.Click Search Button

Validate Product from Search Results
    SearchResults_PO.Validate Search Results

Open Product Details
    SearchResults_PO.Select Product
    ProductDetails_PO.Load Product Details

Add Product into Cart
    ProductDetails_PO.Click Add to Cart Button
    ProductDetails_PO.Validate Cart

Begin Checkout
    FinalCart_PO.Checkout

