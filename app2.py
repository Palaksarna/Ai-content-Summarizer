import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq
import PyPDF2
import requests
from bs4 import BeautifulSoup

# Download necessary NLTK data files
nltk.download('punkt')
nltk.download('stopwords')

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ''
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        text += page.extract_text()
    return text

def extract_text_from_url(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = ' '.join([p.text for p in soup.find_all('p')])
    return text

def summarize_text(text, num_sentences=3):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Tokenize the text into words
    words = word_tokenize(text.lower())
    
    # Remove stopwords and punctuation
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word.isalnum() and word not in stop_words]
    
    # Calculate word frequencies
    word_frequencies = {}
    for word in words:
        if word not in word_frequencies:
            word_frequencies[word] = 1
        else:
            word_frequencies[word] += 1
    
    # Calculate sentence scores based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word]
                else:
                    sentence_scores[sentence] += word_frequencies[word]
    
    # Extract the top 'num_sentences' sentences
    summary_sentences = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)
    
    # Join the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    return summary

def main():
    st.set_page_config(page_title="Text Summarizer", page_icon=":books:", layout="wide")
    
    # Add a header image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://fiverr-res.cloudinary.com/images/t_main1,q_auto,f_auto,q_auto,f_auto/gigs/270764898/original/670fdf9cdc6fcebd44853403c56fdc199e43b0e9/create-a-text-summarization-model-with-pegasus-bart-distilbart-gpt2-and-t5.png" alt="Header Image" style="max-width: 100%; height: auto; border-radius: 10px;">
        </div>
        """,
        unsafe_allow_html=True
    )

    
    st.title("Text Summarizer")
    st.write("Summarize text from input, PDF, or URL")

    st.markdown(
        """
        <style>
        /* Sidebar background and text styling */
        [data-testid="stSidebar"] {
            background-color: lightblue;
            padding: 20px;
            border-radius: 10px;
        }
        
        /* Sidebar header styling */
        [data-testid="stSidebar"] h1 {
            color: #4B9CD3;
            font-size: 30px;
            font-weight: bold;
        }

        /* Sidebar selectbox and slider styling */
        [data-testid="stSidebar"] .stSelectbox, [data-testid="stSidebar"] .stSlider {
            font-size: 16px;
            color: #333;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Sidebar for input selection
    st.sidebar.header("Input Options")
    input_type = st.sidebar.selectbox("Select input type", ["Text", "PDF", "URL"])
    num_sentences = st.sidebar.slider("Number of sentences for the summary", 1, 10, 3)

    # Layout for main content
    col1, col2 = st.columns(2)

    with col1:
        if input_type == "Text":
            text = st.text_area("Enter the text to summarize")
            if st.button("Summarize"):
                summary = summarize_text(text, num_sentences)
                st.write("Summary:")
                st.write(summary)
        
        elif input_type == "PDF":
            pdf_file = st.file_uploader("Upload a PDF file", type="pdf")
            if pdf_file and st.button("Summarize"):
                text = extract_text_from_pdf(pdf_file)
                summary = summarize_text(text, num_sentences)
                st.write("Summary:")
                st.write(summary)
        
        elif input_type == "URL":
            url = st.text_input("Enter the URL to summarize")
            if st.button("Summarize"):
                text = extract_text_from_url(url)
                summary = summarize_text(text, num_sentences)
                st.write("Summary:")
                st.write(summary)

    with col2:
        st.write("Instructions:")
        st.write("""
        1. Select the input type from the sidebar.
        2. Enter the text, upload a PDF, or provide a URL.
        3. Adjust the number of sentences for the summary using the slider.
        4. Click the 'Summarize' button to generate the summary.
        """)

    # Custom CSS for styling
    st.markdown("""
    <style>
    .stButton>button {
        background-color: cornflowerblue;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 8px;
    }
    .stButton>button:hover {
        background-color: darkblue;
        text-decoration: none;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
