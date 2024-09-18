def palindromo(palabra):
    if palabra == None:
        return "No ingreso palabra"
    
    palabraToLowerCase = palabra.lower()

    lenPalabra = len(palabraToLowerCase) - 1

    for count, char in enumerate(palabraToLowerCase):
        if (lenPalabra / 2) < count:
            break
        if char == palabraToLowerCase[lenPalabra - count]:
            pass
        else:
            return False
        
    return True
        

print(palindromo("Malayalam"))