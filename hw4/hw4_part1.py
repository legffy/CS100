import hw4_util
"""
Code determines the strength of ones password based on certain attributes
Positives:Length,amount of uppercase and lowercase letters, amount of digits, and whether or not they have certain characters
Negatives: If password ressembles or license plate or is in the common list of passwords
"""
#this function adds to a passwords strength score based on attributes
# p is short for password
# count will end up being the score at the end
# returns count at end
def passwordPositive(p,count):
# puncs are considered special characters
    punc1 = ['!', '@', '#', '$']
    punc2 = ['%', '^', '&', '*']
# u stands for uppercase count
    u = 0
# l stands for lowercase count
    l = 0
# d stands for digit count
    d = 0

#this next section of code adds to count based on the password length
#length 6 or 7: +1
#length between equal or between 8 and 10: +2 
#length greater than 10: +3
    if len(p) == 6 or len(p) == 7:
        count += 1
        print('Length: +1')
    elif len(p) >= 8 and len(p) <= 10:
        count += 2
        print('Length: +2')
    elif len(p) > 10:
        count += 3
        print('Length: +3')

# this section of code checks the amount of lower and upper case letters and then adds to the score based off these numbers
# 2 > count of upper and lower > 0: +1
# count of upper and lower > 1 : +2  
    for x in p:
        if x.isupper(): u+=1
        if x.islower(): l+=1
    if u > 1 and l > 1: 
        count += 2
        print('Cases: +2')
    elif u > 0 and l > 0:
        count +=1
        print('Cases: +1')

# this section of code checks the amount of digits and assigns a score based off that
# if there is 1 digit: +1
# if there is more than 1 digit: +2
    for x in p:
        if x.isdigit(): d+=1
    if d == 1: 
        count += 1
        print('Digits: +1')
    elif d > 1: 
        count += 2
        print('Digits: +2')

# this section of code checks if any of certain characters are in the code
# if !@#$ exists: +1
# if %^&* exists: +1

    if any(x in p for x in punc1):
        count += 1
        print('!@#$: +1')
    if any(z in p for z in punc2):
        count += 1
        print('%^&*: +1')
    return count

#this function subtracts from a passwords strength score based on attributes
# p is short for password
# count will end up being the score at the end
# returns count at endx
def passwordNegative(p,count):
# check is used to see whether or not something is a license plate
    check = 0
# l100 is just a list of the top 100 most common passwords
    l100 = hw4_util.part1_get_top()
# checks if the first three characters are in the alphabet and if the four precceding are digits to match them to a license plate
# if it is a license plate then we subtract 2 from count
    for x in p:
        if check < 3:
            if x.isalpha(): 
                check += 1
            else:
                check = 0
        elif check >= 3:
            if x.isdigit(): 
                check += 1
                if check == 7:
                    count -=2
                    check = 0
                    print('License: -2')
            else: check = 0

# this section of code checks if the given password is the top 100 most common passwords
# if the password is denoted as common: +3    
    for x in l100:
        p=p.lower()
        if p == x:
            count -=3
            print('Common: -3')
    return count

# based on a given score rates the password
def scoreReport(s):
    if s<=0: return 'rejected'
    elif s<=2: return 'poor'
    elif s<=4: return 'fair'
    elif s<=6: return 'good'
    else: return 'excellent'
if __name__ == "__main__":
    score = 0
    password = input('Enter a password => ')
    print(password)
    score = passwordPositive(password,score) + passwordNegative(password,score)
    print('Combined score: {0}'.format(score))
    print('Password is {0}'.format(scoreReport(score)))