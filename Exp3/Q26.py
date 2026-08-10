#Encrypt and decrypt a message using the Caesar Cipher algorithm. 

text = input("Enter message: ")
key = int(input("Enter key: "))

encrypt = ""
decrypt = ""

for ch in text:
    encrypt += chr(ord(ch) + key)

print("Encrypted =", encrypt)

for ch in encrypt:
    decrypt += chr(ord(ch) - key)

print("Decrypted =", decrypt)