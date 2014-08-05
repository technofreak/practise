"""Caesar Cipher

A Caesar cipher is a simple cipher that is based on the idea of shifting each 
letter of the plain text message a fixed number of positions in the alphabet. 
The original message can be recovered by re-encoding using the negative of the key.

Write an encoder that can take a plain text as input along with the value of 
the key, encode it into a cipher text and write the output into a file named 
after the key value. [10 points]

Write a decoder that can take the file name as input, get the key from the 
filename and decode the cipher text present within the file into the actual 
plain text. [10 points]

Note: the cipher has to implement shifting in a circular fashion, i.e. the 
alphabet after z is again a.
"""

MAX_KEY_SIZE = 26

class MaxKeySizeError(Exception):
	pass

class CaesarCipher(object):
	def __init__(self, key):
		if isinstance(key, int) and key > MAX_KEY_SIZE:
			raise MaxKeySizeError
		elif isinstance(key, str) and int(key) > MAX_KEY_SIZE:
			raise MaxKeySizeError
		else:
			self.key = key

	def __convert(self, text, key):
		result = ''
		for char in text:
			if char.isalpha():
				idx = ord(char)
				idx += key

				if char.isupper():
					if idx > ord('Z'):
						idx -= 26
					elif idx < ord('A'):
						idx += 26
				elif char.islower():
					if idx > ord('z'):
						idx -= 26
					elif idx < ord('a'):
						idx += 26
				result += chr(idx)
			else:
				result += char
		return result

	def encrypt(self, message):
		return self.__convert(message, self.key)

	def decrypt(self, secret):
		return self.__convert(secret, -self.key)
		

if __name__ == "__main__":
	cipher = CaesarCipher(12)
	message = "i want to pass this secret to you"
	print "Message:", message
	secret = cipher.encrypt(message)
	print "Secret:", secret
	uncovered = cipher.decrypt(secret)
	print "Uncovered:", uncovered
