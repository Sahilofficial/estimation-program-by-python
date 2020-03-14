
from statistics import mean
est = [191, 561, 942, 608, 236, 107, 294, 793, 378, 84, 303, 638, 130, 997, 321, 548, 169, 216]
est.sort()
tv = int(0.1*len(est))
est = est[tv:]
est = est[:len(est)-tv]
print(mean(est))