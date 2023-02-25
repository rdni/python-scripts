from cryptography.fernet import Fernet as f

key = f.generate_key()
encrypter = f(key)

with open("key.key", "w") as file:
    file.write(str(key))
    file.close()

with open("encrypt.txt", "r") as file:
    lines = []
    for line in file.readlines():
        lines.append(encrypter.encrypt(line.encode('utf-8')))
        file.close()
with open("encrypt.txt", "w") as file:
    file.write("".join(lines))
    file.close()
print(lines)
