import random
import math

#To generate random prime less than N
def randPrime(N):
	primes = []
	for q in range(2,N+1):
		if(isPrime(q)):
			primes.append(q)
	return primes[random.randint(0,len(primes)-1)]

# To check if a number is prime
def isPrime(q):
	if(q > 1):
		for i in range(2, int(math.sqrt(q)) + 1):
			if (q % i == 0):
				return False
		return True
	else:
		return False

#pattern matching
def randPatternMatch(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatch(q,p,x)

#pattern matching with wildcard
def randPatternMatchWildcard(eps,p,x):
	N = findN(eps,len(p))
	q = randPrime(N)
	return modPatternMatchWildcard(q,p,x)

######################################################################## Helper Functions Start ##########################################################################
def val(alphabet):		#returns the value asigned to the alphabet character ///  Constant time.
	set="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for i in range(26):
		if alphabet==set[i]:
			return i

######################################################################## Helper Functions End ##########################################################################

# return appropriate N that satisfies the error bounds
def findN(eps,m):
	'''
	Probability of f_substring mod q= f_pat mod q is basically probability of q being a prime factor of (f_substriing - f_pat).
	Maximum number of such q are log|(f_substriing - f_pat)|/log(2) (claim 1). Total number of q less than N are Nlog2/(2logN) (claim 2).
	Thus the probability that this happens is (log|(f_substriing - f_pat)|/log2)*2logN/Nlog2. 
	|(f_substriing - f_pat)| is an 'm' digit '26 ary' number which is always less than 26^m.
	thus this probability is less than (mlog26/log2)*2logN/Nlog2. This probability has to be less than eps. so we get the inequality (mlog26/log2)*2logN/Nlog2 < eps for satisfying the condition of controlling error below eps.
	We find that chosing N=(m/eps)*ln(m/eps)*501 satisfies this error probability condition for a safe bound of m/eps>2 (verified by plugging in the expression)
	and chosing a safe value of N= 501 satisfies the condition for m/eps<2 (verified by pluggin in the values).  
	'''
	if m/eps<2:
		return 501
	else:
		N=(m/eps)*math.log(m/eps)*501
	return N

# Return sorted list of starting indices where p matches x
def modPatternMatch(q,p,x):
	m=len(p)					#O(1) time, O(logm) space
	n=len(x)					#O(1) time, O(logn) space

	#calculating h(pattern)=f(pattern)mod q
	hp=0
	for i in range(m):					#O(mlogq) time at the end of all iterations, O(logq) space for hp
		hp=(hp*(26%q)+val(p[i])%q)%q	#O(logq) time each

	#calculating h(text)=f(text)mod q for first m characters	
	hx=0								
	for i in range(m):					#O(mlogq) time at the end of all iterations, O(logq) space for hx
		hx=(hx*(26%q)+val(x[i])%q)%q	#O(logq) time each

	L=[]						#initializing list. O(k) space depending on number of matches.
	cur=0						#initializing cursor. O(logn) space as cursor goes till n.
	#storing (26 ^ m) mod q.       /// O(mlogq) , O(logq) space. 
	msb=1
	for pow in range(m):
		msb=(msb*26)%q
	
	for cur in range(n-m):				#computing and comparing f mod q for each index. #O((n-m)logq) time at the end of all aterations. hx takes O(logq) space
		if hx==hp:						
			L.append(cur)
		hx=(hx*(26%q)+val(x[cur+m])%q-msb*(val(x[cur])%q))%q		#O(logq) time each
	if hx==hp:
		L.append(cur+1)
	return L
'''
Thus the total time and space complexity is the sum of individual time and space complexities which comes out to be O((m+n)logq) for time and O(k+logn+logq) for space. Note that it is given n>=m.
'''

# Return sorted list of starting indices where p matches x
def modPatternMatchWildcard(q,p,x):
	m=len(p)		#O(1) time, O(logm) space
	n=len(x)		#O(1) time, O(logn) space

	#calculating h(pattern)=f(pattern)mod q
	hp=[0]*26				
	for i in range(m):									#O(mlogq) time at the end of all iterations, O(logq) space for hp
		if p[i]!="?":
			for k in range(26):
				hp[k]=(hp[k]*(26%q)+val(p[i])%q)%q		#O(logq) time each
		else:
			for k in range(26):
				hp[k]=(hp[k]*(26%q)+k%q)%q				#O(logq) time each

	#calculating h(text)=f(text)mod q for first m characters	
	hx=0
	for i in range(m):									#O(mlogq) time at the end of all iterations, O(logq) space for hx
		hx=(hx*(26%q)+val(x[i])%q)%q					#O(logq) time each

	L=[]						#initializing list		O(k) space depending on number of matches.
	cur=0						#initializing cursor	O(logn) space as cursor goes till n.
	#storing (26 ^ m) mod q.       /// O(mlogq) time, O(logq) space. 
	msb=1
	for pow in range(m):
		msb=(msb*26)%q
	for cur in range(n-m):		#computing and comparing f mod q for each index. #O((n-m)logq) time at the end of all aterations. hx takes O(logq) space
		if hx in hp:
			L.append(cur)
		hx=(hx*(26%q)+val(x[cur+m])%q-msb*(val(x[cur])%q))%q	#O(logq) time each
	if hx in hp:
		L.append(cur+1)
	return L
'''
Thus the total time and space complexity is the sum of individual time and space complexities which comes out to be O((m+n)logq) for time and O(k+logn+logq) for space. Note that it is given n>=m.
'''
################################################################################ Input Output Start ##########################################################################
#print(modPatternMatch(1000000007, "CD", "ABCDE"),[2])
#print(modPatternMatch(1000000007, "AA", "AAAAA"),[0, 1, 2, 3])
#print(modPatternMatchWildcard(1000000007, "D?", "ABCDE"),[3])
#print(modPatternMatch(2, "AA", "ACEGI"),[0, 1, 2, 3])
#print(modPatternMatchWildcard(1000000007, "?A", "ABCDE"),[])

#print(modPatternMatch(1000, "DW" , "ABCDWEDUHDW"))

################################################################################# Input Output End ###########################################################################