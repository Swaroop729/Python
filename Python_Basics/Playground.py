from os import walk

f=[]
mypath='C:\\Users\\yella\\Desktop\\Python_code\\Python_Basics\\Automation'
for (dirpath,dirnames,filenames) in walk(mypath):
    f.extend(filenames)
    #f = [x for x in f if x.endswith(".xlsx")]
    f = [x for x in f if (".xls") in x]
print(f)
#print([ x for x in walk(mypath)])