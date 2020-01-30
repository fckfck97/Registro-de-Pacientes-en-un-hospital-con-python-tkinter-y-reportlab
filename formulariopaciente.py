# !/usr/bin/env python
# -*- coding: utf-8 -*-
from Tkinter import *
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import registro
from datetime import datetime
import pdf

class FormularioPaciente:
    def __init__(self):
        self.paciente1=registro.Paciente()
        self.genera1 = pdf.Genera()
        self.ventana1=tk.Tk()
        self.ventana1.geometry("1000x470")
        self.ventana1.resizable(1000,600)
        self.ventana1.columnconfigure(0, weight=1)
        self.ventana1.rowconfigure(0, weight=1)
        self.ventana1.rowconfigure(10, weight=1)
        self.ventana1.title("Registro de Pacientes de Obstetricia.")
        self.cuaderno1 = ttk.Notebook(self.ventana1)
        #Paginas del notebook
        self.menu()
        self.carga_paciente() 
        self.datos_segundarios()
        self.nota_pdf()       
        self.generar_pdf()
        self.recibimiento_pdf()
        self.cuaderno1.grid(column=0, row=0, sticky="nsew")
        self.ventana1.mainloop()    



    def menu(self):
        self.menu=Menu(self.ventana1)
        self.ventana1.config(menu=self.menu)
        self.archivo = Menu(self.menu, tearoff=1)
        self.archivo.add_command(label="Parto Normal",command=lambda: self.seleccion(1))
        self.archivo.add_command(label="Cesarea",command=lambda: self.seleccion(2))
        self.archivo.add_separator()
        self.archivo.add_command(label="Salir", command=lambda: self.salir())
        self.Acerca_De = Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Archivo", menu=self.archivo)
        self.Acerca_De.add_command(label="Autor", command=lambda: self.mensajes(1))
        self.Acerca_De.add_command(label="Frase", command=lambda: self.mensajes(2))
        self.Acerca_De.add_command(label="Desarrollador",command=lambda: self.mensajes(3))
        self.menu.add_cascade(label="Acerca de",menu=self.Acerca_De)
   


    def seleccion(self,opc):
        if opc == 1:
                mb.showinfo("Alerta","Usted ya esta en el formulario de parto normal")
        elif opc == 2:
            print("hola")
        else:
            print("asd")


    def salir(self):
        
        accion = mb.askyesno("Advertencia",
                                   "¿Seguro que desea cerrar el programa?\n Todos los cambios no guardados se perderan")
        if accion == True:
            self.ventana1.destroy()

    def mensajes(self,opc):
        if opc==1:
            mb.showinfo("Medico Desarrollador", "Nombre: Yisel Cardenas\n""23705024\n""Medico Cirujano\n")
        if opc==2:
            mb.showinfo("Frase", "Todo hombre fuerte fue debil alguna vez, asi que la proxima vez que lo pienses no me subestimes"
                                       " que aun estoy en el juego")
        if opc==3:
            mb.showinfo("Desarrollador","Nombre: Jesus Delgado\n""21004289\n""Ing. En Sistemas\n")

    def carga_paciente(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.forum_image = tk.PhotoImage(file="imagenes/paciente.png")
        self.cuaderno1.add(self.pagina1, text="Carga de Pacientes",image=self.forum_image,padding=20,compound=tk.RIGHT)
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Datos del Paciente")        
        self.labelframe1.grid(column=1, row=1,columnspan=7, sticky="nsew",padx=5, pady=5, ipadx=5, ipady=5)

        self.labelframe2=ttk.LabelFrame(self.pagina1, text="Antecedentes Familiares, Personales y Ginecos-Obstetricos.")        
        self.labelframe2.grid(column=1, row=4)

        
#-----------DATOS DEL PACIENTE--------------------------------------------------

        self.label1=ttk.Label(self.labelframe1, text="Cedula:")
        self.label1.grid(column=0, row=0)
        self.cedulacarga=tk.StringVar()
        self.entrydcedula=ttk.Entry(self.labelframe1, textvariable=self.cedulacarga)
        self.entrydcedula.grid(column=1, row=0)
        
        self.label2=ttk.Label(self.labelframe1, text="Nombre:")        
        self.label2.grid(column=2, row=0, padx=4, pady=4)
        self.nombrecarga=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombrecarga)
        self.entrynombre.grid(column=3, row=0, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Apellido:")        
        self.label3.grid(column=4, row=0, padx=4, pady=4)
        self.apellidocarga=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe1, textvariable=self.apellidocarga)
        self.entryapellido.grid(column=5, row=0, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Edad:")        
        self.label4.grid(column=0, row=1, padx=4, pady=4)
        self.edadcarga=tk.StringVar()
        self.entryedad=ttk.Entry(self.labelframe1, textvariable=self.edadcarga)
        self.entryedad.grid(column=1, row=1, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="Direccion:")        
        self.label4.grid(column=2, row=1, padx=4, pady=4)
        self.direccioncarga=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe1, textvariable=self.direccioncarga)
        self.entrydireccion.grid(column=3, row=1, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Gestas:")        
        self.label5.grid(column=4, row=1, padx=4, pady=4)
        self.gestacarga=tk.StringVar()
        self.entrygesta=ttk.Entry(self.labelframe1, textvariable=self.gestacarga)
        self.entrygesta.grid(column=5, row=1, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Partos:")        
        self.label6.grid(column=0, row=2, padx=4, pady=4)
        self.partocarga=tk.StringVar()
        self.entryparto=ttk.Entry(self.labelframe1, textvariable=self.partocarga)
        self.entryparto.grid(column=1, row=2, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="Motivo Consulta:")        
        self.label7.grid(column=2, row=2, padx=4, pady=4)
        self.mconsultacarga=tk.StringVar()
        self.entrymconsulta=ttk.Entry(self.labelframe1, textvariable=self.mconsultacarga)
        self.entrymconsulta.grid(column=3, row=2, padx=4, pady=4)


        self.label8=ttk.Label(self.labelframe1, text="Presenta:")        
        self.label8.grid(column=4, row=2, padx=4, pady=4)
        self.presecarga=tk.StringVar()
        self.entryprese=ttk.Entry(self.labelframe1, textvariable=self.presecarga)
        self.entryprese.grid(column=5, row=2, padx=4, pady=4)
        

        self.label9=ttk.Label(self.labelframe1, text="Diagnostico:")        
        self.label9.grid(column=0, row=3, padx=4, pady=4)
        self.diagcarga=tk.StringVar()
        self.entrydiag=ttk.Entry(self.labelframe1, textvariable=self.diagcarga)
        self.entrydiag.grid(column=1, row=3, padx=4, pady=4)

        self.label10=ttk.Label(self.labelframe1, text="F.U.R:")        
        self.label10.grid(column=2, row=3, padx=4, pady=4)
        self.furcarga=tk.StringVar()
        self.entryfur=ttk.Entry(self.labelframe1, textvariable=self.furcarga)
        self.entryfur.grid(column=3, row=3, padx=4, pady=4)

        self.label11=ttk.Label(self.labelframe1, text="Telefono:")        
        self.label11.grid(column=4, row=3, padx=4, pady=4)
        self.telecarga=tk.StringVar()
        self.entrytele=ttk.Entry(self.labelframe1, textvariable=self.telecarga)
        self.entrytele.grid(column=5, row=3, padx=4, pady=4)


#-----------ANTECEDENTES-------------------------------------------------------
        

        self.label2=ttk.Label(self.labelframe2, text="Madre:")
        self.label2.grid(column=0, row=1)
        self.antemadrecarga=tk.StringVar()
        self.entryantemadre=ttk.Entry(self.labelframe2, textvariable=self.antemadrecarga)
        self.entryantemadre.grid(column=1, row=1)

        self.label3=ttk.Label(self.labelframe2, text="Padre:")
        self.label3.grid(column=2, row=1, padx=4, pady=4)
        self.antepadrecarga=tk.StringVar()  
        self.entryantepadre=ttk.Entry(self.labelframe2, textvariable=self.antepadrecarga)
        self.entryantepadre.grid(column=3, row=1, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe2, text="Hermanos:")
        self.label4.grid(column=4, row=1, padx=4, pady=4)
        self.antehercarga=tk.StringVar()
        self.entryanteher=ttk.Entry(self.labelframe2, textvariable=self.antehercarga)
        self.entryanteher.grid(column=5, row=1, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe2, text="Hijos:")
        self.label5.grid(column=0, row=2, padx=4, pady=4)
        self.antehijoscarga=tk.StringVar()
        self.entryantehijos=ttk.Entry(self.labelframe2, textvariable=self.antehijoscarga)
        self.entryantehijos.grid(column=1, row=2, padx=4, pady=4)


        self.label7=ttk.Label(self.labelframe2, text="Patologia Base:")
        self.label7.grid(column=0, row=4, padx=4, pady=4)
        self.antepatocarga=tk.StringVar()
        self.entryantepato=ttk.Entry(self.labelframe2, textvariable=self.antepatocarga)
        self.entryantepato.grid(column=1, row=4, padx=4, pady=4)

        self.label8=ttk.Label(self.labelframe2, text="Alergias:")
        self.label8.grid(column=2, row=4, padx=4, pady=4)
        self.antealergiacarga=tk.StringVar()
        self.entryantealergia=ttk.Entry(self.labelframe2, textvariable=self.antealergiacarga)
        self.entryantealergia.grid(column=3, row=4, padx=4, pady=4)

        self.label9=ttk.Label(self.labelframe2, text="Transfusiones:")
        self.label9.grid(column=4, row=4, padx=4, pady=4)
        self.antesangrecarga=tk.StringVar()
        self.entryantesangre=ttk.Entry(self.labelframe2, textvariable=self.antesangrecarga)
        self.entryantesangre.grid(column=5, row=4, padx=4, pady=4)

        self.label10=ttk.Label(self.labelframe2, text="Intervensiones Qx:")
        self.label10.grid(column=0, row=5, padx=4, pady=4)
        self.anteqxcarga=tk.StringVar()
        self.entryanteqx=ttk.Entry(self.labelframe2, textvariable=self.anteqxcarga)
        self.entryanteqx.grid(column=1, row=5, padx=4, pady=4)        

    

        self.label12=ttk.Label(self.labelframe2, text="Menarquia:")
        self.label12.grid(column=0, row=7, padx=4, pady=4)
        self.antemenarcarga=tk.StringVar()
        self.entryantemenar=ttk.Entry(self.labelframe2, textvariable=self.antemenarcarga)
        self.entryantemenar.grid(column=1, row=7, padx=4, pady=4) 

        self.label14=ttk.Label(self.labelframe2, text="Sexarquia:")
        self.label14.grid(column=2, row=7, padx=4, pady=4)
        self.antesexarcarga=tk.StringVar()
        self.entryantesexar=ttk.Entry(self.labelframe2, textvariable=self.antesexarcarga)
        self.entryantesexar.grid(column=3, row=7, padx=4, pady=4) 

        self.label15=ttk.Label(self.labelframe2, text="Ciclo Menstrual:")
        self.label15.grid(column=4, row=7, padx=4, pady=4)
        self.anteciclocarga=tk.StringVar()
        self.entryanteciclo=ttk.Entry(self.labelframe2, textvariable=self.anteciclocarga)
        self.entryanteciclo.grid(column=5, row=7, padx=4, pady=4) 

        self.label16=ttk.Label(self.labelframe2, text="N# Pareja:")
        self.label16.grid(column=0, row=8, padx=4, pady=4)
        self.anteparejacarga=tk.StringVar()
        self.entryantepareja=ttk.Entry(self.labelframe2, textvariable=self.anteparejacarga)
        self.entryantepareja.grid(column=1, row=8, padx=4, pady=4)


#-------------------cHECKBUTTON----------------------
        self.chk_aco = BooleanVar()
        self.chk_aco = Checkbutton(self.labelframe2, text='ACO', var=self.chk_aco)
        self.chk_aco.grid(column=2, row=8)

        self.chk_citologia = BooleanVar()
        self.chk_citologia = Checkbutton(self.labelframe2, text='Citologia', var=self.chk_citologia)
        self.chk_citologia.grid(column=3, row=8)

        self.chk_its = BooleanVar()
        self.chk_its = Checkbutton(self.labelframe2, text='ITS', var=self.chk_its)
        self.chk_its.grid(column=4, row=8)

        self.chk_diu = BooleanVar()
        self.chk_diu = Checkbutton(self.labelframe2, text='DIU', var=self.chk_diu)
        self.chk_diu.grid(column=5, row=8)









#--------------BOTONES----------------------------------------------------------
        self.boton1=ttk.Button(self.labelframe2, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=10, padx=4, pady=4, columnspan=1, sticky="we")
        self.boton2=ttk.Button(self.labelframe2, text ="Limpiar",command=self.limpiar)
        self.boton2.grid(column=2,row=10,padx=4,pady=4, columnspan=1, sticky="we")
  
    def current_date_format(self,date):
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = "{} de {} del {}".format(day, month, year)

        return messsage

    

    def agregar(self):
        if self.chk_aco == True:
            chk_aco = "Si"
        else:
            chk_aco = "No"

        if self.chk_its == True:
            chk_its = "Si"
        else:
            chk_its = "No"
        if self.chk_citologia == True:
            chk_citologia = "Si"
        else:
            chk_citologia = "No"
        if self.chk_diu == True:
            chk_diu = "Si"
        else:
            chk_diu = "No"

        if self.cedulacarga.get() == "" or self.nombrecarga.get() == "" or self.apellidocarga.get() == "" or self.edadcarga.get() == "" or self.direccioncarga.get() == "" or self.gestacarga.get() == "" or self.partocarga.get() == "" or self.mconsultacarga.get() == "" or self.presecarga.get() == "" or self.diagcarga.get() == "" or self.furcarga.get == "":
            mb.showinfo("Cuidado","Debes ingresar los datos completos")    
        else:
            fecha_sin = datetime.now()
            fecha_for = self.current_date_format(fecha_sin)
            datos=(self.cedulacarga.get(), self.nombrecarga.get(), self.apellidocarga.get(),self.edadcarga.get(),self.direccioncarga.get(),fecha_for,self.gestacarga.get(),self.partocarga.get(),self.mconsultacarga.get(),self.presecarga.get(),self.diagcarga.get(),self.furcarga.get(), self.telecarga.get() ,self.antemadrecarga.get(), self.antepadrecarga.get(),self.antehercarga.get(),self.antehijoscarga.get(),self.antepatocarga.get(),self.antealergiacarga.get(),self.antesangrecarga.get(),self.anteqxcarga.get(),self.antemenarcarga.get(),self.antesexarcarga.get(),self.anteciclocarga.get(),self.anteparejacarga.get(),chk_aco,chk_citologia,chk_its,chk_diu)
            self.paciente1.alta(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
            self.cedulacarga.set("")
            self.nombrecarga.set("")
            self.apellidocarga.set("")
            self.edadcarga.set("")
            self.direccioncarga.set("")
            self.gestacarga.set("")
            self.partocarga.set("")
            self.mconsultacarga.set("")
            self.presecarga.set("")
            self.diagcarga.set("")
            self.furcarga.set("")
            self.telecarga.set("")
            self.antemadrecarga.set("")
            self.antepadrecarga.set("")
            self.antehercarga.set("")
            self.antehijoscarga.set("")
            self.antepatocarga.set("")
            self.antealergiacarga.set("")
            self.antesangrecarga.set("")
            self.anteqxcarga.set("")
            self.antemenarcarga.set("")
            self.antesexarcarga.set("")
            self.anteciclocarga.set("")
            self.anteparejacarga.set("")
            self.chk_aco = False
            self.chk_its = False
            self.chk_citologia = False
            self.chk_diu = False
    def limpiar(self):
        self.cedulacarga.set("")
        self.nombrecarga.set("")
        self.apellidocarga.set("")
        self.edadcarga.set("")
        self.direccioncarga.set("")
        self.gestacarga.set("")
        self.partocarga.set("")
        self.mconsultacarga.set("")
        self.presecarga.set("")
        self.diagcarga.set("")
        self.furcarga.set("")
        self.antemadrecarga.set("")
        self.antepadrecarga.set("")
        self.antehercarga.set("")
        self.antehijoscarga.set("")
        self.antepatocarga.set("")
        self.antealergiacarga.set("")
        self.antesangrecarga.set("")
        self.anteqxcarga.set("")
        self.antemenarcarga.set("")
        self.antesexarcarga.set("")
        self.anteciclocarga.set("")
        self.anteparejacarga.set("")
        self.chk_aco = False
        self.chk_its = False
        self.chk_citologia = False
        self.chk_diu = False

    def datos_segundarios(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.forum_image2 = tk.PhotoImage(file="imagenes/datosS.png")
        self.cuaderno1.add(self.pagina2, text="Datos Secundarios",image=self.forum_image2,padding=20,compound=tk.RIGHT)
        
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Embarazo Anterior y Embarazo Actual")
        self.labelframe1.grid(column=0, row=0,columnspan=7, sticky='WE',padx=5, pady=5, ipadx=5, ipady=5)

        
        self.label4=ttk.Label(self.labelframe1, text="Cedula:")
        self.label4.grid(column=0, row=0, padx=4, pady=4)
        self.cedula_mod=tk.StringVar()
        self.entrycedula_mod=ttk.Entry(self.labelframe1, textvariable=self.cedula_mod)
        self.entrycedula_mod.grid(column=1, row=0, padx=4, pady=4)
        

        self.label1=ttk.Label(self.labelframe1, text="Embarazo Anterior:")
        self.label1.grid(column=2, row=0, padx=4, pady=4)
        self.anteembarazo=tk.StringVar()
        self.entryanteembarazo=ttk.Entry(self.labelframe1, textvariable=self.anteembarazo)
        self.entryanteembarazo.grid(column=3, row=0, sticky="nsew", padx=10, pady=10)

        self.label5=ttk.Label(self.labelframe1, text="Embarazo Actual.")
        self.label5.grid(column=0, row=3, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="Numero de Controles:")
        self.label3.grid(column=0, row=4, padx=4, pady=4)
        self.controles=tk.StringVar()
        self.entrycontroles=ttk.Entry(self.labelframe1, textvariable=self.controles)
        self.entrycontroles.grid(column=1, row=4, padx=4, pady=4)

        self.chk_deseado = BooleanVar()
        self.chk_deseado = Checkbutton(self.labelframe1, text='Deseado', var=self.chk_deseado)
        self.chk_deseado.grid(column=2, row=4)

        self.chk_planificado = BooleanVar()
        self.chk_planificado = Checkbutton(self.labelframe1, text='Planificado', var=self.chk_planificado)
        self.chk_planificado.grid(column=3, row=4)

        self.chk_controlado = BooleanVar()
        self.chk_controlado = Checkbutton(self.labelframe1, text='Controlado', var=self.chk_controlado)
        self.chk_controlado.grid(column=4, row=4)

        self.chk_itu = BooleanVar()
        self.chk_itu = Checkbutton(self.labelframe1, text='Itu', var=self.chk_itu)
        self.chk_itu.grid(column=5, row=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Laboratorio:")
        self.label4.grid(column=0, row=5, padx=4, pady=4)
        self.laboratorio=tk.StringVar()
        self.entrylaboratorio=ttk.Entry(self.labelframe1, textvariable=self.laboratorio)
        self.entrylaboratorio.grid(column=1, row=5, padx=4, pady=4)        

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar2)
        self.boton1.grid(column=0, row=6, padx=4, pady=4)
        self.boton2=ttk.Button(self.labelframe1, text ="Limpiar",command=self.limpiar)
        self.boton2.grid(column=1,row=6,padx=4,pady=4)
  
    def agregar2(self):
        if self.chk_deseado == True:
            chk_deseado = "Si"
        else:
            chk_deseado = "No"

        if self.chk_planificado == True:
            chk_planificado = "Si"
        else:
            chk_planificado = "No"
        if self.chk_controlado == True:
            chk_controlado = "Si"
        else:
            chk_controlado = "No"
        if self.chk_itu == True:
            chk_itu = "Si"
        else:
            chk_itu = "No"

        if self.cedula_mod.get() == "" or self.anteembarazo.get() == "" or self.controles.get() == "" or self.laboratorio.get() == "":
            mb.showinfo("Cuidado","Debes ingresar los datos completos")    
        else:
            datos=(self.anteembarazo.get(),chk_deseado,chk_planificado,chk_controlado,chk_itu,self.controles.get(),self.laboratorio.get(),self.cedula_mod.get())
            self.paciente1.alta2(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
            self.cedula_mod.set("")
            self.anteembarazo.set("")
            self.controles.set("")
            self.laboratorio.set("")

    def nota_pdf(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.forum_image3 = tk.PhotoImage(file="imagenes/nota.png")
        self.cuaderno1.add(self.pagina2, text="Nota de Parto",image=self.forum_image3,padding=20,compound=tk.RIGHT)
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Nota de Parto")
        self.labelframe1.grid(column=0, row=0,columnspan=7, sticky='WE',padx=5, pady=5, ipadx=5, ipady=5)
        self.label1=ttk.Label(self.labelframe1, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedula_parto=tk.StringVar()
        self.entrycedula_parto=ttk.Entry(self.labelframe1, textvariable=self.cedula_parto)
        self.entrycedula_parto.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="1.-")
        self.label2.grid(column=2, row=0, padx=4, pady=4)
        self.uno_parto=tk.StringVar()
        self.entryuno_parto=ttk.Entry(self.labelframe1, textvariable=self.uno_parto)
        self.entryuno_parto.grid(column=3, row=0, padx=4, pady=4)

        self.label3=ttk.Label(self.labelframe1, text="2.-")
        self.label3.grid(column=4, row=0, padx=4, pady=4)
        self.dos_parto=tk.StringVar()
        self.entrydos_parto=ttk.Entry(self.labelframe1, textvariable=self.dos_parto)
        self.entrydos_parto.grid(column=5, row=0, padx=4, pady=4)

        self.label4=ttk.Label(self.labelframe1, text="3.-")
        self.label4.grid(column=0, row=1, padx=4, pady=4)
        self.tres_parto=tk.StringVar()
        self.entrytres_parto=ttk.Entry(self.labelframe1, textvariable=self.tres_parto)
        self.entrytres_parto.grid(column=1, row=1, padx=4, pady=4)

        self.label5=ttk.Label(self.labelframe1, text="4.-")
        self.label5.grid(column=2, row=1, padx=4, pady=4)
        self.cuatro_parto=tk.StringVar()
        self.entrycuatro_parto=ttk.Entry(self.labelframe1, textvariable=self.cuatro_parto)
        self.entrycuatro_parto.grid(column=3, row=1, padx=4, pady=4)

        self.label6=ttk.Label(self.labelframe1, text="5.-")
        self.label6.grid(column=4, row=1, padx=4, pady=4)
        self.cinco_parto=tk.StringVar()
        self.entrycinco_parto=ttk.Entry(self.labelframe1, textvariable=self.cinco_parto)
        self.entrycinco_parto.grid(column=5, row=1, padx=4, pady=4)

        self.label7=ttk.Label(self.labelframe1, text="6.-")
        self.label7.grid(column=0, row=2, padx=4, pady=4)
        self.seis_parto=tk.StringVar()
        self.entryseis_parto=ttk.Entry(self.labelframe1, textvariable=self.seis_parto)
        self.entryseis_parto.grid(column=1, row=2, padx=4, pady=4)

        self.label8=ttk.Label(self.labelframe1, text="7.-")
        self.label8.grid(column=2, row=2, padx=4, pady=4)
        self.siete_parto=tk.StringVar()
        self.entrysiete_parto=ttk.Entry(self.labelframe1, textvariable=self.siete_parto)
        self.entrysiete_parto.grid(column=3, row=2, padx=4, pady=4)

        self.label9=ttk.Label(self.labelframe1, text="8.-")
        self.label9.grid(column=4, row=2, padx=4, pady=4)
        self.ocho_parto=tk.StringVar()
        self.entryocho_parto=ttk.Entry(self.labelframe1, textvariable=self.ocho_parto)
        self.entryocho_parto.grid(column=5, row=2, padx=4, pady=4)

        self.label10=ttk.Label(self.labelframe1, text="Diagnostico:")
        self.label10.grid(column=0, row=3, padx=4, pady=4)
        self.diagnostico_parto=tk.StringVar()
        self.entrydiagnostico_parto=ttk.Entry(self.labelframe1, textvariable=self.diagnostico_parto)
        self.entrydiagnostico_parto.grid(column=1, row=3, padx=4, pady=4)

        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command = self.agregar3)
        self.boton1.grid(column=2, row=3, padx=4, pady=4,columnspan=3, sticky="we")

    def agregar3(self):
  
        if self.cedula_parto.get() == "" or self.uno_parto.get() == "" or self.dos_parto.get() == "" or self.tres_parto.get() == "" or self.cuatro_parto.get() == "" or self.cinco_parto.get() == "" or self.seis_parto.get() == "" or self.siete_parto.get() == "" or self.ocho_parto.get() == "" or self.diagnostico_parto.get() == "":
            mb.showinfo("Cuidado","Debes ingresar los datos completos")    
        else:
            datos=(self.uno_parto.get(),self.dos_parto.get(),self.tres_parto.get(),self.cuatro_parto.get(),self.cinco_parto.get(),self.seis_parto.get(),self.siete_parto.get(),self.ocho_parto.get(),self.diagnostico_parto.get(),self.cedula_parto.get())
            self.paciente1.alta3(datos)
            mb.showinfo("Información", "Los datos fueron cargados")
            self.cedula_parto.set("")
            self.uno_parto.set("")
            self.dos_parto.set("")
            self.tres_parto.set("")
            self.cuatro_parto.set("")
            self.cinco_parto.set("")
            self.seis_parto.set("")
            self.siete_parto.set("")
            self.ocho_parto.set("")
            self.diagnostico_parto.set("")

          



    def generar_pdf(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.forum_image4 = tk.PhotoImage(file="imagenes/historia.png")
        self.cuaderno1.add(self.pagina2, text="Generar Historia",image=self.forum_image4,padding=20,compound=tk.RIGHT)
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Historia Medica del Paciente")
        self.labelframe1.grid(column=0, row=0, sticky="nsew")
        self.label1=ttk.Label(self.labelframe1, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedulapdf=tk.StringVar()
        self.entrycedulapdf=ttk.Entry(self.labelframe1, textvariable=self.cedulapdf)
        self.entrycedulapdf.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Generar Historia",command=self.genera_pdf)
        self.boton1.grid(column=1, row=3, padx=4, pady=4,columnspan=3, sticky="we")
        self.boton2=ttk.Button(self.labelframe1, text="Generar Consentimiento",command=self.genera_pdf2)
        self.boton2.grid(column=1, row=4, padx=4, pady=4, columnspan=3, sticky="we")
        self.boton3=ttk.Button(self.labelframe1, text="Generar Nota de Parto",command=self.genera_pdf3)
        self.boton3.grid(column=1, row=5, padx=4, pady=4, columnspan=3, sticky="we")

    def genera_pdf(self):
        datos = (self.cedulapdf.get(), )
        datos1 = self.cedulapdf.get()
        respuesta=self.paciente1.consulta(datos)
        if len(respuesta)>0:
            self.nombrepdf = (respuesta[0][0])
            self.apellidopdf = (respuesta[0][1])
            self.edadpdf = (respuesta[0][2])
            self.direccionpdf = (respuesta[0][3])
            self.fechapdf = (respuesta[0][4])
            self.gestapdf = (respuesta[0][5])
            self.partopdf = (respuesta[0][6])
            self.motivopdf = (respuesta[0][7])
            self.presentapdf = (respuesta[0][8])
            self.diagnosticopdf = (respuesta[0][9])
            self.furpdf = (respuesta[0][10])
            self.telefonopdf = (respuesta[0][11])
            self.antemadrepdf = (respuesta[0][12])
            self.antepadrepdf = (respuesta[0][13])
            self.anteherpdf =(respuesta[0][14])
            self.antehijospdf = (respuesta[0][15])
            self.antepatopdf =(respuesta[0][16])
            self.antealergiapdf = (respuesta[0][17])
            self.antesangrepdf = (respuesta[0][18])
            self.anteqxpdf = (respuesta[0][19])
            self.antemenarpdf = (respuesta[0][20])
            self.antesexarpdf = (respuesta[0][21])
            self.anteciclopdf = (respuesta[0][22])
            self.anteparejapdf = (respuesta[0][23])
            self.chk_acopdf= (respuesta[0][24])
            self.chk_citologiapdf = (respuesta[0][25])
            self.chk_itspdf = (respuesta[0][26])
            self.chk_diupdf = (respuesta[0][27])
            self.anteembarazopdf = (respuesta[0][28])
            self.chk_deseadopdf = (respuesta[0][29])
            self.chk_planificadopdf = (respuesta[0][30])
            self.chk_controladopdf = (respuesta[0][31])
            self.chk_itupdf = (respuesta[0][32])
            self.controlespdf = (respuesta[0][33])
            self.laboratoriopdf = (respuesta[0][34])
            mb.showinfo("Atencion","Se Ha Generado un pdf de un paciente ")
        else:
            mb.showinfo("Información", "No existe un paciente registrado con ese numero de cedula")

        respuesta1 = self.genera1.generando(self.nombrepdf,self.apellidopdf,self.edadpdf,self.direccionpdf,datos1,self.fechapdf,self.gestapdf,self.partopdf,self.motivopdf,self.presentapdf,self.diagnosticopdf,self.furpdf,self.telefonopdf,self.antemadrepdf,self.antepadrepdf,self.anteherpdf,self.antehijospdf,self.antepatopdf,self.antealergiapdf,self.antesangrepdf,self.anteqxpdf,self.antemenarpdf,self.antesexarpdf,self.anteciclopdf,self.anteparejapdf,self.chk_acopdf,self.chk_citologiapdf,self.chk_itspdf,self.chk_diupdf,self.anteembarazopdf,self.chk_deseadopdf,self.chk_planificadopdf,self.chk_controladopdf,self.chk_itupdf,self.controlespdf,self.laboratoriopdf)

    def genera_pdf2(self):
        datos = (self.cedulapdf.get(), )
        datos1 = self.cedulapdf.get()
        respuesta=self.paciente1.consulta_consentimiento(datos)
        if len(respuesta)>0:
            self.nombrepdf = (respuesta[0][0])
            self.apellidopdf = (respuesta[0][1])
            self.fechapdf = (respuesta[0][2])
            self.diagnosticopdf = (respuesta[0][3])
            mb.showinfo("Atencion","Se Ha Generado un pdf de paciente con cedula %s" % self.cedulapdf)
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

        respuesta1 = self.genera1.generando_consentimiento(self.nombrepdf,self.apellidopdf,datos1,self.fechapdf,self.diagnosticopdf)
  
    def genera_pdf3(self):
        datos = (self.cedulapdf.get(), )
        datos1 = self.cedulapdf.get()
        respuesta=self.paciente1.consulta_nota_de_parto(datos)
        if len(respuesta)>0:
            self.nombrepdf = (respuesta[0][0])
            self.apellidopdf = (respuesta[0][1])
            self.fechapdf = (respuesta[0][2])
            self.nota_unopdf = (respuesta[0][3])
            self.nota_dospdf = (respuesta[0][4])
            self.nota_trespdf = (respuesta[0][5])
            self.nota_cuatropdf = (respuesta[0][6])
            self.nota_cincopdf = (respuesta[0][7])
            self.nota_seispdf = (respuesta[0][8])
            self.nota_sietepdf = (respuesta[0][9])
            self.nota_ochopdf = (respuesta[0][10])
            self.nota_diagnosticopdf = (respuesta[0][11])
            mb.showinfo("Atencion","Se Ha Generado un pdf de paciente con cedula %s" % self.cedulapdf)
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

        respuesta1 = self.genera1.generando_nota_de_parto(self.nombrepdf,self.apellidopdf,datos1,self.fechapdf,self.nota_unopdf,self.nota_dospdf,self.nota_trespdf,self.nota_cuatropdf,self.nota_cincopdf,self.nota_seispdf,self.nota_sietepdf,self.nota_ochopdf,self.nota_diagnosticopdf)
  
    def recibimiento_pdf(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Nota de Recibimiento")
        self.labelframe1=ttk.LabelFrame(self.pagina2, text="Generar Nota de Recibimiento")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Cedula:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cedula=tk.StringVar()
        self.entrycedula=ttk.Entry(self.labelframe1, textvariable=self.cedula)
        self.entrycedula.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Generar")
        self.boton1.grid(column=1, row=3, padx=4, pady=4)



aplicacion1=FormularioPaciente()