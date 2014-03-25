Feature: Home page
    Scenario: Visit the home page
        Given I am an anonymous user
        And I visit the home page
        Then I should see the welcome text
