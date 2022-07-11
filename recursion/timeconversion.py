s = '06:05:45AM'
if s[-2:]=='AM' and s[:2]=='12':
    print('00' + s[2:-2])
if s[-2:]=='AM' and s[:2]!='12':
    print(s[:-2])
    
if s[-2:]=='PM' and s[:2]!='12':
    print(str(int(s[:2])+12) + s[2:-2])
if s[-2:]=='PM' and s[:2]=='12':
    print(s[:-2])
    
# s = input().strip()
# h, m, s = map(int, s[:-2].split(':'))
# p = s[-2:]
# h = h % 12 + (p.upper() == 'PM') * 12
# print(h)
# print(('%02d:%02d:%02d') % (h, m, s))