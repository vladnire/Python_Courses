@web @duckduckgo
Feature: DuckDuckGo Web Browsing
    As a web surfer,
    I want to find information online,
    So I can learn new things and get tasks done.


    Background:
        Given the DuckDuckGo home page is displayed


    Scenario: Basic DuckDuckGo Search
        When the user searches for "panda"
        Then results are shown for "panda"


    Scenario: Lengthy DuckDuckGo Search
        When the user searches for the phrase "declare the causes which impel them to the separation."
        Then one of the results contains "Declaration of Independence"
