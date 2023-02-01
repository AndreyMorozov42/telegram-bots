import argparse

from moviepy.editor import VideoFileClip

def main(path):
    video_clip = VideoFileClip(path)
    video_clip.write_gif("video_to_gif_file.gif")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("path_to_video")
    main(parser.parse_args().path_to_video)
