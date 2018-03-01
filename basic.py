
def parse_dataset(data):

	rows, cols, cars, rides, bonus, steps = map(int, data.readline().strip().split())

	rides = []

	for ride in range(rows):
		row_start, col_start, row_fin, col_fin, start, finish = map(int, data.readline().strip().split())
		ride = {'row_start': row_start, 'col_start': col_start, 'row_fin': row_fin, 'col_fin': col_fin, 't_start': start, 't_finish': finish}
		rides.append(ride)

	return rides

def calculate_d

def main():
	file = 'a_example.in'
	with open(file) as f:
		rides = parse_dataset(f)
	


if __name__ == "__main__":
    main()