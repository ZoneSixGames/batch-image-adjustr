# batch-image-adjustr
A Python script for adjusting images in a folder. Resize, sharpen, brighten, contrast, color. 

This script works as follows:

In addition to the directory and resize percentage, it also gets the adjustment factors for contrast, sharpness, brightness, and color from the user. 

The adjustment factor is a float; a factor of 1.0 means the image is unchanged, less than 1.0 means the property is decreased, and more than 1.0 means it's increased.

For each image file in the directory, it resizes the image and adjusts its contrast, sharpness, brightness, and color using the provided factors.

The adjusted image is then saved back to the directory with the prefix 'adjusted_' added to the original filename.
