from PIL import Image, ImageOps
from skimage.transform import resize

import os, uuid, json
import numpy as np
import torch


class NotAcceptableException(Exception):
    def __init__(self, message):
        self.message = message
    
    
    def __str__(self):
        if self.message:
            return "NotAcceptableException, {}".format(self.message)
        else:
            return "NotAcceptableException has been raised."


class Uni3dService:
    def __init__(self):
        pass


    def predict_simple(self, photo):
        pass