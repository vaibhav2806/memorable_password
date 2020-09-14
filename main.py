

SECURE = (('o','0') , ('s','$') , ('a','@') , ('And','&') , ('h','#') , ('i','1'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a , b)
    return password

if __name__ == "__main__":
    password = input("Enter your password: \n")
    password = securePassword(password)
    print(f"Your secured password is: {password}")