import streamlit as st
st.set_page_config(page_title="PDF Upload", page_icon="📄", layout="centered")
st.markdown("""
    <style>
    body {
        background-color: #000;  /* Black background */
        color: #fff;  /* White text */
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
        background-color: #222;  /* Slightly lighter black */
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


st.title("📄 Stylish PDF Upload")
st.markdown("*Drag and drop your PDF files here, or click to upload.*")


uploaded_file = st.file_uploader("", type="pdf", label_visibility="collapsed")

if uploaded_file is not None:
    
    st.success("File uploaded successfully!")

    st.download_button(label="Download PDF", data=uploaded_file, file_name="uploaded_file.pdf", mime="application/pdf", key="download_button")


#st.markdown('<div class="footer">© 2024 Your Company. All rights reserved.</div>', unsafe_allow_html=True)