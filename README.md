# Brainlox Chatbot 🧠

This repository contains the code for the **Brainlox Chatbot**, an interactive application built with **Streamlit** that utilizes **natural language processing** to answer course-related queries. The chatbot leverages the **Langchain** framework and other powerful AI tools to retrieve and process information from specified courses.

## Features

- **Interactive Chat Interface**: Users can input queries related to courses and receive detailed responses.
- **Document Retrieval**: Retrieves course content from specified URLs using the **UnstructuredURLLoader**.
- **Text Splitting**: Processes large text documents by splitting them into manageable chunks with **RecursiveCharacterTextSplitter**.
- **Semantic Search**: Uses **FAISS** for efficient vector search over the course documents.
- **Language Model Integration**: Integrates with a **Hugging Face** model for generating contextual responses.

## Tech Stack

- **Streamlit**: For building an interactive web interface.
- **Langchain**: Framework for building language model applications.
- **FAISS**: Efficient similarity search and clustering.
- **Hugging Face**: Pre-trained language models.
- **SentenceTransformer**: Embedding model for converting text into vectors.

## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Bhudil/Web_chatbot.git

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt

3. **Run the Streamlit application**:
   ```bash
   streamlit run task1.py

## Configuration

Course URLs: Modify the course_urls list in the app.py file to include the URLs of the courses you want to query.

Hugging Face API Key: Set your Hugging Face API key in the key variable within the app.py file.

Model Selection: The application uses the zephyr-7b-alpha model from Hugging Face by default, but you can change it by modifying the repo_id variable.

## Usage
Enter your query in the text input box provided in the Streamlit interface.
Wait for the response: The application processes your query and returns a detailed answer.
Check the results: If a helpful answer is found, it will be displayed; otherwise, a warning will appear.

## Example
![Screenshot (164)](https://github.com/Bhudil/Web_chatbot/assets/99169324/5f2b3485-5af3-4240-beac-025904fc9588)

## How It Works

Data Loading: Course content is loaded from the specified URLs.
Text Processing: The content is split into chunks for efficient processing.
Vectorization: Each chunk is converted into a vector using SentenceTransformer embeddings.
Similarity Search: The vectors are stored in a FAISS index for quick retrieval.
Query Processing: User queries are matched against the indexed vectors to find the most relevant content.
Response Generation: The Hugging Face model generates a response based on the retrieved content.


### Instructions

- Save this README content in a file named `README.md`.
- Update the repository URL, API key, and other placeholders as necessary.
- Make sure to include any additional setup instructions specific to your project.


## Contribution
Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Acknowledgments
Langchain: For providing the tools and libraries necessary for building the chatbot.
Hugging Face: For the language models that power the response generation.
Streamlit: For making it easy to create interactive applications.





