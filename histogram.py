import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_and_plot_histograms(image_path):
    """
    Analyzes and plots histograms for each color channel (R, G, B) of an image.

    Args:
        image_path: Path to the image file.
    """

    # Read the image and check if successful
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Could not read image from {image_path}")
        return

    # Split the image into its color channels
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)
        plt.xlim([0, 256])

    # Customize the plot
    plt.xlabel('Pixel Intensity')
    plt.ylabel('Pixel Count')
    plt.title('Color Channel Histograms')
    plt.legend(['Blue', 'Green', 'Red'])
    plt.grid(True)

    # Show the plot
    plt.show()

# Example usage:
image_path = 'my_photo-3.jpg'  # Replace with the actual image path
analyze_and_plot_histograms(image_path)