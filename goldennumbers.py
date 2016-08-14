def GoldeNumbers(n):
    def check(num):
        if num == 1 or num == 2 or num == 3 or num == 5:
            return True
        if num%2 != 0 and num%3 != 0 and num%5 != 0:
            return False
        if num%2 == 0:
            return check(num/2)
        if num%3 == 0:
            return check(num/3)
        if num%5 == 0:
            return check(num/5)
    start = 1
    c = 0
    while True:
        if check(start):
            print start
            c += 1
            if c == n:
                return start
        start +=1
    return start

def main():

    print GoldeNumbers(30)


if __name__ == "__main__":
    main()
