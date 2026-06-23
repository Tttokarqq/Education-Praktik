import re

s = input().strip()
pattern = r'^[A-Z]\d{3}[A-Z]{2}$'
if re.match(pattern, s):
    print("Yes")
else:
    print("No")