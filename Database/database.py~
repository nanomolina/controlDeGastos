#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import sys

class Database():

    def __init__(self):
        self.conn = sqlite3.connect('GASTOS.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS gastos4
                               (producto text, precio real, 
                               fecha text, nombre text, id int, 
                               PRIMARY KEY(id))""")
        self.conn.commit()
        self.id = self.get_row_count()

    def insert_data(self, producto, precio, fecha, nombre):
        self.cursor.execute("INSERT INTO gastos4 VALUES (?, ?, ?, ?, ?)", 
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
        for row in self.cursor.execute("SELECT producto FROM gastos4 ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_prices(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT precio FROM gastos4 ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_date(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT fecha FROM gastos4 ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data

    def get_buyer(self):
        counter = 0
        data = {}
        for row in self.cursor.execute("SELECT nombre FROM gastos4 ORDER BY id"):
            data[counter] = str(row[0])
            counter += 1
        return data


    def get_row_count(self):
        for row in self.cursor.execute("SELECT MAX(id) FROM gastos4"):
            if row[0] or row[0]==0:
                result = row[0] + 1
            else:
                result = 0
        return result
