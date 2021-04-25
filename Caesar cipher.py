def encode_caesar(string, shift_amt):
    ''' Encodes the specified `string` using a Caesar cipher with shift `shift_amt`
    
        Parameters
        ----------
        string : str
            The string to encode.
        
        shift_amt : int
            How much to shift the alphabet by.
        
       '''
       
    answer = ""

    for i in range(len(string)):
        letter = string[i]

        if (letter.isupper()):
            if (ord(letter) + shift_amt) <= 90:
                answer += chr((ord(letter) + shift_amt ))
            elif (ord(letter) + shift_amt) > 90 and (ord(letter) + shift_amt + 6) <= 122:
                answer += chr((ord(letter) + shift_amt + 6))
            elif (ord(letter) + shift_amt + 6) > 122:
                answer += chr((ord(letter) + shift_amt -52))


        if (letter.islower()):
            if (ord(letter) + shift_amt) <= 122:
                answer += chr((ord(letter) + shift_amt ))
            elif (ord(letter) + shift_amt) > 122 and (ord(letter) + shift_amt) <=148 :
                answer += chr((ord(letter) + shift_amt - 52-6))
            elif (ord(letter) + shift_amt) > 148:
                answer += chr((ord(letter) + shift_amt - 52))


        if (letter.isspace()):
            answer += string[i]

        if (letter.isnumeric()):
            answer += string[i]

    return answer
