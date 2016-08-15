
def soccerSuperstition(n, k, t):

    pos_d = {
            (i,j):(i,j)
            for i in range(10)
            for j in range(10)
            if i + j > t
            }

    digits = { item
              for row in pos_d
              for item in row
              }

    pos_n = {
            (i,j):(i,j)
            for i in range(min(digits),max(digits)+1)
            for j in range(min(digits), max(digits)+1)
            if abs(i - j) < k
            }
    print pos_n

    all_n ={
            (i,j):(i,j)
            for i in pos_n
            for j in pos_n
            if i[1] + j[0] > t
            }
    print all_n
    
    equal = lambda x,y: x[-1] == y[0] and (y[1], x[0]) in all_n
    add = lambda x,y: tuple(list(x) + [y[1]])
    
    all_coms = {
                add(i,j)
                for i in all_n
                for j in all_n
                if equal(i,j)
            }
    
    count = 3
    while count < n:
        count += 1
        all_coms = {
                    add(i,j)
                    for i in all_coms
                    for j in all_n
                    if equal(i,j)
                    }

    return len(all_coms)

def main():
    print soccerSuperstition(4,2,16)

if __name__ =="__main__":
    main()
