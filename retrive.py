from qdrant_client import QdrantClient
from embed import embed_text

def search_DB(client, text):
    query_list = embed_text(text).tolist()

    res = client.query_points(
        collection_name = "HR",
        query = query_list,
        limit = 3
    )

    return "\n\n".join(r.payload["text"] for r in res.points)