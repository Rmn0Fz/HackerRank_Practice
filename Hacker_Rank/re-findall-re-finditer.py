# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

vow = 'aeiou'
cons = 'qwrtypsdfghjklzxcvbnm'

match = re.findall(r'(?<=[' + cons + '])([' + vow + ']{2,})(?=[' + cons + '])', input(), flags=re.I)
print("\n".join(match or ['-1']))
