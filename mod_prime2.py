#Prime Module

from math import sqrt

class Primeset:
	def __init__(self,prSet=set()):
		if (type(prSet) != set):
			if (type(prSet) != tuple):
				if (type(prSet) != list):
					print("TYPERROR: Primeset Object must be iniciated with a list, tuple or set")
					raise TypeError

		self.primeSet = set(prSet)
		try:
			self.maxprime = max(self.primeSet)
		except ValueError:
			self.maxprime = None
		self.primeAmount = len(self.primeSet)

	def addNextPrime(self):
		if self.primeAmount < 4:
			pl = [2,3,5,7]
			self.primeSet.add(pl[self.primeAmount])
			self.primeAmount += 1
			self.maxprime = pl[self.primeAmount]
			return self.maxprime
		candidate = self.maxprime 
		while True:
			candidate += 2
			breaking = False
			for prime in self.primeSet:
				if candidate%prime == 0:
						breaking = True
						break
			if not breaking:
				self.primeSet.add(candidate)
				self.primeAmount += 1
				self.maxprime = candidate
				return self.maxprime

			# for prime in self.plist():
			# 	if prime >= int(sqrt(candidate)+2):
			# 		self.primeSet.add(candidate)
			# 		self.primeAmount += 1
			# 		self.maxprime = candidate
			# 		return self.maxprime
			# 	elif candidate%prime == 0:
			# 			break

	def __iter__(self):
		pass

	def __next__(self):
		pass

	def __contains__(self,p):
		return (p in self.primeSet)

	def plist(self,revers=False):
		return sorted(self.primeSet,reverse=revers)

	def ptuple(self,revers=False):
		return tuple(self.plist(revers))

	def plen(self):
		return self.primeAmount

	def pmax(self):
		return self.maxprime

	def copy(self):
		return Primeset(self.primeSet)

def isPrime(num,Orset=Primeset((2,3,5,7))):
	pset = Orset.copy()
	if num <= pset.maxprime:
		if num in pset.primeSet:
			return True
		return False

	for prime in pset.primeSet:
		if prime > int(sqrt(num)+2):
			return True
		if num%prime == 0:
			return False

	while True:
		pset.addNextPrime()
		prime = pset.maxprime
		if prime > int(sqrt(num)+2):
			return True
		if num%prime == 0:
			return False

def primeFactors(num,Orset=Primeset((2,3,5,7))):
	pset = Orset.copy()
	testing = num
	factors = []
	for prime in pset.primeSet:
		while True:
			if testing == 1:
				return factors
			elif testing%prime == 0:
				factors.append(prime)
				testing = int(testing/prime)
			else:
				break

	while True:
		pset.addNextPrime()
		prime = pset.pmax()
		while True:
			if testing == 1:
				return factors
			elif testing%prime == 0:
				factors.append(prime)
				testing = int(testing/prime)
			else:
				break

def primeFactorsDic(num):
	# Returns a dictionary where the factors are the keys and their values are the amount of times each factor is on the factorization
	testing = num
	factors = {}
	pset = Primeset((2,3,5,7))
	for prime in pset:
		while True:
			if testing == 1:
				return factors
			elif testing%prime == 0:
				try:
					factors[prime] = factors[prime]+1
				except KeyError:
					factors[prime] = 1
				testing = int(testing/prime)
			else:
				break

	while True:
		pset.addNextPrime()
		prime = pset.pmax()
		while True:
			if testing == 1:
				return factors
			elif testing%prime == 0:
				try:
					factors[prime] = factors[prime]+1
				except KeyError:
					factors[prime] = 1
				testing = int(testing/prime)
			else:
				break

def getPrimesUpTo(limit):
	if limit < 8:
		if limit <= 1:
			return None
		elif limit == 2:
			return [2]
		elif limit == 3:
			return [2,3]
		elif limit < 7:
			return [2,3,5]
		elif limit == 7:
			return [2,3,5,7]

	primeS = Primeset((2,3,5,7))
	while True:
		primeS.addNextPrime()
		if primeS.pmax() > limit:
			return Primeset(primeS.plist()[:-1])

def getNprimes(n):
	if n < 1:
		return None
	if n < 5:
		if n == 1:
			return [2]
		elif n == 2:
			return [2,3]
		elif n == 3:
			return [2,3,5]
		elif n == 4:
			return [2,3,5,7]

	primeS = Primeset((2,3,5,7))
	for i in range(4,n+1):
		primeS.addNextPrime()
	return primeS
