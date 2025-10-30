def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1:-1]

def is_palindrome(word):
    f=first(word)
    l=last(word)
    print('f= ', f)
    print('l= ', l)
    if f==l:
        m = middle(word)
        print('m= ',m)
        if m == '':
            print('It is a palindrome!!')
            return True
        return is_palindrome(m)
    else:
        print('It is NOT a palindrome  :(')
        return False

is_palindrome('madamimadam')