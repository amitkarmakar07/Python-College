sen=input()
vowel=[]
for i in sen:
    if i in "aeiou":
        vowel.append(i)
vowel.sort()
k=0
result=""
for i in sen:
    if i in "aeiou":
        result+=vowel[k]
        k+=1
    else:
        result+=i
print(result)

