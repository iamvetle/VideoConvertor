import argparse

# Local
from change_codec import change_codec
from change_res import change_res

from strip_and_split_filepath import strip_and_split_filepath

valid_options = [
    ["480", (480, 640)],
    ["720", (720, 1280)],
    ["1080", (1080, 1920)],
    ["2160", (2160, 3840)],
    ["4k", (2160, 3840)],
    ["4320", (4320, 7680)],
    ["8k", (4320, 7680)],
]


# The resolution options
def resolution_options(value):

    for option in valid_options:
        if value == option[0]:
            return option[1]
    raise ValueError("None of the resolution options were specified")


format_choices = ("mp4", "avi", "mkv", "webm", "mov ")

res_choices = ("480", "720", "1080", "2160", "4k", "4320", "8k")


def main():
    parser = argparse.ArgumentParser(description="Process a file")

    # Files to process
    parser.add_argument("filepaths", nargs="*", help="Path to the file(s) to process.")
    parser.add_argument(
        "-o",
        "--output",
        type=str,
        required=False,
        help="The output file to convert to.",
    )
    parser.add_argument(
        "-format",
        "--videoformat",
        required=False,
        help="The format to use",
        choices=format_choices,
    )
    parser.add_argument(
        "-r",
        "--resolution",
        choices=res_choices,
        help="Choose a resolution to resize to",
    )

    # All the arguments
    args = parser.parse_args()

    filepaths: list[str] = args.filepaths
    chosen_res = args.resolution
    videoformat = args.videoformat
    output = args.output

    if chosen_res:
        res = resolution_options(chosen_res)

    num_of_files = len(filepaths)

    for filepath in filepaths:
        try:
            # The output file path. Example: spiderman.mp4

            # Output cannot be specified when multiple files are selected
            if num_of_files > 1 and isinstance(output, str):
                raise ValueError(
                    "Output filename cannot be specified when multiple files are selected"
                )

            if num_of_files > 1 and not videoformat:

                videoformat = "mov"

                # raise ValueError("Videoformat must be specified when multiple files are selected")

            input_filename, _ = strip_and_split_filepath(filepath)

            if not output:
                if not chosen_res:
                    output = f"{input_filename}_copy.{videoformat}"
                else:
                    output = f"{input_filename}_copy{chosen_res}p.{videoformat}"

            input_file = filepath

            # Resize if a resolution has been set
            if chosen_res:
                resized_file = change_res(filepath, output, res)
                input_file = resized_file

            change_codec(input_file, output)

        except Exception as e:
            print("Exception occured:", e)


if __name__ == "__main__":
    main()
