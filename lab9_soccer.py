def read_file(filename):
    file = open(filename)
    goal_difference = {}
    for line in file:
        line_values = line.split()
        if len(line_values) >= 9:
            goal_difference[line_values[1]] = abs(int(line_values[6]) - int(line_values[8]))
    return goal_difference

min_diff = 100
team_difference = read_file("football.dat")
for name, diff in team_difference.items():
    if diff < min_diff:
        min_diff = diff
        team_name = name

print(f'{team_name} {min_diff}')