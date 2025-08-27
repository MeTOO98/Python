
def even_odd1(num) :
    """ This Function uses remainder to Know if it is Even or Odd
    """
    if num ==0 :
        print("number is Zero")
    elif num % 2==0 :
        print("number is Even")
    else :
        print("number is Odd")

def even_odd2(num):
    """ This Function uses The first bit in The number to Know if it is Even or Odd 
    """
    if num == 0:
        print("number is Zero")
    elif (num & 1) ==1 :
        print("number is Odd")
    else :
        print("number is Even")

