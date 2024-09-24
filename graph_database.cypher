// Create nodes
CREATE (user1:User {id: 1, name: "John"})
CREATE (user2:User {id: 2, name: "Jane"})
CREATE (user3:User {id: 3, name: "Bob"})

CREATE (interest1:Interest {id: 1, name: "Music"})
CREATE (interest2:Interest {id: 2, name: "Movies"})
CREATE (interest3:Interest {id: 3, name: "Sports"})

// Create relationships
CREATE (user1)-[:FRIEND {since: 2010}]->(user2)
CREATE (user1)-[:FRIEND {since: 2012}]->(user3)
CREATE (user2)-[:FRIEND {since: 2015}]->(user3)

CREATE (user1)-[:INTERESTED_IN]->(interest1)
CREATE (user1)-[:INTERESTED_IN]->(interest2)
CREATE (user2)-[:INTERESTED_IN]->(interest2)
CREATE (user3)-[:INTERESTED_IN]->(interest3)

// 1. Find friends of a user
MATCH (user:User {id: 1})-[:FRIEND]->(friend)
RETURN friend

// 2. Find common interests between two users
MATCH (user1:User {id: 1})-[:INTERESTED_IN]->(interest)
MATCH (user2:User {id: 2})-[:INTERESTED_IN]->(interest)
RETURN interest

// 3. Find users with similar interests
MATCH (user1:User {id: 1})-[:INTERESTED_IN]->(interest)
MATCH (other:User)-[:INTERESTED_IN]->(interest)
WHERE other <> user1
RETURN other

// 4. Find shortest path between two users
MATCH p=shortestPath((user1:User {id: 1})-[*]->(user3:User {id: 3}))
RETURN p

// 5. Find users with most connections
MATCH (user:User)
OPTIONAL MATCH (user)-[:FRIEND]->(friend)
WITH user, COUNT(friend) AS connections
RETURN user, connections
ORDER BY connections DESC
LIMIT 3

// 2. Create Relationship
MATCH (user1:User {name: "John"})
MATCH (user2:User {name: "Jane"})
CREATE (user1)-[:FRIEND]->(user2)


// Find all users:
MATCH (user:User)
RETURN user

// Find all friendships:
MATCH (user1:User)-[:FRIEND]->(user2:User)
RETURN user1, user2