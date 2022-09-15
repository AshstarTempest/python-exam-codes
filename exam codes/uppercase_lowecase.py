while True:
    ch = input("enter a character ")
    unico_val = ord(ch)
    if unico_val >= 65 and unico_val <= 90:
        print("uppercase")
    elif unico_val >= 97 and unico_val <= 122:
        print("lowercase")
    elif unico_val >= 48 and unico_val <= 58:
        print("number")
    else:
        print("special character")
