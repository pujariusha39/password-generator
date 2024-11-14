import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'
         'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Numbers=[0,1,2,3,4,5,6,7,8,9]
symbol=['#','$','%,','*','&']
n_letters=int(input("how many letters do you want?\n"))
n_Numbers=int(input("how many Numbers do you want?\n"))
n_symbol=int(input("how many symbol do you want?\n"))
password=[]
for i in range(1,n_letters+1):
    char=random.choice(letters)
    password += char
for i in range(1,n_Numbers+1):
    value=random.choice(Numbers)
    password +=str(value)
for i in range(1,n_symbol+1):
    path=random.choice(symbol)
    password +=path
    random.shuffle(password)
print(password)
password_list=""  #converting the list in to a string:
for j in password:
    password_list +=j
print(password_list)


