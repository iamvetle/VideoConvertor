import argparse
import os

# Local
from utils.change_codec import change_codec  # Utility function to change video codec
from utils.change_res import change_res  # Utility function to resize video
from utils.strip_and_split_filepath import strip_and_split_filepath  # Utility to split filepath

# The different videoformats to choose from
format_choices = ("mp4", "mov", "avi", "mkv", "webm", "ogv")

def validate_resolution(resolution):
  """
  Validates the provided resolution arguments.
  Raises ValueError if invalid.

  Args:
      resolution: A list of two integers representing the desired width and height of the output video.

  Raises:
      ValueError: If the length of the resolution list is not 2.
  """
  if len(resolution) != 2:
    raise ValueError("Invalid resolution. Please provide two values for width and height. Example: -r 1920 1080")


def main():
  """
  The main function that parses user arguments and processes video files.
  """
  parser = argparse.ArgumentParser(description="Process a file")

  # Files to process
  parser.add_argument("filepaths", nargs="+", help="Path to the file(s) to process.")
  parser.add_argument(
      "-o",
      "--output",
      type=str,
      required=False,
      help="The output file name to convert to.",
  )
  parser.add_argument(
      "-format",
      "--videoformat",
      required=False,
      help="The format to use for the output video",
      choices=format_choices,
  )
  parser.add_argument(
      "-r",
      "--resolution",
      nargs=2,
      # type=list,
      help="Choose a resolution (width and height) to resize the video to",
  )

  # All the arguments
  args = parser.parse_args()

  filepaths: list[str] = args.filepaths
  resolution: list[str] | None = args.resolution
  videoformat: str | None = args.videoformat
  output: str | None = args.output

  num_of_files = None

  # Informational message about resolution being printed for debugging purposes
  print(f"Debug: resolution argument: {resolution}")

  # Validate resolution arguments if provided
  try:
    if resolution:
      validate_resolution(resolution)

    num_of_files = len(filepaths)

    # Output cannot be specified when multiple files are selected
    if num_of_files > 1 and output:
      raise ValueError(
          "Output filename cannot be specified when processing multiple files. Use separate commands for each file or omit the '-o' option."
      )

    # A fileformat must be specified when the num of files are over 1
    if num_of_files > 1 and not videoformat:
      raise ValueError(
          "Videoformat must be specified when processing multiple files. Example: -format mp4"
      )

    if num_of_files == 1 and videoformat:
      raise ValueError("Videoformat is not required when using an output filename. The format will be inferred from the filename extension.")

  except Exception as e:
    print(f"Error: {e}")
    exit()

  if num_of_files == 1:
    filepath = filepaths[0]

    input_file = filepath
    output_file = output

    try:
      _, input_filetype = strip_and_split_filepath(input_file)
      _, output_filetype = strip_and_split_filepath(output_file)

      # Resize if a resolution has been set
      if resolution:
        input_file = change_res(input_file, output_file, resolution)
        print(f"Resized video to {resolution[0]}x{resolution[1]}")

      # Change codec if the filetype is not the same for the input and output
      if input_filetype != output_filetype:
        change_codec(input_file, output_file)
        print("Video file type was changed.")

      if resolution:
        if os.path.exists(input_file):
          os.remove(input_file)

    except Exception as e:
      print(f"Error processing {filepath}:", e)

  if num_of_files > 1:
    for filepath in filepaths:
      try:
        input_file = filepath
        output_file = None

        input_filename, input_filetype = strip_and_split_filepath(input_file)

        if resolution:
          output_file = f"{input_filename}_copy{resolution[0]}{resolution[1]}p.{videoformat}"
          print(f"Processing {filepath}. Output: {output_file} (resized to {resolution[0]}x{resolution[1]})")
        else:
          output_file = f"{input_filename}_copy.{videoformat}"
          print(f"Processing {filepath}. Output: {output_file} (format changed to {videoformat})")

        _, output_filetype = strip_and_split_filepath(output_file)

        # Resize if a resolution has been set
        if resolution:
          input_file = change_res(input_file, output_file, resolution)

        # Change codec if the filetype is not the same for the input and output
        if input_filetype != output_filetype:
          change_codec(input_file, output_file)
          print("Video file type was changed.")

        if resolution:
          if os.path.exists(input_file):
            os.remove(input_file)

      except Exception as e:
        print(f"Error processing {filepath}:", e)


if __name__ == "__main__":
  main()