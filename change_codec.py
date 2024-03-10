import ffmpeg


def change_codec(input_file, output_file):
    """Changes the codec of a video file using ffmpeg.

    Args:
      input_file: Path to the input video file.
      output_file: Path to the output video file with the new codec.
      new_codec: The desired codec for the output video (default: "mp4").
    """
    try:
        print(output_file)
        filename_raw_list = output_file.split(".")
        filetype = filename_raw_list[-1]
        print(filetype)
        filename = filename_raw_list[-2]
        
        output_name = f"{filename}.{filetype}"

        # Construct the ffmpeg command with arguments
        stream = ffmpeg.input(input_file)
        output_stream = ffmpeg.output(stream, output_name)

        # Execute the ffmpeg command using subprocess
        ffmpeg.run(output_stream)
    except Exception as e:
        print(f"An error occured while trying to convert the file\n", e)
