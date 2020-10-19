import hashlib
import time as t
pass_hash = input("Yuki.N> Enter hash MD5 : ")

wordlist = input("File name : ")

try:
    pass_file = open (wordlist, "r")
except:
    print("No file found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    # print(word)
    # print(digest)
    # print(pass_hash)
    counter += 1
    

    if digest == pass_hash:
        print("Password found")
        print("password is " + word)
        flag = 1
        break

if flag == 0:
    print("password/passphrase is in not list")

time.sleep(5)
