from cryptography.fernet import Fernet

# create a key and a key file, need to be used once
'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:  # 'wb' write in byte
        key_file.write(key)'''


# load key
def load_key():
    file = open("key.key", "rb")  # read byte
    key = file.read()  # returns byte datatype not string
    file.close()
    return key


key = load_key()
fer = Fernet(key)


def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()  # rstrip removes '\n'
            user, password = data.split("|")  # data.split returns an array

            # decrypt
            password = fer.decrypt(password.encode()).decode()
            print("Account:", user, ", Password:", password)


def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # encode - turns string into byte type for encrypting
    # encrypt - only accepts byte type
    # decode - change byte to string
    # turns the text into random string in the password.txt file
    password = fer.encrypt(password.encode()).decode()

    # open or create a file
    # using 'with' auto close the file
    # 'w' write or overwrite a file
    # 'r' read the file
    # 'a' append, read and write at the end to an existing file or create new file if does not exist
    with open('password.txt', 'a') as f:
        f.write(name + '|' + password + "\n")

    # using this instead of 'with', close must be manually typed
    # file = open('password.txt', 'a')
    # file.close()


while True:
    mode = input(
        "Would like to add a new password or view existing one (view/add) or q to quit?").lower()

    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
