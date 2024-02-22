import os
import shutil

try:
    import shutil
except ImportError:
    print("shutil not installed. Installing...")
    os.system("pip install -r requirements.txt")


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()

# Your provided banner with blue color for the outside border
banner = """
\033[34m
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
/\/\                                                                         \/\/
\/\/  \033[0m<Program>          Birth Chart            </Program>\033[34m                   \/\/
/\/\                                                                         \/\/
\/\/              \033[0m       <Jyotish/>                       \033[34m                   \/\/
/\/\                                                                         \/\/
\/\/ \033[0m <Developer>        Anurag Badola          </Developer>                 \033[34m\/\/
/\/\                                                                         \/\/
/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/
\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//\/\/\/\/\/\/\/\/\033[34m
"""

# Splitting the banner into lines
banner_lines = banner.strip().split("\n")
# Getting the maximum length line
max_line_length = max(len(line) for line in banner_lines)

# Determine terminal dimensions
terminal_size = shutil.get_terminal_size()
terminal_width = terminal_size.columns
terminal_height = terminal_size.lines

# Calculate padding for centering horizontally and vertically
padding_top = (terminal_height - len(banner_lines)) // 2
padding_bottom = terminal_height - len(banner_lines) - padding_top
padding_left = (terminal_width - max_line_length) // 2

# Print the banner with proper centering
for _ in range(padding_top):
    print()

for line in banner_lines:
    print(" " * padding_left + line)

for _ in range(padding_bottom):
    print()

# Your remaining code goes here
from datetime import datetime, timedelta

# Input time
input_time = datetime.strptime(input("Enter a time (HH:MM): "), "%H:%M")

# Calculate total minutes
total_minutes = input_time.hour * 60 + input_time.minute

# Multiply total minutes by 2.5
result_minutes = total_minutes * 2.5

# Convert result minutes to hours and minutes
result_hours, result_minutes = divmod(result_minutes, 60)

# Create a timedelta object for the result time
result_timedelta = timedelta(hours=result_hours, minutes=result_minutes)

# Calculate the result time by adding the timedelta to the input time
result_time = input_time + result_timedelta

print("Original Time:", input_time.time())
print("ढ़ाई गुणा:", result_time.time())
