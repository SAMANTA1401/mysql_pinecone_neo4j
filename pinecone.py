import pinecone

index_name = 'my_index'
query_vector = [1.0, 2.0, 3.0]

pinecone.init(api_key='YOUR_API_KEY', environment='us-west1-gcp')

index = pinecone.Index(index_name)

# 1. Similarity Search
result = index.query(vectors=[query_vector], top_k=10)

# 2. Vector Insertion
vector = [4.0, 5.0, 6.0]
metadata = {'id': 'vector-1'}
index.upsert(vectors=[vector], metadata=[metadata])


index.delete(vectors=[vector])


print(result)