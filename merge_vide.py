import cv2
import glob
import os
from moviepy.editor import VideoFileClip,concatenate_videoclips

class MERGE_VIDEO:
    def __init__(self, file_path, vcodec=None,base_dir=None,dynamic_name='merge.mp4'):
        self.file_path = file_path
        self.vcodec = vcodec
        self.base_dir = base_dir
        self.dynamic_name = dynamic_name
        
    def read_video_path(self):
        self.fg_video = VideoFileClip(self.file_path, vcodec=self.vcodec)
        self.fg_video_duration = self.fg_video.duration
        self.fg_video_frames = [cv2.resize(frame, (512, 512)) for frame in self.fg_video.iter_frames()]
        self.fg_video_frames_length = len(self.fg_video_frames)
        self.merge_video()
        
        
    def download_video(self):
        download_direc = f"{self.base_dir}/data/download"
        if not os.path.exists(download_direc):
            os.mkdir(download_direc)
        
        
    def merge_video(self):
        clip1 = VideoFileClip(f"{self.base_dir}/data/1.mp4")
        clip2 = VideoFileClip(f"{self.base_dir}/data/2.mp4")
        final_video = concatenate_videoclips([clip1,clip2])
        final_video.write_videofile('final_video4.mp4')
        # return self.base_dir
    
    
    

# imdir = 'data/'
# ext = ['mp4']

# files = []
# [files.extend(glob.glob(imdir + '*.' + e)) for e in ext]

# images = [cv2.imread(file) for file in files]
# print(images)

# clip1 = VideoFileClip()
# clip2 = VideoFileClip()
# final_video = concatenate_videoclips(clip1,clip2)
# final_video.write_videofile('final_video4.mp4')
