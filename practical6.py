#20CE046 SAKINA KUTERWADLI
#PRACTICAL 6
# AIM: You are given n words. Some words may repeat.
#  For each word, output its number of occurrences. 
#  The output order should correspond with the input order of appearance of the word.
#  See the sample input/output for clarification. 
#   Github Repository link: https://github.com/Sakina-K/CE259-PIP_Practicals.git

N=int(input())  #number of words
count_dict={}   # creating a dict to count occurences
string_l=[]     #string to store the words
for i in range(N):
    word=input()
    string_l.append(word)   #appending the word in string
    if word in count_dict:
        count_dict[word]+=1     
    else:
        count_dict[word]=1
print(len(count_dict))      #number of distinct words
print(' '.join([str(count_dict[word]) for word in count_dict]))     #Occurrence of each word