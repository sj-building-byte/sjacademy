import fitz
import os

pdf_path = "SJ_Academy_Pitch_Deck.pdf"
output_dir = "Slides_PNG"

os.makedirs(output_dir, exist_ok=True)

# Open the PDF
doc = fitz.open(pdf_path)

for i in range(len(doc)):
    page = doc.load_page(i)
    # Increase resolution by 2x for high quality
    pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
    # Save as PNG
    output_path = os.path.join(output_dir, f"Slide_{i+1:02d}.png")
    pix.save(output_path)
    print(f"Saved {output_path}")

print("Done exporting all slides.")
