# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

string = input()
sub_str = input()

substring =  re.compile(sub_str)
res = substring.search(string)
if not res: print('(-1, -1)')
while res:
    print('({0}, {1})'.format(res.start(), res.end() - 1))
    res = substring.search(string, res.start() + 1)
