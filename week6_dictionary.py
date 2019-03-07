# create dictionary and assign value
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car["brand"])
print(car.get("brand"))
car["brand"]="BMW"
print(car.get("brand"))

for key,value in car.items() :
    print(key + " is " + str(value))
