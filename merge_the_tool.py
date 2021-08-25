def merge_the_tools(string, k):
    """
    this function takes 2 args. 
    1st arg is a string
    2nd arg is a integer
    
    function will divide the string depending to 2nd arg the user input
    """
    for i in range(0,len(string),k): 
        part = list(string[i:i+k])
        li = []
        [li.append(a) for a in part if a not in li]
        print("".join(li))
      
      
      
        
"""
Sample Input

STDIN       Function
-----       --------
AABCAAADA   string = 'AABCAAADA'
3           k = 3

Sample Output

AB
CA
AD
        
"""
merge_the_tools('LOOLTANN',4)