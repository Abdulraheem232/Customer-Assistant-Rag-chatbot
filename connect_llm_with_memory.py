from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
import os
import dotenv

dotenv.load_dotenv()

# Load llm 
def load_llm(model_name):
    llm = ChatGroq(model_name=model_name,api_key=os.environ["API_KEY"])
    return llm

chat_prompt_insturctions = """Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context
Extra note : if their is any number 3219160283 in the context replace it with +92 3219160283

Context: {context}
Question: {question}

Start the answer directly. No small talk please."""

def create_prompt_template():
    prompt_template = PromptTemplate(
        input_variables=["context", "question"],
        template=chat_prompt_insturctions
    )
    return prompt_template

#Load faiss vector store
embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
vector_store = FAISS.load_local("vectorstore/faiss", embedding_model, allow_dangerous_deserialization=True)

# Create the retrieval chain
chain = RetrievalQA.from_chain_type(
    llm=load_llm("llama3-8b-8192"),
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs={"prompt": create_prompt_template()}
) 

# Function to answer a question using the retrieval chain
def answer_question(question):
    response = chain({"query": question})
    return response['result'], response['source_documents']


