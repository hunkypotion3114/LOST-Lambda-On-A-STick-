# LOST(Lambda On A STick)
A rather trivial encryption when graphed represents a lambda which has been propped on a stick. The enryption is a advanced version of COKE's Encryption, essentially involving more advanced mathematics, particularly coordinate geometry.
# PRINCIPLE BEHIND THE CIPHER:
### Charectors Allowed:
The encryption hopes to encyrpt any charector of the english language. Since the keys of the encryption are more inclusive compared to COKE. We wish to incroporate numbers and a wider array of special charectors.
### Building Blocks of the encryption:
The concept of straight lines is an important part in the making of the keys of the encryption. 
The encryption key is essentially split into three parts , i.e three equations of lines. \
The following are the parameters for the three equations:
#### &emsp; 1. Line One(Uppercase and 0-4):
&emsp; &emsp; a. The first line is the key generator for all the uppercase letters and the nums 0-4. \
&emsp; &emsp; b. Its equation is given by : y=(M1)x + (C1) \
&emsp; &emsp; Where:\
&emsp; &emsp; &emsp; i) M1 = tan(lengthOfString % 180) \
&emsp; &emsp; &emsp; ii) C1 = 30 + Number of special chars. (reason for using 30 is because it represents the positon of lambda in the greek alphabet) 
#### &emsp; 2. Line Two(Lowercase and 5-9):
&emsp; &emsp; a. The second line is the key generator for all the lowercase letters and the nums 5-9. \
&emsp; &emsp; b. Its equation is given by : y=(M2)x + (C2) \
&emsp; &emsp; Where:\
&emsp; &emsp; &emsp; i) M2 = Slope of the line such that the line makes an angle of 1 Radian with Line 1 \
&emsp; &emsp; &emsp; ii) C2 = Y-intercept of equation, Greater than C1 and such that the Point of intersection of Line1 and Line2 are not integers 
#### &emsp; 3. Line Three(Special charectors):
&emsp; &emsp; a. The third line is the key generator for all the special charectors. \
&emsp; &emsp; b. Its equation is given by : y=(M3)x + (C3) \
&emsp; &emsp; Where:\
&emsp; &emsp; &emsp; i) M3 and C3 are such that the x-intercept of the line divides the the line joining the points (X1,0) and (X2,0) in the ratio m:n \
&emsp; &emsp; &emsp; ii) m:n = value of key of "A"/value of key of "a" , X1 = X-intercept of Line1, X2= X-intercept of Line2
