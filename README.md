# AI-Based Content Summarizer

Welcome to the **AI-Based Content Summarizer**, an innovative tool that simplifies content summarization! This application is deployed using **Streamlit**, making it user-friendly and accessible.

## Features
- **Input Formats**: Accepts text input, PDF files, and URLs.
- **Text Extraction**: Extracts text from PDF files and web pages.
- **Summarization**: Uses frequency-based summarization to generate concise summaries.
- **User-Friendly Interface**: Deployed on Streamlit for an intuitive and interactive user experience.

## Installation
Follow these steps to get the application running locally:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/text-summarizer.git
   cd text-summarizer
   ```

2. **Install Dependencies**:
   Ensure you have Python installed. Then, install the required packages using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   Start the Streamlit app:
   ```bash
   streamlit run app2.py
   ```

## Checkout my app:
```bash
https://content-summary.streamlit.app/
```

## Usage
1. **Select Input Type**:
   - Choose between "Text", "PDF", or "URL" as the input type.

2. **Provide Input**:
   - For **Text**: Enter the text you want to summarize in the provided text area.
   - For **PDF**: Upload a PDF file from which you want to extract and summarize text.
   - For **URL**: Enter the URL of the web page you want to summarize.

3. **Set Summary Length**:
   - Use the slider to select the number of sentences for the summary.

4. **Generate Summary**:
   - Click the "Summarize" button to generate and display the summary.

## Example
Here's an example of how to use the application:

1. **Select "Text" as the input type**.
2. **Enter the following text**:
   ```
   Natural Language Processing (NLP) is a field of artificial intelligence that focuses on the interaction between computers and humans through natural language. The ultimate goal of NLP is to enable computers to understand, interpret, and generate human language in a way that is both meaningful and useful.
   ```
3. **Set the number of sentences to 2**.
4. **Click "Summarize"** to generate the summary.

## Dependencies
- `streamlit`
- `nltk`
- `PyPDF2`
- `requests`
- `beautifulsoup4`

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any questions or feedback, please contact palaksarna4@gmail.com.

---
