#===============================================================================
# Plot_IT_File.py
# Python script for plotting the data from the IT Curve files that were generated by the IV Curve text files
# created by the "Tapping_IV_browser - log - 4Gfit copy - Modified for Saving IV Files.vi" LabVIEW Program.
# Open IT text file with two columns [Time (Seconds), Current (nA)] and create a plot using Matplotlib.
# Author: Jon Marrs
# Date: 2017-07-30
#===============================================================================

# Note: Ideally, this Python script should be called by the associated Python script "Plot_All_IT_Files.py"
# to automatically iterate through all files in the "IT Curves" folder

import os
import sys
import pylab

#===============================================================================
# BEGIN Configuration
#===============================================================================

# Debug Mode (1 = True, 0 = False) [Debug Mode is used to print debug info to console]
Debug_Mode = 0

# Show Plot (1 = True, 0 = False) [enable/disable displaying the plot]
Show_Plot = 1

# Save Plot (1 = True, 0 = False) [enable/disable saving the plot]
Save_Plot = 1

# Image File Format Extension (jpg, png, pdf, ...)
image_file_extension = "jpg"

# Set IT File Name (input file) and IT Plot Name (output file)
if Debug_Mode:
    it_file_name = "Amp10nAV_Bias300mV_SolC10Dithiol_MC200_RR20_0023_IT00"    # IT File Name (input file)
    it_plot_name = "Amp10nAV_Bias300mV_SolC10Dithiol_MC200_RR20_0023_IT00"    # IT Plot Name (output file)
else:
    it_file_name = sys.argv[1]    # IT File Name (input file)
    it_plot_name = sys.argv[2]    # IT Plot Name (output file)

# Plot Title
plot_title = it_plot_name

# Plot Label
plot_label = it_plot_name

# X-axis Label
x_axis_label = "Time (Seconds)"

# Y-axis Label
y_axis_label = "Current (nA)"

# IT File Directory Name (Name of the directory where the IT files are relative to the script location)
it_file_directory_name = "IT Curves"

# IT Plot Directory Name (Name of the directory where the IT plot files are relative to the script location)
it_plot_directory_name = "IT Plots"

#===============================================================================
# END Configuration
#===============================================================================

# Need to set the directory if we are in debug mode (calling script would typically do this for us)
if Debug_Mode:
    it_file_directory = os.getcwd() + "\\" + it_file_directory_name
    os.chdir(it_file_directory)

# Set current directory and parent directory
current_directory = os.getcwd()
parent_directory = os.path.dirname(os.getcwd())
if Debug_Mode:
    print(current_directory)
    print(parent_directory)

# Check for "IT Plots" directory, and if it doesn't exist, create it (if we want to save the plot)
if not os.path.exists(parent_directory + "\\" + it_plot_directory_name):
    if Save_Plot:
        os.mkdir(parent_directory + "\\" + it_plot_directory_name)

# Open the file_name that was passed as the first system argument when calling this script
with open(it_file_name, 'r') as infile:

    # BEGIN PLOTTING CODE

    # Generate plot using pylab

    # Read the data from the input IT file
    data = pylab.loadtxt(infile)

    # Plot the data from the input IT file
    pylab.plot(data[:, 0], data[:, 1], label=plot_label)

    # Set the Title, X-axis, Y-axis
    pylab.title(plot_title)
    pylab.xlabel(x_axis_label)
    pylab.ylabel(y_axis_label)

    # Get the current figure, and set it to "fig"
    fig = pylab.gcf()

    # Set figure window title
    fig.canvas.set_window_title(plot_title)

    # Save the plot
    if Save_Plot:
        # Save a new text file as the new file name that was passed as the second system argument
        with open(parent_directory + "\\" + it_plot_directory_name + "\\" + it_plot_name + "." + image_file_extension, 'w') as outfile:
            fig.savefig(parent_directory + "\\" + it_plot_directory_name + "\\" + it_plot_name + "." + image_file_extension)

        # Close output file
        outfile.close()

    # Show the plot
    if Show_Plot:
        pylab.show()

    # END PLOTTING CODE

# Close input file
infile.close()

print(os.path.abspath('../' + it_plot_directory_name))

print(it_plot_name + "." + image_file_extension)

