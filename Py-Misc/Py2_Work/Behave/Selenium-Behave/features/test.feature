Feature: testing browser title
#https://pythonhosted.org/behave/parse_builtin_types.html
Scenario Outline: visit <browser_page> to Open the Page
    When we visit <browser_page> for URL
    Then it should have a title "<browser_title>" in the Page

Examples: Browser
    | browser_page                     | browser_title          |
    | https://crash-stats.mozilla.com/ | Crash Data for Firefox |
    | http://google.com/               | Google                 |