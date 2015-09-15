import unittest
import pytest

class TestStringMethods(unittest.TestCase):
    
    @classmethod
    def setup_class(cls):
        """ setup any state specific to the execution of the given class (which
        usually contains tests).
        """
        print "SetupClass"

    @classmethod
    def teardown_class(cls):
        pass
        print "TearDownClass"
        """ teardown any state that was previously setup with a call to
        setup_class.
        """


    def setup_method(self, method):
        print "SetupMethod"
        pass
        """ setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """


    def teardown_method(self, method):
        """ teardown any state that was previously setup with a setup_method
        call.
        """
        print "TearDownMethod"
        assertEqual(1,1)
    
    def setup_function(function):
        print "SetupFunction"
        pass
        """ setup any state tied to the execution of the given function.
        Invoked for every test function in the module.
        """


    def teardown_function(function):
        """ teardown any state that was previously setup with a setup_function
        call.
        """
        print "TearDownFunction"
        pass
    
if __name__ == '__main__':
    #unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(TestStringMethods)
    unittest.TextTestRunner(verbosity=2).run(suite)
