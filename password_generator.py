
import random

# characters of the password 
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ¢$€£¥₮৲৳௹฿៛₠₡₢₣₤₥₦!#$%&/()=*ª`^_:;,.-º+´~<>0987654321"

#password compliance and amount setting

while 1:
    password_len = int(input("What length would you like for your password?: "))
    password_count = int(input("How many password do you want?:"))
    for x in range(0, password_count):
        password = ""
        for x in range(0,password_len):
            password_char = random.choice(chars)
            password      = password + password_char
        print("Here is your password:", password)    