
def M_pyramid_sh1 (h) :
    """ This Function takes The height of a Pyrmaid as input and prints a pyramid like This 
             *
           * *
         * * *
    as output 
    and h is the number of rows in The pyramid """
    for i in range(1,h+1) :
        print(" "*(h-i)+"*"*i)


def M_pyramid_sh2 (h) :
    """ This Function takes The height of a Pyrmaid as input and prints a pyramid like This
        * * *
        * *
        * 
        as output and h is the number of rows in The pyramid 
        """
    for i in range(h) :
        print("*"*(h-i)+" "*i)


def M_pyramid_sh3 (h) :
    """ This Function takes The height of a Pyrmaid as input and prints a pyramid like This 
        * * *
          * *
            *
        as output and h is the number of rows in the pyramid"""
    for i in range(h) :
        print(" "*i+"*"*(h-i))


def M_pyramid_sh4_list(h) :
    """ This Function takes The height of a Pyrmaid as input and prints a pyramid like This 
        * * *
        * *
        * 
    as output by using list 
    and h is the number of rows in The pyramid """
    l=["*"]*h
    print("".join(l))
    for i in range(1,h+1) :
        l.pop(0)
        l.append(" ")
        print("".join(l))


        









