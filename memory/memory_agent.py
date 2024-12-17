from neo4j import GraphDatabase


class MemoryAgent:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def store_user_preference(self, user, preference_type, preference_value):
        with self.driver.session() as session:
            query = (
                "MERGE (u:User {name: $user}) "
                "MERGE (p:Preference {type: $preference_type, value: $preference_value}) "
                "MERGE (u)-[:PREFERS]->(p)"
            )
            session.run(query, user=user, preference_type=preference_type, preference_value=preference_value)

memory_agent = MemoryAgent("bolt://localhost:7687", "neo4j", "your_password_here")
memory_agent.store_user_preference("John", "Cuisine", "Vegan")