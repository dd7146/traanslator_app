import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

# Create an instance of Translator
translator = Translator()

# Function to translate the text
def translate_text():
    # Get the original text and the selected languages
    source_text = input_text_box.get("1.0", tk.END)
    src_lang = src_lang_combo.get()
    dest_lang = dest_lang_combo.get()

    # Perform the translation
    translated = translator.translate(source_text, src=src_lang, dest=dest_lang)
    
    # Insert the translated text in the output box
    output_text_box.delete("1.0", tk.END)
    output_text_box.insert(tk.END, translated.text)

# Create the main application window
root = tk.Tk()
root.title("Advanced Translator")
root.geometry("800x500")  # Increased size for a more web-like feel

# Set up a vibrant background color scheme
root.config(bg="#e0f7fa")  # Light teal background color

# Styling
HEADER_FONT = ("Arial", 18, "bold")
LABEL_FONT = ("Arial", 12)
TEXTBOX_FONT = ("Arial", 14)
BUTTON_FONT = ("Arial", 12, "bold")

# Header Frame with a colorful gradient-like background
header_frame = tk.Frame(root, bg="#00796b", height=60)
header_frame.pack(fill="x")

header_label = tk.Label(
    header_frame, text="Translate", font=HEADER_FONT, fg="white", bg="#00796b"
)
header_label.pack(pady=10)

# Main Content Frame
content_frame = tk.Frame(root, bg="#e0f7fa")
content_frame.pack(pady=20)

# Source Text Area
input_label = tk.Label(content_frame, text="Enter Text:", font=LABEL_FONT, bg="#e0f7fa")
input_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

input_text_box = tk.Text(content_frame, height=10, width=40, font=TEXTBOX_FONT)
input_text_box.grid(row=1, column=0, padx=10)

# Destination Text Area
output_label = tk.Label(content_frame, text="Translated Text:", font=LABEL_FONT, bg="#e0f7fa")
output_label.grid(row=0, column=2, padx=10, pady=10, sticky="w")

output_text_box = tk.Text(content_frame, height=10, width=40, font=TEXTBOX_FONT)
output_text_box.grid(row=1, column=2, padx=10)

# Language Selection Frame
lang_frame = tk.Frame(content_frame, bg="#e0f7fa")
lang_frame.grid(row=2, column=0, columnspan=3, pady=20)

# Source Language Selection
src_lang_label = tk.Label(lang_frame, text="Source Language:", font=LABEL_FONT, bg="#e0f7fa")
src_lang_label.grid(row=0, column=0, padx=10)

src_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), font=LABEL_FONT, width=20)
src_lang_combo.grid(row=0, column=1, padx=10)
src_lang_combo.set('english')  # Default language is English

# Destination Language Selection
dest_lang_label = tk.Label(lang_frame, text="Target Language:", font=LABEL_FONT, bg="#e0f7fa")
dest_lang_label.grid(row=0, column=2, padx=10)

dest_lang_combo = ttk.Combobox(lang_frame, values=list(LANGUAGES.values()), font=LABEL_FONT, width=20)
dest_lang_combo.grid(row=0, column=3, padx=10)
dest_lang_combo.set('spanish')  # Default language is Spanish

# Translate Button with more vibrant colors
translate_button = tk.Button(root, text="Translate", font=BUTTON_FONT, bg="#ff5722", fg="white", command=translate_text)
translate_button.pack(pady=10)

# Footer Frame
footer_frame = tk.Frame(root, bg="#e0f7fa", height=50)
footer_frame.pack(fill="x", side="bottom")

footer_label = tk.Label(footer_frame, text="Powered by Google Translate", font=("Arial", 10), bg="#e0f7fa")
footer_label.pack(side="bottom", pady=10)

# Start the application
root.mainloop()
