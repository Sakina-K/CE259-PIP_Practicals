#Practical -5 Swap case for a string
def swap_case(Str):                #Function for case swap with parameter and return value
    Output=''
    for char in Str:
        if(char.isupper()==True):       
            Output+=(char.lower())
        elif(char.islower()==True):
            Output+=(char.upper())
        else:
            Output+=char
    return Output

print("Enter a string:")
S=input()               #inputting string
print("After Swapping")
print(swap_case(S))     #function call
