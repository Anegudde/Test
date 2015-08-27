Feature: As a writer for NetTuts
  I wish to demonstrate
  How easy writing Acceptance Tests
  In Python really is.
 
  Background:
    Given I am using the calculator
 
  Scenario: Calculate 2 plus 2 on our calculator
    Given I input "2" add "2"
    Then I should see "4"