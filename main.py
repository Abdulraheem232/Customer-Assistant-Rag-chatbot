import streamlit as st
from connect_llm_with_memory import chain as qa_chain

st.title("Smartfinder customer assistant chatbot")
st.write("A ai chatbot that can answer questions related to Smartfinder.store using a knowledge base.")
text_query = st.text_area(height=250,placeholder="Enter your query here..",label="Write your query")
submit_button = st.button("Enter")


if submit_button or text_query:
   response = qa_chain.invoke({"query":text_query})
   st.chat_message("ai").markdown(response["result"])
   st.write("Source")
   sources = response["source_documents"][0]
   st.code(f"Page {sources.metadata["page"]+1} out of {sources.metadata["total_pages"]} of {sources.metadata["source"]}")