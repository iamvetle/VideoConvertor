import ffmpeg


def change_codec(input_file, output):
    """Changes the codec of a video file using ffmpeg.

    Args:
      input_file: Path to the input video file.
      output: Path to the output video file with the new codec.
      new_codec: The desired codec for the output video (default: "mp4").
    """

    print(input_file)
    print(output)
    try:
        
        input_filetype = input_file.split(".")[-1]
        output_filetype = output.split(".")[-1]
        
        if input_filetype == output_filetype:
            print("The videoformat is the same, no changs made") 
            exit()
  
        # Construct the ffmpeg command with arguments
        ffmpeg.input(input_file).output(output).run()

        # Execute the ffmpeg command using subprocess
    except Exception as e:
        print(f"An error occured while trying to convert the file\n", e)
