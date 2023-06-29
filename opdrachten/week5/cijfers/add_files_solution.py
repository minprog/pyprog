import sys

def add_files(input_filename1: str, input_filename2: str, output_filename: str):
    with open(output_filename, "w") as output_file:
        with open(input_filename1, "r") as input_file1:
            with open(input_filename2, "r") as input_file2:
                for line1 in input_file1:
                    line2 = input_file2.readline()
                    value = float(line1) + float(line2)
                    value = round(value, 2)  # round to max 2 decimals
                    output_file.write(str(value) + '\n')

if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print("Too few command line arguments.")
        print("usage:", sys.argv[0], "<input_filename1> <input_filename2> <output_filename>")
        print("Adds all corresponding values in <input_filename> and <input_filename2> and writes the result to <output_filename>.")
    else:
        input_filename1 = sys.argv[1]
        input_filename2 = sys.argv[2]
        output_filename = sys.argv[3]
        add_files(input_filename1, input_filename2, output_filename)
