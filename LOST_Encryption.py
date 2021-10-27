import math
import time
import random

# BEGIN DEFINING FUNCTIONS FOR COLUMN TRANSPOSITION
def keyGenerator():
    key = []
    storageOfCipher = []
    while len(key) != 8:
        term = random.randint(0,9)
        if term not in key:
            key.append(term)
        if len(storageOfCipher) != 8:
            storageOfCipher.append([])
    key_storage = [key, storageOfCipher]
    return key_storage


def rearrangingKeys(oldIndex, storageOfCipher, sortedCipher):
    value = storageOfCipher[oldIndex]
    sortedCipher.extend(value)
    return sortedCipher


def RCTencryption(plainText):
    storageOfCipher, keys = keyGenerator()[1], keyGenerator()[0]
    for a in range(0,len(plainText)):
        index = a % 8
        indexList = storageOfCipher[index]
        indexList.append(plainText[a])
    sortedKeys =  sorted(keys)
    sortedCipher = []
    list(map(lambda x: rearrangingKeys(keys.index(x), storageOfCipher, sortedCipher), sortedKeys))
    cipher = ["".join(sortedCipher), keys]
    return cipher
# END OF COLUMN/TRANSPOSITION

# LOST STARTS
def slopesConsts(lengthOfText, numOfChars):
    # Angle of inclination of L1, L2
    thetaOne = (lengthOfText)*(math.pi/180)
    thetaTwo = 2.15 + thetaOne
    # Slopes and Y-int of Lines 1,2
    M1 = float("%.5f"%math.tan(thetaOne))
    M2 = float("%.5f"%math.tan(thetaTwo))
    C1 = 30 + numOfChars
    C2 = C1 + round(lengthOfText)
    sAndC = [M1,M2,C1,C2]
    return sAndC


# Function to allote key values
def keyAllotment(M1,M2,C1,C2,lineThreeChrs):
    keys = [[],[],[]]
    # Co-ordinates of point of intersection of L1, L2
    xIntL1L2 = (C2-C1)/(M1-M2)
    yIntL1L2 = (C1*M2 - M1*C2)/(M2-M1)
    # Ratio
    m,n = 1 , 1
    # X-intercepts of L1,L2
    xIntL1 = -C1/M1
    xIntL2 = -C2/M2
    # X-intercept, m, c of L3
    xIntL3 = (m*xIntL2 + n*xIntL1)/(m+n)
    M3 = yIntL1L2/(xIntL1L2- xIntL3)
    C3 = M3*xIntL3
    # Initialising multiples of 37
    primeMultiples = []
    x=23
    while len(primeMultiples)<= 32:
        numFactor = 0
        for b in range(2,x-1):
            if(x % b == 0):
                numFactor +=1
        if(numFactor == 0):
            primeMultiples.append(x)
        x+=1
    # Accessing raw oordinates for key
    lineOneRawOrdinate = list(map(lambda x : float("%.5f"%(-M1*x + C1)), primeMultiples))
    lineTwoRawOrdinate = list(map(lambda x : float("%.5f"%(-M2*x + C2)), primeMultiples))
    lineThreeRawOrdinate = list(map(lambda x : float("%.5f"%(M3*x + C3)), primeMultiples))
    # Formation of key
    for c in range(0,32):
        L1Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineOneRawOrdinate[c])))
        L2Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineTwoRawOrdinate[c])))
        L3Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineThreeRawOrdinate[c])))
        # Pushing key to list of keys
        keys[0].append(sum(list(map(lambda x : int(x)**3, L1Ordinate))))
        keys[1].append(sum(list(map(lambda x : int(x)**3, L2Ordinate))))
        keys[2].append(sum(list(map(lambda x : int(x)**3, L3Ordinate))))
    return keys


# Function to ensure there exists no duplicates in the keys.
def C2Decider(M1,M2,C1,C2,numOfChars,lineThreeChrs):
    keys = keyAllotment(M1,M2,C1,C2,lineThreeChrs)
    newC2 = C2
    tic = time.perf_counter()
    while True :
        duplicates=[list(filter(lambda x : x in keys[1] or x in keys[2] or keys[0].count(x) > 1, keys[0])),
                    list(filter(lambda x : x in keys[0] or x in keys[2] or keys[1].count(x) > 1, keys[1])),
                    list(filter(lambda x : x in keys[1] or x in keys[0] or keys[2].count(x) >1, keys[2]))
                    ]
        if(len(duplicates[0]) > 0 or len(duplicates[1]) > 0 or len(duplicates[2]) > 0):
            newC2 +=1
            keys = keyAllotment(M1,M2,C1,newC2,lineThreeChrs)
            toc = time.perf_counter()
            if(toc - tic >= 5):
                slopesConstants = slopesConsts(12, 1)
                keys = keyAllotment(slopesConstants[0],slopesConstants[1],slopesConstants[2],slopesConstants[3],lineThreeChrs)
                newC2 = slopesConstants[3]
                while True :
                    duplicates=[
                        list(filter(lambda x : x in keys[1] or x in keys[2] or keys[0].count(x) > 1, keys[0])),
                        list(filter(lambda x : x in keys[0] or x in keys[2] or keys[1].count(x) > 1, keys[1])),
                        list(filter(lambda x : x in keys[1] or x in keys[0] or keys[2].count(x) >1, keys[2]))
                    ]
                    if(len(duplicates[0]) > 0 or len(duplicates[1]) > 0 or len(duplicates[2]) > 0):
                        newC2 +=1
                        keys = keyAllotment(slopesConstants[0],slopesConstants[1],slopesConstants[2],newC2,lineThreeChrs)
                    else:
                        keys.append([[slopesConstants[0], slopesConstants[2]],[slopesConstants[1],newC2]])
                        return keys
        else:
            keys.append([[M1,C1],[M2,newC2]])
            break
    return keys


