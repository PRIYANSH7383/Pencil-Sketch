import cv2
import numpy as np
from PIL import Image
import os

# ==========================================
# 1. LOAD IMAGE
# ==========================================

image_path = os.path.join(
    os.path.dirname(__file__),
    "krishna_r.jpg"
)

try:
    pil_image = Image.open(image_path).convert("RGB")

    image = np.array(pil_image)
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    print("Image loaded successfully!")

except Exception as e:
    print("Error loading image:", e)
    exit()


# ==========================================
# 2. RESIZE
# ==========================================

image = cv2.resize(image, (600, 600))


# ==========================================
# 3. CREATE REALISTIC PENCIL SKETCH
# ==========================================

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert image
inverted = 255 - gray

# Blur
blur = cv2.GaussianBlur(
    inverted,
    (21, 21),
    0
)

# Invert blur
inverted_blur = 255 - blur

# Pencil effect
sketch = cv2.divide(
    gray,
    inverted_blur,
    scale=256
)


# ==========================================
# 4. IMPROVE CONTRAST
# ==========================================

sketch = cv2.normalize(
    sketch,
    None,
    0,
    255,
    cv2.NORM_MINMAX
)


# ==========================================
# 5. SAVE FINAL SKETCH
# ==========================================

cv2.imwrite(
    "krishna_pencil_sketch.jpg",
    sketch
)

print("Pencil sketch created!")


# ==========================================
# 6. CREATE DRAWING EFFECT
# ==========================================

# Start with completely white paper
canvas = np.ones_like(sketch) * 255


# ==========================================
# 7. CREATE WINDOW
# ==========================================

cv2.namedWindow(
    "Krishna Pencil Drawing",
    cv2.WINDOW_NORMAL
)

cv2.resizeWindow(
    "Krishna Pencil Drawing",
    600,
    600
)


# ==========================================
# 8. PROGRESSIVE DRAWING
# ==========================================

print("Drawing started...")
print("Press Q to stop.")


height, width = sketch.shape

# Draw from top to bottom
for y in range(height):

    # Copy one horizontal line
    canvas[y:y+1, :] = sketch[y:y+1, :]

    # Show drawing
    cv2.imshow(
        "Krishna Pencil Drawing",
        canvas
    )

    # Drawing speed
    key = cv2.waitKey(5)

    if key == ord("q"):
        break


# ==========================================
# 9. SHOW FINAL IMAGE
# ==========================================

while True:

    cv2.imshow(
        "Krishna Pencil Drawing",
        canvas
    )

    key = cv2.waitKey(1)

    if key == ord("q") or key == 27:
        break


# ==========================================
# 10. SAVE DRAWING
# ==========================================

cv2.imwrite(
    "krishna_final_drawing.jpg",
    canvas
)

print("Drawing completed!")
print("Saved as krishna_final_drawing.jpg")

cv2.destroyAllWindows()