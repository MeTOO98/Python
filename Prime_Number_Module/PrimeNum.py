

def prime_num1(num) :
    """
    This Function Takes a number and checks if it is prime or not 
    """
    if num < 0 :
        num = num * -1 
    if num == 0 :
        return False 
    for i in range (2,num) :
        if num % i ==0 :
            return False
    else :
        return True


# more optimized Function  

def prime_num2(num) :
    """
    This Function Takes a number and checks if it is prime or not 
    """
    if num < 0 :
        num = num * -1 
    if num ==4 or num ==-4 :
        return False 
    if num == 0 :
        return False 
    for i in range (2,num//2) :
        if num % i ==0 :
            return False
    else :
        return True
    

