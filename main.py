import hashlib
import string 
import random


normal_hash = {}
salt_n_pepper = {}
salt = {} 
pepper = {}

string1 = string.ascii_letters
string1 += "!@#$%^&*()}{:?/"
string1 += string.digits

#create hashes

def normal_hash1(password,username):
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    normal_hash[username] = hashed
    return hashed

def salt1(password,username):
    salt_add = "".join(random.sample(string1 , random.randint(1,8)))
    password += salt_add
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    hashed += " " + salt_add
    salt[username] = hashed
    return hashed

def pepper1(password,username):
    pepper_add = random.choice(string.ascii_letters)
    password += pepper_add 
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    pepper[username] = hashed
    return hashed

# salt and peper
def snp(password,username):
    salt_add = "".join(random.sample(string1 , random.randint(1,8)))
    pepper_add = random.choice(string.ascii_letters)
    password += salt_add + pepper_add
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest()
    hashed += " " + salt_add
    salt_n_pepper[username] = hashed
    return hashed 

#<!----------------------------------------------------------------------------------------------->

#password checker 

def normal_hash_check(password,username):
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest() 
    if normal_hash[username] == hashed:
        print("Welcome")
    else:
        print("nonono")

def salt_check(password,username):
    password += salt[username].split()[1]
    hashed = hashlib.sha256(password.encode("utf-8")).hexdigest() 
    if salt[username].split()[0] == hashed:
        return "Welcome"
    else:
        return "nononono"

def pepper_check(password,username):
    for x in string.ascii_letters:
        password1 = password
        password1 += x 
        hashed = hashlib.sha256(password1.encode("utf-8")).hexdigest() 
        if pepper[username] == hashed:
            return "Welcome"
    return "nononono"

#salt and pepper check
def snp_check(password,username):
    salt_add = salt_n_pepper[username].split()[1]
    password += salt_add
    for x in string.ascii_letters:
        password1 = password
        password1 += x
        print(password1)
        hashed = hashlib.sha256(password1.encode("utf-8")).hexdigest() 
        if salt_n_pepper[username].split()[0] == hashed:
            return "Welcome"
        
    return "nonono"


while True:
    print(normal_hash)
    print(salt_n_pepper)
    print(salt)
    print(pepper)
    username = input("Username : ")
    password = input("Password : ") 
    enterpass_or_hash = input("Enter New Hash or Enter Password (NH/P): ")
    which_hash = input("which type of hash Normal , SaltNPeper , Salt , Peper (N,SNP,S,P): ")
    if enterpass_or_hash.lower() == "nh":

        if which_hash.lower() == "n":
            print(normal_hash1(password,username))

        elif which_hash.lower() == "s":
            print(salt1(password,username))

        elif which_hash.lower() == "p":
            print(pepper1(password,username))

        elif which_hash.lower() == "snp":
            print(snp(password,username))

#----------------------------------------------------------------------------           

    elif enterpass_or_hash.lower() == "p":

        if which_hash.lower() == "n":
            print(normal_hash_check(password,username))

        elif which_hash.lower() == "s":
            print(salt_check(password,username))

        elif which_hash.lower() == "p":
            print(pepper_check(password,username))

        elif which_hash.lower() == "snp":
            print(snp_check(password,username))      




        

    

