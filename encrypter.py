import os
import pyaes

#abre o arquivo a ser criptografado

file_name = 'teste.txt'
file = open(file_name,'rb')
file_data = file.read()
file.close()

#remove o arquivo original

os.remove(file_name)

#define a chave para o encrypt

key = b"digitarsuachave"
aes = pyaes.AESModeOfOperationCTR(key)

#criptografa o arquivo

crypto_data = aes.encrypt(file_data)

#salva o arquivo criptografado

new_file = file_name + '.suriv'
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
