import os
import cv2
import numpy as np
from PIL import Image


class Editor:
    image = None
    image_name = None
    image_formate = None
    image_path = None
    image_extension = None
    image_history = list()
    history_position = None
    original_image = None

    def reset_editor(self):
        self.image = None
        self.image_name = None
        self.image_formate = None
        self.image_path = None
        self.image_extension = None
        self.image_history = []
        self.history_position = None
        self.original_image = None

    def pil_to_cv(self, image):
        cv_image = np.array(image)
        cv_image = cv_image[:, :, ::-1].copy()
        return cv_image

    def cv_to_pil(self, image):
        pil_image = Image.fromarray(image)
        return pil_image

    def load_image(self, image):
        try:
            self.image = Image.open(image).convert("RGB")
            self.image_formate = self.image.format
            self.image_name, self.image_extension = os.path.splitext(
                os.path.basename(image)
            )
            self.image_path = os.path.dirname(os.path.realpath(image))
            self.original_image = self.image
            print("Imagem carregada com sucesso.")
            return True
        except:
            print("Não foi possivel carregar a imagem.")
            return False

    def save_image(self, path, image_name, extension=None):
        if extension == None:
            extension = self.image_extension
        save_path = f"{path}/{image_name}{extension}"
        self.image.save(save_path, self.image_formate)
        self.reset_editor()

    def reset_image(self):
        self.image = self.original_image

    def smooth_image(self):
        cv_image = self.pil_to_cv(self.image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        cv_image = cv2.equalizeHist(cv_image)
        cv_image = cv2.GaussianBlur(cv_image, (9, 9), 1)  # suavisa a imagem

        self.image = self.cv_to_pil(cv_image)

    def binary(self):
        cv_image = self.pil_to_cv(self.image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        cv_image = cv2.equalizeHist(cv_image)
        cv_image = cv2.GaussianBlur(cv_image, (9, 9), 1)  # suavisa a imagem

        return cv_image

    def binary_image(self):
        cv_image = self.binary()
        valor_retorno, cv_image = cv2.threshold(
            cv_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
        )
        self.image = self.cv_to_pil(cv_image)

    def binary_image_reverse(self):
        cv_image = self.binary()
        valor_retorno, cv_image = cv2.threshold(
            cv_image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
        )
        self.image = self.cv_to_pil(cv_image)

    def binary_image_trunc(self):
        cv_image = self.binary()
        valor_retorno, cv_image = cv2.threshold(
            cv_image, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU
        )
        self.image = self.cv_to_pil(cv_image)

    def binary_image_tozero(self):
        cv_image = self.binary()
        valor_retorno, cv_image = cv2.threshold(
            cv_image, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU
        )
        self.image = self.cv_to_pil(cv_image)

    def binary_image_tozero_reverse(self):
        cv_image = self.binary()
        valor_retorno, cv_image = cv2.threshold(
            cv_image, 0, 255, cv2.THRESH_TOZERO_INV + cv2.THRESH_OTSU
        )
        self.image = self.cv_to_pil(cv_image)

    def adaptable_binary_image_mean(self):
        cv_image = self.binary()
        cv_image = cv2.adaptiveThreshold(
            cv_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2
        )

        self.image = self.cv_to_pil(cv_image)

    def adaptable_binary_image_gaussian(self):
        cv_image = self.binary()
        cv_image = cv2.adaptiveThreshold(
            cv_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2
        )

        self.image = self.cv_to_pil(cv_image)

    def gray_scale_image(self):
        cv_image = self.pil_to_cv(self.image)
        cv_image = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        self.image = self.cv_to_pil(cv_image)

    def rotate_image(self, sentido="horario", angulo=90):
        if sentido == "horario":
            self.image = self.image.rotate(angulo * -1)
        elif sentido == "anti_horario":
            self.image = self.image.rotate(angulo)

    def cartoon_image(self):
        cv_image = self.pil_to_cv(self.image)
        cv_image_gray = cv2.cvtColor(cv_image, cv2.COLOR_BGR2GRAY)
        cv_image_gray = cv2.medianBlur(cv_image_gray, 5)
        edges = cv2.adaptiveThreshold(
            cv_image_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9
        )

        color = cv2.bilateralFilter(cv_image, 9, 250, 250)
        cartoon = cv2.bitwise_and(color, color, mask=edges)
        self.image = self.cv_to_pil(cartoon)


editor = Editor()
