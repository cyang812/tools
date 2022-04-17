from typing import Mapping
import xlrd,xlsxwriter

#待合并excel
path = "C:/Users/youngchen/Desktop/New folder/1/total/"
allxls = ["1.xlsx","2.xlsx","3.xlsx","4.xlsx","5.xlsx","6.xlsx","7.xlsx"]        

#目标excel
end_xls = "C:/temp/yj/aaa.xlsx"

def open_xls(file):
    try:
        fh = xlrd.open_workbook(file)
        return fh
    except Exception as e:
        print("打开文件错误："+e)

#根据excel名以及第几个标签信息就可以得到具体标签的内容
def get_file_value(filename,sheetnum):
    rvalue = []
    fh = open_xls(filename)
    sheet = fh.sheets()[sheetnum]
    row_num = sheet.nrows
    for rownum in range(0,row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue

def get_file_value_1(filename,sheetnum):
    rvalue = []
    fh = open_xls(filename)
    sheet = fh.sheets()[sheetnum]
    row_num = sheet.nrows
    for rownum in range(1,row_num):
        rvalue.append(sheet.row_values(rownum))
    return rvalue

def write_sheet_value(sheet):
    #将列表all_sheet_value的内容写入目标excel
    num1 = -1
    for sheet1 in sheet:
        print("how many times")
        # insert blank line
        end_xls_sheet.write(num1, -1, "sheet3")    
        num1 += 1
        for sheet2 in sheet1:
            num1 += 1
            num2 = -1
            for sheet3 in sheet2:
                num2 += 1
                print(num1,num2)
                #在第num1行的第num2列写入sheet3的内容
                end_xls_sheet.write(num1, num2, sheet3)    

if __name__=="__main__":

    #获取第一个excel的sheet个数以及名字作为标准
    inFileName = path + allxls[0]
    print(inFileName)
    first_file_fh = open_xls(inFileName)
    first_file_sheet = first_file_fh.sheets()
    first_file_sheet_num = len(first_file_sheet)
    
    #定义目标excel    
    # all_sheet_value.append([])    
    outFileName = end_xls
    print(outFileName)
    endxls = xlsxwriter.Workbook(outFileName)
    all_sheet_value = []    
    sheet_name = []    
    
    # make 10 sheet    
    for sheetname in first_file_sheet:
        sheet_name.append(sheetname.name)
        
    #把所有内容都放到列表all_sheet_value中
    for sheet_num in range(0, first_file_sheet_num):
        
        for i, file_name in enumerate(allxls):
            print("正在读取" + file_name + "的第" + str(sheet_num + 1)+"个标签...")        
            file_value = get_file_value(path + file_name, sheet_num)
            all_sheet_value.append(file_value)                        
                
        #print(all_sheet_value)
        print("Done, write to a file", outFileName)
        
        end_xls_sheet=endxls.add_worksheet(sheet_name[sheet_num])
        write_sheet_value(all_sheet_value)
        all_sheet_value = []
        
        '''
        num = -1
        #将列表all_sheet_value的内容写入目标excel
        sheet_index = -1
        for sheet in all_sheet_value:
            sheet_index += 1
            print("wrting sheet,", sheet_index)
            end_xls_sheet=endxls.add_worksheet(sheet_name[sheet_index])
            
            num += 1
            num1 = -1
            for sheet1 in sheet:
                for sheet2 in sheet1:
                    num1 += 1
                    num2 = -1
                    for sheet3 in sheet2:
                        num2 += 1
                        #print(num,num1,num2,sheet3)
                        #在第num1行的第num2列写入sheet3的内容
                        end_xls_sheet.write(num1,num2,sheet3)    
        '''
        
    endxls.close()
    