#20CE046 SAKINA KUTERWADLI
#PRACTICAL 7
# AIM: Lapindrome is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character.
# If there are odd number of characters in the string, we ignore the middle character and check for lapindrome.
# For example gaga is a lapindrome, since the two halves ga and ga have the same characters with same frequency.
# Also, abccab, rotor and xyzxy are a few examples of lapindromes. 
# Note that abbaab is NOT a lapindrome. 
#The two halves contain the same characters but their frequencies do not match. Your task is simple.
# Given a string, you need to tell if it is a lapindrome. 
#   Github Repository link: https://github.com/Sakina-K/CE259-PIP_Practicals.git

N=int(input())
s1=""
s2=""
for i in range(N):      #inputting words
    S=input()
    l=len(S)            #length of each word in l
    mid=int(l/2)        #finding the middle character
    if(l%2==0):
        s1=S[:mid]      #dividing the string in two parts if l is even
        s2=S[mid:]
    else:
        s1=S[:mid]      #dividing the string in two parts by ignoring the middle character
        s2=S[mid+1:]    #if l is odd
    l1=list(s1)
    l2=list(s2)         #storing the string as lists
    l1.sort()
    l2.sort()           #sorting the lists

    if l1==l2:          #printing output as YES if strings are equal else NO
        print("YES")
    else:
        print("NO")

