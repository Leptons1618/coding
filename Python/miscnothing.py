import re

s = 'A quick brown foX jumps over the lazy dog'
t = 'fox'
r = 'LioN'

ch = re.sub(t, r.capitalize(), s,flags=re.IGNORECASE)
print(ch)