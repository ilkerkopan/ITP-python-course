from operator import itemgetter
d = {"ilker":90,
          "ali":10,
          "veli":40}

for w in sorted(d, key=d.get, reverse=True):
  print(w, d[w])