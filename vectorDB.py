from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams, PointStruct
from embed import embed_chunks


def init_db():
    client = QdrantClient(path = "./HR")

    if not client.collection_exists("HR"):

        client.create_collection(
            collection_name= "HR",
            vectors_config=VectorParams(
                distance = Distance.COSINE,
                size = 384
            )
        )
    
    return client

def addToDB(client, chunks):
    embeddings = embed_chunks(chunks)
    points = []

    for i , (chunk, vector) in enumerate(zip(chunks, embeddings)):

        points.append(
            PointStruct(
                id = i,
                vector = vector.tolist(),
                payload = {
                    "text" : chunk
                }
            )
        )

    client.upsert(
        collection_name = "HR",
        points = points
    )
