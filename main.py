import customtkinter as ctk
from tkinter import filedialog, messagebox
from pdf_operations import *
from logger import log_action

# Set application theme
ctk.set_appearance_mode('dark')

# Create main application window
app = ctk.CTk()
app.title('PDF Merger & Splitter Pro')
app.geometry('900x600')

# Store selected PDF files
files = []

# Text area to display selected file paths
box = ctk.CTkTextbox(app)
box.pack(fill='both', expand=True, padx=10, pady=10)

# Function to select PDF files
def add_files():
    global files

# Open file picker and select PDF files
    files = list(filedialog.askopenfilenames(
        filetypes=[('PDF', '*.pdf')]
    ))

# Clear previous file list
    box.delete('1.0', 'end')

# Display selected files
    for f in files:
        box.insert('end', f + '\n')

# Function to merge selected PDFs
def merge():
# Check whether files are selected
    if not files:
        return

# Ask user where to save merged PDF
    out = filedialog.asksaveasfilename(
        defaultextension='.pdf'
    )

    if out:
        merge_pdfs(files, out)

# Save action in log file
        log_action('Merged PDFs')

# Show success message
        messagebox.showinfo(
            'Success',
            'Merged successfully'
        )

# Function to split a PDF into pages
def split():
    # Select PDF file
    pdf = filedialog.askopenfilename(
        filetypes=[('PDF', '*.pdf')]
    )

    # Select output folder
    folder = filedialog.askdirectory()

    if pdf and folder:
        split_pdf(pdf, folder)

        # Save action in log file
        log_action('Split PDF')

        # Show success message
        messagebox.showinfo(
            'Success',
            'Split complete'
        )

# Frame to hold buttons
frame = ctk.CTkFrame(app)
frame.pack(fill='x')

# Button to add PDF files
ctk.CTkButton(
    frame,
    text='Add PDFs',
    command=add_files
).pack(side='left', padx=5, pady=5)

# Button to merge PDFs
ctk.CTkButton(
    frame,
    text='Merge',
    command=merge
).pack(side='left', padx=5)

# Button to split PDF
ctk.CTkButton(
    frame,
    text='Split',
    command=split
).pack(side='left', padx=5)

# Start the application
app.mainloop()