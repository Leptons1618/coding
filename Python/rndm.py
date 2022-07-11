import random
print(("Call Maa. Maa se badkar koi naa", "Srijita ke call koro")[(sum(random.uniform(0, 1) for _ in range(14501)) / 14501)>0.5])