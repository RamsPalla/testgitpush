import logging
logging.basicConfig(filename="Question2.log", level=logging.DEBUG, format=  '%(asctime)s'  ' %(name)s' '  %(levelname)s' ' %(message)s')
try:
    import mysql.connector as conn
    import pandas as pd
    import xlrd
    #import MySQLdb
    import pymysql

    pymysql.install_as_MySQLdb()

    # Open the workbook and define the worksheet
    #book = xlrd.open_workbook(r"C:\Users\Rambabu\Desktop\Data Science Full Stack Developer\Pandas\Attribute DataSet.xls")
    #sheet = book.sheet_by_name("Sheet1")
    book = xlrd.open_workbook(r"C:\Users\Rambabu\Desktop\Data Science Full Stack Developer\Pandas\Dress Sales.xls")
    sheet = book.sheet_by_name("Sheet1")

    # Establish a MySQL connection
    db = conn.connect(host="localhost", user="root", passwd="Rams@mysql1", db = "task8")

    # Get the cursor, which is used to traverse the database, line by line
    cursor = db.cursor()

    # Create the INSERT INTO sql query
    #query = """INSERT INTO attributedataset(Dress_ID, Style, Price, Rating, Size, Season, NeckLine, SleeveLength, waiseline, Material, FabricType, Decoration, PatternType, Recommendation) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

    # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
    #for r in range(1, sheet.nrows):
        #Dress_ID = sheet.cell(r, 0).value
        #Style = sheet.cell(r, 1).value
        #Price = sheet.cell(r, 2).value
        #Rating = sheet.cell(r, 3).value
        #Size = sheet.cell(r, 4).value
        #Season = sheet.cell(r, 5).value
        #NeckLine = sheet.cell(r, 6).value
        #SleeveLength = sheet.cell(r, 7).value
        #waiseline = sheet.cell(r, 8).value
        #Material = sheet.cell(r, 9).value
        #FabricType = sheet.cell(r, 10).value
        #Decoration = sheet.cell(r, 11).value
        #PatternType = sheet.cell(r, 12).value
        #Recommendation = sheet.cell(r, 13).value

        # Assign values from each row
        #values = (Dress_ID, Style, Price, Rating, Size, Season, NeckLine, SleeveLength, waiseline, Material, FabricType, Decoration, PatternType, Recommendation)

        # Execute sql Query
        #cursor.execute(query, values)
        #db.commit()
    # Create the INSERT INTO sql query
    query = "INSERT INTO dressdataset(Dress_ID, Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    # Create a For loop to iterate through each row in the XLS file, starting at row 2 to skip the headers
    for r in range(1, sheet.nrows):
        Dress_ID = sheet.cell(r, 0).value
        Day1 = sheet.cell(r, 1).value
        Day2 = sheet.cell(r, 2).value
        Day3 = sheet.cell(r, 3).value
        Day4 = sheet.cell(r, 4).value
        Day5 = sheet.cell(r, 5).value
        Day6 = sheet.cell(r, 6).value
        Day7 = sheet.cell(r, 7).value
        Day8 = sheet.cell(r, 8).value
        Day9 = sheet.cell(r, 9).value
        Day10 = sheet.cell(r, 10).value
        Day11 = sheet.cell(r, 11).value
        Day12 = sheet.cell(r, 12).value
        Day13 = sheet.cell(r, 13).value
        Day14 = sheet.cell(r, 14).value
        Day15 = sheet.cell(r, 15).value
        Day16 = sheet.cell(r, 16).value
        Day17 = sheet.cell(r, 17).value
        Day18 = sheet.cell(r, 18).value
        Day19 = sheet.cell(r, 19).value
        Day20 = sheet.cell(r, 20).value
        Day21 = sheet.cell(r, 21).value
        Day22 = sheet.cell(r, 22).value
        Day23 = sheet.cell(r, 23).value
        values = (Dress_ID, Day1, Day2, Day3, Day4, Day5, Day6, Day7, Day8, Day9, Day10, Day11, Day12, Day13, Day14, Day15, Day16, Day17, Day18, Day19, Day20, Day21, Day22, Day23)
        cursor.execute(query, values)
        db.commit()
    # Close the cursor
    cursor.close()

    # Commit the transaction
    db.commit()

    # Close the database connection
    db.close()
except Exception as e:
    logging.exception(e)