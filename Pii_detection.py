import os
import re
import PyPDF2
from sentence_transformers import SentenceTransformer, util
import streamlit as st

# Define the RAGPipeline class
class RAGPipeline:
    def __init__(self, pdf_path, model_name='all-MiniLM-L6-v2', chunk_size=500):
        self.pdf_path = pdf_path
        self.chunk_size = chunk_size
        self.model = SentenceTransformer(model_name)
        self.text = self.extract_text_from_pdf()
        self.chunks = self.preprocess_text(self.text)
        self.chunk_embeddings = self.encode_chunks(self.chunks)

    def extract_text_from_pdf(self):
        with open(self.pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            text = ""
            for page in reader.pages:
                text += page.extract_text()
        return text

    def preprocess_text(self, text):
        chunks = []
        for i in range(0, len(text), self.chunk_size):
            chunk = text[i:i + self.chunk_size]
            chunks.append(chunk)

        processed_chunks = [chunk.strip() for chunk in chunks if chunk.strip()]
        return processed_chunks

    def encode_chunks(self, chunks):
        return self.model.encode(chunks, convert_to_tensor=True)

    def retrieve_relevant_chunks(self, query, top_k=3):
        query_embedding = self.model.encode(query, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.chunk_embeddings)[0]

        top_k = min(top_k, len(self.chunks))
        top_results = scores.topk(top_k)
        return [self.chunks[idx] for idx in top_results.indices]

    # Method to find PII information
    def find_pii_information(self, query_list):
        text = ' '.join(self.chunks)

        pii_info = {}
        # Aadhaar regex
        aadhaar_pattern = r'\b\d{4} \d{4} \d{4}\b'
        aadhaar_number = re.search(aadhaar_pattern, text)
        if aadhaar_number:
            pii_info['Aadhaar'] = aadhaar_number.group()

        # Check for the presence of other PII based on the query list
        for query in query_list:
            if query.lower() in text.lower():
                pii_info[query] = True

        return pii_info

# Streamlit UI setup
st.set_page_config(page_title="PDF Upload", page_icon="📄", layout="centered")

st.markdown("""
    <style>
    body {
        background-color: #000;
        color: #fff;
        font-family: 'Arial', sans-serif;
    }
    .drag-drop-area {
        border: 3px dashed #1e3a8a;
        padding: 50px;
        text-align: center;
        color: #1e3a8a;
        background-color: #111;
        border-radius: 15px;
        transition: background-color 0.3s ease;
    }
    .drag-drop-area:hover {
        background-color: #222;
    }
    .upload-button {
        background-color: #1e3a8a;
        color: #fff;
        border: none;
        padding: 12px 24px;
        border-radius: 5px;
        cursor: pointer;
        font-size: 16px;
        margin-top: 20px;
    }
    .upload-button:hover {
        background-color: #3b82f6;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #111;
        color: #888;
        text-align: center;
        padding: 10px 0;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Upload your PDF to Find PII")
st.markdown("*Drag and drop your PDF files here, or click to upload.*")

# File uploader widget
uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")

if uploaded_file is not None:
    st.success('File uploaded successfully!')

    # Create "tmp" directory if it doesn't exist
    tmp_dir = "tmp"
    try:
        if not os.path.exists(tmp_dir):
            os.makedirs(tmp_dir)
            print(f'Directory "{tmp_dir}" created.')
        else:
            print(f'Directory "{tmp_dir}" already exists.')

        # Save uploaded file to the "tmp" directory
        file_path = os.path.join(tmp_dir, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

    # Initialize the RAGPipeline with the uploaded PDF
    pipeline = RAGPipeline(file_path)

    # Define your queries
    query = [
        "Aadhaar", "Passport number", "Account Number", "Driving License Number", "PAN card", 
        "Application Number", "Email Address", "Phone number", "Biometric data", "IP address", 
        "Voter identity", "Date of birth"
    ]

    # Retrieve and display the PII information
    pii_info = pipeline.find_pii_information(query)
    st.write(pii_info)

    st.download_button(label="Download PDF", data=uploaded_file, file_name="uploaded_file.pdf", mime="application/pdf", key="download_button")
