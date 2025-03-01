from PIL import Image
import os

images = ["Photo 0.jpg", "Photo 1.jpg", "Photo 2.jpg", "Photo 3.jpg", "Photo 4.jpg"]
resize_configs = [
    ((1400, 1000), "VK"),
    ((1080, 1080), "Instagram"),
    ((1200, 629), "Facebook")
]
for i, images in enumerate(images):
    folder_name = os.path.splitext(images)[0]
    os.makedirs(folder_name, exist_ok=True)

    image = Image.open(images)

    for size, platform in resize_configs:
        resized_image = image.resize(size)
        if platform == "Instagram":
            width, height = resized_image.size
            left = 10
            right = width - 10
            top = 0 
            bottom = height
            cropped_image = resized_image.crop((left, top, right, bottom))
            filename = os.path.join(folder_name, f"{platform}.jpeg")
            cropped_image.save(filename)
        else:
            filename = os.path.join(folder_name, f"{platform}.jpeg")
            resized_image.save(filename)