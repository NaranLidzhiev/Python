def is_isogram(string):
    
    jail_for_letters = []
    for i in range(len(string)):
        if string[i] not in jail_for_letters:
            jail_for_letters.append(string[i])
        elif string[i] in jail_for_letters:
            return False
    return True


print(is_isogram("Dermatoglyphics"))