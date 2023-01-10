# 1.Read ecd(xml) file line by line
# 2.If this line contains facility code, verify it.
# 3.If this line contains error code, parse the facility code and offset, then verify facility code, if good, generate new code and replace the original one.
# 4.ErroCode = ((facilityCode | 0X8000)<<16) + Offset

import argparse
import os, sys
import re

ec_flag="<ErrorCode>"
fc_flag="<Value>"

def args_parse():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--ecf_path", required=True,
        help="path to error code file, .ecd or .xml")
    ap.add_argument("-fo", "--facility_offset", required=True,
        help="new facility offset")
    args = vars(ap.parse_args())
    return args

def GenerateErrorCode(facility, offset):
    return ((facility | 0X8000)<<16) + offset

def ParseErrorCode(errorCode):
    facility = (errorCode&0x7FFF0000)>>16;
    offset = errorCode&0x0000FFFF;
    return facility, offset

def VerifyFacilityCode(newFacility, oldFacility):
    if newFacility != oldFacility:
        raise Exception("Facility code:"+str(newFacility)+" is wrong, expected:"+str(oldFacility))

def UpdateFacilityCodeLine(line, facilityOffset):
    print("Updating facility code line:" + line, end = "")
    matchObj = re.search("(\d{5})", line)
    if matchObj:
        facilityCode = matchObj.group(1)
        # VerifyFacilityCode(int(facilityCode),oldFacility)
        line = line.replace(facilityCode, str(int(facilityCode) + facilityOffset))
        oldFacility = int(facilityCode)
    else:
        raise Exception("No facility code was found!")
    return line, oldFacility

def UpdateErrorCodeLine(line, oldFacility, facilityOffset):
    print("Updating error code line:"+line, end="")
    matchObj = re.search("(\d{10})", line)
    if matchObj:
        oldEC = matchObj.group(1)
        facility, offset = ParseErrorCode(int(oldEC))
        VerifyFacilityCode(facility, oldFacility)
        newFacility = facility + facilityOffset
        newEC = GenerateErrorCode(newFacility, offset)
        line = line.replace(oldEC, str(newEC))
    else:
        raise Exception("No error code was found!")
    return line

def UpdateErrorCodes(ecfPath, facilityOffset):
    oldFacility = 0
    findFacility = False
    file_data = ""
    with open(ecfPath, "r", encoding="utf-8") as f:
        for line in f:
            if ec_flag in line:
                line = UpdateErrorCodeLine(line, oldFacility, facilityOffset)
            elif fc_flag in line and not findFacility:
                line, oldFacility = UpdateFacilityCodeLine(line, facilityOffset)
                findFacility = True
                if oldFacility == 0:
                    raise Exception("No facility code was found!")
            file_data +=line
    with open(ecfPath, "w", encoding="utf-8") as f:
        f.write(file_data)

#Example: python .\ErrorCodeUpdate_batch.py -p "C:\MTE\project\Gaviota\TS-HuntingtonBeach" -fo 2432
if __name__=='__main__':
    args = args_parse()
    # Load parameters...
    errorCodeFilePath = args["ecf_path"]
    facilityOffset = int(args["facility_offset"])
    print("facilityOffset"+str(facilityOffset) + "; path="+errorCodeFilePath)

    facilityCnt = 0
    for folderName, subFolders, fileNames in os.walk(errorCodeFilePath):
        for fileName in fileNames:
            if fileName.endswith(".ecd"):
                facilityCnt += 1
                filePath = os.path.join(folderName, fileName)
                print("Updating error code file:"+filePath)
                UpdateErrorCodes(filePath, facilityOffset)

    print("Total facility code:"+str(facilityCnt))


