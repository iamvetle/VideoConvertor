from moviepy.editor import VideoFileClip
import argparse

parser = argparse.ArgumentParser(description="Process a file")

# First argument
parser.add_argument("filepath", help="Path to the file to process.")

# Optional argument
parser.add_argument("-o", "--output", type=str, required=True, help="The filename output.")

# The resolution options
def resolution_options(value):
    valid_options = [
    ["480", (640, 480)],
    ["720", (1280, 720)],
    ["1080", (1920, 1080)],
    
    ["2160", (3840, 2160)],
    ["4k", (3840, 2160)],
    ["4320", (7680, 4320)],
    ["8k", (7680, 4320)],    
    ]

    for option in valid_options:
        print(value)
        if value == option[0]:
            return option[1]
    raise ValueError("None of the resolution options were specified")

parser.add_argument("-r", "--resolution", required=True, choices=["480", "720", "1080", "2160", "4k", "4320", "9k"], help="Choose a resolution to convert to" )

# All the arguments
args = parser.parse_args()

filepath = args.filepath
output_file = args.output

chosen_res = args.resolution
res = resolution_options(chosen_res)

if not filepath:
    print("No file was specified")
    exit()

try:

    moviesize = res

    clip = VideoFileClip(filepath)

    # Resizing
    resized_clip = clip.resize(moviesize)

    # Writing new file
    resized_clip.write_videofile(output_file)

    print(f'Video converted from {filepath} to {output_file} at "{chosen_res}" resolution.')

except Exception as e:
    print(e)
