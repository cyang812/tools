# 1.Read ecd(xml) file line by line
# 2.If this line contains facility code, verify it.
# 3.If this line contains error code, parse the facility code and offset, then verify facility code, if good, generate new code and replace the original one.
# 4.ErroCode = ((facilityCode | 0X8000)<<16) + Offset
# Note: For ecd file, a know issue is, you have to update the facility code by yourself.

import argparse
import os, sys
import re

ec_flag="<ErrorCode>"
fc_flag="<Facility>"

def args_parse():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--ecf_path", required=True,
        help="path to error code file, .ecd or .xml")
    ap.add_argument("-of", "--old_facility", required=True,
        help="old facility code")
    ap.add_argument("-nf", "--new_facility", required=True,
        help="new facility code")
    args = vars(ap.parse_args())
    return args


def GenerateErrorCode(facility, offset):
    return ((facility | 0X8000)<<16) + offset

def ParseErrorCode(errorCode):
    facility = (errorCode&0x7FFF0000)>>16;
    offset = errorCode&0x0000FFFF;
    return facility,offset

def VerifyFacilityCode(newFacility, oldFacility):
    if newFacility!=oldFacility:
        raise Exception("Facility code:"+str(newFacility)+" is wrong, expected:"+str(oldFacility))

def UpdateFacilityCodeLine(line, oldFacility, newFacility):
    print("Updating facility code line:"+line, end="")
    matchObj = re.search("(\d{5})", line)
    if matchObj:
        facilityCode = matchObj.group(1)
        VerifyFacilityCode(int(facilityCode),oldFacility)
        line = line.replace(facilityCode, str(newFacility))
    else:
        raise Exception("No facility code was found!")
    return line

def UpdateErrorCodeLine(line, oldFacility, newFacility):
    print("Updating error code line:"+line, end="")
    matchObj = re.search("(\d{10})", line)
    if matchObj:
        oldEC = matchObj.group(1)
        facility, offset =ParseErrorCode(int(oldEC))
        VerifyFacilityCode(facility,oldFacility)
        newEC = GenerateErrorCode(newFacility,offset)
        line = line.replace(oldEC, str(newEC))
    else:
        raise Exception("No error code was found!")
    return line

def UpdateErrorCodes(ecfPath, oldFacility, newFacility):
    file_data = ""
    with open(ecfPath, "r", encoding="utf-8") as f:
        for line in f:
            if ec_flag in line:
                line = UpdateErrorCodeLine(line, oldFacility, newFacility)
            elif fc_flag in line:
                line = UpdateFacilityCodeLine(line, oldFacility, newFacility)
            file_data +=line
    with open(ecfPath, "w", encoding="utf-8") as f:
        f.write(file_data)

#Example: python ErrorCodeUpdate.py --ecf_path "E:\Repos\TS-Zaca\Audio\src\Audio.Activities\AudioAnalysisTest.ErrorsAndMeasurements.ecd" --old_facility 25619 --new_facility 27149
if __name__=='__main__':
    args = args_parse()
    # Load parameters...
    oldFacilityCode = int(args["old_facility"])
    newFacilityCode = int(args["new_facility"])
    errorCodeFilePath = args["ecf_path"]
    print("oldFacilityCode:"+str(oldFacilityCode)+"; newFacilityCode："+str(newFacilityCode) + "; path="+errorCodeFilePath)
    try:
        UpdateErrorCodes(errorCodeFilePath, oldFacilityCode, newFacilityCode)
        print("Sucess! And pleae remember to manually update facility code!!")
    except Exception as err:
        print(err)

