import math
plainText = input("Enter The text to be encrypted: ")
lengthOfText = len(plainText)%90
problemLengths = [1,2,3,4,0]
if(lengthOfText in problemLengths):
    lengthOfText = 7
# Initialising list of available chars
lineOneChrs = []
lineTwoChrs =[]
for a in range(0,26):
    asciiUpperCase = 65 + a
    asciiLowerCase = 97+a
    lineOneChrs.append(chr(asciiUpperCase))
    lineTwoChrs.append(chr(asciiLowerCase))
lineOneChrs.extend(["0","1","2","3","4"," "])
lineTwoChrs.extend(["5","6","7","8","9","\t"])
lineThreeChrs = ["`","~","!","@","#","$","%","^","&","*","(",")","-","_","=","+","{","}","[","]","|","\\",";",":","\'","\"",",","<",".",">","/","?"]
# Angle of inclination of L1, L2
thetaOne = (lengthOfText)*(math.pi/180)
thetaTwo = 2.15 + thetaOne
# Slopes and Y-int of Lines 1,2
M1 = float("%.15f"%math.tan(thetaOne))
M2 = float("%.15f"%math.tan(thetaTwo))
numOfChars = len(list(filter(lambda x : x in lineThreeChrs , plainText)))
C1 = 30 + numOfChars
C2 = C1 + round(lengthOfText)
print(M1, thetaOne,C2)
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
def C2Decider(M1,M2,C1,C2, lineThreeChrs):
    keys = keyAllotment(M1,M2,C1,C2,lineThreeChrs)
    newC2 = C2
    while True :
        duplicates=[list(filter(lambda x : x in keys[1] or x in keys[2] or keys[0].count(x) > 1, keys[0])),
                    list(filter(lambda x : x in keys[0] or x in keys[2] or keys[1].count(x) > 1, keys[1])),
                    list(filter(lambda x : x in keys[1] or x in keys[0] or keys[2].count(x) >1, keys[2]))
                    ]
        # print(duplicates)
        if(len(duplicates[0]) > 0 or len(duplicates[1]) > 0 or len(duplicates[2]) > 0):
            newC2 +=1
            keys = keyAllotment(M1,M2,C1,newC2,lineThreeChrs)
        else:
            keys.append([C2,newC2])
            return keys

keys = C2Decider(M1,M2,C1,C2,lineThreeChrs)
# keys = keyAllotment(M1,M2,C1,C2,lineThreeChrs)
duplicates=[list(filter(lambda x : x in keys[1] or x in keys[2] or keys[0].count(x) > 1, keys[0])),
            list(filter(lambda x : x in keys[0] or x in keys[2] or keys[1].count(x) > 1, keys[1])),
            list(filter(lambda x : x in keys[1] or x in keys[0] or keys[2].count(x) >1, keys[2]))
            ]
# print(duplicates)