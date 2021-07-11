import random
def Gen():
    List1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","&"]
    charnos = input("Enter number of characters\n")
    charnos = int(charnos)    
    i=0
    while i < charnos:
        Password = random.choice(List1)
        print(Password, end="")         # end="" parameter will enable to print the characters in one line 
        i += 1
    return Password
x = Gen()