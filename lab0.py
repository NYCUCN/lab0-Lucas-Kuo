def myFunction():
    '''
    Write a Python function that return the sum of every digit of your student ID
    And print the answer before you return
    You can write in python2 or python3 :D
    '''
    ID = "109550162"
    sum = 0
    for digit in ID:
        try:
            sum += int(digit)
        except:
            pass
    

    return sum


if __name__ == '__main__':
    myFunction()
