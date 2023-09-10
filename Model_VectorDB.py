import logging
from pymongo import MongoClient
from langchain.vectorstores import MongoDBAtlasVectorSearch
from langchain.document_loaders import UnstructuredURLLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from utils import Mongo_cluster_URI,Urls
from langchain.memory import ConversationBufferWindowMemory
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA    
from langchain import OpenAI
from utils import OpenAI_api_key 
import re
import os

os.environ["OPENAI_API_KEY"] = OpenAI_api_key 

# Configure logging
logging.basicConfig(filename='my_app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s: %(message)s',filemode='w')

#Load files from remote URLs using Unstructured.
logging.info("Loading files from remote URLs.")

loaders = UnstructuredURLLoader(urls = Urls)
data = loaders.load()

logging.info("Files loaded successfully.")


# Text Splitter
logging.info("Splitting text into documents.")

text_splitter = CharacterTextSplitter(separator='\n',
                                      chunk_size=1200,  #how many token or words in one chuck as we pass it to llm
                                      chunk_overlap=300  # Number of overlaps to keep track of the continous context
                                              )

docs = text_splitter.split_documents(data)

logging.info("Text splitting completed.")

#Defining an Open - source embedding model 
logging.info("Initializing Sentence Transformer Embeddings.")

embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

logging.info("Embeddings model initialized successfully.")

#Config for the mongo client
logging.info("Connecting to MongoDB Atlas.")

client = MongoClient(Mongo_cluster_URI)

db_name = "langchain_db"
collection_name = "langchain_col"
collection = client[db_name][collection_name]
index_name = "langchain_demo"

# insert the documents in MongoDB Atlas with their embedding
Vector_DB = MongoDBAtlasVectorSearch.from_documents(
    docs, embeddings, collection=collection, index_name=index_name
)

logging.info("MongoDB Atlas connection established & Vector store completed")

#adjust the temp according to how creative you want the bot
llm = OpenAI(temperature=0.5) 

#Creating a prompt template so we can keep the answer close to accurate you can change according to your needs
prompt_template = """Use the latest finance data given to you and answer the question and add some of your past knowledge 
to give insights only if you dont have recent data from vector storage, don't try to make up an answer.

{context}

Question: {question}
"""
PROMPT = PromptTemplate(template=prompt_template, input_variables=["context", "question"])

#store upto part 3 prompt and response from chatbot, can change k accordingly
memory = ConversationBufferWindowMemory(k=3)
chain_type_kwargs = {"prompt": PROMPT}

#Interactive model for question and answers
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=Vector_DB.as_retriever(), memory=memory, chain_type_kwargs=chain_type_kwargs)

logging.info("QA LLM model initialized with vectorstore ")

#function to retrieve answer from user query

def get_answer(query):
    results = qa.run(query)
    results = results.strip('\nAnswer:')
    # Use regular expressions to remove extra characters
    clean_answer = re.sub(r'[^\x00-\x7F]+', '',results)
    return clean_answer


