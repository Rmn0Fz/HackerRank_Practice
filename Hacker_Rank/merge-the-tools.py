def merge_the_tools(string, k):
    # your code goes here
    ti = []
    len_ti = 0
    for t in string:
        len_ti += 1
        if t not in ti:
            ti.append(t)
        if len_ti == k:
            print(''.join(ti))
            ti = []
            len_ti = 0
        

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)