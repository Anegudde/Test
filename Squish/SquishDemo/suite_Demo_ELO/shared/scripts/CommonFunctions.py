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
              
def CreateDict():
    dict = {}
    for row in testData.dataset('Y:\suite_Demo_ELO\shared\ObjectRepository.tsv'):
        dict[testData.field(row,"ObjectName")] = testData.field(row,"ObjectProperty")
    return(dict)
 
# def CreateDict():
#     START_ROW = 0
#     file_path = '/run/user/1000/gvfs/smb-share:server=3.204.38.30,share=elo-project/ObjectRepository.xls'
#     rb = xlrd.open_workbook(file_path)
#     r_sheet = rb.sheet_by_index(0) # read only copy to introspect the file
#     #wr = copy(rb)
#     #wb = (rb) # a writable copy (I can't read values out of this, only write to it)
#     #w_sheet = wr.get_sheet(0) # the sheet to write to within the writable copy
#     dict = {}
#     for row_index in range(START_ROW, r_sheet.nrows):
#         dict [r_sheet.cell(row_index, Objectname).value] = r_sheet.cell(row_index, ObjectProperty).value
#         test.log("check rows",r_sheet.cell(row_index, Objectname).value)
#     return(dict)