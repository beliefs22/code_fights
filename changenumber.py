def changumangu223(n):
    max_2 = n/2
    edge = {0:0,1:0,2:1,3:1}
    if n in edge:
        return edge[n]
    max_2 = loops(max_2,n,2,3)
    max_3 = max_2/3
    max_3 = loops(max_3,max_2*2,3,2)
    return max_3 + 1

def loops(max_n, n, m, mod):
    while max_n != 0 and n%(max_n*m) != 0 and n%(max_n*m)%mod != 0:
        print max_n
        max_n -= 1
    return max_n

def nested(n):
    solutions = [sum([2]*i+[3]*j)
                 for i in range(0,n/2 + 1)
                 for j in range(0,n/3 + 1)
                 if sum([2]*i+[3]*j) == n
                 ]
    return len(solutions)
            
def main():
    myn = int(raw_input("what is your nber? "))
    print nested(myn)

if __name__ == "__main__":
    main()
