# discount calculator
unit_cost=100
discount_rate=0.1
print("Enter quantity:")
quantity=int(input())

total_amount=quantity*unit_cost

if total_amount > 1000:
    discount = total_amount * discount_rate
    print("Making discount. Total Cost:" + str(total_amount-discount)+" tl")
else :
    print("Total Cost:" + str(total_amount)+" tl")