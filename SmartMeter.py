# Step 1: Create and write smart meter readings to a file
readings = [
    "Voltage: 230V\n",
    "Current: 5A\n",
    "Power: 1150W\n"
]

# Writing to a file
with open("smart_meter.txt", 'w') as fh:
    fh.writelines(readings)  # using writelines()

# Step 2: Appending more data
with open("smart_meter.txt", 'a') as fh:
    fh.write("Energy: 10.5kWh\n")  # using write()

# Step 3: Reading full content
with open("smart_meter.txt", 'r') as fh:
    content = fh.read()  # using read()
    print("Full content:\n", content)

# Step 4: Reading line-by-line using readline
with open("smart_meter.txt", 'r') as fh:
    print("Reading lines one at a time:")
    line1 = fh.readline()  # using readline()
    print(line1.strip())
    line2 = fh.readline()
    print(line2.strip())

# Step 5: Reading all lines into a list using readlines
with open("smart_meter.txt", 'r') as fh:
    lines = fh.readlines()  # using readlines()
    print("\nAll lines as a list:")
    print(lines)
