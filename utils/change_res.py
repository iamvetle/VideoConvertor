from moviepy.editor import VideoFileClip
import os

# Local

from utils.strip_and_split_filepath import strip_and_split_filepath

def change_res(input, output, res):
    """
    Resizes the video input to the desired resolution

    Args:
       input: The input file to resize
       output: The output file path 
       res: The resolution to use. As a tuple (w, h)
       
    Return: it returns the path to the place the write file is
    """

    print("Trying to resize video..")
    
    if not res:
        print("No resolution specified")
        return
    try:
        
        input_filename, input_filetype = strip_and_split_filepath(input)
        
        print(input_filename)
        print(input_filetype)
        
        output_filename, output_filetype = strip_and_split_filepath(output)
        
        output_file = output

        
        if output_filetype != input_filetype:
            output_file = f"{output_filename}resized_to_{res[1]}.{input_filetype}"
        
        print(output_filename)

        # The video object
        
        with VideoFileClip(input) as clip:

            # Resizing
            resized_clip = clip.resize(res)


            # Write to file based on video format
            if input_filetype == "mov":
                resized_clip.write_videofile(output_file, codec="libx264")
            elif input_filetype == "avi":
                resized_clip.write_videofile(output_file, codec="png")
            elif input_filetype == "ogv":
                resized_clip.write_videofile(output_file, codec="libvorbis")
            elif input_filetype == "webm":
                resized_clip.write_videofile(output_file, codec="libvpx")
            else:
                resized_clip.write_videofile(output_file)

            print(f"{input_filename} resized to {res[1]}p")

            clip.close()
            return output_file

    except Exception as e:
        print("An error eccured while trying to change resolution:", e)
        return
