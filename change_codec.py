import ffmpeg

# Local
from strip_and_split_filepath import strip_and_split_filepath


def change_codec(input, output):
    """Changes the codec of a video file using ffmpeg.

    Args:
      input: Path to the input video file.
      output: Path to the output video file with the new codec.
      new_codec: The desired codec for the output video (default: "mp4").
    """

    try:
        _, input_filetype  = strip_and_split_filepath(input)
        
        _, output_filetype = strip_and_split_filepath(output)
        
        if input_filetype == output_filetype:
            print("The videoformat is the same, no changes made") 
            return
        # Construct the ffmpeg command with arguments
        ffmpeg.input(input).output(output).run()
        
        print(f"Successfully converted the file to .{output_filetype}")

        # Execute the ffmpeg command using subprocess
    except Exception as e:
        print(f"An error occured while trying to convert the file\n", e)
        return
