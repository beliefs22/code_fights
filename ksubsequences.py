import time
def ksubsequences(k, nums):
    c = 0
    if sum(nums)%k == 0:
        c += 1
    for i in range(len(nums)+1):
        for j in range(len(nums[i+1:])+2):
            ans = nums[i:i+j]
            print ans
            if sum(ans)%k == 0 and sum(ans) != 0:
                c += 1

    return c
            

def main():
    k = 3
    
    nums =[1,2,3,4,1]

    print ksubsequences(k, nums)

if __name__ =="__main__":
    start = time.time()
    main()
    end = time.time()
    print end-start
    
