import argparse
import os, sys
import subprocess

def args_parse():
    # construct the argument parse and parse the arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-p", "--ecf_path", required=True,
        help="path to error code file, .ecd or .xml")
    args = vars(ap.parse_args())
    return args

def deleteFile(filePath, postfix):
    for folderName, subFolders, fileNames in os.walk(filePath):
        for fileName in fileNames:
            if fileName.endswith(postfix):
                filePath = os.path.join(folderName, fileName)
                print("Deleting file:" + filePath)
                os.remove(filePath)

def findNameSpace(errorCodeFileName):
    nameSpace = ''
    # print("findNameSpace:"+errorCodeFileName)
    fileName = errorCodeFileName.replace("ErrorsAndMeasurements.ecd.","")
    with open(fileName, "r", encoding="utf-8") as f:
        for line in f:
            if 'namespace' in line:
                nameSpace = line.split(' ')[1].strip()
                # print("findNameSpace:"+nameSpace)
    if nameSpace == '':
        raise Exception("No namespace was found!")
    return nameSpace

def GenerateErrorCode(filePath, nameSpace):
    # print("GenerateErrorCode:"+str(facility)+","+str(offset))
    powershell = "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe"
    tool = 'errorCodeGenerator.exe'
    parameter = "/filename " + filePath + " /namespace " + nameSpace
    cmd = powershell + ", " + tool + ", " + parameter
    print("cmd:"+cmd)
    subprocess.run([powershell, tool, parameter])
    return

#Example: python .\ErrorCodeGenerator_batch.py -p "C:\MTE\project\Gaviota\TS-HuntingtonBeach"
if __name__=='__main__':
    args = args_parse()
    # Load parameters...
    errorCodeFilePath = args["ecf_path"]
    print("path="+errorCodeFilePath)

    facilityCnt = 0
    for folderName, subFolders, fileNames in os.walk(errorCodeFilePath):
        for fileName in fileNames:
            if fileName.endswith(".ecd.cs"):
                facilityCnt += 1
                filePath = os.path.join(folderName, fileName)
                # print("Updating error code file:" + filePath)
                nameSpace = findNameSpace(filePath)
                GenerateErrorCode(filePath.replace(".cs",""), nameSpace)

    deleteFile(errorCodeFilePath, '.ecd.h')

    print("Total facility code:"+str(facilityCnt))


