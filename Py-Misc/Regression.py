from unittest import TestLoader, TestSuite
from HtmlTestRun import HTMLTestRunner
import datetime
import Test1
import Test2

list = {"testEqual","testNotEqual"}

class Regression():
    if __name__ == "__main__":
        file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_report.html")
        output = open(file_name, "w")
        loader = TestLoader()
        suite = TestSuite((loader.loadTestsFromTestCase(Test1)))
        #loader.loadTestsFromTestCase(Test2)))
        runner = HTMLTestRunner(stream = output, verbosity = 2, title="Regression Suite")
        runner.run(suite)
