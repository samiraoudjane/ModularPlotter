import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np
import pdb
import os


# Connect to the SQLite database
db_filename = "processing 2_2.db"
connection = sqlite3.connect(db_filename)
cursor = connection.cursor()

# Select data from the "bacteria_0" table
cursor.execute("SELECT * FROM bacteria_2")

# Fetch all rows from the result set
rows = cursor.fetchall()

# Close the database connection
connection.close()

# Initialize an empty list to store the data as floats
data_as_floats = []

# Convert the data to floats and store it in the list
for row in rows:
    row_as_floats = [float(value) for value in row]
    data_as_floats.append(row_as_floats)

# Initialize a counter to keep track of the number of instances of 0 in the first column
zero_count = 0

# Initialize a counter to keep track of the number of data points before the break
data_point_count = 0

# Iterate through the data and populate the section_colors list
for value in data_as_floats:
    if value[0] == 0.0:
        zero_count += 1
        if zero_count > 1:
            break  # Stop populating section_colors after the second instance of 0
    data_point_count += 1  # Increment the data point count

# Split data_as_floats into sections of size data_point_count and plot each section
section_size = data_point_count  # Set the section size to data_point_count

# Initialize a list to store the colors for each section
section_colors = []

#print (data_as_floats)

for i in range(0, len(data_as_floats), section_size):    
    section = data_as_floats[i:i + section_size]    
    first_column = [row[0] for row in section]
    second_column = [float(row[1]) for row in section]    
    #print (second_column)
    inoc_column = [int(row[3]) for row in section]  # Convert to int  
    # Determine the section color based on the first value of the inoc_column
    section_color = 'green' if inoc_column[0] == 1 else 'black'
    section_colors.append(section_color)

    # Create a plot for each section with the specified color
    plt.plot(first_column, label='First Column', color=section_color)
    plt.plot(second_column, label='Second Column', color=section_color)
    
# Add labels and legend
plt.title('two_Luminescence')
plt.ylabel('Luminescence(arb)')
plt.xlabel('Time(hours)')

# Save the plot as a PNG file with the title as the file name
plot_title = 'two_Luminesence.png'
plot_path = os.path.join('plots', plot_title)
plt.savefig(plot_path)

plt.clf()

for i in range(0, len(data_as_floats), section_size):    
    section = data_as_floats[i:i + section_size]    
    first_column = [row[0] for row in section]
    second_column = [float(row[2]) for row in section]    
    #print (second_column)
    inoc_column = [int(row[3]) for row in section]  # Convert to int  
    # Determine the section color based on the first value of the inoc_column
    section_color = 'green' if inoc_column[0] == 1 else 'black'
    section_colors.append(section_color)

    # Create a plot for each section with the specified color
    #plt.plot(first_column, label='First Column', color=section_color)
    plt.plot(second_column, label='Second Column', color=section_color)
    
# Add labels and legend
plt.title('two_absorbance')
plt.ylabel('absorbance(ratio)')
plt.xlabel('Time(hours)')

# Save the plot as a PNG file with the title as the file name
plot_title = 'two_Absorbance.png'
plot_path = os.path.join('plots', plot_title)
plt.savefig(plot_path)

plt.clf()

for i in range(0, len(data_as_floats), section_size):    
    section = data_as_floats[i:i + section_size]    
    first_column = [row[0] for row in section]
    second_column = [float(row[4]) for row in section]    
    #print (second_column)
    inoc_column = [int(row[3]) for row in section]  # Convert to int  
    # Determine the section color based on the first value of the inoc_column
    section_color = 'green' if inoc_column[0] == 1 else 'black'
    section_colors.append(section_color)

    # Create a plot for each section with the specified color
    #plt.plot(first_column, label='First Column', color=section_color)
    plt.plot(second_column, label='Second Column', color=section_color)
    
# Add labels and legend
plt.title('two_GFP')
plt.ylabel('Fluorescence')
plt.xlabel('Time(hours)')

# Save the plot as a PNG file with the title as the file name
plot_title = 'two_GFP.png'
plot_path = os.path.join('plots', plot_title)
plt.savefig(plot_path)

plt.clf()

for i in range(0, len(data_as_floats), section_size):    
    section = data_as_floats[i:i + section_size]    
    first_column = [row[0] for row in section]
    second_column = [float(row[1]) / float(row[2]) for row in section]  
    #print (second_column)
    inoc_column = [int(row[3]) for row in section]  # Convert to int  
    # Determine the section color based on the first value of the inoc_column
    section_color = 'green' if inoc_column[0] == 1 else 'black'
    section_colors.append(section_color)

    # Create a plot for each section with the specified color
    #plt.plot(first_column, label='First Column', color=section_color)
    plt.plot(second_column, label='Second Column', color=section_color)
    
# Add labels and legend
plt.title('two_Luminescence/absorbance')
plt.ylabel('Luminescence(arb)/absorbance')
plt.xlabel('Time(hours)')

# Save the plot as a PNG file with the title as the file name
plot_title = 'two_LuminescenceOverAbsorbance.png'
plot_path = os.path.join('plots', plot_title)
plt.savefig(plot_path)

plt.clf()

for i in range(0, len(data_as_floats), section_size):    
    section = data_as_floats[i:i + section_size]    
    first_column = [row[0] for row in section]
    second_column = [float(row[4]) / float(row[2]) for row in section]  
    #print (second_column)
    inoc_column = [int(row[3]) for row in section]  # Convert to int  
    # Determine the section color based on the first value of the inoc_column
    section_color = 'green' if inoc_column[0] == 1 else 'black'
    section_colors.append(section_color)

    # Create a plot for each section with the specified color
    #plt.plot(first_column, label='First Column', color=section_color)
    plt.plot(second_column, label='Second Column', color=section_color)
    
# Add labels and legend
plt.title('two_GFP/absorbance')
plt.ylabel('GFP(arb)/absorbance')
plt.xlabel('Time(hours)')

# Save the plot as a PNG file with the title as the file name
plot_title = 'two_GFPoverAbsorbance.png'
plot_path = os.path.join('plots', plot_title)
plt.savefig(plot_path)

plt.clf()
