from math import gcd
class RSA:
	def __init__(self) -> None:
		self.k = 0
		self.e = 0
		self.n = 0
		self.d = 0
		self.phi_n = 0

	def setne(self,n,e):
		self.n = n
		self.e = e

	def setpqe(self,p,q,e):
		self.e = e
		self.n = p * q
		self.phi_n = (p - 1) * (q - 1)
		
		if not 1 < e < self.phi_n or gcd(self.phi_n,e) != 1:
			return False

		self.d = pow(self.e,-1,self.phi_n) 
		return ((self.d * self.e) % self.phi_n == 1 )

	def exponentModulo(self,a,b,mod):
		return pow(int(a),int(b),int(mod))

	def encrypt(self,m):
		return self.exponentModulo(m,self.e,self.n)

	def decrypt(self,c):
		return self.exponentModulo(c,self.d,self.n)

	def getprivatekey(self):
		return (self.d,self.n)

	def getpublickey(self):
		return (self.e,self.n)
