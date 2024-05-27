import random
 
harfler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola = ""


sayi = int(input("şifreniz ne kadar uzun olsun"))

for i in range(sayi):
    
    a = random.choice(harfler)


    parola += a

print(parola)
