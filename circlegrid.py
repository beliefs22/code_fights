import math
import time
def circleGrid(X, Y, R):
    #distance formula
    d = lambda a,b: ((a-X)**2 + (b-Y)**2)**.5 < R
    #find all points in the smallest squre that encloses the circl
    #if the distance between a point in that squre and the center of the circle is greater
    #than the radius, then the point is outside of the circle
    p = [(x,y)
              for x in range(int(math.ceil(X-R)),int(math.floor(X+R)) + 1)
              for y in range(int(math.ceil(Y-R)),int(math.floor(Y+R)) + 1)
              if d(x,y)
              ]
    return len(p)

def main():
    print circleGrid(-3.9, -2.35, 2.4)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print end - start
    

