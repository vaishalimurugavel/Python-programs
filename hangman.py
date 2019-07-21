import msvcrt as mv
import random
char=0
count=0
blanks=[]
word_list=["india","china","antartica","australia"]
clue_fact=["has the highest cricket ground in the world","has the largest population","is the largest desert in the world","kangroo is the national animal"]
index=random.randint(0,3)
word=word_list[index]
fact=clue_fact[index]

list_word=list(word)

def update_choice():
    for i in blanks:
        print(i,end=" ")
    print("\n")

def find_duplicate(list_word,user_character,blanks,count):
    dup_list=[]
    for x,char in enumerate(list_word):
        if char is user_character:
            if x not in dup_list:
                dup_list.append(x)
                blanks[x]=user_character
                count+=1
    return count

print("\n\t\tCOUNTRIES")
for i in list_word:
    if i is not ' ':
        blanks.append("_")
        char += 1
update_choice()
print(fact)

while count <= char-1:
    
    user_character=input("enter a letter  ")
    if user_character not in blanks:
        count=find_duplicate(list_word,user_character,blanks,count)
    update_choice()

print("\n\t\tCORRECT GUESS")
mv.getch()
