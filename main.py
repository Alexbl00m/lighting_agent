from agents import run_creative, run_technical
from pdf_utils import extract_pdf_text
from vision_utils import analyze_image
from word_export import export_to_word

pdf_text = extract_pdf_text("examples/produktblad.pdf")
spec_result = run_technical(f"Sammanfatta detta produktblad och skapa en teknisk specifikation i tabellform:\n{pdf_text}")

improvements = run_creative(f"Föreslå förbättringar och unika USPar för denna produkt:\n{pdf_text}")

# Alternativ bildanalys
# image_summary = analyze_image("examples/produktbild.jpg")

export_to_word("Produkt Specifikation", spec_result.content, improvements.content)

print("✅ Word-rapport skapad: produkt_spec.docx")