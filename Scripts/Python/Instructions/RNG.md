# Comprehensive Number Selector

## Table of Contents

 • Overview
 • Features
 • Installation
 • Usage
 • Command-Line Interface (CLI) Mode
 • Graphical User Interface (GUI) Mode
 • Exporting Results
 • Logging
 • Error Handling
 • License

## Overview

The Comprehensive Number Selector is a versatile Python application designed to help users randomly select numbers based on customizable criteria. Whether you prefer using the command line or a graphical interface, this tool offers flexibility to meet your needs. It’s ideal for generating lottery numbers, random samples for studies, or any scenario requiring random number selection.

## Features

 • Dual Interface: Operate via Command-Line Interface (CLI) or Graphical User Interface (GUI) using Tkinter.
 • Customizable Range: Define the start and end of the number range.
 • Selection Parameters: Specify the number of numbers to select and the number of sets to generate.
 • Randomization Methods:
 • Random Sample (No Replacement)
 • Shuffle and Select
 • Random Choices (With Replacement)
 • Reproducibility: Option to set a seed for consistent results across runs.
 • Export Options: Save results in CSV or TXT formats.
 • Logging: Comprehensive logging of operations and errors for troubleshooting.

## Installation

## Prerequisites

 • Python 3.6 or higher must be installed on your system. You can download it from Python’s official website.

Clone the Repository

git clone <https://github.com/yourusername/comprehensive-number-selector.git>
cd comprehensive-number-selector

Install Dependencies

The script uses the standard Python library, but for GUI functionality, Tkinter is required.

Windows

Tkinter is usually included with Python on Windows. To verify, run:

python -m tkinter

If a simple GUI window appears, Tkinter is installed.

macOS

Tkinter should be included with Python on macOS. If not, you can install it via Homebrew:

brew install python-tk

Linux

Install Tkinter using your distribution’s package manager.
 • Debian/Ubuntu:

sudo apt-get update
sudo apt-get install python3-tk

 • Fedora:

sudo dnf install python3-tkinter

 • Arch Linux:

sudo pacman -S tk

Verify Installation

Ensure all dependencies are installed by running:

python number_selector.py --help

You should see the help message without errors.

Usage

The application can be run in two modes:

 1. Command-Line Interface (CLI) Mode
 2. Graphical User Interface (GUI) Mode

Command-Line Interface (CLI) Mode

Running in CLI Mode

To launch the application in CLI mode, simply run:

python number_selector.py

Step-by-Step Instructions

 1. Start the Application

python number_selector.py

 1. Input Prompts
The application will prompt you for the following inputs:
 • Start of Range: The beginning number of the range (default: 1).
 • End of Range: The ending number of the range (default: 15).
 • Numbers to Select: How many numbers to select per set (default: 6).
 • Number of Sets: How many sets to generate (default: 1).
 • Randomization Method:
 • 1: Random Sample (No Replacement)
 • 2: Shuffle and Select
 • 3: Random Choices (With Replacement)
 • Random Seed (Optional): Enter an integer to set the seed for reproducibility.
 2. Exporting Results
After generating the sets, you'll be prompted to export the results:
 • Export Option: Choose y to export or n to skip.
 • File Format: Select between csv or txt.
 • Filename: Enter a desired filename or accept the default.
 3. Completion
The generated sets will be displayed in the terminal. If exported, a confirmation message will appear.

Example Session

### Enter the start of the range [1]

Enter the end of the range [15]: 30
How many numbers to select [6]: 5
How many sets to generate [1]: 3

Select Randomization Method:

1. Random Sample (No Replacement)
2. Shuffle and Select
3. Random Choices (With Replacement)
Enter choice (1/2/3) [1]: 2
Enter a seed for randomness (or leave blank for random): 42

Set 1: [5, 12, 23, 7, 19]
Set 2: [14, 3, 27, 8, 21]
Set 3: [2, 16, 9, 25, 11]

Would you like to export the results? (y/n) [n]: y
Enter file format ('csv' or 'txt') [csv]: txt
Enter filename [number_sets_20250103_123456.txt]: my_number_sets.txt
Results successfully exported to my_number_sets.txt

### Graphical User Interface (GUI) Mode

Running in GUI Mode

To launch the application in GUI mode, use the --gui flag:

python number_selector.py --gui

### GUI Components

