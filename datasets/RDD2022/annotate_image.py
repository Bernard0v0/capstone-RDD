import os
import cv2

# 类别到颜色的映射
category_colors = {
    1: (0, 255, 0),   # 绿色，longitudinal crack
    2: (0, 0, 255),   # 红色，transverse crack
    3: (255, 0, 0),   # 蓝色，alligator crack
    4: (255, 255, 0)  # 黄色，pothole
}

# 类别到标签的映射
category_labels = {
    1: 'longitudinal crack',
    2: 'transverse crack',
    3: 'alligator crack',
    4: 'pothole'
}

# 读取标注信息并解析
# 读取标注信息并解析
def draw_annotation(image,annotation):
    numbers = annotation.split()
    for i in range(0, len(numbers), 5):
        group = numbers[i:i + 5]
        color = category_colors[int(group[0])]
        thickness = 2
        x1 = int(group[1])
        y1 = int(group[2])
        x2 = int(group[3])
        y2 = int(group[4])
        image = cv2.rectangle(image, (x1, y1), (x2, y2), color, thickness)
        label = category_labels[int(group[0])]
        cv2.putText(image, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,255,255), 1)
    return image
# 绘制标注框


# 标注图片并保存
def annotate_images(image_folder, annotation_file, save_folder):
    # 确保保存文件夹存在
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    # 读取标注文件
    with open(annotation_file, 'r') as file:
        annotations = file.readlines()

    for annotation in annotations:
        # 获取图片名字

        image_name, annots = annotation.split(',', 1)
        image_path = os.path.join(image_folder, image_name)
        if annots == '' or annots == '\n':
            print(f'image: {image_name} does not have any annotation, passed')
            continue
        # 读取图片
        image = cv2.imread(image_path)
        image = draw_annotation(image, annots)
        save_name = os.path.splitext(image_name)[0] + '_annotated.jpg'
        # 保存标注后的图片
        save_path = os.path.join(save_folder, save_name)
        cv2.imwrite(save_path, image)

        print(f'image: {image_name} completed and saved at: {save_path}')

if __name__ == "__main__":
    # 文件夹路径
    image_folder = "test1_images"
    annotation_file = "/home/zelinqian/Desktop/IFB398/yolov7/runs/detect/exp5/result"
    save_folder = "annotated_images"

    annotate_images(image_folder, annotation_file, save_folder)
# python detect.py --weights yolov7x_640.pt --source /home/zelinqian/Desktop/IFB398/datasets/RDD2022/test1_images --img-size 800 --conf-thres 0.2 --iou-thres 0.25 --device 0
