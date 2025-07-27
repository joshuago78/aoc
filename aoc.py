import argparse
import importlib
import os


def read_data_file(year, day, test=False):
	test = 'test' if test else ''
	filename = f'day{day:02}{test}.txt'
	path = os.path.join(str(year), filename)
	with open(path) as datafile:
		return datafile.read()


def get_function(year, day, part):
	module = importlib.import_module(f'{year}.day{day:02}')
	function = getattr(module, f'part{part}')
	return function


def main(year, day, part, test, use_input):
	function = get_function(year, day, part)
	if use_input:
		raw_data = input('Input data: ')
	else:
		raw_data = read_data_file(year, day, test)
	answer = function(raw_data)
	output = f'The solution for {year} day {day}, part {part} is: {answer}'
	if test:
		output += '  [USING TEST DATA]'
	print(output)


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("year", type=int, help="The challenge year")
	parser.add_argument("day", type=int, help="The challenge day")
	parser.add_argument("part", type=int, choices=[1,2], help="The challenge part (1 or 2)")
	parser.add_argument("-t", "--test", action="store_true", help="Use test data file")
	parser.add_argument("-i", "--input", action="store_true", help="Use provided input")
	args = parser.parse_args()
	main(args.year, args.day, args.part, args.test, args.input)

