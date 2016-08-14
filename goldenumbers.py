import time
def GoldeNumbers(n):
    found = {}
    pos = 1
    c = 0
    while c < n:
        if pos == 1 or pos == 2 or pos == 3 or pos == 5:
            found[pos] = "Allowed"
            c += 1
            pos += 1            
            continue
        if pos%2 != 0 and pos%3 !=0 and pos%5 != 0:
            pos += 1
            continue
        if found.get(pos/2) or found.get(pos/3) or found.get(pos/5):
            found[pos] = "Allowed"
            c += 1
            pos += 1
            continue
        pos += 1
    return pos - 1

def main():
    print GoldeNumbers(11)

if __name__ =="__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
    
