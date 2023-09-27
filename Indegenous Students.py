import plotly.express as px
import numpy as np

# Create a dictionary to map the ASGS Remoteness region codes to their full names
asgs_region_dict = {
    "MC": "Major Cities of Australia",
    "IR": "Inner Regional Australia",
    "OR": "Outer Regional Australia",
    "R": "Remote Australia",
    "VR": "Very Remote Australia"
}

# Prompt the user to enter the ASGS Remoteness region codes to be included in the plot
asgs_regions = input("Enter the ASGS Remoteness region codes to be included in the plot (MC, IR, OR, R, VR): ").split()

# Check if at least two codes have been entered
if len(asgs_regions) < 2:
    print("Error: At least two ASGS Remoteness region codes must be entered.")
    exit(1)

# Check if all of the codes are valid
invalid_codes = []
for code in asgs_regions:
    if code not in asgs_region_dict.keys():
        invalid_codes.append(code)

if invalid_codes:
    print("Error: The following ASGS Remoteness region codes are invalid:", invalid_codes)
    exit(1)

# Load the data
data = np.loadtxt("asgs_indigenous_students.csv", delimiter=",")

# Calculate the mean percentage of indigenous students for each region
mean_indigenous_students = np.mean(data[:, 1:], axis=0)

# Create a list of region names for the plot
region_names = []
for code in asgs_regions:
    region_names.append(asgs_region_dict[code])

# Create the bar plot
fig = px.bar(x=region_names, y=mean_indigenous_students, title="Mean Percentage of Indigenous Students by ASGS Remoteness Region")

# Show the plot
fig.show()
