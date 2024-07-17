
# VisionForge

VisionForge is a Python-based image converter application with a custom GUI using `tkinter` and `customtkinter`.

## Overview
VisionForge is an advanced image conversion tool designed to handle multiple image formats. It leverages Python with `tkinter` and `customtkinter` for the graphical user interface (GUI), and `Pillow` for image processing. This application allows users to select, convert, and save images in various formats, demonstrating the practical use of Python in image processing and GUI development.

## Features
- **Dynamic Image Selection**: Enables conversion of multiple image files to various formats.
- **Multithreaded Conversion**: Utilizes multiple threads to enhance performance.
- **Localization Support**: Offers a multilingual interface with support for English and French.
- **Customizable Output**: Allows customization of output quality and the option to preserve metadata.
- **User-Friendly Interface**: Simplifies operation with an intuitive GUI, eliminating the need for code modifications.
- **Dark Mode**: Provides a dark mode for a comfortable user experience.

## How It Works
1. **Setup Logging**: Initializes logging to record application events.
2. **Initialize Variables**: Sets up default values for UI variables.
3. **Localization Setup**: Configures translations for English and French languages.
4. **Create Widgets**: Constructs the main components of the GUI, including the sidebar and main frame.
5. **File Selection**: Allows users to select image files for conversion.
6. **Output Directory Selection**: Enables users to choose the directory for saving converted files.
7. **Start Conversion**: Begins the conversion process in a separate thread to ensure a responsive UI.
8. **Convert Files**: Uses a thread pool to convert selected files concurrently, enhancing performance.
9. **Update UI**: Refreshes the UI to reflect the current status of the conversion process.

## Requirements
- Python 3.x
- `tkinter`
- `customtkinter`
- `Pillow`

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/SilentForge/VisionForge.git
   ```
2. Navigate to the project directory:
   ```bash
   cd VisionForge
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the application:
```bash
python VisionForge.py
```

## Why This Tool?
VisionForge is designed for users who need a reliable and efficient image conversion tool. It is ideal for photographers, designers, and anyone dealing with multiple image formats. This tool automates the conversion process, making it invaluable for tasks requiring batch image processing.

## Contributing
Contributions are welcome! Please fork the repository, make your changes, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License
Distributed under the MIT License. See `LICENSE` for more information.

## Disclaimer
This tool is for educational purposes only. Be mindful of the target website's terms of service regarding web scraping and data usage.
