*** Settings ***
Library    Collections
Library    DateTime
Library    OperatingSystem
Library    String
Library    ${CURDIR}/../../libraries/rebook_backend.py
Variables  ${CURDIR}/variables.py
Resource   keywords/rebook_checks.resource

*** Keywords ***
Disable Warnings
    No Operation

GET RATAN TOKEN
    [Arguments]    ${token_ops_maker}=    ${token_ops_checker}=
    No Operation

Reset Backend State
    Reset Backend State Impl