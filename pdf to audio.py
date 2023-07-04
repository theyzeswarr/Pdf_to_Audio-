import PyPDF2
import pyttsx3

def convert_pdf_to_audio(pdf_path, output_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        
        # Extract text from each page of the PDF
        for page in pdf_reader.pages:
            text += page.extract_text()
        engine = pyttsx3.init()
        engine.save_to_file(text, output_path)
        engine.runAndWait()
pdf_file_path = "seaborn.pdf"
audio_file_path = "output.wav"
convert_pdf_to_audio(pdf_file_path, audio_file_path)
