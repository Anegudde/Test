def main():
    startApplication("Q2")
    source(findFile("scripts","Y:\suite_Demo_ELO\shared\scripts\CommonFunctions.py"))
    dict1 = CreateDict()
    snooze(5)
    click_link(dict1["Lnk_AnalysisPage"])
    clickButton(dict1["Button_Filter"])
    click_link(dict1["Lnk_Filter 001_Button_Filter"])
    click_link(dict1["Lnk_Filter 002_Button_Filter"])
    select_dropdown(dict1["Combobox_End Date"],"4 weeks ago")
    clickButton(dict1["Button_File"])
    click_link(dict1["Lnk_Save as PDF_Button_File"])
    select_dropdown(dict1["Combobox_TableSize"],"100")
    select_dropdown(dict1["Combobox_TableSize"],"10")
    select_dropdown(dict1["Combobox_End Date"],"6 weeks ago")
    
    
    
    
    