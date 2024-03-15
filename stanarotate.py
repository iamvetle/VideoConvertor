from moviepy.editor import VideoFileClip
from moviepy.video import fx

input = "./longstana.mov"

def main():

    try:
        with VideoFileClip(input) as clip:
            # print(clip)
            rotated_clip = clip.rotate(90)
            rotated_clip.write_videofile("rotatedStana.mov", codec="libx264")
            rotated_clip.close()
    except Exception as e:
        print(e)




main()