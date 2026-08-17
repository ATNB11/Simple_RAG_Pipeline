from qdrant_client import QdrantClient
from embed import embed_text
from reranker import rerank

def search_DB(client, text):
    query_list = embed_text(text).tolist()

    res = client.query_points(
        collection_name = "HR",
        query = query_list,
        limit = 10
    )

    return rerank(text, res.points)