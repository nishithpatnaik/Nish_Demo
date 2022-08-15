*** Settings ***
Library    SeleniumLibrary


*** Keywords ***
Validate Search Results
    wait until page contains    results for "${SEARCH_ITEM}"

Select Product
    [Documentation]    For this test we are selecting the first item on the Search Results
    click link    css=#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.sg-row > div.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span:nth-child(4) > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(3) > div > div > div > div > div > div > div.a-section.a-spacing-small.puis-padding-left-small.puis-padding-right-small > div.a-section.a-spacing-none.a-spacing-top-small.s-title-instructions-style > h2 > a
    #click link    Ferrari Remote Control Cars - 1:24 BEZGAR Officially Licensed RC Series, Electric Sport Racing Toy Car Model Vehicle, 2.4Ghz RC Car for Kids, Adults, Girls and Boys Holiday Ideas Gift (71900 Red)