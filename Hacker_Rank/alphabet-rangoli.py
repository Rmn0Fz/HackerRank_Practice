
def print_rangoli(size):
    # your code goes here
    import string
    alphabet = string.ascii_lowercase
    
    L = []
    for i in range(size):
        s = "-".join(alphabet[i:size])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        
    print("\n".join(L[:0:-1] + L))
        
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)