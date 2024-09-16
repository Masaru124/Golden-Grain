import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import webbrowser
import os
import sys

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS 
    except Exception:
        base_path = os.path.abspath(".") 
    return os.path.join(base_path, relative_path)

image_paths = {
    'Corn': resource_path('images/Corn.png'),
    'Carrot': resource_path('images/Carrot.png'),
    'LOGO': resource_path('images/LOGO.png')
}

def load_image(filename, size=(200, 200)):
    try:
        image_path = image_paths.get(filename, '')
        if not os.path.isfile(image_path):
            raise FileNotFoundError(f"Image file not found: {image_path}")
        image = Image.open(image_path)
        image.thumbnail(size)
        return ImageTk.PhotoImage(image)
    except Exception as e:
        print(f"Error loading image from file: {e}")
        return None

# Create main window
root = tk.Tk()
root.title("Golden Grain")
root.geometry("1200x900")  
root.configure(bg='#002F4C')  

# Load logo image
logo_image = load_image('LOGO', size=(150, 150))  
if logo_image is None:
    print("Failed to load logo image.")
else:
    logo_label = tk.Label(root, image=logo_image, bg='#002F4C')
    logo_label.grid(row=0, column=0, padx=20, pady=20, sticky='nw')

# Define custom styles
style = ttk.Style()
style.configure('TCombobox',
                font=('Arial', 14),
                background='#003366',
                foreground='black',
                fieldbackground='#003366',
                )
style.map('TCombobox',
          foreground=[('readonly', 'black')],
          background=[('readonly', '#003366')]
          )
style.configure('TLabel', font=('Tenez Test Black', 12), background='#002F4C', foreground='gold')
style.configure('TButton', font=('Tenez Test Black', 12, 'bold'), padding=10, background='#004080', foreground='gold')
style.map('TButton', background=[('active', '#003366')])

# Amazon product URLs for seeds and cures
amazon_seed_links = {
    'Corn': 'https://www.amazon.com/dp/B09CornSeeds123',
    'Carrot': 'https://www.amazon.com/dp/B08CarrotSeeds456'
}

amazon_cure_links = {
    'Corn': 'https://www.amazon.com/dp/B09CornCure123',
    'Carrot': 'https://www.amazon.com/dp/B08CarrotCure456'
}

# Crop data with image file paths and links for seeds and disease cures
crops_info = {
    'Corn': {
        'English': {
            'Growth Conditions': 'Corn requires full sun and fertile soil with good drainage.',
            'Diseases': 'Common diseases include corn smut and rust.',
            'Prevention': 'Plant resistant varieties and rotate crops annually.',
            'Harvesting': 'Harvest when ears are full and kernels are plump and milky.',
            'Image Filename': 'Corn',
            'Seed Link': amazon_seed_links['Corn'],
            'Amazon Link': amazon_cure_links['Corn']
        },
        'Kannada': {
            'Growth Conditions': 'ಮಕ್ಕಳಿಗೆ ಸಂಪೂರ್ಣ ಸೂರ್ಯ ಮತ್ತು ಉತ್ತಮ ನಿಕಾಶ ಹೊಂದಿರುವ ಮಾಟು ಹೊರುವ ಸಮೃದ್ಧ ಮಣ್ಣು ಬೇಕು.',
            'Diseases': 'ಸಾಮಾನ್ಯ ರೋಗಗಳು ಕಾರ್ನ್ ಸ್ಮಟ್ ಮತ್ತು ರಸ್ಟ್.',
            'Prevention': 'ಹಣದರ ವೈಶಿಷ್ಟ್ಯಗಳು ಮತ್ತು ವರುಷಕ್ಕೆ ಬೆಳೆಗಳನ್ನು ಮಾರ್ಚು ಮಾಡುವುದು.',
            'Harvesting': 'ಮೂಗಿಯಷ್ಟು ಶೀಘ್ರದಲ್ಲೆ ಆಯಿತು ಮತ್ತು ಕರ್ಣೆ ಮುಪ್ಪು ತಿನ್ನುವಾಗ.',
            'Image Filename': 'Corn',
            'Seed Link': amazon_seed_links['Corn'],
            'Amazon Link': amazon_cure_links['Corn']
        }
    },
    'Carrot': {
        'English': {
            'Growth Conditions': 'Carrots need full sun and loose, well-drained soil.',
            'Diseases': 'Common diseases include carrot rust fly and powdery mildew.',
            'Prevention': 'Use insect nets and practice good garden hygiene.',
            'Harvesting': 'Harvest carrots when they reach the desired size and are tender.',
            'Image Filename': 'Carrot',
            'Seed Link': amazon_seed_links['Carrot'],
            'Amazon Link': amazon_cure_links['Carrot']
        },
        'Kannada': {
            'Growth Conditions': 'ಮುರಿದಿಲ್ಲದ ಹುಣಸೆ ಹಣ್ಣು ಸಂಪೂರ್ಣ ಸೂರ್ಯ ಮತ್ತು ಸುಮ್ಮನಾದ ಮಣ್ಣು ಬೇಕು.',
            'Diseases': 'ಸಾಮಾನ್ಯ ರೋಗಗಳು ಕ್ಯಾರೆಟ್ ರಸ್ಟ್ ಫ್ಲೈ ಮತ್ತು ಪೌಡರಿ ಮಿಲ್ಡ್ಯೂ.',
            'Prevention': 'ಹಣ್ಣು ನೆಟ್‌ಗಳನ್ನು ಬಳಸುವುದು ಮತ್ತು ಉತ್ತಮ ಉದ್ಯಾನಗಾರಿಕೆ ಸ್ವಚ್ಛತೆ.',
            'Harvesting': 'ಹಣ್ಣನ್ನು ತಲುಪಿದಾಗ ಅಥವಾ ಹೆಚ್ಚು ತಂಪಾಗಿಯು ಕಾರ್ಟ್ ಮಾಡಿದಾಗ.',
            'Image Filename': 'Carrot',
            'Seed Link': amazon_seed_links['Carrot'],
            'Amazon Link': amazon_cure_links['Carrot']
        }
    }
}

