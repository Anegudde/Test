def text_edit(fieldname,value):
    waitForObject(fieldname)
    if value!='':
        if object.exists(fieldname):
            type(fieldname,value)
            test.log("The "+value+" has been entered successfully")
            snooze(1.0)
            return("True")
        else:
            test.log("The field "+fieldname+" is not identified")
            return("False")   
        
def push_button(btn):
    waitForObject(btn)
    if object.exists(btn):
        clickButton(btn)
        test.log("The "+btn+" has been identified and clicked successfully")
        snooze(1.0)
        return("True")
    else:
        test.log("The field "+btn+" is not identified")
        return("False")        


def click_link(mmubtn):
    waitForObject(mmubtn)
    if object.exists(mmubtn):
        clickLink(mmubtn)
        test.log("The "+mmubtn+" has been identified and clicked successfully")
        snooze(1.0)
        return("True")
    else:
        test.log("The field "+mmubtn+" is not identified")
        return("False")
        

def select_dropdown(fieldname,value):
    waitForObject(fieldname)
    if value!='':
        if object.exists(fieldname):
            selectOption(fieldname,value)
            test.log("The "+value+" has been selected successfully in the dropdown")
            snooze(1.0)
            return("True")
        else:
            test.log("The field "+fieldname+" is not identified")
            return("False")                
        
def checkbox(fieldname,value):
    waitForObject(fieldname)
    if object.exists(fieldname):
        if value == "Check":
            clickButton(fieldname)
            test.log("The" +fieldname+" has been checked successfully")
            snooze(1.0)
            return("True")
        else:
            test.log("The" +fieldname+" has been unchecked as per the user request")
    else:
        test.log("The field "+fieldname+" is not identified")
        return("False")                

        
     