import os
import rawpy
from PIL import Image

INPUT_FOLDER = "Input/Chess Tournament"
OUTPUT_FOLDER = "Output/Chess"


def single_cr2_to_jpg(input_path, output_path, quality=95):
    with rawpy.imread(input_path) as raw:
        rgb = raw.postprocess(
            use_camera_wb=True,
            no_auto_bright=True,
            output_bps=8,
        )

    img = Image.fromarray(rgb)
    img.save(
        output_path,
        "JPEG",
        quality=quality,
    )


def main():
    os.makedirs(OUTPUT_FOLDER, exist_ok=True)

    total = len(os.listdir(INPUT_FOLDER))
    count = 0

    for file in os.listdir(INPUT_FOLDER):
        if file.lower().endswith(".cr2"):
            input_path = os.path.join(INPUT_FOLDER, file)
            output_file = os.path.splitext(file)[0] + ".jpg"
            output_path = os.path.join(OUTPUT_FOLDER, output_file)
            
            
            count += 1
            if count % 10 == 0:
                print(f"Processed {count}/{total}")

            single_cr2_to_jpg(input_path, output_path)

    print("Done!!!")


if __name__ == "__main__":
    main()