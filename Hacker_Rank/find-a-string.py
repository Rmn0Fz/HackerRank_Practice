def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string) - len(sub_string) + 1):
        if string[i] == sub_string[0]:
            f = 1
            for j in range(0, len(sub_string)):
                if string[i+j] != sub_string[j]:
                    f = 0
                    break
            if f == 1:
                counter += 1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)