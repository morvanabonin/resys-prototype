'''
    Importer movielens dataset for Neo4J database
'''
from neo4j.v1 import GraphDatabase
from logger import *
import sys

# conexão com o banco de grafos neo4j
try:
    driver = GraphDatabase.driver("bolt://172.20.0.2:7687", auth=("neo4j", "201125"))

    logger.info("Conexão efetuada com sucesso!")
except Exception as e:
    logger.error("Houve erro ao efetuar a conexão com o banco. Erro: {0}".format(e))


