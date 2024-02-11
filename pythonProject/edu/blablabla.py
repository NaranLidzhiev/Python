def separator(arr):
    string = ""
    for i in range(len(arr)):
        if i == len(arr)-1:
            string += "and "
        string += arr[i]+" "
    return string

spam = ['apples', 'bananas', 'tofu', 'cats']
print(separator(spam))