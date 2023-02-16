*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Fill Out Web Form
    Open Browser  http://sampleapp.tricentis.com/101/app.php  chrome
    Wait Until Page Contains Element  id=make  timeout=10s
    Select From List by Value  id=make  Audi
    Input Text  id=engineperformance  200
    Input Text  id=dateofmanufacture  02/16/2023
    Select From List by Value  id=numberofseats  4
    Select From List by Value  id=fuel  Gas
    Input Text  id=listprice  40000
    Input Text  id=licenseplatenumber  ABC123
    Input Text  id=annualmileage  10000
    Click Button  css=button[id="nextenterinsurantdata"]
    Sleep    3s
    Close Browser