# run_morphometrix.py

import sys
import os

# Add the directory containing morphometrix to the Python path
morphometrix_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(morphometrix_dir)

from morphometrix.__main__ import main

if __name__ == "__main__":
    # Set your custom arguments here
    # image_path = "/path/to/your/image.jpg"
    # id = 1234
    # focal_length = 25.0
    # altitude = 50.0
    # pixel_dim = 0.0045

    image_path = None
    id = None
    focal_length = None
    altitude = None
    pixel_dim = None

    # Run the MorphoMetriX program with custom arguments
    main(image_path=image_path, id=id, focal_length=focal_length, altitude=altitude, pixel_dim=pixel_dim)