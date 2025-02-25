# PII Detection and Encryption for Secure Data Handling

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python)](https://www.python.org/)  
[![Streamlit](https://img.shields.io/badge/Streamlit-%23FF4B4B.svg?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io/)  
[![Encryption](https://img.shields.io/badge/Security-Encryption-green?style=for-the-badge&logo=security&logoColor=white)](#)

## 🔍 Overview
We propose an **AI-powered solution** to identify and locate **Personally Identifiable Information (PII)** across various document types, ensuring no sensitive information goes unnoticed. This approach addresses **data leakage** by combining **detection and encryption**, effectively mitigating the risks of **privacy breaches and financial losses**. 

AI's advanced **pattern recognition** enhances accuracy and speed in identifying PII, making **data protection more robust and reliable**. To achieve this, we utilize a **Retrieval-Augmented Generation (RAG) model** to detect PII information, improving both precision and adaptability across various document formats.

## 🚀 Features
- **PII Detection**: Identifies sensitive information such as names, PAN, passport numbers, etc.
- **RAG Model Integration**: Leverages Retrieval-Augmented Generation for more accurate PII detection.
- **Encryption**: Uses **HashiCorp Vault** for secure encryption and key management.
- **Decryption**: Key-based access control to decrypt sensitive information.
- **User-Friendly Interface**: Built using **Streamlit** for easy document uploads and processing.
- **Secure Data Storage**: Stores encrypted data to prevent unauthorized access.

## 🏗️ Tech Stack
- **Programming Language**: Python
- **Frameworks**: Streamlit
- **Libraries**: PyPDF2, OpenAI API, 
- **Model**: Retrieval-Augmented Generation (RAG) for PII detection
- **Encryption Methods**: **HashiCorp Vault**, AES (Advanced Encryption Standard), RSA (Rivest-Shamir-Adleman)


## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pii-detection-encryption.git
   cd pii-detection-encryption
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## 📜 Usage
1. Upload a document (PDF, TXT, DOCX) containing sensitive information.
2. The system detects PII using the **RAG model** and encrypts it automatically.
3. Download the encrypted file or view the masked version.
4. Authorized users can decrypt the data using a secure key.

## 🔐 Security Measures
- **End-to-End Encryption**: All PII data is encrypted before storage.
- **Access Control**: Only authorized users with the correct key can decrypt data.
- **Audit Logs**: Maintains logs of encryption and decryption events for monitoring.

## 📌 Future Enhancements
- Implement multi-factor authentication for decryption.
- Integrate with cloud storage for encrypted data handling.
- Extend support for real-time PII detection in chat applications.

## 📬 Contact
For any queries or contributions, reach out to **Naresh**:  
📩 [Kaggle Profile](https://www.kaggle.com/nareshv16)  
🐙 [GitHub](https://github.com/yourusername)

---
🔒 **Ensuring data privacy with AI-powered PII detection and encryption!**
