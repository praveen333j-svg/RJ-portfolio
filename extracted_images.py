"""
Word Document Image Extractor
==============================
Reads all .docx files in a folder and its subfolders,
extracts embedded images, and saves them to an output folder.
"""

import zipfile
import shutil
from pathlib import Path

# Folder to scan. "." means the folder where this script is located.
SEARCH_FOLDER = "."

# Output folder. Relative paths are created beside this script.
OUTPUT_FOLDER = "extracted_images"

IMAGE_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".bmp", ".tiff", ".tif", ".emf", ".wmf"
}

SKIP_SMALL_IMAGES = True
MIN_SIZE_KB = 5


SCRIPT_DIR = Path(__file__).resolve().parent


def sanitise_filename(name):
    """Remove characters not allowed in Windows filenames."""
    for ch in r'\/:*?"<>|':
        name = name.replace(ch, "_")
    return name.strip()


def unique_path(path):
    """Return a non-existing path by adding _001, _002, etc. if needed."""
    if not path.exists():
        return path

    stem = path.stem
    suffix = path.suffix
    parent = path.parent

    i = 1
    while True:
        candidate = parent / f"{stem}_{i:03d}{suffix}"
        if not candidate.exists():
            return candidate
        i += 1


def extract_images_from_docx(docx_path, output_path, doc_label):
    count = 0

    try:
        with zipfile.ZipFile(docx_path, "r") as z:
            media_files = [
                f for f in z.namelist()
                if f.replace("\\", "/").startswith("word/media/")
            ]

            for media_file in sorted(media_files):
                suffix = Path(media_file).suffix.lower()

                if suffix not in IMAGE_EXTENSIONS:
                    continue

                info = z.getinfo(media_file)
                size_kb = info.file_size / 1024

                if SKIP_SMALL_IMAGES and size_kb < MIN_SIZE_KB:
                    continue

                count += 1
                img_name = f"{doc_label}__img_{count:03d}{suffix}"
                img_out = unique_path(output_path / img_name)

                with z.open(media_file) as src, open(img_out, "wb") as dst:
                    shutil.copyfileobj(src, dst)

    except zipfile.BadZipFile:
        print(f"  ! Skipping invalid docx/zip: {docx_path.name}")
    except Exception as e:
        print(f"  X Error reading {docx_path.name}: {e}")

    return count


def main():
    print("""
===================================
 Word Document Image Extractor
===================================
""")

    search_root = (SCRIPT_DIR / SEARCH_FOLDER).resolve()
    output_path = (SCRIPT_DIR / OUTPUT_FOLDER).resolve()
    output_path.mkdir(parents=True, exist_ok=True)

    print(f"Scanning:  {search_root}")
    print(f"Saving to: {output_path}")
    print()

    docx_files = sorted(search_root.rglob("*.docx"))

    if not docx_files:
        print("No .docx files found.")
        return

    print(f"Found {len(docx_files)} Word document(s). Extracting images...\n")

    total_images = 0
    docs_with_images = 0

    for docx_path in docx_files:
        if docx_path.name.startswith("~$"):
            continue

        # Skip files inside the output folder, if any happen to match later.
        if output_path in docx_path.resolve().parents:
            continue

        relative_label = docx_path.relative_to(search_root).with_suffix("")
        doc_label = sanitise_filename(str(relative_label).replace("\\", "__").replace("/", "__"))

        if len(doc_label) > 80:
            doc_label = doc_label[:80]

        count = extract_images_from_docx(docx_path, output_path, doc_label)

        if count > 0:
            docs_with_images += 1
            total_images += count
            print(f"  OK  {docx_path.name} -> {count} image(s) extracted")
        else:
            print(f"  --  {docx_path.name} (no images)")

    print(f"""
===================================
 DONE
===================================
Total images extracted : {total_images}
From {docs_with_images} document(s) out of {len(docx_files)} scanned
Saved to: {output_path}
""")


if __name__ == "__main__":
    main()