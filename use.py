from re import U
from rsa import RSA

def main():
	rsa = RSA()
	success = rsa.setpqe(191,197,13)
	m = 0x4a616b20746f207769647a69737a20746f207a6e61637a79207a6520647a69616c61206a616b206e616c657a792e

	c = rsa.encryptblock(m)
	m = rsa.decryptblock(c)
	print("".join([chr(u) for u in m][::-1]))

	print(rsa.getprivatekey())

if __name__ == "__main__":
	main()