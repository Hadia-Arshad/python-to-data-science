import random
import string
st=input("Enter message")
words = st.split(" ")
coding=input("1 for coding 0 for decoding")
coding= True if (coding=="1") else False
if(coding):
    newwords=[]
    for word in words:
        if(len(word)>=3):
            r1=" ".join(random.choices(string.ascii_lowercase,k=3)) 
            r2=" ".join(random.choices(string.ascii_lowercase,k=3))
            stnew=r1+ word[1:]+ word[0]+ r2
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])
    print(" " .join(newwords))  
else:
    newwords=[]
    for word in words:
        if(len(word)>=9):
            stnew= word[3:-3]
            stnew = stnew[-1] + stnew[:-1]
            newwords.append(stnew)
        else:
            newwords.append(word[::-1])  
    print(" " .join(newwords))  