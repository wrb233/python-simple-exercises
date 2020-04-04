from moviepy.editor import *
import cv2    
import dlib  
import numpy as np   
from moviepy.editor import *   
from PIL import Image  

# video_save_path = '_result.mp4'
#
# video_path = './pic/origin.mp4'
# # final = VideoFileClip(video_save_path)
# # final_vedio = final.set_audio(AudioFileClip(video_path))
# # final_vedio.write_videofile('./final_vedio.mp4')

# final = VideoFileClip('./pic/origin.mp4').subclip(4, 11)
# final.write_videofile('./original.mp4')

path = './result/'
video_path = "./pic/original.mp4"
shape = (1280, 720)
file = os.listdir(path)  # 获取该目录下的所有文件名
filelist = ['{}.png'.format(i) for i in range(len(file))]
print(filelist)
fps = 30
video_save_path = video_path.split('.')[0] + "result.mp4"  # 导出路径
print(video_save_path)
fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
video = cv2.VideoWriter(video_save_path, fourcc, fps, shape)
for item in filelist:  # 开始拼接视频
    if item.endswith('.png'):  # 判断图片后缀是否是.png
        item = path + '/' + item
        print(item)
        img = cv2.imread(item)
        video.write(img)  # 把图片写进视频
video.release()  # 释放
final = VideoFileClip(video_save_path)
final_vedio = final.set_audio(AudioFileClip(video_path))  # 捕获原先视频中的音频信息，并拼接到新的视频当中
final_vedio.write_videofile('./final_vedio.mp4')