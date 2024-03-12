from moviepy.editor import VideoFileClip
import argparse

# Local
from change_codec import change_codec
from change_res import change_res

from strip_and_split_filepath import strip_and_split_filepath

def main():
    parser = argparse.ArgumentParser(description="Process a file")

    # First argument
    parser.add_argument("filepaths", nargs="*", help="Path to the file(s) to process.")

    parser.add_argument(
        "-o", "--output", type=str, required=True, help="The output file to convert to."
    )


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
            if value == option[0]:
                return option[1]
        raise ValueError("None of the resolution options were specified")


    parser.add_argument(
        "-r",
        "--resolution",
        choices=["480", "720", "1080", "2160", "4k", "4320", "9k"],
        help="Choose a resolution to convert to",
    )

    # All the arguments
    args = parser.parse_args()

    # List of paths chosen
    filepaths = args.filepaths

    # The resolution that is going to be converted to
    chosen_res = args.resolution
    
    if chosen_res:
        res = resolution_options(chosen_res)

    num_of_files = len(filepaths)
    print(f"Converting {num_of_files} files to {chosen_res}p\n")

    for filepath in filepaths:
        try:
            
            # The output file path. Example: spiderman.mp4
            output = args.output
            
            if not output:
                input_filename, input_filetype = strip_and_split_filepath(filepath)
                
                if not chosen_res:
                    output = f"{input_filename}copy.{input_filename}"
                else:
                    output = f"{input_filename}{chosen_res}copy.{input_filename}"
                
            input_file = filepath
            
            # Resize if a resolution has been set
            if chosen_res:
                resized_file = change_res(filepath, output, res)
                input_file = resized_file
            
            change_codec(input_file, output)

        except Exception as e:
            print(e)
            exit()

if __name__ == "__main__":
    main()