import os
from memory.memory_agent import MemoryAgent


def test_store_user_preference():
    """Test storing a user preference in the Neo4j database."""
    neo4j_uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
    neo4j_user = os.getenv("NEO4J_USER", "neo4j")
    neo4j_password = os.getenv("NEO4J_PASSWORD")

    # Ensure credentials are set
    assert neo4j_password, "NEO4J_PASSWORD is not set"

    # Create MemoryAgent instance
    memory_agent = MemoryAgent(neo4j_uri, neo4j_user, neo4j_password)

    # Test storing a user preference
    memory_agent.store_user_preference("TestUser", "Cuisine", "Vegan")
    print("Test passed: User preference stored successfully.")

    # Close connection
    memory_agent.close()
