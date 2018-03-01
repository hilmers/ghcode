
def parse_dataset(data):

	rows, cols, cars, nbr_rides, bonus, steps = map(int, data.readline().strip().split())

	rides = []
	car_a = [True] * cars
	car_p = [(0,0)] * cars

	for ride in range(nbr_rides):
		row_start, col_start, row_fin, col_fin, start, finish = map(int, data.readline().strip().split())
		ride = {'row_start': row_start, 'col_start': col_start, 'row_fin': row_fin, 'col_fin': col_fin, 't_start': start, 't_finish': finish}
		rides.append(ride)

	return steps, cars, car_a, car_p, rides

def calc_dist(ride):
	# Get the distance for a ride.
	row_dist = abs(ride['row_start'] - ride['row_fin'])
	col_dist = abs(ride['col_start'] - ride['col_fin'])
	return row_dist + col_dist

def output_str(rides):
	output_line = "%d " % len(rides)
	for ride in rides:
		output_line += ("%d " % ride)
	output_line += '\n'
	return output_line


file = 'b_should_be_easy' # The input file
# Open the input file
with open(file + '.in') as f:
	steps, cars, car_available, car_pos, rides = parse_dataset(f)

car_to_ride = [[] for _ in range(cars)]


# THE SIMULATION
for i, ride in enumerate(rides):
	car_to_ride[i % cars].append(i)


# Write the output
with open(file + '.out', 'w') as f:
	output = ""
	for car_ride in car_to_ride:
		output += output_str(car_ride)
	f.write(output)


