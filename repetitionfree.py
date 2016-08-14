def repetitionFree(n):
    if n = 1:
        return 1
    c = 1
    s = 2
    current_sum = 1
    while True:
        g = lambda x, i: x[i] in x[i+1:]
        body = str(s)
        if "0" in body:
                s += 1
                continue
        if s < 10:
                current_sum += s
                c += 1
                if c == n:
                    body = str(current_sum)
                    if "0" not in bod
                    for i in range(len(body)):
                        if g(body,i)
        if c == n:
            body = str(current_sum)
            for i in range(len(body)):
                if g(body,i):
                    while True:
                        
