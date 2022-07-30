import logging
logging.basicConfig(filename="Question4.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    import mysql.connector as conn
    db = conn.connect(host = "localhost", user = "root", passwd = "Rams@mysql1", database = "task8")
    cursor = db.cursor()
    import pandas as rams
    import pymysql
    import openpyxl as xl
    import sqlite3
    import psycopg2
    import sqlalchemy
    ad = rams.read_excel(r"C:\Users\Rambabu\Desktop\Data Science Full Stack Developer\Pandas\Attribute DataSet.xlsx")
    print(ad)
    ad.to_json('D:\Attribute DataSet.json')
    sql_queryattribute = rams.read_sql('select * from attributedataset', db)
    print(rams.DataFrame(sql_queryattribute, columns = ['Dress_ID', 'Style', 'Price', 'Rating', 'Size', 'Season', 'NeckLine', 'SleeveLength', 'waiseline', 'Material', 'FabricType', 'Decoration', 'PatternType', 'Recommendation']))
    ad1 = rams.DataFrame(sql_queryattribute, columns = ['Dress_ID', 'Style', 'Price', 'Rating', 'Size', 'Season', 'NeckLine', 'SleeveLength', 'waiseline', 'Material', 'FabricType', 'Decoration', 'PatternType', 'Recommendation'])
    ad1.to_json('E:\Attribute DataSet.json')

except Exception as e:
    logging.exception(e)
