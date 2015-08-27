import unittest
from UnitTest_Demo import SearchTest1
from UnitTest_Demo2 import SearchTest2
import os
import HtmlTestRun


def main():
    search_tests1 = unittest.TestLoader().loadTestsFromTestCase(SearchTest1)
    search_tests2 = unittest.TestLoader().loadTestsFromTestCase(SearchTest1)
    ## Put them in the Array
    smoke_tests = unittest.TestSuite([search_tests1, search_tests2])
    ## File
    dir = os.getcwd()
    outfile = open(dir + "\SmokeTestReport.html", "w")
    runner = HtmlTestRun.HTMLTestRunner(stream = outfile,title = 'Selenium Test',
                                        description = 'Smoke Tests')
    runner.run(smoke_tests)


if __name__ == "__main__":
    main()