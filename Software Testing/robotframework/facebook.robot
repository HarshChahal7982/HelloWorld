*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${fName}    Donald
${sName}    Duck
${email}    abc@yahoo.com
${pass}    12345678

*** Test Cases ***
Facebook register
    Open Browser    https://www.facebook.com/r.php    Chrome
    Sleep    2s

    Maximize Browser Window

    Page Should Contain    Only allow essential cookies
    Click Element    xpath://button[@title='Only allow essential cookies']
    Page Should Contain    Create a new account

    Click Element    xpath://input[@name='firstname']
    Input Text    xpath/://input[@name='firstname']    ${fName}
    Textfield Should Contain    xpath://input{@name='firstname'}    ${fName}

     Click Element    xpath://input[@name='lastname']
    Input Text    xpath/://input[@name='lastname']    ${sName}
    Textfield Should Contain    xpath://input{@name='lastname'}    ${sName}

    

