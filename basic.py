
def parse_dataset(data):

	rows, cols, cars, rides, bonus, steps = map(int, data.readline().strip().split())

	rides = []
	car_a = [True] * cars
	car_p = [(0,0)] * cars

	for ride in range(rows):
		row_start, col_start, row_fin, col_fin, start, finish = map(int, data.readline().strip().split())
		ride = {'row_start': row_start, 'col_start': col_start, 'row_fin': row_fin, 'col_fin': col_fin, 't_start': start, 't_finish': finish}
		rides.append(ride)

	return car_a, car_p, rides

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

cars = []
file = 'a_example'
with open(file + '.in') as f:
	car_available, car_pos, rides = parse_dataset(f)

# THE SIMULATION

#Example output
rides = [0, 3, 7]
with open(file + '.out', 'w') as f:
	f.write(output_str(rides))


