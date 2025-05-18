# Bulk File Renamer - Python Project

A simple Python script to rename multiple files in a folder with a chosen prefix and numbering sequence. Files are renamed based on their last modified time (oldest first). Perfect for organizing photo collections, scanned documents, or any file batch.

![Python](https://img.shields.io/badge/python-3.x-blue)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)

---

## Features
- Rename files in bulk using a custom prefix and number sequence
- Sorts files by last modified time (oldest → newest)
- Optionally filter by file extension (e.g. only `.jpg`)
- Cross-platform (works on Windows, macOS, and Linux)
- Easy to use – just run the script and follow the prompts

---

## Requirements
- Python 3.x
- No external libraries required — only Python's built-in modules (os, os.path).  

---

## How to Use
1. Make sure you have Python installed (Python 3 recommended).
2. Clone this repository
```bash
git clone https://github.com/SltnBM/bulk-file-renamer.git
```
3. Navigate to the project directory
```bash
cd bulk-file-renamer
```
4. Run the script using terminal or command prompt
```bash
python renamer.py
```

🖥️ Example Prompt
```bash
> python renamer.py
Enter the folder path: C:\Users\YourName\Pictures
Enter the new filename prefix: holiday_
Enter the starting number: 1
Only rename files with this extension (e.g. .jpg), or leave blank:
```

---

## Example Output
Before:
```bash
Photos/
├── IMG_1825.jpg
├── DSC_0012.jpg
├── IMG_2025.jpg
```

After:
```bash
Photos/
├── holiday_1.jpg
├── holiday_2.jpg
├── holiday_3.jpg
```

---

## License
This project is open-source and free to use.