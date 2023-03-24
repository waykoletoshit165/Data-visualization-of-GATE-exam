num_forces = int(input("Enter the number of forces present in question: "))

forces = []
distances = []
directions = []

for i in range(num_forces):
    force = int(input(f"Enter the value of force {i+1} (in Newton): "))
    distance = int(input(f"Enter the perpendicular distance between force {i+1} and point (in mm): "))
    direction = input(f"Enter the direction of force {i+1} (clockwise or anticlockwise): ")
    forces.append(force)
    distances.append(distance)
    directions.append(direction)

moment = 0
for i in range(num_forces):
    if directions[i] == "clockwise":
        moment += forces[i] * distances[i]
    elif directions[i] == "anticlockwise":
        moment -= forces[i] * distances[i]
    else:
        print("You entered something wrong.")
        break

print(f"The moment about point = {moment} N-mm")