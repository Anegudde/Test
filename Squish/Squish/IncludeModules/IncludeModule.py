import sys 
# Include folder with "mymodule.py" in Python's search path:
sys.path.append("D:\Work\Git\Squish\Squish\IncludeModules\MyModule.py")
import MyModule

def main():
        #startApplication("my_aut")
        #mymodule.click_button(":object_name")
        print ("In the Main")
        MyModule.Module_click_button(":Test")

if __name__ == "__main__":
        main()