Upon launching, the GUI window will display the following components:

 1. Input Fields
 • Start of Range: Input box to enter the starting number (default: 1).
 • End of Range: Input box to enter the ending number (default: 15).
 • Numbers to Select: Input box to specify how many numbers to select per set (default: 6).
 • Number of Sets: Input box to define how many sets to generate (default: 1).
 • Random Seed: Optional input box to set the seed for reproducibility.
 2. Randomization Method
 • Random Sample (No Replacement)
 • Shuffle and Select
 • Random Choices (With Replacement)
 3. Export Options
 • Export Results: Checkbox to enable exporting.
 • File Format: Radio buttons to choose between CSV and TXT.
 4. Generate Button
 • Click to execute the number selection based on the provided inputs.
 5. Output Display
 • A text area displaying the generated sets.
 6. Save Dialog
 • If exporting is enabled, a dialog will prompt you to choose the save location and filename.

### Step-by-Step Instructions

 1. Launch the GUI

python number_selector.py --gui

 2. Enter Inputs
 • Fill in the Start of Range, End of Range, Numbers to Select, and Number of Sets.
 • Optionally, enter a Random Seed for reproducibility.
 3. Select Randomization Method
 • Choose one of the available randomization methods.
 4. Export Options
 • Check the Export Results box if you wish to save the generated sets.
 • Select the desired File Format (CSV or TXT).
 5. Generate Sets
 • Click the Generate button.
 • The generated sets will appear in the output text area.
 6. Save Results
 • If exporting, a save dialog will appear.
 • Choose the destination folder, enter a filename, and save.
 7. Close the Application
 • Click the close button or select Quit from the window menu.

## Exporting Results

The application allows exporting the generated number sets in two formats:

 1. CSV (Comma-Separated Values)
 2. TXT (Plain Text)

### Exporting in CLI Mode

After generating the sets:

 1. Choose to Export: When prompted, enter y to export.
 2. Select File Format: Enter csv or txt.
 3. Enter Filename: Provide a filename or accept the default.

### Exporting in GUI Mode

 1. Enable Export: Check the Export Results box.
 2. Select File Format: Choose between CSV and TXT.
 3. Generate Sets: Click Generate.
 4. Save File: In the save dialog, specify the location and filename.

Exported File Structure
 • CSV Format:

Set Number Selected Numbers
1 5, 12, 23, 7, 19
2 14, 3, 27, 8, 21
3 2, 16, 9, 25, 11

 • TXT Format:

Set 1: [5, 12, 23, 7, 19]
Set 2: [14, 3, 27, 8, 21]
Set 3: [2, 16, 9, 25, 11]

## Logging

The application maintains a log file named number_selector.log in the same directory as the script. This log records detailed information about operations, selections, exports, and any errors encountered.

### Log Details

 • Timestamp: Date and time of the event.
 • Log Level: INFO, DEBUG, WARNING, ERROR.
 • Message: Description of the event.

### Example Log Entries

2025-01-03 12:34:56,789 - INFO - Available numbers: [1, 2, 3, ..., 15]
2025-01-03 12:35:01,123 - INFO - Randomization method selected: shuffle
2025-01-03 12:35:02,456 - INFO - Set 1: [5, 12, 23, 7, 19]
2025-01-03 12:35:03,789 - ERROR - Failed to export results: [Error Details]

### Accessing the Log

Open the number_selector.log file using any text editor to review the logs.

## Error Handling

The application includes robust error handling to ensure smooth operation. Here’s how it manages potential issues:

### Common Errors

 1. Invalid Inputs
 • Non-integer Values: If a non-integer is entered where an integer is expected, the application will display an error message and exit (CLI) or show an error dialog (GUI).
 • Negative or Zero Values: Inputs like range boundaries or selection counts must be positive integers. Invalid values trigger error messages.
 2. Range Issues
 • End Range Less Than Start Range: The application checks if the end of the range is greater than or equal to the start. If not, it alerts the user.
 3. Selection Constraints
 • Exceeding Available Numbers: In methods without replacement (sample and shuffle), selecting more numbers than available triggers an error.
 4. Unsupported Randomization Method
 • If an unknown method is specified, the application defaults to sample and logs an error.
 5. Export Failures
 • Issues during file export (e.g., permission errors) are caught, logged, and communicated to the user.
 6. Tkinter Availability
 • If Tkinter is not installed and the user attempts to launch GUI mode, the application notifies the user and exits gracefully.

### Handling Keyboard Interrupt (CLI)

If the user interrupts the CLI process (e.g., using Ctrl+C), the application will:
 • Display a cancellation message.
 • Log the interruption.
 • Exit without crashing.

Logging Errors

All errors are logged with the ERROR level in the number_selector.log file, providing details for troubleshooting.

## License

This project is licensed under the MIT License.

Created with ❤️ by Exios66
