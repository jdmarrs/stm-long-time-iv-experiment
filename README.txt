Long-Time IV Experiment

This project includes a collection of Python scripts that are used to process data collected from a
Scanning Tunneling Microscope (STM).

The initial raw data files are generated from a LabVIEW program which are then converted into IV text
files generated by the "Tapping_IV_browser - log - 4Gfit copy - Modified for Saving IV Files.vi" LabVIEW Program.

"Convert_All_IV_Files_SF_*_Hz.py" Iteratively calls "IV_to_IT_File_Conversion_SF_*_Hz.py" to convert
each IV file in the "IV Curves" folder from Voltage to Time, and save new files in the "IT Curves" folder.

"IV_to_IT_File_Conversion_SF_00_1_Hz.py" Opens IV text file with two columns (voltage, current) and
convert voltage to time (V --> Seconds) using voltage sweep frequency (Hz) and range (V). In other words,
it converts 4 quadrants of voltage sweep cycle [0 --> +, + --> 0, 0 --> -, - --> 0] into one continuous
linear time progression. It also removes bias (0.3 V in the default case) before converting voltage to time.

"Plot_All_IT_Files.py" is a Python script for plotting the data from the IT Curve files that were generated
by the IV Curve text files created by the "Tapping_IV_browser - log - 4Gfit copy - Modified for Saving IV
Files.vi" LabVIEW Program. It iteratively calls "Plot_IT_File.py" to generate plots for each IT file in
the "IT Curves" folder.

"Plot_IT_File.py" is a Python script for plotting the data from the IT Curve files that were generated by
the IV Curve text files created by the "Tapping_IV_browser - log - 4Gfit copy - Modified for Saving IV
Files.vi" LabVIEW Program. It opens IT text files with two columns [Time (Seconds), Current (nA)] and
creates a plot using Matplotlib.

Author: Jon Marrs
Date: 2017-08-01
