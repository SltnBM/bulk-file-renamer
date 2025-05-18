import os
import sys

def bulk_rename(folder_path, prefix, start_number, extension_filter=None):
    if not os.path.isdir(folder_path):
        print(f"❌ Error: The folder '{folder_path}' does not exist.")
        return
    
    # Get all files (skip directories) and store full paths
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and
        (extension_filter is None or f.lower().endswith(extension_filter.lower()))
    ]

    if not files:
        print("⚠️ No files found to rename with given criteria.")
        return

    # Sort files by modification time (oldest first)
    files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

    # Rename each file
    count = start_number
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        _, ext = os.path.splitext(filename)
        new_filename = f"{prefix}{count}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        
        if os.path.exists(new_path):
            print(f"⚠️ Skipping rename because '{new_filename}' already exists.")
            count += 1
            continue
        
        try:
            os.rename(old_path, new_path)
            print(f"✅ Renamed: {filename} → {new_filename}")
        except Exception as e:
            print(f"❌ Failed to rename {filename}: {e}")
        count += 1

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    prefix = input("Enter the new filename prefix: ").strip()
    
    try:
        start = int(input("Enter the starting number: ").strip())
    except ValueError:
        print("❌ Invalid input! Starting number must be an integer.")
        sys.exit(1)
            
    ext_filter = input("Only rename files with this extension (e.g. .jpg), or leave blank: ").strip()
    ext_filter = ext_filter if ext_filter else None

    bulk_rename(folder, prefix, start, ext_filter)
