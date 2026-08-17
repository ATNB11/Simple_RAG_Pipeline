from vectorDB import *
from loader import *
from retrive import *

client = init_db()

text = data_loader("./data/HR.txt")

chunks = chunker(text)

addToDB(client, chunks)

query = input("Type your query....")

print (search_DB(client, query))