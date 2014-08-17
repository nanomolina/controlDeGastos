#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import sys

DB_NAME = 'Database/.Database/DEFAULT.db'

class Database():

    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS gastos
                               (producto text, precio real, 
                               fecha text, nombre text, id int, 
                               PRIMARY KEY(id))""")
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS salary
                               (sueldo real)""")
        self.conn.commit()
        self.id = self.get_row_count()
        print "CALL DATABASE INIT"

    def insert_data(self, producto, precio, fecha, nombre):
        self.cursor.execute("INSERT INTO gastos VALUES (?, ?, ?, ?, ?)", 
                            (producto, precio, fecha, nombre, self.id))
        print "(%s, %s, %s) insertados a la BD" % (producto, precio, fecha)
        self.conn.commit()
        self.id += 1

    def get_products(self):
        """
        Esta funcion devuelve un diccionario con clave id y los datos de la base
        de datos referente a los productos.
        """
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT producto FROM gastos ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_prices(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT precio FROM gastos ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_date(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT fecha FROM gastos ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_buyer(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT nombre FROM gastos ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_row_count(self):
        for row in self.cursor.execute("SELECT MAX(id) FROM gastos"):
            if row[0] or row[0]==0:
                result = row[0] + 1
            else:
                result = 0
        return result

    def set_salary(self, value):
        self.cursor.execute("INSERT INTO salary VALUES (?)", (value,))
        print "Sueldo inicial establecido: %s" % value
        self.conn.commit()

    def get_salary(self):
        result = 0
        for row in self.cursor.execute("SELECT sueldo FROM salary"):
            if row[0]:
                result = row[0]
                break
            else:
                result = 0
        return result
