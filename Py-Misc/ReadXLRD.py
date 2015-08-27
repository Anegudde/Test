import xlrd, xlwt
DEBUG=1
PRINT=1
book = xlrd.open_workbook("data.xls") #open our xls file, there's lots of extra default options in this call, for logging etc. take a look at the docs
 
sheet = book.sheets()[0] #book.sheets() returns a list of sheet objects... alternatively...
#sheet = book.sheet_by_name("Input") #we can pull by name
#sheet = book.sheet_by_index(0) #or by the index it has in excel's sheet collection
 
r = sheet.row(0) #returns all the CELLS of row 0,
c = sheet.col_values(0) #returns all the VALUES of row 0,
 
data = [] #make a data store
for i in xrange(sheet.nrows):
    print (sheet.row_values(i))
    data.append(sheet.row_values(i)) 


if (DEBUG):
    print list(data)
    
if (PRINT):
    book = xlwt.Workbook()   
    style = xlwt.XFStyle()
    #style.num_format_str = '0.00E+00' 
    sheet = book.add_sheet("Sheet Name") 
    sheet = book.sheet_by_index(0)
#     for i in range(len(data[0])):
#         for item in len(data):            
#             sheet.write(i, item,item[i])
    for values in (array(data)):
        sheet.writerow(values)
    book.save("New.xls")    

