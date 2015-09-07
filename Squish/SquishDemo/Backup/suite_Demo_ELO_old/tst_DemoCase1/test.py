#(**************************tst_DemoCase1**********************************************************************)
#Script Name
#tst_DemoCase1
#Description
#First demo script - ELO with user action

#Author
#Input Parameters : The inputs values will be imported from the .tsv file
#Output Parameters : The output values will be exported to the xml/HTML file.
#Created Date : 09/25/2014
#(*****************************************************************************************************************)
def main():
#try:
        # Call the common functions to be used for this script
    source(findFile("scripts","CommonFunctions.py"))
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
        if object.exists(":Q2_HomePage_General Electric My Application_HTML_Object"):
            test.passes("Application hooked successfully")
        else:
            test.fail("Application not hooked. Check it manually")
            
        #Scenario 1  
        #Page Validation ---------------------------------------Start    
        click_link(":Q2_HomePage_NavigationTab_Dashboard_HTML_Object") 
        Tabvalue = findObject(":Q2_Dashboard_Text").innerText
        if Tabvalue == "Dashboard":
            test.passes(Tabvalue+" page validation successfull")
        else:
            test.fail(Tabvalue+" page validation failed")
            
        click_link(":Q2_HomePage_NavigationTab_Patient List_HTML_Object") 
        Tabvalue = findObject(":Patient List_HTML_Object").innerText
        if "Patient List" in Tabvalue:
            test.passes(Tabvalue+" page validation successfull")
        else:
            test.fail(Tabvalue+" page validation failed")
            
        click_link(":Q2_HomePage_NavigationTab_Patient Detail_HTML_Object") 
        Tabvalue = findObject(":Patient Detail Patient Overview Post Care Analytics Comments_HTML_Object").innerText
        if "Patient Detail" in Tabvalue:
            test.passes("Patient Detail Page validation success")
        else:
            test.fail(Tabvalue+" Page validation failed")                
    
        snooze(5.0)
        #Page Validation ---------------------------------------End    
        
        #Scenario 2
        
        #Patient List - Filter-----------------------------------Start
        click_link(":Q2_HomePage_NavigationTab_Patient List_HTML_Object") 
    
        select_dropdown(":select-zone_select-one", argument["PatientList_Filter_Zone"])
        select_dropdown(":select-site_select-one", argument["PatientList_Filter_Site"])
        select_dropdown(":select-measure_select-one", argument["PatientList_Filter_Measure"])
        select_dropdown(":select-fulfillment-zone_select-one", argument["PatientList_Filter_Fulfillment"])
        select_dropdown(":select-practice_select-one", argument["PatientList_Filter_Practice"])
        checkbox(":show-discharged_checkbox", argument["Showme_dischargedpatients"])    
        
        text_edit(":_text", argument["PatientList_Filter_FindSearch"])
        nativeType("<space>")
        clickButton(":optionsRadios_radio")
       
        
        if object.exists("{container=':_SPAView' innerText='"+argument["PatientList_Filter_FindSearch"]+"' tagName='A' type='HTML_Object'}"):
            test.passes("Patient Detail Filter - Validation success")
        else:
            test.fail("Patient Detail Filter - Validation failed")
            
        snooze(5.0)
        #Scenario 3
        #Navigating to the Patient Detail page
        click_link(":Q2_HomePage_NavigationTab_Patient Detail_HTML_Object") 
        click_link(":Post Care_HTML_Object") 
        text_edit(":_text_2", argument["Post Op Check In"])
        select_dropdown(":_select-one", argument["Appointment_Time"])
        select_dropdown(":_select-one_2", argument["Appointment_Time AM/PM"])
        select_dropdown(":_select-one_3", argument["ImageFilter_Viewing1"])
        select_dropdown(":_select-one_3", argument["ImageFilter_Viewing2"])
        
        checkbox(":check1_checkbox", "Check")
        checkbox(":check2_checkbox", "Check")
        checkbox(":check3_checkbox", "Check")
    
        clickButton(waitForObject(":optionsRadios_radio_3"))
        push_button(":Vew Details_submit")
        
        test.passes("Demo Case Completed")
    
 
    
    
    
    
    
#except():
