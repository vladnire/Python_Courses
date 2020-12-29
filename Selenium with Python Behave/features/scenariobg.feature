Feature: OrangeHRM Login

    Background: common steps
        Given I launch browser
        When I open application
        And Enter valid username "admin" and password "admin123"
        And Click on login

    Scenario: Login to HRM Application
        Then User must successfully login

    Scenario: Search user
        When Navigate to my info page
        Then My info page should display correct name

    Scenario: Advanced Search user
        When Navigate to Buzz page
        Then Check Buzz page
