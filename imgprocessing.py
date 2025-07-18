import os
from PIL import Image, ImageEnhance, ImageFilter

def process_single_image(image_path, dest_folder, suffix="_processed"):
    if not os.path.isfile(image_path):
        print("File does not exist.")
        return

    try:
        with Image.open(image_path) as img:
            print(f"\nLoaded image: {os.path.basename(image_path)} | Size: {img.size}, Mode: {img.mode}\n")
            original_mode = img.mode

            while True:
                print("\nChoose an operation to perform:")
                print("1. Resize the image")
                print("2. Rotate the image")
                print("3. Flip the image")
                print("4. Convert color mode")
                print("5. Adjust brightness/contrast/color/sharpness")
                print("6. Apply filter (blur, sharpen, emboss, etc.)")
                print("7. Save and exit")

                choice = input("Enter your choice (1-7): ").strip()

                if choice == "1":
                    w = int(input("Enter new width: "))
                    h = int(input("Enter new height: "))
                    img = img.resize((w, h))
                    print(f"Image resized to {w}x{h}")

                elif choice == "2":
                    angle = float(input("Enter rotation angle in degrees: "))
                    img = img.rotate(angle, expand=True)
                    print(f"Image rotated by {angle}°")

                elif choice == "3":
                    flip_type = input("Flip Horizontally (h) or Vertically (v): ").lower()
                    if flip_type == "h":
                        img = img.transpose(Image.FLIP_LEFT_RIGHT)
                        print("Image flipped horizontally")
                    elif flip_type == "v":
                        img = img.transpose(Image.FLIP_TOP_BOTTOM)
                        print("Image flipped vertically")
                    else:
                        print("Invalid flip type")

                elif choice == "4":
                    print("Available color modes:")
                    print("  L     → Grayscale")
                    print("  RGB   → Standard color")
                    print("  RGBA  → Color + Transparency")
                    print("  CMYK  → For print")
                    print("  1     → Black & White (1-bit)")
                    target_mode = input("Enter target mode from the list above: ").strip().upper()

                    valid_modes = {"L", "RGB", "RGBA", "CMYK", "1"}
                    if target_mode in valid_modes:
                        img = img.convert(target_mode)
                        print(f"Image converted to {target_mode}")
                    else:
                        print("Invalid color mode. Please choose from the listed options.")

                elif choice == "5":
                    print("Adjustments:")
                    print(" a. Brightness")
                    print(" b. Contrast")
                    print(" c. Color")
                    print(" d. Sharpness")
                    adj = input("Choose adjustment type: ").strip().lower()

                    factor = float(input("Enter enhancement factor (e.g., 1.2 for slight increase): "))
                    if adj == 'a':
                        enhancer = ImageEnhance.Brightness(img)
                    elif adj == 'b':
                        enhancer = ImageEnhance.Contrast(img)
                    elif adj == 'c':
                        enhancer = ImageEnhance.Color(img)
                    elif adj == 'd':
                        enhancer = ImageEnhance.Sharpness(img)
                    else:
                        print("Invalid choice.")
                        continue
                    img = enhancer.enhance(factor)
                    print(f"Adjustment applied with factor {factor}")

                elif choice == "6":
                    print("Available filters: BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EMBOSS, SHARPEN")
                    ftype = input("Enter filter type: ").strip().upper()
                    filter_map = {
                        "BLUR": ImageFilter.BLUR,
                        "CONTOUR": ImageFilter.CONTOUR,
                        "DETAIL": ImageFilter.DETAIL,
                        "EDGE_ENHANCE": ImageFilter.EDGE_ENHANCE,
                        "EMBOSS": ImageFilter.EMBOSS,
                        "SHARPEN": ImageFilter.SHARPEN
                    }
                    if ftype in filter_map:
                        img = img.filter(filter_map[ftype])
                        print(f"Applied filter: {ftype}")
                    else:
                        print("Unknown filter type")

                elif choice == "7":
                    ext = os.path.splitext(image_path)[1].lower()
                    format_folder = os.path.join(dest_folder, ext.lstrip('.'))
                    os.makedirs(format_folder, exist_ok=True)

                    base_name = os.path.splitext(os.path.basename(image_path))[0]
                    new_name = f"{base_name}{suffix}{ext}"
                    save_path = os.path.join(format_folder, new_name)

                    img.save(save_path)
                    print(f"\nImage saved to: {save_path}")
                    break
                else:
                    print("Invalid choice. Try again.")

    except Exception as e:
        print(f"Error processing image: {e}")


if __name__ == "__main__":
    print("\nInteractive Image Processor Tool: \n")

    image_path = input("Enter full path to an image file: ").strip()
    dest_folder = input("Enter destination folder to save processed image: ").strip()
    process_single_image(image_path, dest_folder)
