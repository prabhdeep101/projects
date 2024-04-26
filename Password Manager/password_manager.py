from cryptography.fernet import Fernet
# cryptography--> library for encryption, decryption, hashing, keys
# fernet--> an encryption algorithm

'''def write_key():
    key = Fernet.generate_key()#generates key
    with open("key.key", "wb") as key_file:#wb->write bytes mode,,,, key.key->file to store keys
        key_file.write(key)

write_key()'''
#Create the key once. To regenrate the key, uncomment the function. 

def load_key():
    file = open("key.key", "rb")#file is a variable used to represent file object(open file)
    key = file.read()
    file.close()
    return key


key = load_key()
fer = Fernet(key)    #creating an instance of class fernet
# fer contains ciphertext(encrypted data) using the key we created



def view():
    with open("passwords.txt", "r") as f:#open file as variable f in the program, for read only
        for line in f.readlines():
            data= line.rstrip()
            user, pswd = data.split(" | ")
            print('Username: '+ user)
            print('Password: '+ fer.decrypt(pswd.encode()).decode())

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("passwords.txt", "a") as pass_file:
        pass_file.write(name + ' | ' + fer.encrypt(pwd.encode()).decode() + "\n")#.decode() to store it in a txt file






while True:
    mode = input("Would you like to add a new password or view existing passwords (add/view)? Press q to quit. ".lower())

    if mode == "q":
        quit()

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else:
        print('Invalid mode. Please try again.')
        continue


