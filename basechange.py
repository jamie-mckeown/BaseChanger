class BaseChange :
    
    @staticmethod
    def _basea_to_dec (num, a) :
        a = int(a)
        n = num # num is given as a string, but could be int

        if a == 10:
            dec = n
        else:
            digits = list(str(n))
            digits.reverse() # so index 0 is the 0th power of a, etc...
        
            dec = 0
            for i in range(len(digits)):
                dec += int(digits[i]) * (a**i)

        return dec


    @staticmethod
    def _dec_to_baseb (dec, b):
        if b == 10:
            n = str(dec)
        else:
            dec = int(dec)
            digits = []

            while dec != 0:
                digit = dec % b # the digit is the remainder when dividing by mod b
                digits.append(digit) # store the digit, then rescale n
                dec = dec // b # this returns essentially n/b - remainder to give the nearest whole number

            digits.reverse() # digits stores powers of 2 left to right so flip it

            #   Create a string out of the digits
            n = ''
            for digit in digits:
                n += str(digit)

        return n
    

    @staticmethod
    def basechange (num, old_base, new_base):
        '''Takes a number as a string and the base it is in, and returns the number written in the new base.'''
        a = int(old_base)
        b = int(new_base)

        #   Base case when the same base is given twice
        if a == b:
            return num
        #   Convert num from base a to decimal
        n = BaseChange._basea_to_dec(num, a)

        #   Convert num from decimal to base b
        if b == 10:
            return n 
        else:
            n = BaseChange._dec_to_baseb(n, b)
            return n
        