# File to store comments
comments_file = "comments.txt"

# Function to update information based on selected crop and language
def update_info(event=None):
    crop = crop_var.get()
    lang = lang_var.get()
    
    if crop == 'Select a crop':
        # Show introductory text
        intro_label.grid(row=1, column=1, columnspan=4, padx=20, pady=20)
        
        # Hide crop-specific information
        image_label.configure(image='')
        image_label.image = None
        
        # Clear crop-specific text
        growth_conditions_var.set('')
        diseases_var.set('')
        prevention_var.set('')
        harvesting_var.set('')
        
        # Remove links and reset labels
        cure_label.config(text='', fg="gold", cursor="")
        seed_label.config(text='', fg="gold", cursor="")
        
        # Reset labels to initial state
        growth_conditions_label.config(text="Growth Conditions:")
        diseases_label.config(text="Diseases:")
        prevention_label.config(text="Prevention:")
        harvesting_label.config(text="Harvesting:")
        
    else:
        # Hide introductory text
        intro_label.grid_forget()
        
        # Retrieve and display crop-specific information
        info = crops_info.get(crop, {}).get(lang, {})
        
        growth_conditions_var.set(info.get('Growth Conditions', 'N/A'))
        diseases_var.set(info.get('Diseases', 'N/A'))
        prevention_var.set(info.get('Prevention', 'N/A'))
        harvesting_var.set(info.get('Harvesting', 'N/A'))
        
        # Load and update image
        image_filename = info.get('Image Filename', '')
        image = load_image(image_filename)
        if image:
            image_label.configure(image=image)
            image_label.image = image  # Keep a reference to avoid garbage collection
        else:
            image_label.configure(image='')
            image_label.image = None
        
        # Update Amazon link for disease cure
        amazon_cure_link = info.get('Amazon Link', '')
        if amazon_cure_link:
            cure_label.config(text=f"Buy Cure for {crop} Diseases", fg="lightcoral", cursor="hand2")
            cure_label.bind("<Button-1>", lambda e: webbrowser.open(amazon_cure_link))
        else:
            cure_label.config(text='', fg="gold", cursor="")
        
        # Update Amazon link for seeds
        amazon_seed_link = info.get('Seed Link', '')
        if amazon_seed_link:
            seed_label.config(text=f"Buy {crop} Seeds", fg="lightcoral", cursor="hand2")
            seed_label.bind("<Button-1>", lambda e: webbrowser.open(amazon_seed_link))
        else:
            seed_label.config(text='', fg="gold", cursor="")
        
        # Update label texts based on selected language
        if lang == 'English':
            growth_conditions_label.config(text="Growth Conditions:")
            diseases_label.config(text="Diseases:")
            prevention_label.config(text="Prevention:")
            harvesting_label.config(text="Harvesting:")
        elif lang == 'Kannada':
            growth_conditions_label.config(text="ಬೆಳೆ ಸಂಬಂಧಿ ಶರತ್ತುಗಳು:")
            diseases_label.config(text="ಅರೋಗ್ಯಗಳು:")
            prevention_label.config(text="ಪೂರ್ವಾಗ್ರಹ:")
            harvesting_label.config(text="ಕಟುವು:")

def submit_comment():
    comment = comment_entry.get("1.0", tk.END).strip()
    if comment:
        with open(comments_file, "a") as file:
            file.write(comment + "\n")
        comment_entry.delete("1.0", tk.END)
        load_comments()
    else:
        messagebox.showwarning("Warning", "Comment cannot be empty.")

def load_comments():
    try:
        with open(comments_file, "r") as file:
            comments = file.readlines()
            comments_text = ''.join(comments)
            comments_display.config(state=tk.NORMAL)
            comments_display.delete("1.0", tk.END)
            comments_display.insert(tk.END, comments_text)
            comments_display.config(state=tk.DISABLED)
    except FileNotFoundError:
        comments_display.config(state=tk.NORMAL)
        comments_display.delete("1.0", tk.END)
        comments_display.insert(tk.END, "No comments yet.")
        comments_display.config(state=tk.DISABLED)

