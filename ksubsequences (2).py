import pickle
def ksubsequences(k, nums):
    found = {"[]":True}
    if sum(nums)%k == 0:
        found[str(nums)] = True
    for i in range(0,len(nums)+1):
        for j in range(len(nums)):
            if i + j < len(nums):
                base = nums[j:j+i]
                leftover = nums[j+i]
                if str(base) in found:
                    if j+i < len(nums):
                        if leftover%k == 0:
                            found[str(base+[leftover])] = True
                            continue
                else:
                    ans = nums[j:j+i+1]
                    if sum(ans)%k == 0:
                        found[str(ans)] = True
                        continue
    return len(found)-1

def main():
    k = 25
    testfile = open('test.txt','r')
    nums = pickle.load(testfile)
    nums = [int(num) for num in nums]
    print nums[100:110]
    
    print ksubsequences(k, nums)

if __name__ == "__main__":
    main()
