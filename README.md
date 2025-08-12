# RAG-Powered-Chat-Assistant

A professional Streamlit chat assistant powered by Retrieval-Augmented Generation (RAG) and Groq's Llama3 model. Supports both direct LLM and RAG-enhanced chat.

## Project Structure

```
![Simple LLM Chat Diagram](https://raw.githubusercontent.com/your-repo/RAG-Powered-Chat-Assistant/main/assets/simple-llm-chat-diagram.png)
![RAG Chat Diagram](https://raw.githubusercontent.com/your-repo/RAG-Powered-Chat-Assistant/main/assets/rag-chat-diagram.png)

## Project Structure

```

SLAIC/
│
├── llm_chat.py # LLM chat (no RAG)
├── rag_chat.py # RAG-enabled chat
├── requirements.txt # Python dependencies
├── data/
│ └── data.pdf # Example document for RAG
└── storage/
├── default**vector_store.json
├── docstore.json
├── graph_store.json
├── image**vector_store.json
└── index_store.json

````

## Features

- **llm_chat.py**: Direct chat with Llama3 via Groq API (no retrieval).
- **rag_chat.py**: RAG chat—retrieves context from local documents (`data/`) and augments LLM responses.
- **Streamlit UI**: Interactive web interface for chatting.
- **Session History**: Maintains chat history per session.

## Installation

```sh
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pip install python-dotenv
```

Create a `.env` file in the project root and add your Groq API key:

```env
GROQ_API_KEY=your-groq-api-key-here
```

## Usage

### LLM Chat (No RAG)

```sh
streamlit run llm_chat.py
```

### RAG Chat

Place your documents in the `data/` folder (e.g., `data.pdf`), then run:

```sh
streamlit run rag_chat.py
```

## Architecture

### Simple LLM Chat

#### Figure Diagram

![Simple LLM Chat Diagram](https://raw.githubusercontent.com/your-repo/RAG-Powered-Chat-Assistant/main/assets/simple-llm-chat-diagram.png)

#### ASCII Diagram

```
+--------+      +-------------+      +-------------------+
|  User  | ---> | Streamlit UI| ---> | Llama3 Groq Model |
+--------+      +-------------+      +-------------------+
      ^                |                    |
      |                +<-------------------+
      |                      Response
      +-------------------------------------+
```

### RAG Chat

#### Figure Diagram

![RAG Chat Diagram](https://raw.githubusercontent.com/your-repo/RAG-Powered-Chat-Assistant/main/assets/rag-chat-diagram.png)

#### ASCII Diagram

```
+--------+      +-------------+      +-----------+      +-------------------+
|  User  | ---> | Streamlit UI| ---> | RAG Engine| ---> | Llama3 Groq Model |
+--------+      +-------------+      +-----------+      +-------------------+
      ^                |                    |                   |
      |                |                    |                   |
      |                |                    +<------------------+
      |                |                    |   Augmented Query
      |                +<-------------------+                   |
      |                |   Response         |                   |
      +----------------+--------------------+-------------------+
```

## Dependencies

- `streamlit`
- `llama-index`
- `llama-index-core`
- `llama-index-embeddings-huggingface`
- `llama_index.llms.groq`

## How it Works

- **llm_chat.py**: Sends user input directly to Llama3 via Groq API.
- **rag_chat.py**: Loads documents, builds vector index, retrieves relevant context, and augments LLM responses.

## Customization

- To use your own documents, add them to the `data/` folder.
- Update API keys in the Python files as needed.

## License

MIT

---

> For figure diagrams, add your own PNG/SVG files in the `assets/` folder and update the image links above.
````
