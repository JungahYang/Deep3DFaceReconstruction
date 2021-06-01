import cv2

def maintain_aspect_ratio_resize(image, width=None, height=None):
    # Grab the image size and initialize dimensions
    dim = None
    (h, w) = image.shape[:2]
    # Return original image if no need to resize
    if width is None and height is None:
        return image
    # We are resizing height if width is none
    if width is None:
        # Calculate the ratio of the height and construct the dimensions
        r = height / float(h)
        dim = (int(w * r), height)
    # We are resizing width if height is none
    else:
        # Calculate the ratio of the 0idth and construct the dimensions
        r = width / float(w)
        dim = (width, int(h * r))
    # Return the resized image
    return cv2.resize(image, dim)


img = cv2.imread("/mnt/DATA/yg/uniinfo/3DDFA_V2/examples/inputs/YunJu.jpg")
print(img.shape)
img = maintain_aspect_ratio_resize(img, width=800)
print(img.shape)
cv2.imshow('', img)
cv2.waitKey(0)