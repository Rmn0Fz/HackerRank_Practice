def split_and_join(line):
    # write your code here
    str = line.split(" ")
    new_str = ("-").join(str)
    return new_str

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)