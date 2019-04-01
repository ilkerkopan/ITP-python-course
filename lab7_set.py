set1 = set("Basketbol THY Avrupa Ligi'nde 27. hafta maçlarının ardından Anadolu Efes ile İspanyol temsilcisi Barcelona Lassa play-off’a kalmayı garantiledi".split(" "))
set2= set("THY Avrupa Ligi'nde Anadolu Efes play-off'u garantiledi Ligde 27. hafta maçlarının ardından Anadolu Efes Barcelona Lassa play-off'a kalmayı garantiledi".split(" "))

print(set1 | set2)
print(set1 & set2)
print(set1 ^ set2)
print(set1 - set2)