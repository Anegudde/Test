def main():
    source(findFile("scripts",'/run/user/1000/gvfs/smb-share:server=3.204.38.30,share=elo-project/suite_Demo_ELO/shared/scripts/CommonFunctions.py'))
    dict1 = CreateDict()
    snooze(1)
  #  value = ObjName("Lnk_PatientDetail")
    value = dict1["Lnk_PatientDetail"]
    test.log("here is the value", value)
    snooze(10)