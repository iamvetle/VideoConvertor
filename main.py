from moviepy.editor import VideoFileClip
import argparse

# Local
from change_codec import change_codec
from change_res import change_res

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
        required=True,
        choices=["480", "720", "1080", "2160", "4k", "4320", "9k"],
        help="Choose a resolution to convert to",
    )

    # All the arguments
    args = parser.parse_args()

    # List of paths chosen
    filepaths = args.filepaths

    # The output file path. Example: spiderman.mp4
    output = args.output

    # The resolution that is going to be converted to
    chosen_res = args.resolution
    res = resolution_options(chosen_res)

    num_of_files = len(filepaths)
    print(f"Converting {num_of_files} files to {chosen_res}\n")

    for filepath in filepaths:
        try:

            resized_file = change_res(filepath, res)

            change_codec(resized_file, output)


            # print(resized_file)

            # filename_raw_list = filepath.split(".")
            # old_filetype = filename_raw_list[-1]
            # filename = (filename_raw_list[-2]).split("\\")[1]
            # new_filename = f"{filename}_modto{chosen_res}"
            # output_file = f"{new_filename}.{filetype}"

            # print("filepath", filename)

            # print("Trying to convert video format..")


            # new_file_path = f"{new_filename}.{filetype}"

            # # Size for the video
            # moviesize = res

            # # The video object
            # clip = VideoFileClip(new_file_path)

            # print(f"Converting '{filename}.{old_filetype}' to {chosen_res}p resolution.")

            # # ! There is a problem with codec with moviepy edior i dont know why

            # # Resizing
            # resized_clip = clip.resize(moviesize)

            # # Writing new file
            # resized_clip.write_videofile(output_file)

            # print(
            #     f"Video converted from '{new_filename}' to {chosen_res}p resolution.\n"
            # )

            # change_codec(filepath, output_file)


        except Exception as e:
            print(e)



if __name__ == "__main__":
    main()