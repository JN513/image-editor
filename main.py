import os
import cv2
import numpy
from PIL import Image


class Editor:
    image = None
    image_name = None
    image_formate = None
    image_path = None
    image_extension = None
    image_history = list()
    history_position = None

    def reset_editor(self):
        image = None
        image_name = None
        image_formate = None
        image_path = None
        image_extension = None
        image_history = []
        history_position = None

    def open_image(self):
        pass

    def save_image(self):
        pass

    def binary_image(self):
        pass

    def adaptable_binary_image(self):
        pass

    def gray_scale_image(self):
        pass

    def rotate_image(self):
        pass
