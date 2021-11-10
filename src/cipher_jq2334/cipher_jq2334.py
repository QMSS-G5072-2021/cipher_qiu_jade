def cipher(text, shift, encrypt=True):
    """
    Encrypts and decrypts codes using the Caesar cipher

    Parameters
    ----------
    text : code to encrypt or decrypt
    shift :  the number of places shifted down the alphabet for this particular encrypted / decrypted code
    encrypt : boolean to indicate whether function should be used to encrypt or decrypt text

    Returns
    -------
    new_text
      the encrypted (if encrypt = True) or decrypted (if encrypt = False) message

    Examples
    --------
    >>> from cipher_jq2334 import cipher
    >>> cipher('Hello', 1, encrypt = True)
    ['Ifmmp']
    >>> cipher('Ifmmp', 1, encrypt = False)
    ['Hello']
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text