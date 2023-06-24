import os
from PIL import Image, ImageEnhance

def adjust_image(directory, resize_percentage, contrast, sharpness, brightness, color):
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff', '.bmp', '.gif')):
            img = Image.open(os.path.join(directory, filename))
            
            # Resize
            width, height = img.size
            new_size = (int(width * resize_percentage), int(height * resize_percentage))
            img = img.resize(new_size, Image.ANTIALIAS)

            # Adjust contrast, sharpness, brightness and color
            img = ImageEnhance.Contrast(img).enhance(contrast)
            img = ImageEnhance.Sharpness(img).enhance(sharpness)
            img = ImageEnhance.Brightness(img).enhance(brightness)
            img = ImageEnhance.Color(img).enhance(color)

            # Save the adjusted image
            img.save(os.path.join(directory, f'adjusted_{filename}'))
            print(f'Adjusted image saved as: adjusted_{filename}')

if __name__ == "__main__":
    dir_path = input("Enter the directory path: ")
    resize_perc = float(input("Enter the resize percentage (as a decimal): "))
    contrast = float(input("Enter the contrast adjustment factor (1.0 is original): "))
    sharpness = float(input("Enter the sharpness adjustment factor (1.0 is original): "))
    brightness = float(input("Enter the brightness adjustment factor (1.0 is original): "))
    color = float(input("Enter the color adjustment factor (1.0 is original): "))
    
    adjust_image(dir_path, resize_perc, contrast, sharpness, brightness, color)
