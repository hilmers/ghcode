
def parse_dataset(data):

	rows, cols, cars, nbr_rides, bonus, steps = map(int, data.readline().strip().split())

	rides = []
	car_a = [True] * cars
	car_p = [(0,0)] * cars

	for ride in range(nbr_rides):
		row_start, col_start, row_fin, col_fin, start, finish = map(int, data.readline().strip().split())
		ride = {'row_start': row_start, 'col_start': col_start, 'row_fin': row_fin, 'col_fin': col_fin, 't_start': start, 't_finish': finish, 'used': 0}
		rides.append(ride)

	return steps, cars, car_a, car_p, rides

def ride_dist(ride):
	# Get the distance for a ride.
	row_dist = abs(ride['row_start'] - ride['row_fin'])
	col_dist = abs(ride['col_start'] - ride['col_fin'])
	return row_dist + col_dist

def get_dist(a, b, x, y):
	return abs(a - x) + abs(b - y)

def output_str(rides):
	output_line = "%d " % len(rides)
	for ride in rides:
		output_line += ("%d " % ride)
	output_line += '\n'
	return output_line

def get_closest_ride(car_pos, rides):
	dummy_list = []
	for ride in rides:
		if ride['used'] == 1:
			dummy_list.append(99999999999999)
		else:
			dummy_list.append(get_dist(car_pos[0], car_pos[1], ride['row_start'], ride['col_start']))
	x, i = min((x, i) for (i, x) in enumerate(dummy_list))
	return i, x


file = 'b_should_be_easy' # The input file
# Open the input file
with open(file + '.in') as f:
	steps, cars, car_available, car_pos, rides = parse_dataset(f)

car_to_ride = [[] for _ in range(cars)]


#car_pos_test = (0,0)
#rides_test = [{'row_start': 4, 'col_start': 2}, {'row_start': 2, 'col_start': 1}, {'row_start': 1, 'col_start': 1}]


#i, x = get_closest_ride(car_pos_test, rides_test)
#print(i)
#print(x)

# THE SIMPLE SIMULATION
"""
for i, ride in enumerate(rides):
	car_to_ride[i % cars].append(i)
"""

# THE NEXT STEP

car_timings = [0] * cars
for step in range(steps):
	for car_idx, car_t in enumerate(car_timings):
		if car_t >= step:
			ride_i, ride_distance = get_closest_ride(car_pos[car_idx], rides)
			if rides[ride_i]['used'] != 1:
				if (ride_distance != 0) and ((rides[ride_i]['t_start'] - step) > 0):
					car_timings[car_idx] = ride_distance + (rides[ride_i]['t_start'] - step) + ride_dist(rides[ride_i])
				elif (ride_distance == 0) and ((rides[ride_i]['t_start'] - step) > 0):
					car_timings[car_idx] = ride_distance + rides[ride_i]['t_start'] + ride_dist(rides[ride_i])
				elif (rides[ride_i]['t_start'] - step) <= 0:
					car_timings[car_idx] = ride_distance + step + ride_dist(rides[ride_i])

				car_pos[car_idx] = (rides[ride_i]['row_fin'], rides[ride_i]['col_fin']) # Updating the position of the car.
				car_to_ride[car_idx].append(ride_i) # Appending a ride to a car
				rides[ride_i]['used'] = 1

# Write the output

with open(file + '.txt', 'w') as f:
	output = ""
	for car_ride in car_to_ride:
		output += output_str(car_ride)
	f.write(output)




"""
For ts in steps:
	for car in cars:
		if car['endTs'] >= ts
			distances = getDistanceToRides(rides)
			ride = index(min(distances))
			car['ride'] = ride
			car['endTs'] = distance2startpos + (ts-earlystart) + ridelength
			car['endPos'] = rideEndingPosition
			rides[ride] = []
"""