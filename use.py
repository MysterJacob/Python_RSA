from re import U
from rsa import RSA

def main():
	rsa = RSA()
	success = rsa.setpqe(719,727,41)
	m = 0x54686520717569636b2062726f776e20666f78206a756d7073206f76657220746865206c617a7920646f67

	c = rsa.encryptblock(m)
	m = rsa.decryptblock(c)
	print("".join([chr(u) for u in m][::-1]))

	print(rsa.getprivatekey())

if __name__ == "__main__":
	main()