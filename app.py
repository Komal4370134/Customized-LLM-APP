import gradio as gr
from huggingface_hub import InferenceClient
from typing import List, Tuple
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")

class CorporateSecurityApp:
    def __init__(self) -> None:
        self.documents = []
        self.embeddings = None
        self.index = None
        self.load_pdf("corporate_security_policy.pdf")  # Ensure this PDF is in your working directory
        self.build_vector_db()

    def load_pdf(self, file_path: str) -> None:
        doc = fitz.open(file_path)
        self.documents = []
        for page_num in range(len(doc)):
            page = doc[page_num]
            text = page.get_text()
            self.documents.append({"page": page_num + 1, "content": text})
        print("CISO Handbook PDF processed successfully!")

    def build_vector_db(self) -> None:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        self.embeddings = model.encode([doc["content"] for doc in self.documents])
        self.index = faiss.IndexFlatL2(self.embeddings.shape[1])
        self.index.add(np.array(self.embeddings))
        print("Vector database built successfully!")

    def search_documents(self, query: str, k: int = 3) -> List[str]:
        model = SentenceTransformer('all-MiniLM-L6-v2')
        query_embedding = model.encode([query])
        D, I = self.index.search(np.array(query_embedding), k)
        results = [self.documents[i]["content"] for i in I[0]]
        return results if results else ["No relevant security policy information found."]

app = CorporateSecurityApp()

def respond(
    message: str,
    history: List[Tuple[str, str]],
    system_message: str,
    max_tokens: int,
    temperature: float,
    top_p: float,
):
    system_message = "You are a knowledgeable Corporate Security Policy Advisor based on 'The CISO Handbook'. Provide concise, accurate information about corporate security policies. Be professional and focus on security best practices. Prioritize the company's security and compliance. If unsure, advise consulting official policy documents or the security department."
    messages = [{"role": "system", "content": system_message}]

    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    messages.append({"role": "user", "content": message})

    retrieved_docs = app.search_documents(message)
    context = "\n".join(retrieved_docs)
    messages.append({"role": "system", "content": "Relevant CISO Handbook information: " + context})

    response = ""
    for message in client.chat_completion(
        messages,
        max_tokens=150,
        stream=True,
        temperature=0.7,
        top_p=0.9,
    ):
        token = message.choices[0].delta.content
        response += token
        yield response

demo = gr.Blocks()

with demo:
    gr.Markdown(
        "‼️Disclaimer: This chatbot is based on 'The CISO Handbook' and is for informational purposes only. For official policy information, please refer to your company's authorized resources.‼️"
    )
    
    chatbot = gr.ChatInterface(
        respond,
        examples=[
            ["What are the key components of a strong password policy?"],
            ["How should we handle a potential data breach?"],
            ["What are best practices for employee security training?"],
            ["Can you explain the concept of defense in depth?"],
            ["What should be included in an incident response plan?"],
            ["How can we secure our remote work environment?"],
            ["What are the main compliance standards we should be aware of?"],
        ],
        title='Corporate Security Policy Advisor 🛡️💼'
    )

if __name__ == "__main__":
    demo.launch()