"""
PetDataset
"""

import cv2
import numpy as np
import random
import os
import glob


# class Image(object):
#     def __init__(self, filename):
#         pass
#
#     def get_normalized_value(self, random=true):
#
#


class PetDataset(object):
    def __init__(self, directory="temp\images", image_width=28, image_height=28):
        self.directory=directory
        self.image_width = image_width
        self.image_height = image_height

    def load(self):
        dogs = self.generate_label_data(glob.glob(os.path.join(self.directory, "shiba_inu_*.jpg")), 0)
        cats = (self.generate_label_data(glob.glob(os.path.join(self.directory, "Abyssinian_*.jpg")), 1))

        self.file_list = []
        self.file_list.extend(dogs)
        self.file_list.extend(cats)


    def generate_label_data(self, files, label):
        data = []
        for name in files:
            data.append([name, label])
        return data

    def generate_batch(self, size=100):
        batch = []
        for i in range(size):
            image, label = self.get_randomized_image()
            normalized = self.normalize_image(image)
            batch.append([normalized, label])
        return batch

    def get_randomized_image(self):
        filename, label = self.file_list[random.randrange(len(self.file_list))]
        image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
        image = cv2.resize(image, (self.image_width, self.image_height))
        if bool(random.getrandbits(1)):
            image = cv2.flip(image, 1) #  左右反転
        return image, label

    def normalize_image(self, image):
        return image.flatten().astype(np.float32)/255.0


    def __repr__(self):
        return
