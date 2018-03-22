import os
import re

CURRENT_DIR = os.getcwd()
IMAGES_DIR = os.path.join(CURRENT_DIR, "prank_2")


def rename_files(dir):
    for image_name in os.listdir(dir):
        image_path = os.path.join(dir, image_name)
        new_image_name = re.sub(r'\d+', ' ', image_name)  # Or use image_name.translate(None, '0123456789') instead
        new_image_path = os.path.join(dir, new_image_name)
        os.rename(image_path, new_image_path)
        print("Rename image {} to {}".format(image_name, new_image_name))


rename_files(IMAGES_DIR)
