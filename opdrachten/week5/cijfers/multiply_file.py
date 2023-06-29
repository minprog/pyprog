import sys

def multiply_file(input_filename: str, multiplier: float, output_filename: str):
    with open(output_filename, "w") as output_file:
        with open(input_filename, "r") as input_file:
            for line in input_file:
                value = float(line) * multiplier
                value = round(value, 2)  # round to 2 decimals
                output_file.write(str(value) + '\n')

if __name__ == '__main__':
    if len(sys.argv) <= 3: # not enough command line arguments given
        print("Too few command line arguments.")
        print("usage:", sys.argv[0], "<input_filename> <multiplier> <output_filename>")
        print("Multiplies all values in <input_filename> with <multiplier> and writes the result to <output_filename>.")
    else:
        input_filename = sys.argv[1]    # read 'input_filename' from the command line arguments
        multiplier = float(sys.argv[2]) # read 'multiplier' from the command line arguments
        output_filename = sys.argv[3]   # read 'output_filename' from the command line arguments
        multiply_file(input_filename, multiplier, output_filename)
