#Input
inputString = input("Enter the string")
#Value to tell whether the list should be adding characters or not
deleteToggle = False
#if encounters a open '<' don't read chars till encountering a closing '>'
newString=""
for i in range(len(inputString)):
    if inputString[i]== "<":
        deleteToggle=True
   
    if deleteToggle==False:
        newString=newString + inputString[i]

    if inputString[i]==">":
        deleteToggle=False
        if len(newString)>0:
            if newString[len(newString)-1]!=',':
                newString=newString + ',';
if len(newString)>0:
    if newString[len(newString)-1]==',':
        newString= newString[:-1]
#placeholder print
print(newString)
