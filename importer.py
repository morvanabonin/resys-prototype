# Importer movielens dataset for Neo4J database

# from neo4j import GraphDatabase
from neo4j.v1 import GraphDatabase

# driver = GraphDatabase.driver("bolt://172.20.0.2:7687", auth=("neo4j", "neo4j"), encrypted=false)
driver = GraphDatabase.driver("bolt://172.19.0.2:7687", auth=("neo4j", "201125"))
print(driver)
# db = GraphDatabase("http://localhost:7474", username="neo4j", password="neo4j")
# print_r(db)

# db = GraphDatabase("bolt://172.20.0.2:7687", username="neo4j", password="neo4j")
# print_r(db)
