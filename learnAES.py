from Crypto.Cipher import AES
import base64

my_key="WangJinzhou"

def adder_16(my_str):
    while len(my_str)%16!=0:
        my_str+='\0'
    return my_str.encode(encoding='utf-8')

def encrypt_AES(text):
    obj = AES.new(adder_16(my_key),AES.MODE_ECB)
    result = obj.encrypt(adder_16(text))
    result = str(base64.encodebytes(result), encoding="utf-8").strip()
    return result

def decrypt_AES(text):
    aes = AES.new(adder_16(my_key),AES.MODE_ECB)
    result = base64.decodebytes(text.encode(encoding='utf-8'))
    result = str(aes.decrypt(result),encoding='utf-8').replace("\0",'')
    return result

test=input("Please input your message")
test1 = encrypt_AES(test)
print(test1)
print(decrypt_AES(test1))