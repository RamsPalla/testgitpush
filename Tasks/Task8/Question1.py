import logging
logging.basicConfig(filename="Question1.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    import mysql.connector as conn

    db = conn.connect(host="localhost", user="root", passwd="Rams@mysql1")
    cursor = db.cursor()
    #cursor.execute("create database task8")
    #cursor.execute("show databases")
    """ The above line of code must be executed inorder to execute below 'fetchall' code, otherwise we won't get the list of databases"""
    #print(cursor.fetchall())
    cursor.execute("create table task8.AttributeDataSet(Dress_ID int(30), Style varchar(80), Price varchar(80), Rating float(30), Size varchar(80), Season varchar(80), NeckLine varchar(80), SleeveLength varchar(80), waiseline varchar(80), Material varchar(80), FabricType varchar(80), Decoration varchar(80), PatternType varchar(80), Recommendation int(30))")
    cursor.execute("create table task8.DressDataSet(Dress_ID int(30), Day1 int(30), Day2 int(30), Day3 int(30), Day4 int(30), Day5 int(30), Day6 int(30), Day7 int(30), Day8 int(30), Day9 int(30), Day10 int(30), Day11 int(30), Day12 int(30), Day13 int(30), Day14 int(30), Day15 int(30), Day16 int(30), Day17 int(30), Day18 int(30), Day19 int(30), Day20 int(30), Day21 int(30), Day22 int(30), Day23 int(30))")
except Exception as e:
    logging.exception(e)


