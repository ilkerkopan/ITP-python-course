# find fibonacci numbers using for loop
fibonacci=[0,1]
for index in range(2,10):
    fibonacci.append(fibonacci[index-2]+fibonacci[index-1]) 
    
for index in range(10):
    print(fibonacci[index])