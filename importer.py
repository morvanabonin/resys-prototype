'''
    Importer movielens dataset for Neo4J database
'''
import csv
import sys
import re

from neo4j.v1 import GraphDatabase
from logger import *


# conexão com o banco de grafos neo4j
try:
    driver = GraphDatabase.driver("bolt://172.18.0.2:7687", auth=("neo4j", "201125"))

    logger.info("Conexão efetuada com sucesso!")
except Exception as e:
    logger.error("Houve erro ao efetuar a conexão com o banco. Erro: {0}".format(e))


# leitura do csv
try:
    # with open('ml-latest/movies.csv', 'r+') as csvmovies:
    #     movies = csv.reader(csvmovies, delimiter=',', quotechar='|')
    #     for movie in movies:

    with open('ml-latest/movies.csv', 'r') as movieFile:
        # retira a 1ª linha do arquivo (header)
        next(movieFile)
        reader = csv.reader(movieFile)
        movies = list(reader)

    with open('ml-latest/users.csv', 'r') as usersFile:
        # retira a 1ª linha do arquivo (header)
        next(usersFile)
        reader = csv.reader(usersFile)
        users = list(reader)

    with open('ml-latest/ratings.csv', 'r') as ratingsFile:
        # retira a 1ª linha do arquivo (header)
        next(ratingsFile)
        reader = csv.reader(ratingsFile)
        ratings = list(reader)

    # for index, movie in enumerate(movies):

    for movie in movies:
        indexMovie = movie[0]
        nameMovie = movie[1]
        genres = movie[2]
        for user in users:
            indexUser = user[0]
            firstName = user[1]
            lastName = user[2]
            for rating in ratings:
                userId = rating[0]
                movieId = rating[1]
                rating = rating[2]

                if(indexMovie == movieId and indexUser == userId):
                    # cria apenas um unico nome
                    name = firstName +' '+ lastName
                    movieGenres = genres.split('|')

                    # gambi para dar slip no nome do filme e ano tirando os parenteses
                    movie = nameMovie.replace(")", " ").split('(')
                    title = movie[0]
                    titleGlued = title.replace(" ", "")
                    year = movie[1]

                    relation = [firstName, lastName, title, year, movieGenres, rating]
                    with open('ml-latest/relations.csv', 'a', newline='', encoding='utf-8') as writeFile:
                        writer = csv.writer(writeFile)
                        #print(relation)
                        # abrindo uma sessão no Neo4J
                        # dbg = driver.session()

                        # # Criação e select para inserção e retorno de dados
                        # ret = dbg.run("CREATE (" + firstName + ":Person {name:'" + name + "'})-[w:WATCH]->" +
                        # "(" + titleGlued + ":Movie {title:'" + title +"', released:" + year +"});")
                        # print(ret)
                                                
                        # escrita em arquivo
                        writer.writerow(relation)
                    writeFile.close()
    # fechando sessão
    dbg = driver.close()

    movieFile.close()
    usersFile.close()
    ratingsFile.close()  
    
except Exception as e:
    logger.error("Houve erro ao ler o arquivo de CSV. Erro: {0}".format(e))

def getDictGenres(genres):
    return genres.split('|')

def testeCreate():
    # abrindo uma sessão no Neo4J
    dbg = driver.session()
    # Match para retorno de dados (tipo um select)
    ret = dbg.run("CREATE (database:Database {name:'Neo4j'})-[r:SAYS]->(message:Message {name:'Hello World!'}) RETURN database, message, r")
    # for do resultado
    for r in ret:
        print(r)
    # fechando sessão
    dbg = driver.close()

def testeConexãoMatch():
    # abrindo uma sessão no Neo4J
    dbg = driver.session()
    # Match para retorno de dados (tipo um select)
    ret = dbg.run("MATCH (a)-[:ACTED_IN]->(m)<-[:DIRECTED]-(d) RETURN a,m,d LIMIT 10")
    # for do resultado
    for r in ret:
        print(r)
    # fechando sessão
    dbg = driver.close()