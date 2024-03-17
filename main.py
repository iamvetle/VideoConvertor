import argparse

# Local
from utils.change_codec import change_codec
from utils.change_res import change_res

from utils.strip_and_split_filepath import strip_and_split_filepath

import os

# valid_options = [
#     ["480p", (480, 640)],
#     ["720p", (720, 1280)],
#     ["1080p", (1080, 1920)],
#     ["2160p", (2160, 3840)],
#     ["4k", (2160, 3840)],
#     ["4320p", (4320, 7680)],
#     ["8k", (4320, 7680)],
# ]

format_choices = ("mp4", "mov", "avi", "mkv", "webm", "ogv")


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
        nargs=2,
        # type=list,
        help="Choose a (two) resolution to resize to",
    )

    # All the arguments
    args = parser.parse_args()

    filepaths: list[str] = args.filepaths
    resolution: list[str] | None = args.resolution
    videoformat: str | None = args.videoformat
    output: str | None = args.output

    print(resolution)

    if resolution:
        if len(resolution) > 2 or len(resolution) == 1:
            raise ValueError(
                "There has to be two define resolutions. Example: -r 1920 1080"
            )

    num_of_files = len(filepaths)

    # Output cannot be specified when multiple files are selected
    if num_of_files > 1 and output:
        raise ValueError(
            "Output filename cannot be specified when multiple files are selected"
        )

    # A fileformat must be specified when the num of files are over 1
    if num_of_files > 1 and not videoformat:
        raise ValueError(
            "Videoformat must be specified when multiple files are selected"
        )

    for filepath in filepaths:
        try:
            input_filename, input_filetype = strip_and_split_filepath(filepath)

            if not output:
                print("There is no ouput name so making just a copy name")
                if resolution:
                    output = f"{input_filename}_copy{resolution[0]}{resolution[1]}p.{input_filetype}"
                else:
                    output = f"{input_filename}_copy.{videoformat}"

            _, output_filetype = strip_and_split_filepath(output)

            input_file = filepath

            # Resize if a resolution has been set
            if resolution:
                input_file = change_res(filepath, output, resolution)

            # Change codec if the filetype is not the same for the input and output
            if input_filetype != output_filetype:
                if filepath != input_file:
                    status = change_codec(input_file, output)
                    if status == True:
                        os.remove(input_file)
                else:
                    change_codec(input_file, output)

        except Exception as e:
            print("Exception occured:", e)


if __name__ == "__main__":
    main()
