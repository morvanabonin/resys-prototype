# Importer movielens dataset for Neo4J database

from neo4j import GraphDatabase

db = GraphDatabase("http://localhost:7474", username="neo4j", password="neo4j")

