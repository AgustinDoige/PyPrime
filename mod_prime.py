#Prime Module

from math import sqrt

def addNextPrime(primeList):
	if len(primeList) < 4:
		pl = [2,3,5,7]
		primeList.append(pl[len(primeList)])
		return 
	candidate = primeList[-1]+2
	while True:
		for prime in primeList:
			if prime >= sqrt(candidate)+1:
				primeList.append(candidate)
				return
			else:
				if candidate%prime == 0:
					break
		candidate += 2

def isPrime(num):
	r_list = [2,3,5,7]
	if num < 2:
		return False
	elif num in r_list:
		return True

	for prime in r_list:
		if num%prime == 0:
			return False

	while True:
		addNextPrime(r_list)
		prime = r_list[-1]
		if prime > int(sqrt(num)+1):
			return True
		if num%prime == 0:
			return False

def directPrimeTest(n):
	if n == 2:
		return True
	elif n <= 1:
		return False
	elif n % 2 == 0:
		return False
	else:
		g = (f for f in range(3, int(sqrt(n))+1, 2))
		for value in g:
			if n % value == 0:
				return False
		return True

def getPrimeFactors(num):
	testing = num
	factors = []
	l_primes = [2,3,5,7]
	for prime in l_primes:
		while True:
			if testing == 1:
				return factors
			elif testing%prime == 0:
				factors.append(prime)
				testing = int(testing/prime)
			else:
				break

	while True:
		addNextPrime(l_primes)
		prime = l_primes[-1]
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
	l_primes = [2,3,5,7]
	for prime in l_primes:
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
		addNextPrime(l_primes)
		prime = l_primes[-1]
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

	primeL = [2,3,5,7]
	while True:
		addNextPrime(primeL)
		if primeL[-1] > limit:
			del primeL [-1]
			return primeL

def getNprimes(n):
	if n < 1:
		return None
	elif n == 1:
		return [2]
	elif n == 2:
		return [2,3]
	elif n == 3:
		return [2,3,5]
	elif n == 4:
		return [2,3,5,7]

	count = 4
	primeList = [2,3,5,7]
	for i in range(4,n):
		addNextPrime(primeList)
	return primeList
