import sys

def multiply_file(input_filename: str, multiplier: float, output_filename: str):
    with open(output_filename,"w") as output_file:
        with open(input_filename,"r") as input_file:
            for line in input_file:
                value = float(line) * multiplier
                value = round(value, 2) # round to 2 decimals
                output_file.write(str(value) + '\n')
            
if __name__ == '__main__':
    # print( sys.argv ) # uncomment to print all command line arguments
    if len(sys.argv)<=3:
        print("Too few arguments.")
        print("usage:",sys.argv[0],"<input_filename> <multiplier> <output_filename>")
        print("Multiplies all values in <input_filename> with <multiplier> and writes the result to <output_filename>.")
    else:
        input_filename=sys.argv[1]
        multiplier=float(sys.argv[2])
        output_filename=sys.argv[3]
        multiply_file(input_filename,multiplier,output_filename)
