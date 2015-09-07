import sys 
from Mod_A import ModA
from Mod_B import ModB

def main():
        #startApplication("my_aut")
        #mymodule.click_button(":object_name")
        print ("In the Main")
        ModA.ModuleA(":Test")
        ModB.ModuleB_1(":Test2")
        ModB.ModuleB_2(":Test2")

if __name__ == "__main__":
        main()
