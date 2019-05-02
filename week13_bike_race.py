# bike race problem
def meeting_distance(total_distance, speed_a, speed_b):
    distance = (total_distance * speed_a) / (speed_a + speed_b)
    return distance

total_distance = int(input("Distance between cities in km: "))
speed_a = int(input("Speed of bike 1 in km/h: "))
speed_b = int(input("Speed of bike 2 in km/h: "))

print(f'Bikes will meet at {meeting_distance(total_distance,speed_a,speed_b)}  km after city A')