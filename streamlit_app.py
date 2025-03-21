import os
import streamlit as st
from database import session, ProductSpec
from pdf_utils import extract_pdf_text
from agents import run_technical, run_creative
from word_export import export_to_word

st.title("🔎 Lighting Product Analyzer (GPT-4o + DB)")

uploaded_pdf = st.file_uploader("Ladda upp produktblad (PDF)", type=["pdf"])

if uploaded_pdf:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_pdf.read())
    st.success("PDF uppladdad!")

    if st.button("Analysera"):
        pdf_text = extract_pdf_text("temp.pdf")
        spec = run_technical(f"Sammanfatta och skapa en teknisk specifikation i tabellform:\n{pdf_text}")
        improvements = run_creative(f"Föreslå förbättringar för denna produkt:\n{pdf_text}")

        # Visa resultat
        st.subheader("✅ Teknisk Specifikation")
        st.write(spec.content)

        st.subheader("💡 Förbättringsförslag")
        st.write(improvements.content)

        # Spara i DB
        product = ProductSpec(
            name="Uppladdad produkt",
            spec=spec.content,
            improvements=improvements.content,
            source_pdf="temp.pdf"
        )
        session.add(product)
        session.commit()

        # Exportera Word
        export_to_word("Produkt Specifikation", spec.content, improvements.content)
        st.success("Word-rapport skapad!")

        with open("produkt_spec.docx", "rb") as docx_file:
            st.download_button("Ladda ner Word-rapport", docx_file, file_name="produkt_spec.docx")