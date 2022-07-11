import random
from collections import Counter
check = [random.choice(['maa', 'srijita']) for i in range(14501)]
cnt = Counter(check)
print(check)
print([f'{key}: {value}' for key, value in cnt.items()])
print('you should call:', max(set(check), key = check.count))