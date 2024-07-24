# VisionForge: Advanced Python Image Converter

VisionForge is a powerful Python-based image converter application with a custom GUI using `tkinter` and `customtkinter`, designed for efficient batch processing and format conversion.

![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

![VisionForge GUI](https://i.ibb.co/bHVDq3j/visionforge.png)

## Overview

VisionForge is an advanced image conversion tool engineered to handle multiple image formats with ease. It leverages Python's robust libraries, combining `tkinter` and `customtkinter` for a sleek graphical user interface (GUI), while utilizing `Pillow` for high-performance image processing. This application empowers users to select, convert, and save images in various formats, showcasing the practical application of Python in image processing and GUI development.

## Key Features

- **Dynamic Image Selection**: Convert multiple image files to various formats in a single operation.
- **Multithreaded Conversion**: Utilize multiple threads for enhanced performance and faster processing.
- **Localization Support**: Enjoy a bilingual interface with support for English and French.
- **Customizable Output**: Fine-tune your conversions with adjustable output quality and metadata preservation options.
- **User-Friendly Interface**: Simplify your workflow with an intuitive GUI, eliminating the need for code modifications.
- **Dark Mode**: Reduce eye strain with a built-in dark mode for comfortable use in any lighting condition.
- **Flexible Output Formats**: Support for JPEG, PNG, GIF, BMP, WEBP, and TIFF formats.
- **Progress Tracking**: Real-time progress bar and status updates during conversion.

## How It Works

1. **Logging Setup**: Initializes a logging system to record application events.
2. **Variable Initialization**: Sets up default values for UI variables.
3. **Localization Configuration**: Configures translations for English and French languages.
4. **Widget Creation**: Constructs the main components of the GUI, including the sidebar and main frame.
5. **File Selection**: Allows users to select multiple image files for conversion.
6. **Output Directory Selection**: Enables users to choose the directory for saving converted files.
7. **Conversion Process**: Utilizes a thread pool to convert selected files concurrently, enhancing performance.
8. **UI Updates**: Continuously refreshes the interface to reflect real-time conversion status.

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

Launch VisionForge with a simple command:

```bash
python VisionForge.py
```

Follow the intuitive on-screen instructions to select images, choose output formats, and initiate the conversion process.

## Why Choose VisionForge?

VisionForge is the ideal solution for users seeking a reliable, efficient, and user-friendly image conversion tool. It's perfect for:

- Professional photographers managing diverse image formats
- Graphic designers requiring quick and batch format conversions
- IT professionals handling large-scale image processing tasks
- Students and educators exploring image processing and GUI development

By automating the conversion process, VisionForge significantly reduces time and minimizes errors, making it an indispensable tool for anyone regularly dealing with image format conversions.

## Contributing

Contributions to VisionForge are welcome! Here's how you can get involved:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

For major changes, please open an issue first to discuss what you would like to change.

## License

VisionForge is distributed under the MIT License. See `LICENSE` file for more information.

## Acknowledgements

- [customtkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI components
- [Pillow](https://python-pillow.org/) for image processing capabilities

---

Developed with ❤️ by [PixelPerfekt](https://pixelperfekt.me/)
