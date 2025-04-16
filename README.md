# Introweek Photobooth

To run the script, it is important to change the global variables in the rename_pics.py. (I wanted to do arguments, but was too lazy)
The variables to change are listed below:
- NAMES_CSV_FILE = "names.csv"  # Path to the CSV file containing names and groups
- PHOTO_FOLDER = "photos"  # Path to the folder containing photos to be named
- OUTPUT_FOLDER = "output" # Path to the output folder of the renamed photos.

After this is filled in properly, run:
- python rename_pics.py

When running, the dictionary of people will be saved (with the group as key and the value a list of people) will be saved so one can see what happened. Also, errors will be put if something is wrong in the initial data. (All files that aren't renamed should still be in the original folder)