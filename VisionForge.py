import tkinter as tk
from tkinter import filedialog, messagebox
import customtkinter as ctk
from PIL import Image
import os
import threading
import logging
from concurrent.futures import ThreadPoolExecutor
import multiprocessing

class ImageConverterApp(ctk.CTk):
    """
    Main application class for the VisionForge image converter.
    """
    def __init__(self):
        """
        Initialize the main application window and its components.
        """
        super().__init__()

        self.title("VisionForge")
        self.geometry("1000x600")

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.setup_logging()
        self.init_variables()
        self.setup_localization()
        self.create_widgets()
        self.create_layout()

    def setup_logging(self):
        """
        Set up logging configuration to log info and error messages to a file.
        """
        logging.basicConfig(filename='visionforge.log', level=logging.INFO,
                            format='%(asctime)s - %(levelname)s - %(message)s')

    def init_variables(self):
        """
        Initialize UI variables with default values.
        """
        self.selected_files = []
        self.output_format = ctk.StringVar(value="JPEG")
        self.quality = ctk.IntVar(value=85)
        self.max_threads = ctk.IntVar(value=multiprocessing.cpu_count())
        self.preserve_metadata = ctk.BooleanVar(value=True)
        self.output_directory = ctk.StringVar(value="")
        self.current_language = ctk.StringVar(value="en")

    def setup_localization(self):
        """
        Set up localization with translations for English and French languages.
        """
        self.translations = {
            "en": {
                "select_images": "Select Images",
                "convert": "Convert",
                "output_format": "Output Format:",
                "quality": "Quality:",
                "threads": "Number of threads:",
                "preserve_metadata": "Preserve metadata",
                "output_directory": "Output Directory",
                "appearance": "Appearance:",
                "language": "Language:",
                "waiting_selection": "Waiting for selection...",
                "files_selected": "{} files selected",
                "converting": "Converting... ({}/{})",
                "conversion_complete": "Completed. {} out of {} files converted.",
                "error": "Error",
                "select_files_error": "Please select files first.",
            },
            "fr": {
                "select_images": "Sélectionner Images",
                "convert": "Convertir",
                "output_format": "Format de sortie :",
                "quality": "Qualité :",
                "threads": "Nombre de threads :",
                "preserve_metadata": "Conserver les métadonnées",
                "output_directory": "Dossier de sortie",
                "appearance": "Apparence :",
                "language": "Langue :",
                "waiting_selection": "En attente de sélection...",
                "files_selected": "{} fichiers sélectionnés",
                "converting": "Conversion en cours... ({}/{})",
                "conversion_complete": "Terminé. {} sur {} fichiers convertis.",
                "error": "Erreur",
                "select_files_error": "Veuillez d'abord sélectionner des fichiers.",
            }
        }

    def get_text(self, key):
        """
        Retrieve the translation for the current language.

        Args:
            key (str): The key for the translation string.

        Returns:
            str: The translated string.
        """
        return self.translations[self.current_language.get()].get(key, key)

    def create_widgets(self):
        """
        Create main containers for the sidebar and main frame, and initialize their widgets.
        """
        self.sidebar = ctk.CTkFrame(self, width=250, corner_radius=0)
        self.main_frame = ctk.CTkFrame(self)

        self.create_sidebar_widgets()
        self.create_main_frame_widgets()

    def create_sidebar_widgets(self):
        """
        Create and place widgets in the sidebar.
        """
        self.logo_label = ctk.CTkLabel(self.sidebar, text="VisionForge", font=ctk.CTkFont(size=24, weight="bold"))
        self.select_button = ctk.CTkButton(self.sidebar, text=self.get_text("select_images"), command=self.select_files)
        self.convert_button = ctk.CTkButton(self.sidebar, text=self.get_text("convert"), command=self.start_conversion)
        
        self.format_label = ctk.CTkLabel(self.sidebar, text=self.get_text("output_format"))
        self.format_menu = ctk.CTkOptionMenu(self.sidebar, values=["JPEG", "PNG", "GIF", "BMP", "WEBP", "TIFF"],
                                             variable=self.output_format)
        
        self.quality_label = ctk.CTkLabel(self.sidebar, text=self.get_text("quality"))
        self.quality_slider = ctk.CTkSlider(self.sidebar, from_=1, to=100, variable=self.quality,
                                            command=self.update_quality_label)
        self.quality_value_label = ctk.CTkLabel(self.sidebar, text="85")
        
        self.thread_label = ctk.CTkLabel(self.sidebar, text=self.get_text("threads"))
        self.thread_slider = ctk.CTkSlider(self.sidebar, from_=1, to=multiprocessing.cpu_count(),
                                           number_of_steps=multiprocessing.cpu_count()-1,
                                           variable=self.max_threads,
                                           command=self.update_thread_label)
        self.thread_value_label = ctk.CTkLabel(self.sidebar, text=str(multiprocessing.cpu_count()))
        
        self.preserve_metadata_checkbox = ctk.CTkCheckBox(self.sidebar, text=self.get_text("preserve_metadata"),
                                                          variable=self.preserve_metadata)
        
        self.output_dir_button = ctk.CTkButton(self.sidebar, text=self.get_text("output_directory"), command=self.select_output_directory)
        
        self.appearance_mode_label = ctk.CTkLabel(self.sidebar, text=self.get_text("appearance"))
        self.appearance_mode_menu = ctk.CTkOptionMenu(self.sidebar, values=["Light", "Dark", "System"],
                                                      command=self.change_appearance_mode)
        self.appearance_mode_menu.set("Dark")

        self.language_label = ctk.CTkLabel(self.sidebar, text=self.get_text("language"))
        self.language_menu = ctk.CTkOptionMenu(self.sidebar, values=["English", "Français"],
                                               command=self.change_language)
        self.language_menu.set("English")

    def create_main_frame_widgets(self):
        """
        Create and place widgets in the main frame.
        """
        self.file_list = ctk.CTkTextbox(self.main_frame, width=400)
        self.progressbar = ctk.CTkProgressBar(self.main_frame)
        self.status_label = ctk.CTkLabel(self.main_frame, text=self.get_text("waiting_selection"))

    def create_layout(self):
        """
        Configure the grid layout for the main window and place the main containers.
        """
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.sidebar.grid(row=0, column=0, sticky="nsew")
        self.main_frame.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        # Sidebar layout
        self.sidebar.grid_rowconfigure(15, weight=1)
        widgets = [self.logo_label, self.select_button, self.convert_button, 
                   self.format_label, self.format_menu, self.quality_label, 
                   self.quality_slider, self.quality_value_label, self.thread_label, 
                   self.thread_slider, self.thread_value_label, 
                   self.preserve_metadata_checkbox, self.output_dir_button, 
                   self.appearance_mode_label, self.appearance_mode_menu,
                   self.language_label, self.language_menu]
        
        for i, widget in enumerate(widgets):
            widget.grid(row=i, column=0, padx=20, pady=(10 if i == 0 else 5), sticky="ew")

        # Main frame layout
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.file_list.grid(row=0, column=0, sticky="nsew", padx=20, pady=20)
        self.progressbar.grid(row=1, column=0, sticky="ew", padx=20, pady=(0, 10))
        self.status_label.grid(row=2, column=0, sticky="ew", padx=20, pady=(0, 20))

    def select_files(self):
        """
        Open a file dialog to select images and update the UI accordingly.
        """
        filetypes = [("Images", "*.png;*.jpg;*.jpeg;*.gif;*.bmp;*.webp;*.tiff")]
        file_paths = filedialog.askopenfilenames(filetypes=filetypes)
        if file_paths:
            self.selected_files = list(file_paths)
            self.file_list.delete("1.0", tk.END)
            for file_path in self.selected_files:
                self.file_list.insert(tk.END, os.path.basename(file_path) + "\n")
            self.status_label.configure(text=self.get_text("files_selected").format(len(self.selected_files)))
            logging.info(f"{len(self.selected_files)} files selected")

    def select_output_directory(self):
        """
        Open a directory dialog to select the output directory and update the corresponding variable.
        """
        directory = filedialog.askdirectory()
        if directory:
            self.output_directory.set(directory)
            logging.info(f"Output directory selected: {directory}")

    def start_conversion(self):
        """
        Start the file conversion process in a separate thread.
        """
        if not self.selected_files:
            messagebox.showerror(self.get_text("error"), self.get_text("select_files_error"))
            return
        threading.Thread(target=self.convert_files, daemon=True).start()

    def convert_files(self):
        """
        Perform the conversion of selected files using multiple threads.
        """
        total_files = len(self.selected_files)
        converted_files = 0
        self.progressbar.set(0)

        # Use ThreadPoolExecutor to manage concurrent conversions
        with ThreadPoolExecutor(max_workers=self.max_threads.get()) as executor:
            futures = [executor.submit(self.convert_file, file_path) for file_path in self.selected_files]

            for future in futures:
                try:
                    if future.result():
                        converted_files += 1
                        self.progressbar.set(converted_files / total_files)
                        self.status_label.configure(text=self.get_text("converting").format(converted_files, total_files))
                except Exception as e:
                    logging.error(f"Error during conversion: {str(e)}")

        self.status_label.configure(text=self.get_text("conversion_complete").format(converted_files, total_files))
        logging.info(f"Conversion completed. {converted_files}/{total_files} files converted.")

    def convert_file(self, file_path):
        """
        Convert a single file and save it to the output directory.

        Args:
            file_path (str): The path of the file to be converted.

        Returns:
            bool: True if the file was converted successfully, False otherwise.
        """
        try:
            with Image.open(file_path) as img:
                output_format = self.output_format.get()
                output_filename = f"{os.path.splitext(os.path.basename(file_path))[0]}.{output_format.lower()}"
                
                output_path = os.path.join(self.output_directory.get() or os.path.dirname(file_path), output_filename)

                if output_format == "JPEG":
                    img = img.convert("RGB")

                save_args = {"format": output_format, "quality": self.quality.get()}
                
                if self.preserve_metadata.get():
                    exif = img.info.get("exif")
                    if exif:
                        save_args["exif"] = exif

                img.save(output_path, **save_args)

            logging.info(f"File converted successfully: {file_path}")
            return True
        except Exception as e:
            logging.error(f"Error converting file {file_path}: {str(e)}")
            return False

    def update_quality_label(self, value):
        """
        Update the quality value label based on the slider value.

        Args:
            value (int): The current value of the quality slider.
        """
        self.quality_value_label.configure(text=f"{int(value)}")

    def update_thread_label(self, value):
        """
        Update the thread count label based on the slider value.

        Args:
            value (int): The current value of the thread slider.
        """
        self.thread_value_label.configure(text=f"{int(value)}")

    def change_appearance_mode(self, new_appearance_mode: str):
        """
        Change the appearance mode of the UI.

        Args:
            new_appearance_mode (str): The new appearance mode ('Light', 'Dark', 'System').
        """
        ctk.set_appearance_mode(new_appearance_mode)

    def change_language(self, new_language: str):
        """
        Change the language of the UI.

        Args:
            new_language (str): The new language ('English', 'Français').
        """
        self.current_language.set("en" if new_language == "English" else "fr")
        self.update_ui_text()

    def update_ui_text(self):
        """
        Update all UI text elements based on the current language.
        """
        self.select_button.configure(text=self.get_text("select_images"))
        self.convert_button.configure(text=self.get_text("convert"))
        self.format_label.configure(text=self.get_text("output_format"))
        self.quality_label.configure(text=self.get_text("quality"))
        self.thread_label.configure(text=self.get_text("threads"))
        self.preserve_metadata_checkbox.configure(text=self.get_text("preserve_metadata"))
        self.output_dir_button.configure(text=self.get_text("output_directory"))
        self.appearance_mode_label.configure(text=self.get_text("appearance"))
        self.language_label.configure(text=self.get_text("language"))
        self.status_label.configure(text=self.get_text("waiting_selection"))

if __name__ == "__main__":
    app = ImageConverterApp()
    app.mainloop()
