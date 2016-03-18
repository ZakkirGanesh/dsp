# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    if count >= 10:
        return("Number of donuts: many")
    else:
        return("Number of donuts: %s" % count)

    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    raise NotImplementedError

def both_ends(s):
    if len(s) < 2:
        return ""
    else:
        return s[:2] + s[-2:]

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    raise NotImplementedError
    
def fix_start(s):
    letters = list(s)
    i = 1
    while i < len(letters):
        if letters[i] == letters[0]:
            letters[i] = "*"
        i += 1
    return "".join(letters)

    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    raise NotImplementedError


def mix_up(a, b):
    a1 = a[:2]
    a2 = a[2:]
    b1 = b[:2]
    b2 = b[2:]
    b1a2 = b1 + a2
    a1b2 = a1 + b2
    return b1a2 + " " + a1b2

    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    raise NotImplementedError


def verbing(s):
    if len(s) < 3:
        return s
    else:
        if s[-3:] == "ing":
            return s + "ly"
        else:
            return s + "ing"

    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swiming')
    'swimingly'
    >>> verbing('do')
    'do'
    """
    raise NotImplementedError


def not_bad(s):
    not_substr = " not "
    bad_substr = " bad"
    if not_substr in s:
        s_not_index = s.find(not_substr)
        front_s = s[:s_not_index]
        back_s = s[s_not_index:]
        if bad_substr in back_s:
            s_bad_index = back_s.find(bad_substr) + 4
            not_bad_substr = back_s[:s_bad_index]
            new_back_s = back_s.replace(not_bad_substr, "good")
            return front_s + " " + new_back_s
        else:
            return s
    else:
        return s

    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'

    >>> not_bad('This movie is not so bad')
    'This movie is good'
    >>> not_bad('This dinner is not that bad!')
    'This dinner is good!'
    >>> not_bad('This tea is not hot')
    'This tea is not hot'
    >>> not_bad("It's bad yet not")
    "It's bad yet not"
    """
    raise NotImplementedError


def front_back(a, b):
    if len(a) % 2 == 0:
        if len(b) % 2 == 0:
            return(a[:int(len(a)/2)]+b[:int(len(b)/2)]+a[int(len(a)/2):]
                    +b[int(len(b)/2):])
        else:
            return(a[:int(len(a)/2)]+b[:int(len(b)//2 +1)]+a[int(len(a)/2):]
                    +b[int(len(b)//2 +1):])
    else:
        if len(b) % 2 == 0:
            return(a[:int(len(a)//2 +1)]+b[:int(len(b)/2)]+a[int(len(b)//2 +1):]
                    +b[int(len(b)/2):])
        else:
            return(a[:int(len(a)//2 +1)]+b[:int(len(b)//2 +1)]
                    +a[int(len(b)//2 +1):]+b[int(len(b)//2 +1):])

    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back

    >>> front_back('abcd', 'xy')
    'abxcdy'
    >>> front_back('abcde', 'xyz')
    'abcxydez'
    >>> front_back('Kitten', 'Donut')
    'KitDontenut'
    """
    raise NotImplementedError
