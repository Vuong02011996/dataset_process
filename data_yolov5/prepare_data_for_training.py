from glob import glob
import os
import shutil


def prepare_folder_image_label_for_traing():
    path_images_training = "/storages/data/DATA_YOLOV5/BBGT/images/"
    path_labels_training = "/storages/data/DATA_YOLOV5/BBGT/labels/"

    src_dir = "/storages/data/vuonglv/traffic_sign/Trafic_sign/Training/darknet/data/obj"
    for jpgfile in glob(os.path.join(src_dir, "*.jpg")):
        shutil.copy(jpgfile, path_images_training)

    for txtfile in glob(os.path.join(src_dir, "*.txt")):
        shutil.copy(txtfile, path_labels_training)


if __name__ == '__main__':
    prepare_folder_image_label_for_traing()