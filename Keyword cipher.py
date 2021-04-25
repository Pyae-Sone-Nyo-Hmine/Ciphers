def encode_keyword(string, keyword):
    ''' Encodes the specified `string` using a Keyword cipher with keyword `keyword`.
    
        Parameters
        ----------
        string : str
            The string to encode.
        
        keyword : str
            The keyword to use in the substitution alphabet.

       '''
    
    keyword = keyword.replace(" ", "")
    ret = ""

    for lett in keyword:
        if lett in ret:
            pass
        else:
            ret = ret + lett
    
    ordinary = "abcdefghijklmnopqrstuvwxyz"
    abc_string = "abcdefghijklmnopqrstuvwxyz"
    for lette in ret:
        abc_string = abc_string.replace(lette, "")
    
    decoded_string = ret + abc_string
    
    answer = ""
    for keys in string:
        if keys in ordinary:
            location = ordinary.find(keys)
            new = decoded_string[location]
            answer = answer + new
        else:
            answer = answer + keys
            
    return answer