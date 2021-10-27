import numpy as np
import time

# RCT DECRYPTION
def RCTdecryption(cipher):
    cipherText, keys = cipher[0], cipher[1]
    sortedKeys = sorted(keys)
    numOfChrs = []
    storageOfSort = []
    if len(cipherText) > 8:
        numOfChrs = list(np.ones(8, dtype=int))
        indexCounter = 0
        while sum(numOfChrs) != len(cipherText):
            numOfChrs[indexCounter] = numOfChrs[indexCounter] +1
            if(indexCounter == 7):
                indexCounter = 0
            else:
                indexCounter +=1
    else:
        list(np.ones(len(cipherText), dtype=int))
    chrList = list(cipherText)
    sliceStart = 0
    for c in range(0, len(sortedKeys)):
        index = keys.index(sortedKeys[c])
        sliceEnd = numOfChrs[index] + sliceStart
        storageOfSort.append(chrList[sliceStart:sliceEnd])
        sliceStart = sliceEnd
    finalSort = []
    for d in keys:
        indexToPush = sortedKeys.index(d)
        chrsPushed = storageOfSort[indexToPush]
        if(len(chrsPushed) != max(numOfChrs)):
            chrsPushed.append(" ")
        finalSort.append(chrsPushed)
    finalSort = np.array(finalSort)
    limit = np.shape(finalSort)[1]
    counter = 0
    plainText = ""
    while counter <= (limit-1):
        plainText += "".join(finalSort[:,counter])
        counter += 1
    return plainText


# LOST DECRYPTION
# AVAILABLE KEYS
def keyInitialise():
    # Initialising list of available chars
    lineOneChrs = []
    lineTwoChrs =[]
    lineThreeChrs = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+",
                     "{","}","[","]","|","\\",";",":","\'","\"",",","<",".",">","/","?"
    ]
    for a in range(0,26):
        asciiUpperCase = 65 + a
        asciiLowerCase = 97+a
        lineOneChrs.append(chr(asciiUpperCase))
        lineTwoChrs.append(chr(asciiLowerCase))
    lineOneChrs.extend(["0","1","2","3","4"," "])
    lineTwoChrs.extend(["5","6","7","8","9","\t"])
    key = [lineOneChrs, lineTwoChrs, lineThreeChrs]
    return key


# ALLOTMENT OF KEYS
def keyAllotment(SandC,lineThreeChrs):
    L1,L2 = SandC[0], SandC[1]
    M1, C1 = L1[0], L1[1]
    M2, C2 = L2[0], L2[1]
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


def reverseBaseChange(num):
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
    # print(num)
    # num = list(filter(lambda x : x in BaseChangeIndex, num))
    # print(num)
    baseChangedList = list(map(lambda x: BaseChangeIndex.index(x)*(100**(-num.index(x)+ len(num) -1)) , num))
    baseChangedNum = sum(baseChangedList)
    return baseChangedNum

def decryption(cipher,key):
    RCTList = [cipher, key[0]]
    lineOneChrs, lineTwoChrs, lineThreeChrs = keyInitialise()[0],keyInitialise()[1], keyInitialise()[2]
    decryptionLevelOne = list(RCTdecryption(RCTList))
    for a in range(0, len(decryptionLevelOne)):
        if decryptionLevelOne[a] in lineOneChrs:
            decryptionLevelOne[a] = " "
    decryptionLevelTwo = "".join(decryptionLevelOne)
    decryptionLevelThree =  list(filter(lambda x: x != "" , decryptionLevelTwo.split(" ")))
    decryptionLevelFour = list(map(lambda x: reverseBaseChange(x), decryptionLevelThree))
    lineOneKeys, lineTwoKeys, lineThreeKeys = keyAllotment(key[1], lineThreeChrs)[0],keyAllotment(key[1], lineThreeChrs)[1], keyAllotment(key[1], lineThreeChrs)[2]
    decryptionLevelFive = list(map(lambda x: lineOneChrs[lineOneKeys.index(x)] if(x in lineOneKeys) 
                                    else( lineTwoChrs[lineTwoKeys.index(x)] if(x in lineTwoKeys) 
                                    else(lineThreeChrs[lineThreeKeys.index(x)] if(x in lineThreeKeys) 
                                    else(x))), decryptionLevelFour))
    plainText = "".join(decryptionLevelFive)
    return plainText

cipherText = eval(input("enter cipher text: "))
tic = time.perf_counter()
plainText = decryption(cipherText[0], cipherText[1])
toc = time.perf_counter()
timeTaken = toc-tic
print(plainText, "\n""time taken:",timeTaken)