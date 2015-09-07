import sys
import os
# Include folder with "mymodule.py" in Python's search path:
sys.path.append("D:\Work\Git\Squish\Squish\IncludeModules\MyModule.py")
import MyModule
import imported
'''
sys.path.append( ".\root" )
from .root import MyModule3
sys.path.append( ".\root\test" )
from .test import MyModule2
'''
'''


Config3file = '~/root/MyModule3.py'
Config2file = '~/root/test/MyModule2.py'
sys.path.append(os.path.dirname(os.path.expanduser(Config2file)))
sys.path.append(os.path.dirname(os.path.expanduser(Config3file)))
import MyModule3
import MyModule2
'''
imported.import_file('D:/Work/Git/Squish/Squish/IncludeModules/root/MyModule3.py')
imported.import_file('D:/Work/Git/Squish/Squish/IncludeModules/root/test/MyModule2.py')

def main():
        #startApplication("my_aut")
        #mymodule.click_button(":object_name")
        print ("In the Main")
        MyModule.Module_click_button(":Test")        
        MyModule3.Module_TestModule3(":Test")
        MyModule2.Module_TestModule2(":Test")
        

if __name__ == "__main__":
        main()
