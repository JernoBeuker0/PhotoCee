import os
import rawpy
from PIL import Image
import sys

def single_cr2_to_jpg(input_path, output_path, quality=95):
    with rawpy.imread(input_path) as raw:
        rgb = raw.postprocess(
            use_camera_wb=True,
            output_bps=8,
        )

    img = Image.fromarray(rgb)
    img.save(
        output_path,
        "JPEG",
        quality=quality,
    )

def convert_all_folder(input_folder, output_folder):
    total = len(os.listdir(input_folder))
    count = 0

    for file in os.listdir(input_folder):
        if file.lower().endswith(".cr2"):
            input_path = os.path.join(input_folder, file)
            output_file = os.path.splitext(file)[0] + ".jpg"
            output_path = os.path.join(output_folder, output_file)
            
            
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{total}")

            single_cr2_to_jpg(input_path, output_path)

def main():
    event_name = sys.argv[1]
    input_folder = 'Input/' + event_name
    output_folder = 'Output/' + event_name
    
    os.makedirs(output_folder, exist_ok=True)
    
    convert_all_folder(input_folder, output_folder)
    print("Done!!!")


if __name__ == "__main__":
    main()