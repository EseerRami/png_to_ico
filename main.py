from PIL import Image

def combine_png_to_ico(png_files, output_ico_file):
    """
    Combine multiple PNG files into a single ICO file.

    Parameters:
    - png_files (list of str): List of paths to PNG files to be combined.
    - output_ico_file (str): Path to the output ICO file.
    """
    images = []
    
    # Open each PNG file and append to images list
    for png_file in png_files:
        img = Image.open(png_file)
        images.append(img)
    
    # Save images as a single ICO file
    images[0].save(output_ico_file, format='ICO', append_images=images[1:])

png_files = ['images/icon1.png', 'images/icon2.png', 'images/icon3.png']  # Replace with actual paths
output_ico_file = 'combined/output_icon.ico'  # Replace with desired output path

combine_png_to_ico(png_files, output_ico_file)
