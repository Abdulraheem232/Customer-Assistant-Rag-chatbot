# 🤖 Customer Assistant RAG Chatbot

A sophisticated Retrieval-Augmented Generation (RAG) chatbot designed to provide intelligent customer support for SmartFinder.Store electronics retailer. This system combines the power of large language models with a comprehensive knowledge base to deliver accurate, contextual responses to customer inquiries.

## 🌟 Features

- **🔍 Intelligent Document Retrieval**: Uses FAISS vector database for fast and accurate document retrieval
- **💬 Natural Language Processing**: Powered by advanced language models via ChatGroq
- **📚 Comprehensive Knowledge Base**: Trained on detailed customer support documentation
- **⚡ Real-time Responses**: Fast query processing and response generation
- **🎯 Context-Aware**: Maintains conversation context for better user experience
- **🔧 Modular Architecture**: Easy to extend and customize for different use cases

## 🏗️ Architecture

```
User Query → Document Retrieval (FAISS) → Context Enhancement → LLM Processing (ChatGroq) → Response Generation
```

The system follows a RAG architecture where:
1. User queries are embedded and matched against the knowledge base
2. Relevant documents are retrieved using semantic search
3. Retrieved context is combined with the user query
4. The enhanced prompt is processed by the language model
5. A contextually relevant response is generated

## 🛠️ Technology Stack

- **LangChain Community**: Framework for building LLM applications
- **LangChain HuggingFace**: Integration with HuggingFace models and embeddings
- **LangChain ChatGroq**: High-performance language model inference
- **FAISS-CPU**: Facebook AI Similarity Search for vector operations
- **Python**: Primary programming language
- **Streamlit/Gradio**: Web interface (optional)

## 📋 Prerequisites

- Python 3.8 or higher
- pip package manager
- **API Keys**: Get your free Groq API key from [console.groq.com](https://console.groq.com/)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Abdulraheem232/Customer-Assistant-Rag-chatbot.git
   cd Customer-Assistant-Rag-chatbot
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install langchain-community langchain-huggingface langchain-chatgroq faiss-cpu
   pip install -r requirements.txt  # If additional requirements exist
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   API_KEY=your_groq_api_key_here
   ```
   Get your free API key from [Groq Console](https://console.groq.com/)

## ⚙️ Configuration

### Environment Setup

Create a `.env` file with your Groq API key:

```env
# API Key (Get from https://console.groq.com/)
API_KEY=your_groq_api_key
```

### Pre-built Knowledge Base

The vector embeddings are already included in the repository, so no additional setup is required for the knowledge base.

## 🎯 Usage

### Running the Application

```bash
python main.py
```

This will start the customer support assistant chatbot.

## 📁 Project Structure

```
Customer-Assistant-Rag-chatbot/
├── __pycache__/               # Python cache files
├── data/                      # Data directory
├── vectorstore/               # Pre-built FAISS embeddings
├── .env                       # Environment variables (API_KEY)
├── connect_llm_with_memory.py # LLM connection with memory
├── create_memory_for_llm.py   # Memory creation for LLM
├── main.py                    # Main application file
└── README.md                  # This file
```

## 🔧 How It Works

The RAG system operates by:

1. **Query Processing**: User input is processed and embedded
2. **Document Retrieval**: FAISS searches pre-built vector embeddings in `vectorstore/` for relevant context
3. **Memory Management**: `create_memory_for_llm.py` handles conversation memory
4. **Response Generation**: `connect_llm_with_memory.py` generates responses using ChatGroq with retrieved context
5. **Main Interface**: `main.py` coordinates the entire process

## 📊 Performance

- **Fast Retrieval**: Pre-built FAISS embeddings ensure quick response times
- **Accurate Responses**: Context-aware generation using retrieved documents
- **Memory Efficient**: Optimized for CPU usage with FAISS-CPU
- **Scalable**: Can handle multiple concurrent users

## 🧪 Testing

Simply run the application and test with sample queries:

```bash
python main.py

# Try these sample questions:
# - "What is your return policy?"
# - "How do I track my order?"
# - "What smartphones do you sell?"
# - "How can I contact customer support?"
```

## 📈 Features

The chatbot can help with:

- **Product Information**: Details about electronics and specifications
- **Order Management**: Tracking orders and order status
- **Returns & Refunds**: Policy information and procedures  
- **Technical Support**: Device troubleshooting and setup
- **General Inquiries**: Store policies and contact information

## 🔐 Security Considerations

- **API Key Management**: Store API keys securely in environment variables
- **Input Validation**: Sanitize user inputs to prevent injection attacks
- **Rate Limiting**: Implement rate limiting for production deployments
- **Data Privacy**: Ensure customer data is handled according to privacy regulations

## 🚀 Deployment

### Local Deployment

```bash
python main.py
```

The application will start and you can interact with the customer support assistant through the command line interface.

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines

- Follow PEP 8 style guidelines
- Write comprehensive tests for new features
- Update documentation for any API changes
- Ensure backward compatibility when possible

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **LangChain Community** for the excellent RAG framework
- **HuggingFace** for providing state-of-the-art embeddings
- **Groq** for high-performance language model inference
- **Facebook AI** for the FAISS vector search library

## 📞 Support

For support and questions:

- **Email**: abdulraheemabdullah859@gmail.com
- **Phone**: 3219160283
- **GitHub Issues**: [Create an issue](https://github.com/Abdulraheem232/Customer-Assistant-Rag-chatbot/issues)

## 🔄 Changelog

### Version 1.0.0 (Current)
- Initial release
- Basic RAG implementation
- FAISS vector store integration
- ChatGroq language model support
- Web interface with Streamlit

### Upcoming Features
- Multi-language support
- Advanced conversation memory
- Integration with customer databases
- Real-time learning capabilities
- Performance analytics dashboard

---

## 🎯 SmartFinder.Store Integration

This chatbot is specifically designed for SmartFinder.Store customer support:

- **Product Knowledge**: Comprehensive electronics product information
- **Order Management**: Handle order inquiries and tracking
- **Technical Support**: Provide device troubleshooting assistance
- **Return/Refund Process**: Guide customers through return procedures
- **Warranty Information**: Answer warranty and service questions

  An Plz click the star button if you like this repository It motivates me to make more projects for you guys

Visit [SmartFinder.Store](https://smartfinder.store) to see the chatbot in action!

---

**Made with ❤️ by Abdul Raheem**
