from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

# embeddings = HuggingFaceEndpointEmbeddings(
#     model="google/embeddinggemma-300m",#not good for semanti search.
#     # huggingfacehub_api_token=hf_token
# )

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2" #good one for semantic search
)

documents = [
    "Babar Azam is one of the most consistent batsmen in world cricket.",
    "Shaheen Afridi’s pace and swing make him a deadly bowler with the new ball.",
    "The Pakistan cricket team is known for its unpredictable but exciting performances.",
    "Shadab Khan is an excellent all-rounder and a sharp fielder in the squad.",
    "Mohammad Rizwan’s wicketkeeping and batting have been outstanding in recent years.",
    "Pakistan won the ICC T20 World Cup in 2009 under Younis Khan’s captaincy."
]
query = "Tell me about Babar Azam"


doc_embeddings = embeddings.embed_documents(documents)
query_embedding = embeddings.embed_query(query)

scores = cosine_similarity([query_embedding],doc_embeddings)[0]

idx,score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]
print("User:",query)
print("Assistant:",documents[idx])
print("Similarity Score is:",score)

