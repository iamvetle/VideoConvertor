from moviepy.editor import VideoFileClip

def change_res(input, res):
    
    """
     Resizes the video input to the desired resolution

     Args:
        input: The input file to resize
        res: The resolution to use. As a tuple (w, h)
     """

    print("Trying to resize video..")

    try:
        input_filename = (input.split(".")[-2]).split("\\")[1]
        input_filetype = input.split(".")[-1]

        output = f"{input_filename}{res[1]}.{input_filetype}"
    
        # The video object
        clip = VideoFileClip(input)

        # Resizing
        resized_clip = clip.resize(res)
        
        # Write to file based on video format
        if input_filetype == "mov":
            resized_clip.write_videofile(output, codec="libx264")   
        elif input_filetype == "avi":
            resized_clip.write_videofile(output, codec="png")
        elif input_filetype == "ogv":
            resized_clip.write_videofile(output, code="libvorbis")
        else:
            resized_clip.write_videofile(output)         

        return output

    except Exception as e:
        print("An error eccured while trying to change resolution:", e)
