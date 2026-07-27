import os
import shutil
from PIL import Image

# Define relative paths based on running this from the project root
ASSETS_DIR = "assets"
BACKUP_DIR = "assets_backup"


def optimize_images():
    # 1. Create a backup of the original assets
    if not os.path.exists(BACKUP_DIR):
        print(f"Creating backup directory at '{BACKUP_DIR}'...")
        shutil.copytree(ASSETS_DIR, BACKUP_DIR)
        print("Backup successfully created.\n")
    else:
        print(
            f"Backup directory '{BACKUP_DIR}' already exists. Skipping backup to prevent overwriting.\n"
        )

    # 2. Process and optimize images
    print("Starting optimization...")
    for filename in os.listdir(ASSETS_DIR):
        if filename.lower().endswith(".png"):
            filepath = os.path.join(ASSETS_DIR, filename)

            try:
                with Image.open(filepath) as img:
                    # Define new WebP filename
                    new_filename = os.path.splitext(filename)[0] + ".webp"
                    new_filepath = os.path.join(ASSETS_DIR, new_filename)

                    # Save as WebP with 80% quality (excellent balance of size and visual fidelity)
                    img.save(new_filepath, "WEBP", quality=80)

                    # Get file sizes to show the improvement
                    old_size = os.path.getsize(filepath) / (1024 * 1024)
                    new_size = os.path.getsize(new_filepath) / (1024 * 1024)

                    print(f"Optimized: {filename} -> {new_filename}")
                    print(f"  Size reduced from {old_size:.2f} MB to {new_size:.2f} MB")

                    # Remove the original heavy PNG from the live assets folder
                    os.remove(filepath)

            except Exception as e:
                print(f"Failed to process {filename}: {e}")

    print(
        "\nOptimization complete! All originals are safely stored in 'assets_backup'."
    )


if __name__ == "__main__":
    optimize_images()
