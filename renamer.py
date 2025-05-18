import os

def bulk_rename(folder_path, prefix, start_number, extension_filter=None):
    # Get all files (skip directories) and store full paths
    files = [
        f for f in os.listdir(folder_path)
        if os.path.isfile(os.path.join(folder_path, f)) and
        (extension_filter is None or f.lower().endswith(extension_filter.lower()))
    ]

    # Sort files by modification time (oldest first)
    files.sort(key=lambda f: os.path.getmtime(os.path.join(folder_path, f)))

    # Rename each file
    count = start_number
    for filename in files:
        old_path = os.path.join(folder_path, filename)
        _, ext = os.path.splitext(filename)
        new_filename = f"{prefix}{count}{ext}"
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_filename}")
        count += 1

if __name__ == "__main__":
    folder = input("Enter the folder path: ").strip()
    prefix = input("Enter the new filename prefix: ").strip()
    start = int(input("Enter the starting number: ").strip())
    ext_filter = input("Only rename files with this extension (e.g. .jpg), or leave blank: ").strip()
    ext_filter = ext_filter if ext_filter else None

    bulk_rename(folder, prefix, start, ext_filter)
