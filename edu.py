def solution(text, ending):
    t = False
    last_occurence = text.rfind(ending)
    if (len(ending) > len(text)):
        return False

    d = last_occurence+len(ending)
    z = len(text)

    print(d)
    print(z)
    if (d == z):
        t = True
   
    return t

solution("abc", "abcd")