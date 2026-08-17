from sentence_transformers import CrossEncoder

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

def rerank(query, results):

    pairs = [
        (query, r.payload["text"])
        for r in results
    ]

    scores = model.predict(pairs)

    ranked = sorted(
        zip(results, scores),
        key = lambda x: x[1],
        reverse= True
    )

    return "\n\n".join(item.payload["text"] for item, _ in ranked[:3])