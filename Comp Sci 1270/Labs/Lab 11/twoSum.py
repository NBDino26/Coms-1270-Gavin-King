# Gavin King            12/11/2025

# Two Sum programs

# Citation for the article on twoSum: 
# Wagner, T., & Platt, D. (n.d.). Two sum (interview solution). 
#   Two Sum (Interview Solution). https://interviewing.io/questions/two-sum#solution1 

def twoNumLoops(a,b):
   result ="N/A"
   for i in a:
       for j in range(i+1,len(a)):
           if i + j == b:
               result = str(i)+ "+" + str(j) 
               break
   return result

def twoNumDict(a,b):
    result = "N/A"
    index = {}
    for i in range(0, len(a)):
        add = b - a[i]
        if add in index:
            result = str(add) + "+" + str(a[i])
        index[a[i]] = i
    return result
        

def main():
    nums = [4,5,6,10,2,8]
    target_Num = 9
    answer1 = twoNumLoops(nums, target_Num)
    answer2 = twoNumDict(nums, target_Num)
    print(answer1)
    print(answer2)


if __name__ == "__main__":
    main()