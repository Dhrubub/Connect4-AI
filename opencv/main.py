import cv2

img1: str = "./test/img1.png"
img2: str = "./test/img2.png"


def show(img, title=""):
    cv2.imshow(title, img)
    cv2.moveWindow(title, 200, 200)
    cv2.waitKey(0)


def resize_img(filename, width=500):
    new_width = 500
    img = cv2.imread(filename)
    img_h, img_w, _ = img.shape
    scale = width / img_w
    img_w = int(img_w * scale)
    img_h = int(img_h * scale)
    img = cv2.resize(img, (img_w, img_h), interpolation=cv2.INTER_AREA)

    return img


if __name__ == "__main__":
    resized_img = resize_img(img2)
    show(resized_img)
