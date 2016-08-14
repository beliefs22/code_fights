import time
def completewords(word,fragments):
    #fragments = [fragment for fragment in fragments if fragment in word]
    possible_solutions = [[""]]
    all_solutions = []
    while possible_solutions != []:
        #print possible_solutions, "new loop"
        possible_solutions = [
                solution + [fragment]
                for solution in possible_solutions[:]
                for fragment in fragments
                if word.replace("".join(solution),"").startswith(fragment)
                ]
        for solution in possible_solutions:
            if "".join(solution) == word:
                all_solutions.append(len(solution))


    return min(all_solutions) - 1

def main():
    word = "July 15, 1993"
    fragments =["July ", 
     "51", 
     "3991", 
     "3", 
     ", ", 
     "19", 
     "9", 
     "J", 
     "1", 
     "5", 
     "15", 
     "u", 
     "l", 
     "y"]
    

    print completewords(word,fragments)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
            
        
    
    
                
                    
