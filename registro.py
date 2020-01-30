# !/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3


conexion=sqlite3.connect("paciente.db")
try:
    conexion.execute("""create table paciente (
                              codigo integer primary key AUTOINCREMENT,
                              cedula text,
                              nombre text,
                              apellido text,
                              edad real,
                              direccion text,
                              fecha text,
                              gesta integer,
                              partos integer,
                              motivo_consulta text,
                              presenta text,
                              diagnostico text,
                              fur text,
                              telefono text,
                              antemadre text,
                              antepadre text,
                              antehermanos text,
                              antehijos text,
                              patologias text,
                              alergias text,
                              transfuciones text,
                              intervensiones text,
                              menarquia text,
                              sexarquia text,
                              ciclomens text,
                              parejas text,
                              aco text,
                              citologia text,
                              its text,
                              diu text,
                              embarazo_ante text,
                              deseado text,
                              planificado text,
                              controlado text,
                              itu text,
                              numero_control text,
                              laboratorio text,
                              nota_uno text,
                              nota_dos text,
                              nota_tres text,
                              nota_cuatro text,
                              nota_cinco text,
                              nota_seis text,
                              nota_siete text,
                              nota_ocho text,
                              nota_diagnostico text


                        )""")
    print("se creo la tabla paciente")                        
except sqlite3.OperationalError:
    print("La tabla paciente ya existe")                    
conexion.close()

class Paciente:

    def abrir(self):
        conexion=sqlite3.connect("paciente.db")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into paciente(cedula, nombre, apellido, edad, direccion, fecha, gesta, partos, motivo_consulta, presenta, diagnostico, fur, telefono, antemadre, antepadre, antehermanos, antehijos , patologias, alergias, transfuciones, intervensiones, menarquia, sexarquia, ciclomens, parejas, aco, citologia, its, diu) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def alta2(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update paciente set embarazo_ante=?, deseado=? , planificado=?, controlado=?, itu=?, numero_control=?, laboratorio=? where cedula=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

    def alta3(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="update paciente set nota_uno=?,nota_dos=?,nota_tres=?,nota_cuatro=?,nota_cinco=?,nota_seis=?,nota_siete=?,nota_ocho=?,nota_diagnostico=? where cedula=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas modificadas            
        except:
            cone.close()

    def consulta(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido,edad,direccion,fecha, gesta, partos,motivo_consulta, presenta,diagnostico,fur,telefono,antemadre,antepadre,antehermanos,antehijos,patologias,alergias,transfuciones,intervensiones,menarquia,sexarquia,ciclomens, parejas, aco,citologia,its,diu,embarazo_ante,deseado,planificado,controlado,itu,numero_control,laboratorio from paciente where cedula=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def consulta_consentimiento(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido,fecha,diagnostico from paciente where cedula=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()

    def consulta_nota_de_parto(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select nombre, apellido,fecha,nota_uno,nota_dos,nota_tres,nota_cuatro,nota_cinco,nota_seis,nota_siete,nota_ocho,nota_diagnostico from paciente where cedula=?"
            cursor.execute(sql, datos)
            return cursor.fetchall()
        finally:
            cone.close()
            
    def recuperar_todos(self):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="select codigo, cedula, nombre, apellido, edad, direccion, fecha from paciente"
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cone.close()

    def baja(self, datos):
        try:
            cone=self.abrir()
            cursor=cone.cursor()
            sql="delete from paciente where cedula=?"
            cursor.execute(sql, datos)
            cone.commit()
            return cursor.rowcount # retornamos la cantidad de filas borradas
        except:
            cone.close()
    
    