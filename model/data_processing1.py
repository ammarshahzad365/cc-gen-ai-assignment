input_file = 'input.txt'  # Your input file name
output_file = 'output.txt'  # The output file name

bucket_path = 'gs://gen-ai-bucket-cc/'

with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
    for line in infile:
        # Split the line at the comma
        image_name, description = line.strip().split(',', 1)
        
        # Write the new formatted line to the output file
        outfile.write(f"{bucket_path}{image_name},{description}\n")

print("Conversion complete. Output written to", output_file)
