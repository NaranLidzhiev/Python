def is_pangram(s):
    alfabet = "abcdefghijklmnopqrstuvwxyz"
    s = s.lower()
    temp = []
    for i in range(len(s)):
        if s[i] in alfabet and s[i] not in temp:
            temp.append(s[i])
    print(temp)
    if (len(temp) == 26):
        return True
    return False

is_pangram("jsadlasndcaskjcnjaslcmslasdkmefbdijnaksDDDDZZZm")
print(is_pangram("The quick, brown fox jumps over the lazy dog!)"))