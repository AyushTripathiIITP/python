def is_leap(year):
    leap = False
    
    # Write your logic here
    if(year / 4 != year //4):
        return leap
    elif(year / 100 == year // 100 and year / 400 != year //400):
        return leap
    elif(year / 4 == year // 4):
        return True 
 
year = int(input())