import cv2
import dlib
import numpy as np
from moviepy.editor import *
from PIL import Image

class Valentine(object):
    def __init__(self, eye_img="pic/face1.jpg", video_path="./pic/origin.mp4", size=(1280, 720)):
        self.src_img = eye_img
        self.video_path = video_path
        self.shape = size
        self.paste_pic()
        self.pic_2_video()

    def img_deal(self, input_img):
        img = cv2.imread(input_img, cv2.IMREAD_UNCHANGED)
        rows, cols, channel = img.shape

        img1 = np.zeros((rows, cols, 4), np.uint8)
        img1[:, :, 0:3] = img[:, :, 0:3]

        img_circle = np.zeros((rows, cols, 1), np.uint8)
        img_circle[:, :, :] = 0
        img_circle = cv2.circle(img_circle, (int(cols / 2), int(rows / 2)), int(min(rows, cols) / 2), 255, -1)

        img1[:, :, 3] = img_circle[:, :, 0]
        cv2.imwrite('./pic/src_circle.png', img1)

    def paste_pic(self):
        cap = cv2.VideoCapture(self.video_path)  # 视频文件的读取
        if cap.isOpened() != True:
            exit(-1)
        num = 0
        detector = dlib.get_frontal_face_detector()
        predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
        # 对象创建成功后isOpened()将返回true
        while True:
            # 一帧一帧的捕获
            ret, img = cap.read()
            if ret != True:
                break
            #眼睛内容图片
            src = cv2.imread(self.src_img)
            gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            faces = detector(gray)

            for face in faces:
                landmarks = predictor(gray, face)  # 识别面部的特征点
                areaX1 = max(landmarks.part(37).x, landmarks.part(41).x)
                areaX2 = min(landmarks.part(38).x, landmarks.part(40).x)
                areaY1 = max(landmarks.part(37).y, landmarks.part(38).y)
                areaY2 = min(landmarks.part(41).y, landmarks.part(40).y) # 找到眼部的坐标位置
                r = int(min(areaX2-areaX1,areaY2-areaY1)/2)  # 找到眼部的长度
                d=2*r
                midx = int((areaX1 + areaX2)/2)
                midy = int((areaY1 + areaY2)/2)

                left = cv2.resize(src, (d, d), interpolation=cv2.INTER_AREA)  # 调整女主的图片大小
                cv2.imwrite("./pic/left_eye.png", left)
                self.img_deal("./pic/left_eye.png")  # 将调整后女主的图片改成圆形，贴合人眼的形状
                im = Image.fromarray(img[...,::-1])
                eye = Image.open("./pic/src_circle.png")
                im.paste(eye,(midx-r,midy-r),eye)  # 将女主图片贴到原图左眼中，下面的右眼采用同样的方式

                area2X1 = max(landmarks.part(43).x,landmarks.part(47).x)
                area2X2 = min(landmarks.part(44).x,landmarks.part(46).x)
                area2Y1 = max(landmarks.part(43).y,landmarks.part(44).y)
                area2Y2 = min(landmarks.part(47).y,landmarks.part(46).y)
                r2 = int(min(area2X2-area2X1,area2Y2-area2Y1)/2)
                d2=2*r2
                midx2 = int((area2X1 + area2X2)/2)
                midy2 = int((area2Y1 + area2Y2)/2)

                try:
                    right = cv2.resize(src, (d2, d2), interpolation=cv2.INTER_AREA)
                    cv2.imwrite("./pic/right_eye.png", right)
                    self.img_deal("./pic/right_eye.png")
                    eye = Image.open("./pic/src_circle.png")
                    im.paste(eye,(midx2-r2,midy2-r2),eye)
                    im.save("./result/{}.png".format(num))
                except cv2.error as e:
                    im.save("./result/{}.png".format(num))

            num += 1

    def pic_2_video(self):
        path = './result/'
        file = os.listdir(path)  # 获取该目录下的所有文件名
        filelist = ['{}.png'.format(i) for i in range(len(file))]
        print(filelist)
        fps = 30
        video_save_path = self.video_path.split('.')[0] + "result.mp4"  # 导出路径
        print(video_save_path)
        fourcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')  # 不同视频编码对应不同视频格式（例：'I','4','2','0' 对应avi格式）
        video = cv2.VideoWriter(video_save_path, fourcc, fps, self.shape)
        for item in filelist:  # 开始拼接视频
            if item.endswith('.png'):  # 判断图片后缀是否是.png
                item = path + '/' + item
                print(item)
                img = cv2.imread(item)
                video.write(img)  # 把图片写进视频
        video.release()  # 释放
        final = VideoFileClip(video_save_path)
        final_vedio = final.set_audio(AudioFileClip(self.video_path))  # 捕获原先视频中的音频信息，并拼接到新的视频当中
        final_vedio.write_videofile('./final_vedio.mp4')


if __name__ == '__main__':
    Valentine(eye_img="pic/face1.jpg", video_path="./pic/original.mp4", size=(1280, 720))



