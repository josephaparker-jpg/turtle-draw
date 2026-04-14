TurtleDraw Application
Author: Joseph Parker
File: TurtleDraw_jp.py

----------------------------------------
SUMMARY
----------------------------------------
This Python application reads drawing instructions from a text file and uses the Turtle graphics library to render lines and shapes on the screen.

Each line in the input file contains a color and (x, y) coordinate. The program draws connected line segments between points. When the program encounters the word "stop", it lifts the pen and begins a new drawing segment.

The application also calculates the total distance of all connected line segments and displays it on the screen.

----------------------------------------
REQUIREMENTS
----------------------------------------
- Python 3 installed
- Turtle graphics library (included with Python)

----------------------------------------
HOW TO RUN
----------------------------------------
1. Open a terminal or command prompt
2. Navigate to the folder containing the files
3. Run the program using:

   python TurtleDraw_jp.py

4. When prompted, enter the file name:

   turtle-draw-data.txt

----------------------------------------
INPUT FILE FORMAT
----------------------------------------
Each line must follow this format:

   color x y

Example:
   red 50 100
   blue -20 75

Special command:
   stop

- "stop" tells the program to lift the pen and start a new drawing segment
- Coordinates must be numeric values
- Colors must be valid Turtle color names

----------------------------------------
FEATURES
----------------------------------------
- Opens a 450x450 graphics window
- Draws lines based on file input
- Supports multiple disconnected shapes using "stop"
- Changes colors dynamically
- Calculates and displays total drawing distance
- Waits for user input before closing

----------------------------------------
NOTES
----------------------------------------
- The input file must be in the same directory as the Python file
- File names are case-sensitive
- The program will display an error if the file cannot be opened

----------------------------------------
END
----------------------------------------
