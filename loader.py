def data_loader(path):

    file = open(path, "r")
    text = file.read()
    file.close()
    
    return text

def chunker(text):

    chunks = []

    for chunk in text.split("\n\n"):

        chunk = chunk.strip()

        if chunk:
            chunks.append(chunk)
    
    return chunks