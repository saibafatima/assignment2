# Q5. Create a generator function for prime numbers less than 1000. Use the next() method to print the
# first 20 prime numbers.

def generate_primes():
    num = 2
    primes = []
    while True :
        is_prime = True
        for prime in primes:
            if num % prime == 0 :
                is_prime = False
                break
        if is_prime :
            primes.append(num)
            yield num 
        num += 1

# using generator function 
prime_generator = generate_primes()

#printing 1st 20 prime numbers 
for i in range(20):
    prime = next(prime_generator)
    print(prime)
