from rsa import RSA

def main():
	rsa = RSA()
	success = rsa.setpqe(719,727,7)
	m = 65
	print(rsa.getpublickey())
	print("Sucess:",success)

	c = rsa.encrypt(m)
	print(c)
	m = rsa.decrypt(c)
	print(m)
	

if __name__ == "__main__":
	main()