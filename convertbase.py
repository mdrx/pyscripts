
def base10toN(num, base, digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ', endexp=-10):
    """
    Converts num (int or float expressed in base 10) to given base. 
    Bases 2-36 work fine with standard digits. If supplied with longer set of 
    digits, higher bases are also supported.
    Doesn't get scared of floats.
    """
    newstring = ''

    try:
        intnumber=int(num)
        floatnumber=num-intnumber
        while intnumber>=1:
            mod = intnumber % base
            intnumber = intnumber // base
            newstring = digits[mod] + newstring
        if floatnumber == 0: return newstring
        newstring+='.'
        currexp = -1 #starting with first 'digit' after dec point
        while currexp >= endexp:
            for newdigit in range(base):
                if((newdigit+1)*base**currexp)>floatnumber:
                    newstring += digits[newdigit]
                    floatnumber = floatnumber - newdigit*base**currexp
                    break
            currexp-=1
        return newstring
        
    except:
        raise ValueError("An error occurred. Please check your inputs")
        
def baseNto10(numstring, base, digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    """
    Converts numstring (must be string) expressed in base base to base 10. 
    Bases 2-36 work fine with standard digits. If supplied with longer set of 
    digits, higher bases are also supported.
    Doesn't get scared of floats.
    """
    newnum = 0
    point = False
    pointexp=-1
    
    try:
        for digit in numstring:
            if digit == '.': point = True
            else: 
                if point:
                    newnum += digits.index(digit)*base**pointexp
                    pointexp -= 1 
                else:
                    newnum = newnum*base+digits.index(digit)
        return newnum   
    except:
        raise ValueError("An error occurred. Please check your inputs")
