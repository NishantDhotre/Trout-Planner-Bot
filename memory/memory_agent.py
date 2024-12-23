import os
from neo4j import GraphDatabase


class MemoryAgent:
    def __init__(self, uri, user, password):
        """Initialize the MemoryAgent with Neo4j connection details."""
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def store_user_preference(self, user, preference_type, preference_value):
        """Store a user preference in the Neo4j database."""
        with self.driver.session() as session:
            query = (
                "MERGE (u:User {name: $user}) "
                "MERGE (p:Preference {type: $preference_type, value: $preference_value}) "
                "MERGE (u)-[:PREFERS]->(p)"
            )
            session.run(query, user=user, preference_type=preference_type, preference_value=preference_value)

    def close(self):
        """Close the connection to the Neo4j database."""
        self.driver.close()


# Fetch Neo4j credentials from environment variables
NEO4J_URI = os.getenv("NEO4J_URI", "bolt://localhost:7687")
NEO4J_USER = os.getenv("NEO4J_USER", "neo4j")
NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")

if not NEO4J_PASSWORD:
    raise ValueError("NEO4J_PASSWORD is not set. Please set it in your CI/CD secrets or local environment.")

# Example usage (this part would typically be in your application logic or tests)
if __name__ == "__main__":
    memory_agent = MemoryAgent(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)
    memory_agent.store_user_preference("John", "Cuisine", "Vegan")
    print("User preference stored successfully.")
    memory_agent.close()
