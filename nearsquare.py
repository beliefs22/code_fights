import time
def Near_Square(n):
    if str(n**.5).endswith(".0"):
        return [int(n**.5),int(n**.5)]
    ans = [1,n]

    if n%2 == 0:
        for i in xrange(2,n/2 + 1,2):
            if n%i != 0:
                continue
            if abs((n/i) - i) < abs(ans[0]-ans[1]):
                ans = [i, n/i]
    else:
        for i in xrange(3,n/2 + 1,2):
            if n%i != 0:
                continue
            if abs((n/i) - i) < abs(ans[0]-ans[1]):
                ans = [i, n/i]
    ans.sort()
    return ans
def Near_Square2(n):
    if str(n**.5).endswith(".0"):
        return [int(n**.5),int(n**.5)]

    if str((n+1)**.5).endswith(".0"):
           return [int((n+1)**.5)-1, int((n+1)**.5) + 1]
    a = [1,n]

    def p(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n%2 == 0:
            return False
        for i in xrange(3,int(n**.5)+1,2):
            if n%i == 0:
                return False
        return True

    if p(n):
        return [1, n]

    if n%2 == 0:
        i = 2
        m = n
        while i < m:
            if n%i == 0:
                m = n/i
                if abs((n/i)-i) < abs(a[0] - a[1]):
                    a = [i, n/i]
            i += 2
    else:
        i = 3
        m = n
        while i < m:
            if n%i == 0:
                m = n/i
                if abs((n/i)-i) < abs(a[0] - a[1]):
                    a = [i, n/i]
            i += 2        
    a.sort()
    return a            
            
        
def main():
    print Near_Square2(70308224)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
