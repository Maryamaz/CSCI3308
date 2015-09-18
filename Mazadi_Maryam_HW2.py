import random
import math
from fractions import gcd

def isPrime(x):
  if (x == 1) or (x == 2):
    return 1;
  result = 1;
  for i in range(2, int(math.ceil(x**0.5)+1)):
    if( (x % i) == 0 ):
      result = 0;
      break;
  return result;



#for j in range(1, 100):
#  print "%d is prime? %d", j, isPrime(j)

n = 7;
primes = [i for i in range(2**(n-1), (2**n)-1) if isPrime(i)]
print primes;

p = random.choice(primes);
q = random.choice(primes);
print "p = %d, q = %d" % (p, q)

N = p*q;
#print "N = %d"% N;
for i in range(2, (p-1)*(q-1)):
  if(gcd(i, (p-1)*(q-1)) == 1):
    e = i;
    break;
#print "e = %d" % e;
print "Public key = (N, e) = (%d, %d)" % (N, e);
Q = (p-1)*(q-1);
for i in range(0, Q):
  if(i*e%Q == 1):
    d = i;
    print "d = %d" % d
    break;

print "Private key = d = %d" % d;

print (d*e)%((p-1)*(q-1))

x = 2015;
print "Encrypt = E(x) = y = %d" % ( x**e % N);
y = (x**e % N);
print "Decrypt = D(y) = x = %d" % (y**d % N);
