from tkinter import *
import sys
from tkinter.filedialog import askopenfilename
from sys import platform

sys.path.append("./crypt/py")

import cryptmod

class UI:
	def __init__(self):
		self.log = []
		self.main()
		self.log.append("Started; \n")
		self.dir = ""

	def getFileName(self):
		self.dir = askopenfilename()
		if self.dir != "":
			self.log.append("Opened-"+self.dir+";\n")
		else:
			self.log.append("NotOpenedAnything(CancelBtn)\n")
		if self.dir != "":
			self.dirShow.config(text=str(self.dir))
		else:
			self.dirShow.config(text="File Goes Here")
		print(self.log)

	def genKey(self):
		key = cryptmod.gen_Key()
		self.keyText.delete("1.0", END)
		self.keyText.insert("1.0", key)

	def encrypt(self):
		key = self.keyText.get("1.0", END)
		cryptmod.Key(key).encrypt(self.dir)

	def decrypt(self):
		if ".cryptor" in self.dir:
			key = self.keyText.get("1.0", END)
			cryptmod.Key(key).decrypt(self.dir)
		else:
			self.msg.config(text="Encrypted file must have type '.cryptor'")	

	def main(self):
		self.dir = "File Goes Here"
		# Frame Settings
		frame = Tk()
		if platform == 'darwin':
			from Foundation import NSBundle
			bundle = NSBundle.mainBundle()
			if bundle:
				info = bundle.localizedInfoDictionary() or bundle.infoDictionary()
				if info and info['CFBundleName'] == 'Python':
					info['CFBundleName'] = "Cryptor"
		frame.title("Cryptor")
		frame.geometry("500x175")
		frame.resizable(False, False)
		# Buttons
		openbtn = Button(frame, text="Open", command=self.getFileName)
		genKeyBtn = Button(frame, text="Generate Key", command=self.genKey)
		encryptBtn = Button(frame, text="Encrypt", command=self.encrypt)
		decryptBtn = Button(frame, text="Decrypt", command=self.decrypt)
		# Labels
		self.dirShow = Label(frame, text=self.dir)
		lbl = Label(frame, text="Key:")
		self.msg = Label(frame, text="-----")
		# TextFields
		self.keyText = Text(frame, height=1, width=45)
		# Packing
		openbtn.pack()
		self.dirShow.pack()
		lbl.pack()
		self.keyText.pack()
		genKeyBtn.pack()
		encryptBtn.pack()
		decryptBtn.pack()
		self.msg.pack()
		# Mainloop
		frame.mainloop()

