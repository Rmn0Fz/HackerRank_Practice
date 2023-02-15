def swap_case(s):
    string = ""
    for l in s:
        if l.isupper():
            string += (l.lower())
        else:
            string += l.upper()
    return string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)