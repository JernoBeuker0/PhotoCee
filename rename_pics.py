import csv
import os
import json
from pathlib import Path
from collections import defaultdict
from natsort import natsorted

NAMES_CSV_FILE = "names.csv"  # Path to the CSV file containing names and groups
PHOTO_FOLDER = "photos"  # Path to the folder containing photos to be named
OUTPUT_FOLDER = "output"
ALLOWED_EXTENSIONS = [".jpg", ".jpeg", ".png", ".cr2"]  # Allowed photo file extensions

def load_grouped_names(filename: str) -> dict[str, list[str]]:
    """
    Reads a CSV where groups are indicated in column A, and the names in column B
    (Every person in column B should have their group in column A).
    
    returns a dictionary where the keys are the group names and the values are lists of names.
    """
    grouped_names = defaultdict(list)

    with open(filename, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        for line in reader:
            grouped_names[line[0]].append(line[1].replace(" ", "_"))

    return dict(grouped_names)

def save_dict(filename: str, data: dict):
    """
    Saves a dictionary as a JSON file.

    Args:
        filename (str): Path to the output JSON file.
        data (dict): Dictionary to be saved.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

def rename_photos_by_names(
    names: list[str], 
    photo_folder: str=PHOTO_FOLDER, 
    output_folder: str=OUTPUT_FOLDER, 
    allowed_extentions: list[str]=ALLOWED_EXTENSIONS,
    names_file: str=NAMES_CSV_FILE
    ) -> None:
    """
    Renames photos in a folder based on a list of names.
    Assumes filenames contain a number (e.g., '001.jpg'), and sorts based on that.
    """
    # Grab the photos from the folder and sort them based on a number in their name.
    folder = Path(photo_folder)
    photos = [f for f in folder.glob("*") if f.suffix.lower() in allowed_extentions]
    sorted_photos = natsorted(photos, key=lambda f: f.name)

    # Check if the lengths match, if they dont, then raise an error as there is a mistake somewhere.
    if len(names) > len(sorted_photos):
        raise ValueError(f"More names than photos. Please check the {names_file} file and the fotos in the {folder} directory.")
    elif len(names) < len(sorted_photos):
        raise ValueError(f"More names than photos. Please check the {names_file} file and the fotos in the {folder} directory.")

    # If there is not such directory already, make one, and saturate it with the photos with the new names.
    os.makedirs(output_folder, exist_ok=True)
    for photo, name in zip(sorted_photos, names):
        new_filename = name + photo.suffix.lower()
        new_path = output_folder + '/' + new_filename

        photo.rename(new_path)

if __name__ == "__main__":
    # Load the names corresponding with the group in a dictionary and saving it.
    names = load_grouped_names(NAMES_CSV_FILE)
    save_dict(names)
    
    # Flatten the dictionary to get a list of names and rename the photos based on that list.
    flattened_names = [name for group in names.values() for name in group]
    rename_photos_by_names(flattened_names)
    
    print('Task succesful, jeejj:)')