import time


def luckyandprime2(l,r,k):
    def isPrime(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2

        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True
    possible_primes = range(0,r + 1)
    to_check = possible_primes[l:r+1]
    primes = {
            prime : prime
            for prime in possible_primes
            if isPrime(prime)
            }
    ans = [
            1
            for num in to_check
            if len([p for p in primes if num%p == 0]) == k
            ]
    return len(ans)
    
def main():
    print luckyandprime2(1,10000,5)
    

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
