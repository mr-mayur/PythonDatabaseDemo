import xlrd as read
import xlwt as write
import os


class ExcelOperations :

    filePath ='E:\Python class\\userInfo.xls'
    listOfLines = []
    readExcelDataList=[]

    def getDataFromFile(self):
        file = open('E:\Python class\\sampl.txt')
        for line in file.readlines():
            ExcelOperations.listOfLines.append(line.strip())

    def writeIntoExcel(self):
        workBook = write.Workbook()
        userInfoSheet = workBook.add_sheet('UserInfo')
        count = 0
        cols = []
        for item in ExcelOperations.listOfLines:
            for words in item.split(','):
                cols.append(words)

        for num in range(ExcelOperations.listOfLines.__len__()):
            row = userInfoSheet.row(num)
            for item in range(3):
                row.write(item,cols.__getitem__(count))
                count+=1

        workBook.save(ExcelOperations.filePath)


    def readDataFromExcel(self):
        workbook = read.open_workbook(ExcelOperations.filePath)
        userinfosheet = workbook.sheet_by_name("UserInfo")

        for rindex in range(0,userinfosheet.nrows):
            for cindex in range(0,userinfosheet.ncols):
                ExcelOperations.readExcelDataList.append(userinfosheet.cell(rindex,cindex).value)




if __name__ == '__main__':
    ob = ExcelOperations()

    ob.getDataFromFile()
    print(ExcelOperations.listOfLines)

    ob.writeIntoExcel()

    print('read data from  excel')
    ob.readDataFromExcel()
    print(ExcelOperations.readExcelDataList)