# importing required modules
import PyPDF2
import csv
from itertools import islice
import pandas as pd
  
# creating a pdf file object
pdfFileObj = open('RAMPNOV2.pdf', 'rb')
with open('ramptocsv.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
  
    # creating a pdf reader object
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# printing number of pages in pdf file
    # print(pdfReader.numPages)
    # x = pdfReader.numPages
  
# creating a page object
    pageObj = pdfReader.getPage(0)
  
# extracting text from page
    # print(pageObj.extractText())
    for page_num in range(pdfReader.numPages):
        pdf_page = pdfReader.getPage(page_num)
        rowdata = pdf_page.extractText()
        writer.writerow([rowdata])


    

newlist = []
secondlist = []
with open('ramptocsv.csv', mode='r') as file:
    csvFile = csv.reader(file) 
    with open('ramptocsv2.csv', 'w', encoding='UTF8', newline='') as g:
        writerz = csv.writer(g)
        for lines in csvFile:
            x = ', '.join(lines)
            x.replace("\n","")
            writerz.writerow([x])

# df = pd.read_csv("ramptocsv2.csv")
# with open("my_markdown.md", 'w') as md:
#   df.to_markdown(buf=md, tablefmt="grid")       
    
        # x.replace("\n","")
    # print(x)
    # for i in lines:
    #     newlist.append(i)
    # print(newlist)

#     for i in newlist[0]:
#         secondlist.append(i)
# print(secondlist)
        
        
        # print(x)
    
    # newlist.append(x)
    # print(newlist)
    # writer.writerow([testData])
# closing the pdf file object
pdfFileObj.close()
f.close()