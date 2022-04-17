import pickle

dealDictionary = {'zxc':123, 'asd':234}

def writeDictToFile(dict, fileName):
    with open(fileName, 'wb') as dictFile:
        print('save dict to file')
        pickle.dump(dict, dictFile)

def loadDictFromFile(fileName):
    with open(fileName, 'rb') as dictFile:
        dict = pickle.load(dictFile)
        return dict


if __name__ == '__main__':
    #writeDictToFile(dealDictionary, 'dealDictFile')
    dealDict = loadDictFromFile('dealDictFile')
    print(dealDict)
    print(len(dealDict))
    print(dealDict.get('zxc'))