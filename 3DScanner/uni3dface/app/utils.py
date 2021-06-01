import os
import numpy as np
from matplotlib import pyplot as plt


class SafeUtils:
    @staticmethod
    def remove_files(files):
        for file in files:
            try:
                os.remove(file)
            except Exception:
                pass