def splitAndReturn(string, keys):
    strList = string.split("-")
    keyList = keys[int(strList[1])-1]
    value = keyList[int(strList[0])]
    return value


def baseChange(num):
    BaseChangeIndex = [
        '\u16A0', '\u16A1', '\u16A2', '\u16A3', '\u16A4', '\u16A5', '\u16A6', '\u16A7', '\u16A8',
        '\u16AA', '\u16AB', '\u16AC', '\u16AD', '\u16AE', '\u16AF',
        '\u16B0', '\u16B1', '\u16B2', '\u16B3', '\u16B4', '\u16B5', '\u16B6', '\u16B7', '\u16B8',
        '\u16BA', '\u16BB', '\u16BC', '\u16BD', '\u16BE', '\u16BF',
        '\u16C0', '\u16C1', '\u16C2', '\u16C3', '\u16C4', '\u16C5', '\u16C6', '\u16C7', '\u16C8',
        '\u16CA', '\u16CB', '\u16CC', '\u16CD', '\u16CE', '\u16CF',
        '\u16D0', '\u16D1', '\u16D2', '\u16D3', '\u16D4', '\u16D5', '\u16D6', '\u16D7', '\u16D8',
        '\u16DA', '\u16DB', '\u16DC', '\u16DD', '\u16DE', '\u16DF',
        '\u16E0', '\u16E1', '\u16E2', '\u16E3', '\u16E4', '\u16E5', '\u16E6', '\u16E7', '\u16E8',
        '\u16EA', '\u16EB', '\u16EC', '\u16ED', '\u16EE', '\u16EF',
        '\u03B0', '\u03B1', '\u03B2', '\u03B3', '\u03B4', '\u03B5', '\u03B6', '\u03B7', '\u03B8', '\u03B9',
        '\u03BA', '\u03BB', '\u03BC', '\u03BD', '\u03BE', '\u03A9'
        '\u03C0', '\u03C1', '\u03C2', '\u03C3', '\u03C4', '\u03C5', '\u03C6', '\u03C7', '\u03C8', '\u03C9'
        ]
    maxPower= int(math.log(num, 100))
    baseChangedNum = ""
    i = maxPower
    while i >=0:
        bsValue = int(num/(100**i))
        num = num % (100**i)
        i -= 1
        baseChangedNum += BaseChangeIndex[bsValue]
    return baseChangedNum

def keyInitialise():
    # Initialising list of available chars
    lineOneChrs = []
    lineTwoChrs =[]
    lineThreeChrs = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|","\\",";",":","\'","\"",",","<",".",">","/","?"]
    for a in range(0,26):
        asciiUpperCase = 65 + a
        asciiLowerCase = 97+a
        lineOneChrs.append(chr(asciiUpperCase))
        lineTwoChrs.append(chr(asciiLowerCase))
    lineOneChrs.extend(["0","1","2","3","4"," "])
    lineTwoChrs.extend(["5","6","7","8","9","\t"])
    key = [lineOneChrs, lineTwoChrs, lineThreeChrs]
    return key


def encryption(plainText):
    lineOneChrs,lineTwoChrs, lineThreeChrs = keyInitialise()[0], keyInitialise()[1], keyInitialise()[2]
    lengthOfText = len(plainText)%90
    numOfChars = len(list(filter(lambda x : x in lineThreeChrs , plainText)))
    problemLength = 0
    if(lengthOfText == problemLength):
        lengthOfText = 69
    lineParams = slopesConsts(lengthOfText, numOfChars)
    keys = C2Decider(lineParams[0],lineParams[1],lineParams[2],lineParams[3],numOfChars,lineThreeChrs)
    encryptionLevelOne = list(map(lambda x : str(lineOneChrs.index(x))+"-1" if x in lineOneChrs else(str(lineTwoChrs.index(x))+"-2" if x in lineTwoChrs else(str(lineThreeChrs.index(x))+"-3" if x in lineThreeChrs else False)) , plainText))
    encryptionLevelTwo = list(map(lambda x : splitAndReturn(x, keys), encryptionLevelOne))
    encryptionLevelThree = list(map(lambda x : baseChange(x)+lineOneChrs[random.randint(0,26)], encryptionLevelTwo))
    prelimnaryCipher = "".join(encryptionLevelThree)
    cipherTextAndKey = RCTencryption(prelimnaryCipher)
    cipherText, cipherKey = cipherTextAndKey[0], [cipherTextAndKey[1]]
    cipherKey.append(keys[3])
    cipherTextAndKey = [cipherText, cipherKey]
    return cipherTextAndKey

tic = time.perf_counter()
plainText = list(input("Enter The text to be encrypted: "))
cipher = encryption(plainText)
toc = time.perf_counter()
timeTaken = toc-tic
print(cipher,"\n""time taken:",timeTaken)
