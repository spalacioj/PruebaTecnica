
def anagrama(palabra1, palabra2):
    listChars = []
    for char in palabra1:
        listChars.append(char)
    
    for char in palabra2:
        if char in listChars:
            listChars.remove(char)
        else:
            return False
    
    if(len(listChars) != 0):
        return False
    

    return True

print(anagrama("lapicero", "copiarle"))

