def ispalindrome(str):
    return (str==str[::-1])
sen=input()
result=""
for i in range(len(sen)):
    for j in range(i,len(sen)+1):
        if(ispalindrome(sen[i:j])):
            if(len(sen[i:j])>len(result)):
                result=sen[i:j]
print(result)
