*** Settings ***
Library    AAA
Library    BBB

*** Test Cases ***
Test AAA API
    [Documentation]    测试AAA接口
    
    ${response}=    AAA.aaa_aaa    character_id=123
    
    Log    Response内容: ${response}
    
    # 提取第一个pack的packId
    ${pack_id}=    Set Variable    ${response['packList'][0]['packId']}
    # 将packId设置为全局变量，并进行数字运算
    ${result}=    Evaluate    int(${pack_id}) + 401
    Set Suite Variable    ${PACK_ID}    ${result}
    Log To Console    提取的packId: ${PACK_ID}

Test BBB API
    [Documentation]    测试BBB接口
    
    # 第二个用例引用第一个用例的PACK_ID
    ${response}=    BBB.bbb_bbb    PACK_ID=${PACK_ID}
    
    Log    Response内容: ${response}
