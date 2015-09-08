Feature: Switch to window, pop up, frame, tab
  Scenario: Switch to window
    When I open seleniumframework website
    And I click open new browser window
    Then I switch to new window
    And back to parent window
 
  Scenario: Switch to JavaScript Alert
    When I open seleniumframework website
    And I click javascript alert window
    Then I print the text in javascript alert
 
  Scenario: Switch to browser tab
    When I open seleniumframework website
    And I click new browser tab
    Then I switch to new tab
    And back to main window
 
  Scenario: Switch to message window
    When I open seleniumframework website
    And I click new message window button
    Then I print text for message window
 
  Scenario: Switch to frame
    When I open yourhtmlsource website
    Then I switch to frame and print its text