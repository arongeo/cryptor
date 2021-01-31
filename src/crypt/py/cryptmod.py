from cryptography.fernet import Fernet
import string
import random

def gen_Key():
	result = Fernet.generate_key().decode("utf-8")
	return result

class Key:
	def __init__(self, key):
		self.key = Fernet(key.encode("utf-8"))

	def encrypt(self, file):
		fr = open(file, "rb").read()
		encrypted = self.key.encrypt(fr)
		fw = open(file+".cryptor", "wb").write(encrypted)

	def decrypt(self, file):
		fr = open(file, "rb").read()
		decryptedutf = self.key.decrypt(fr)
		decrypted = decryptedutf
		filename = file.replace(".cryptor", "")
		fw = open(filename, "wb").write(decrypted)
