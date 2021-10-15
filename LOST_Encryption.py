import math
plainText = input("Enter The text to be encrypted: ")
lengthOfText = len(plainText)
lineOneKeys, lineTwoKeys, lineThreeKeys = [], [], []
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
thetaOne = (lengthOfText%180)*(math.pi/180)
thetaTwo = 2.15 + thetaOne
# Slopes and Y-int of Lines 1,2
M1 = math.tan(thetaOne)
M2 = math.tan(thetaTwo)
numOfChars = len(list(filter(lambda x : x in lineThreeChrs , plainText)))
C1 = 30 + numOfChars
C2 = C1 + 23
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
primeMultipleL1 = []
primeMultipleL2 = []
primeMultipleL3 = []
x=7
counter = 1
while len(primeMultipleL3)<= 32:
    numFactor = 0
    for b in range(2,x-1):
        if(x % b == 0):
            numFactor +=1
    if(numFactor == 0):
        if(counter%3 ==1):
            primeMultipleL1.append(x)
        elif(counter%3 ==2):
            primeMultipleL2.append(x)
        else:
            primeMultipleL3.append(x)
        counter+=1
    x+=1
# Accessing raw oordinates for key
lineOneRawOrdinate = list(map(lambda x : float("%.5f"%(-M1*x + C1)), primeMultipleL1))
lineTwoRawOrdinate = list(map(lambda x : float("%.5f"%(-M2*x + C2)), primeMultipleL2))
lineThreeRawOrdinate = list(map(lambda x : float("%.5f"%(M3*x + C3)), primeMultipleL3))
# print(lineOneRawOrdinate, lineTwoRawOrdinate, lineThreeRawOrdinate)

# Formation of key
for c in range(0,32):
    L1Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineOneRawOrdinate[c])))
    L2Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineTwoRawOrdinate[c])))
    L3Ordinate = list(filter(lambda x: x not in lineThreeChrs, str(lineThreeRawOrdinate[c])))
    # Pushing key to list of keys
    lineOneKeys.append(sum(list(map(lambda x : int(x)**5 , L1Ordinate))))
    lineTwoKeys.append(sum(list(map(lambda x : int(x)**5 , L2Ordinate))))
    lineThreeKeys.append(sum(list(map(lambda x : int(x)**5 , L3Ordinate))))
# print(lineOneKeys,lineTwoKeys,lineThreeKeys)

# checking for duplicates in other lists
l1Duplicates = list(filter(lambda x : x in lineTwoRawOrdinate or x in lineThreeRawOrdinate, lineOneRawOrdinate))
l2Duplicates = list(filter(lambda x : x in lineOneRawOrdinate or x in lineThreeRawOrdinate, lineTwoRawOrdinate))
l3Duplicates = list(filter(lambda x : x in lineTwoRawOrdinate or x in lineOneRawOrdinate, lineThreeRawOrdinate))
print(l1Duplicates, l2Duplicates, l3Duplicates)

l1Duplicates = list(filter(lambda x : x in lineTwoKeys or x in lineThreeKeys, lineOneKeys))
l2Duplicates = list(filter(lambda x : x in lineOneKeys or x in lineThreeKeys, lineTwoKeys))
l3Duplicates = list(filter(lambda x : x in lineTwoKeys or x in lineOneKeys, lineThreeKeys))
print(l1Duplicates, l2Duplicates, l3Duplicates)