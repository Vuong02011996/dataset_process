from glob import glob
import cv2


def get_all_file_image_and_label():
    labels_dir = '/home/vuong/Desktop/head-dataset/500_first_labels/'
    images_dir = '/home/vuong/Desktop/head-dataset/500_first_images/'

    list_file_labels = glob(labels_dir + '*.txt')
    list_file_labels.sort()
    for i in range(len(list_file_labels)):
        label_file = list_file_labels[i]
        print('label_file', label_file)
        with open(label_file, "r+") as fr:
            lines = fr.readlines()
            if len(lines) == 0:
                print()
                a = 0
            # fr.seek(0)
            # for line in lines:
            #     class_id = int(float(line.split(' ')[0]))
            #     if class_id == 1:
            #         continue
            #     boding_box_label = line.split(' ')[0] + ' ' + line.split(' ')[1] + ' ' + line.split(' ')[2] + ' ' \
            #                        + line.split(' ')[3] + ' ' + line.split(' ')[4]
            #     fr.write(boding_box_label)
            # fr.truncate()


if __name__ == '__main__':
    get_all_file_image_and_label()
