# Corporate Security Policy Advisor Chatbot

## Overview

The Corporate Security Policy Advisor is a chatbot designed to provide concise and accurate information about corporate security policies based on "The CISO Handbook." This application uses Retrieval-Augmented Generation (RAG) to enhance its responses with relevant content from the handbook.

## Features

- **PDF Processing:** Automatically extracts and processes text from the provided PDF, "The CISO Handbook."
- **Vector Database:** Uses SentenceTransformer and FAISS to build a vector database for efficient document retrieval.
- **Chat Interface:** Provides a user-friendly interface using Gradio for users to interact with the chatbot.
- **Contextual Responses:** Combines user queries with relevant content from the handbook to generate informative responses.

## Installation

To run this application, you need to install the required dependencies. Create a virtual environment and install the dependencies from `requirements.txt`.

```bash
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
pip install -r requirements.txt
```

## Usage

1. Ensure the PDF "corporate_security_policy.pdf" is in the working directory.
2. Run the `app.py` script to launch the Gradio interface.

```bash
python app.py
```

## Project Structure

- `app.py`: Main application file containing the logic for loading the PDF, building the vector database, and handling user interactions.
- `requirements.txt`: Lists the required Python libraries.
- `corporate_security_policy.pdf`: The PDF document used as the knowledge base for the chatbot.

## Example Queries

- What are the key components of a strong password policy?
- How should we handle a potential data breach?
- What are best practices for employee security training?
- Can you explain the concept of defense in depth?
- What should be included in an incident response plan?
- How can we secure our remote work environment?
- What are the main compliance standards we should be aware of?

## License

This project is for informational purposes only and is based on "The CISO Handbook" by Michael Gentile, CISSP, Ronald D. Collette, CISSP, and Thomas D. August, CISSP. For official policy information, please refer to your company's authorized resources.

## Disclaimer

‼️Disclaimer: This chatbot is based on 'The CISO Handbook' and is for informational purposes only. For official policy information, please refer to your company's authorized resources.‼️

---

Feel free to contribute to this project by submitting issues or pull requests on GitHub.
