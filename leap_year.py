def is_leap(year):
    '''
    function takes 1 arg which a year an integer type
    
    and it tells whether its a leap year or not
    '''
    leap =  True if year%4 == 0 and (year%100 != 0 or year%400 == 0) else False
    return leap


year = int(input())
print(is_leap(year))