# Initialize intro label
intro_label = tk.Label(root, text="WELCOME TO THE GOLDEN GRAIN\n\nPlease select a crop from the dropdown menu to see detailed information",
                       font=('Tenez Test Black', 16), bg='#002F4C', fg='gold', justify=tk.CENTER)
intro_label.grid(row=1, column=1, columnspan=4, padx=20, pady=20)

# Dropdown menu for crop selection
crop_var = tk.StringVar()
crop_var.set('Select a crop')

crop_menu = ttk.Combobox(root, textvariable=crop_var)
crop_menu['values'] = ['Select a crop'] + list(crops_info.keys())
crop_menu.bind('<<ComboboxSelected>>', update_info)
crop_menu.grid(row=0, column=1, padx=20, pady=20, columnspan=3, sticky='ew')

# Dropdown menu for language selection
lang_var = tk.StringVar()
lang_var.set('English')

lang_menu = ttk.Combobox(root, textvariable=lang_var)
lang_menu['values'] = ['English', 'Kannada']
lang_menu.bind('<<ComboboxSelected>>', update_info)
lang_menu.grid(row=0, column=4, padx=20, pady=20, sticky='ne')

# Labels for crop information
growth_conditions_label = tk.Label(root, text="Growth Conditions:", font=('Tenez Test Black', 14), bg='#002F4C', fg='gold')
growth_conditions_label.grid(row=2, column=0, sticky='w', padx=20)
growth_conditions_var = tk.StringVar()
tk.Label(root, textvariable=growth_conditions_var, wraplength=600, anchor='w', bg='#002F4C', fg='gold').grid(row=2, column=1, padx=20, columnspan=4, sticky='w')

diseases_label = tk.Label(root, text="Diseases:", font=('Tenez Test Black', 14), bg='#002F4C', fg='gold')
diseases_label.grid(row=3, column=0, sticky='w', padx=20)
diseases_var = tk.StringVar()
tk.Label(root, textvariable=diseases_var, wraplength=600, anchor='w', bg='#002F4C', fg='gold').grid(row=3, column=1, padx=20, columnspan=4, sticky='w')

prevention_label = tk.Label(root, text="Prevention:", font=('Tenez Test Black', 14), bg='#002F4C', fg='gold')
prevention_label.grid(row=4, column=0, sticky='w', padx=20)
prevention_var = tk.StringVar()
tk.Label(root, textvariable=prevention_var, wraplength=600, anchor='w', bg='#002F4C', fg='gold').grid(row=4, column=1, padx=20, columnspan=4, sticky='w')

harvesting_label = tk.Label(root, text="Harvesting:", font=('Tenez Test Black', 14), bg='#002F4C', fg='gold')
harvesting_label.grid(row=5, column=0, sticky='w', padx=20)
harvesting_var = tk.StringVar()
tk.Label(root, textvariable=harvesting_var, wraplength=600, anchor='w', bg='#002F4C', fg='gold').grid(row=5, column=1, padx=20, columnspan=4, sticky='w')

# Labels for Amazon links
cure_label = tk.Label(root, text="", fg="gold", cursor="hand2", bg='#002F4C', font=('Arial', 12, 'italic'))
cure_label.grid(row=6, column=1, padx=20, pady=10, columnspan=4, sticky='w')

seed_label = tk.Label(root, text="", fg="gold", cursor="hand2", bg='#002F4C', font=('Arial', 12, 'italic'))
seed_label.grid(row=7, column=1, padx=20, pady=10, columnspan=4, sticky='w')

# Label for displaying crop image
image_label = tk.Label(root, bg='#002F4C', borderwidth=2, relief="solid")
image_label.grid(row=0, column=5, rowspan=8, padx=20, pady=20)

# Discussion frame
discussion_frame = tk.Frame(root, bg='#002F4C')
discussion_frame.grid(row=8, column=0, columnspan=6, padx=20, pady=20, sticky='nsew')

tk.Label(discussion_frame, text="Discussion about Crops", font=('Arial', 14, 'bold'), bg='#002F4C', fg='gold').grid(row=0, column=0, padx=10, pady=10)

comment_entry = tk.Text(discussion_frame, height=4, width=80, wrap=tk.WORD)
comment_entry.grid(row=1, column=0, padx=10, pady=10)

# Create the submit button with the custom style
submit_button = tk.Button(discussion_frame, text="Submit", font=('Tenez Test Black', 12, 'bold'), bg='#FFD700', fg='blue', command=submit_comment)
submit_button.grid(row=2, column=0, padx=10, pady=10, sticky='e')

comments_display = tk.Text(discussion_frame, height=10, width=80, wrap=tk.WORD, state=tk.DISABLED)
comments_display.grid(row=3, column=0, padx=10, pady=10)
load_comments()

# Run the application
root.mainloop()
