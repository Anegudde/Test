#
# payroll_steve_jeff.py
# Report payrates for two employees across multiple spreadsheets
#
import win32com.client as win32
import glob
import os

xlfiles = sorted(glob.glob("*.xls"))
print "Reading %d files..."%len(xlfiles)

steve = []
jeff = []
cwd = os.getcwd()
excel = win32.gencache.EnsureDispatch('Excel.Application')
for xlfile in xlfiles:
    wb = excel.Workbooks.Open(cwd+"\\"+xlfile)
    ws = wb.Sheets('PAYROLL')
    xldata = ws.UsedRange.Value
    names = [r[1] for r in xldata]
    if u'SMITHFIELD, STEVE' in names:
        indx = names.index(u'SMITHFIELD, STEVE')
        steve.append(xldata[indx][4])
    else:
        steve.append(0)

    if u'JOHNSON, JEFF' in names:
        indx = names.index(u'JOHNSON, JEFF')
        jeff.append(xldata[indx][4])
    else:
        jeff.append(0)
    wb.Close()


print "File,Jeff,Steve"
for i in range(len(xlfiles)):
    print "%s,%0.2f,%0.2f"%(xlfiles[i],jeff[i],steve[i])
excel.Application.Quit()