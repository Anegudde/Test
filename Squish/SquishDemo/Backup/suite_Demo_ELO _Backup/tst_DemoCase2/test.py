#(**************************tst_DemoCase1**********************************************************************)
#Script Name
#tst_DemoCase1
#Description
#First demo script - ELO with user action

#Author
#Input Parameters : The inputs values will be imported from the .tsv file
#Output Parameters : The output values will be exported to the xml/HTML file.
#Created Date : 09/25/2014
#Modified Date : 10/08/2014
#Accessing the objects via tsv file instead of object map
#(*****************************************************************************************************************)
def main():
#try:
        # Call the common functions to be used for this script
    #source(findFile("scripts","CommonFunctions.py"))
    source(findFile("scripts","Y:\suite_Demo_ELO\shared\scripts\CommonFunctions.py"))
    dict1 = CreateDict()
    
    # End of calling Library Functions
    
    # Variable Declaration---------------------------------Start
    count = 0
    for row in testData.dataset("firstscript_data.tsv"):
        count=count+1
        if count==0:
            test.log("No Test data is found. Please check")
        argument={}
        argument["Execute"]=testData.field(row, "Execute?")
        argument["PatientList_Filter_Zone"]=testData.field(row, "PatientList_Filter_Zone")
        argument["PatientList_Filter_Site"]=testData.field(row, "PatientList_Filter_Site")
        argument["PatientList_Filter_Measure"]=testData.field(row, "PatientList_Filter_Measure")
        argument["PatientList_Filter_Fulfillment"]=testData.field(row, "PatientList_Filter_Fulfillment")
        argument["PatientList_Filter_Practice"]=testData.field(row, "PatientList_Filter_Practice")
        argument["Showme_dischargedpatients"]=testData.field(row, "Showme_dischargedpatients")
        argument["PatientList_Filter_FindSearch"]=testData.field(row, "PatientList_Filter_FindSearch")
        argument["Post Op Check In"]=testData.field(row, "Post Op Check In")
        argument["Appointment_Time"]=testData.field(row, "Appointment_Time")
        argument["Appointment_Time AM/PM"]=testData.field(row, "Appointment_Time AM/PM")
        argument["ImageFilter_Viewing1"]=testData.field(row, "ImageFilter_Viewing1")
        argument["ImageFilter_Viewing2"]=testData.field(row, "ImageFilter_Viewing2")
        
        
        
            
    # Variable Declaration----------------------------------End
    
    # Application Hook--------------------------------------Start
    startApplication("Q2")
 
    snooze(5)
   
    if argument["Execute"] == "Yes":
        if object.exists(dict1["Q2_Homepage"]):
            test.passes("Application hooked successfully")
        else:
            test.fail("Application not hooked. Check it manually")
            
        #Scenario 1  
        #Page Validation ---------------------------------------Start    
        click_link(dict1["Q2_Tab_Dashboard"]) 
        Tabvalue = findObject(dict1["Q2_Text_Dashboard"]).innerText
        if Tabvalue == "Dashboard":
            test.passes(Tabvalue+" page validation successfull")
        else:
            test.fail(Tabvalue+" page validation failed")
            
        click_link(dict1["Q2_Tab_PatientList"]) 
        Tabvalue = findObject(dict1["Q2_Text_PatientList"]).innerText
        if "Patient List" in Tabvalue:
            test.passes(Tabvalue+" page validation successfull")
        else:
            test.fail(Tabvalue+" page validation failed")
            
        click_link(dict1["Q2_Tab_PatientDetail"]) 
        Tabvalue = findObject(dict1["Q2_Text_PatientDetail"]).innerText
        if "Patient Detail" in Tabvalue:
            test.passes("Patient Detail Page validation success")
        else:
            test.fail(Tabvalue+" Page validation failed")                
    
        snooze(5.0)
        #Page Validation ---------------------------------------End    
        
        #Scenario 2
        
        #Patient List - Filter-----------------------------------Start
        click_link(dict1["Q2_Tab_PatientList"]) 
    
        select_dropdown(dict1["Q2_PatientList_DropDown_Zone"], argument["PatientList_Filter_Zone"])
        select_dropdown(dict1["Q2_PatientList_DropDown_Site"], argument["PatientList_Filter_Site"])
        select_dropdown(dict1["Q2_PatientList_DropDown_Measure"], argument["PatientList_Filter_Measure"])
        select_dropdown(dict1["Q2_PatientList_DropDown_fulfillmentzone"], argument["PatientList_Filter_Fulfillment"])
        select_dropdown(dict1["Q2_PatientList_DropDown_Practice"], argument["PatientList_Filter_Practice"])
        checkbox(dict1["Q2_PatientList_Checkbox_Showdischarged"], argument["Showme_dischargedpatients"])    
        
        text_edit(dict1["Q2_PatientList_Text_Searchtext"], argument["PatientList_Filter_FindSearch"])
        nativeType("<space>")
        clickButton(dict1["Q2_PatientList_Radio_Option"])
       
        
        if object.exists("{container=':_SPAView' innerText='"+argument["PatientList_Filter_FindSearch"]+"' tagName='A' type='HTML_Object'}"):
            test.passes("Patient Detail Filter - Validation success")
        else:
            test.fail("Patient Detail Filter - Validation failed")
            
        snooze(5.0)
        #Scenario 3
        #Navigating to the Patient Detail page
        click_link(dict1["Q2_Tab_PatientDetail"]) 
        click_link(dict1["Q2_PatientDetail_Tab_PostCare"]) 
        text_edit(dict1["Q2_PatientDetail_PostCare_Text_PostOpCheckIn"], argument["Post Op Check In"])
        select_dropdown(dict1["Q2_PatientDetail_PostCare_DropDown_AppointmentTime"], argument["Appointment_Time"])
        select_dropdown(dict1["Q2_PatientDetail_PostCare_Dropdown_TimeAM/PM"], argument["Appointment_Time AM/PM"])
        select_dropdown(dict1["Q2_PatientDetail_PostCare_Dropdown_ImageFilterViewing1"], argument["ImageFilter_Viewing1"])
        
        checkbox(dict1["Q2_PatientDetail_PostCare_Checkbox_Check1"], "Check")
        checkbox(dict1["Q2_PatientDetail_PostCare_Checkbox_check2"], "Check")
        checkbox(dict1["Q2_PatientDetail_PostCare_Checkbox_Check3"], "Check")
    
        clickButton(waitForObject(dict1["Q2_PatientDetail_PostCare_Option_Radio3"]))
        push_button(dict1["Q2_PatientDetail_PostCare_Button_ViewSubmit"])
        
        test.passes("Demo Case Completed")
    
 
    
    
    
    
    
#except():
