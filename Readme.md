# Golden Grain Crop Information Application

## Overview

The Golden Grain application is a Tkinter-based GUI application designed to provide detailed information about various crops, including growth conditions, diseases, prevention methods, and harvesting tips. The application also allows users to view images of the crops, purchase seeds and disease cures from Amazon, and participate in discussions by submitting comments.

## Features

- **Crop Information**: Displays detailed information about different crops, including growth conditions, common diseases, prevention methods, and harvesting tips.
- **Multilingual Support**: Information is available in both English and Kannada.
- **Image Display**: Shows images of selected crops.
- **Amazon Links**: Provides links to purchase seeds and disease cures on Amazon.
- **Discussion Section**: Allows users to submit and view comments related to crops.

## Requirements

- Python 3.x
- Tkinter (typically included with Python)
- Pillow (`PIL` library) for image processing
- Web browser for opening Amazon links

## Installation

1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd golden-grain
    ```

2. **Install the required libraries**:
    ```bash
    pip install pillow
    ```

3. **Ensure image files are in place**: Make sure you have the image files (`Corn.png`, `Carrot.png`, `LOGO.png`) in the `images` directory.

## Usage

1. **Run the application**:
    ```bash
    python app.py
    ```

2. **Interact with the application**:
   - **Select a Crop**: Use the dropdown menu to select a crop.
   - **Choose Language**: Select the desired language to view information in English or Kannada.
   - **View Crop Information**: Detailed information, images, and Amazon links for seeds and disease cures will be displayed.
   - **Submit Comments**: Enter comments in the discussion section and submit them to be saved and displayed.

## File Structure

- `app.py`: The main Python script that runs the Tkinter application.
- `images/`:
  - `Corn.png`: Image file for corn.
  - `Carrot.png`: Image file for carrot.
  - `LOGO.png`: Logo image file.
- `comments.txt`: File to store submitted comments.

## Example

When you start the application, you will see a window with a dropdown menu to select a crop. After selecting a crop, information about the crop will be displayed, including an image, growth conditions, diseases, prevention methods, and harvesting tips. Additionally, links to purchase seeds and disease cures will be available. The discussion section at the bottom allows users to submit and view comments.

## Troubleshooting

- **Image Not Displaying**: Ensure that the image files are located in the `images` directory and named correctly.
- **Amazon Links Not Working**: Verify that the URLs in the `amazon_seed_links` and `amazon_cure_links` dictionaries are correct.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

For questions or feedback, please contact [your email or contact information].

---

Thank you for using Golden Grain! We hope this application helps you with your crop information needs.
