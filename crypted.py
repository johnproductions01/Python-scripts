import random


msg="Bonjourat xDD 008 "
print(f'original message :{msg}')



encryption_level=120 // 8

char_pool=''
for i in range(0x00,0x255):
    char_pool=chr(i)
    
key=''
for i in range(encryption_level):
    key +=random.choice(char_pool)
    
key_index=0
max_key_index=encryption_level-1
encrypted_msg=""
for char in msg:
    encrypted_char= ord(char) ^ ord(key[key_index])
    encrypted_msg+= chr(encrypted_char)
    if key_index>=max_key_index:
        key_index= 0
    else:
        key_index+=1
print(f'Encrypted message:  {encrypted_msg}')

key_index=0
decrypted_msg=''
for char in encrypted_msg:
    decrypted_char = ord(char) ^ ord(key[key_index])
    decrypted_msg += chr(decrypted_char)
    if key_index >= max_key_index:
        key_index=0
    else:
        key_index+=1
print(f'decrypted messgae:  {decrypted_msg}')
