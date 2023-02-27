"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.

#fibonacci function
def foo(x):
   a = 0
   b = 0
   if x <= 1:
        return x
   else:
        a = (foo(x-1))
        b = (foo(x-2))
    pass

def longest_run(mylist, key):
    ### TODO
    longestvalue = 0
    currentvalue = 0
    for i in range(len(mylist)):
        if mylist[i] == key:
            currentvalue +=1
            if currentvalue <= longestvalue:
                longestvalue = longestvalue
            if currentvalue >= longestvalue: 
                longestvalue = currentvalue ##could also use a find the maximum function here instead of two if statements 
         else: 
            currentvalue = 0
     return longestvalue
    pass


class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size               # run on left side of input
        self.right_size = right_size             # run on right side of input
        self.longest_size = longest_size         # longest run in input
        self.is_entire_range = is_entire_range   # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))
    
    
def longest_run_recursive(mylist, key):
    ### TODO
    #need to take max of left side, then max of right side and then combine them 
    #if the longest span CROSSES where we divide the list we also need to account for that
    if len(mylist) ==1: 
        if mylist[0] == key: #best case scenario 
            return 1
        else:
            return 0
     midsized = len(mylist) // 2 #split the list into two
     leftresult = longest_run_recursive(mylist[:mid], key) # right side
     rightresult = longest_run_recursive(myarray[mid:}, key) # left side
     midresult = crosses(mylist, mid, key)
 def crosses(mylist, mid, key):
     left_size = 0
     right_size = 0
     longest_size = 0
     overeverythingmax = 0
     
     left_sum = 0 #find left sum
     for i in range(mid-1, -1, -1):
        if mylist[i] == key:
            left_size += 1
            left_size = max(left_size, left_sum)
        else:
            left_sum = 0

    right_sum = 0 #find right sum
    for i in range(mid, len(mylist)):
        if mylist[i] == key:
            right_sum += 1
            right_size = max(right_size, right_sum)
        else:
            right_sum = 0

    max_with_mid = left_size + right_size
    if mylist[mid] == key:
        max_with_mid += 1
    
    total_max = max(left_size, right_size, longest_size)
     return Result(left_size, right_size, total_max, max_with_mid)

  def combineeverything(leftresult, rightresult, midresult): #combine results to find the actualmaximum continous sequence
        total_max = max(leftresult.total_max, rightresult.total_max, midresult.total_max
        return Result(leftresult.left_max, rightresult.right_max, total_max, midresult.max_with_mid)
    pass

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3


