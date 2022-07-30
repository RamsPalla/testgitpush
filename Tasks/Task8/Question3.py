#https://sparkbyexamples.com/pandas/pandas-read-sql-query-or-table/
import logging
logging.basicConfig(filename="Question3.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    import mysql.connector as conn
    db = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1", database = "task8")
    cursor = db.cursor()
    import pandas as rams
    import pymysql
    import openpyxl as xl
    ad = rams.read_excel(r"C:\Users\Rambabu\Desktop\Data Science Full Stack Developer\Pandas\Attribute DataSet.xlsx")
    print(ad)
    dd = rams.read_excel(r"C:\Users\Rambabu\Desktop\Data Science Full Stack Developer\Pandas\Dress Sales.xlsx")
    print(dd)
    sql_queryattribute = rams.read_sql('select * from attributedataset', db)
    print(rams.DataFrame(sql_queryattribute, columns = ['Dress_ID', 'Style', 'Price', 'Rating', 'Size', 'Season', 'NeckLine', 'SleeveLength', 'waiseline', 'Material', 'FabricType', 'Decoration', 'PatternType', 'Recommendation']))
    sql_querydress = rams.read_sql('select * from dressdataset', db)
    print(rams.DataFrame(sql_querydress,columns=['Dress_ID', 'Day1', 'Day2', 'Day3', 'Day4', 'Day5', 'Day6', 'Day7', 'Day8', 'Day9', 'Day10', 'Day11', 'Day12', 'Day13', 'Day14', 'Day15', 'Day16', 'Day17', 'Day18', 'Day19', 'Day20', 'Day21', 'Day22', 'Day23']))
except Exception as e:
    logging.exception(e)
