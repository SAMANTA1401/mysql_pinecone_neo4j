from neo4j import GraphDatabase

# Replace with your Neo4j instance details
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "password")

# Create a driver instance
driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)

# Create a new session
session = driver.session()


# Execute a Cypher query
result = session.run("MATCH (user:User) RETURN user")

# Process the results
for record in result:
    print(record)


# Close the session
session.close()

# Close the driver
driver.close()



def connect_to_neo4j():
    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    session = driver.session()
    return session

def execute_query(session, query):
    result = session.run(query)
    return result

def process_results(result):
    for record in result:
        print(record)

def main():
    session = connect_to_neo4j()
    query = "MATCH (n) RETURN n"
    result = execute_query(session, query)
    process_results(result)
    session.close()
    driver.close()

if __name__ == "__main__":
    main()



from py2neo import Graph, Node, Relationship

graph = Graph("bolt://localhost:7687", auth=("neo4j", "password"))

# Create a node
node = Node("Person", name="John")
graph.create(node)

# Create a relationship
node1 = graph.nodes.match("Person", name="John").first()
node2 = graph.nodes.match("Person", name="Jane").first()
rel = Relationship(node1, "FRIEND", node2)
graph.create(rel)