from memory.memory_agent import MemoryAgent


def test_store_user_preference():
    memory_agent = MemoryAgent(
        "bolt://localhost:7687",
        "neo4j",
        "your_password_here")
    memory_agent.store_user_preference("TestUser", "Cuisine", "Vegan")
    assert True  # Simply check if no exceptions were raised
