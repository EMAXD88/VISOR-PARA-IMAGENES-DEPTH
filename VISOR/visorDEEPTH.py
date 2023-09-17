import numpy as np
import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

def adjust_brightness(image, factor):
    adjusted_image = np.clip(image * factor, 0, 255).astype(np.uint8)
    return adjusted_image

def main():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Seleccione una imagen de profundidad",
        filetypes=[
            ("Archivos NPY", "*.npy"),
            ("Archivos PNG", "*.png"),
            ("Archivos JPG", "*.jpg *.jpeg"),
            ("Todos los archivos", "*.*")
        ]
    )

    if not file_path:
        print("No se seleccionó ninguna imagen.")
        return

    image = None

    if file_path.endswith('.npy'):
        image = np.load(file_path)
    elif file_path.endswith('.png') or file_path.endswith('.jpg') or file_path.endswith('.jpeg'):
        image = cv2.imread(file_path, cv2.IMREAD_UNCHANGED)
    else:
        print("Formato de archivo no compatible.")
        return

    if image is not None:
        brightness_factor = 2.0  # Puedes ajustar este valor para cambiar el brillo
        adjusted_image = adjust_brightness(image, brightness_factor)

        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        plt.title("Imagen original")
        plt.imshow(image, cmap="gray")

        plt.subplot(1, 2, 2)
        plt.title("Imagen ajustada de brillo")
        plt.imshow(adjusted_image, cmap="gray")

        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    main()
