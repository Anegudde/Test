import unittest
import datetime

from HtmlTestRun import HTMLTestRunner

from TestClassA import TestClassA
from TestClassB import TestClassB
from TestClassC import TestClassC


if __name__ == '__main__':   
    file_name = datetime.datetime.now().strftime("%Y_%m_%d_%H%M_HTML.html")
    output = open(file_name, "w")
    test_classes_to_run = [TestClassC, TestClassB, TestClassA]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)
    runner = HTMLTestRunner(stream = output, verbosity = 2, title="HTML Python Suite")
    runner.run(suite)