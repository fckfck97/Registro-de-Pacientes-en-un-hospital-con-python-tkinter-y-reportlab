# !/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from reportlab.lib.enums import TA_JUSTIFY,TA_CENTER,TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.styles import ParagraphStyle as PS
from reportlab.lib.colors import magenta,purple
from reportlab.lib import colors

class Genera():
    """docstring for Genera"""
    def generando(self,nombre,apellido,edad,direccion,cedula,fecha,gesta,parto,motivo,presenta,diagnostico,fur,telefono,madre,padre,hermanos,hijos,patologias,alergias,sangre,qx,menarquia,sexarquia,ciclo,parejas,aco,citologia,its,diu,anteembarazo,deseado,planificado,controlado,itu,controles,laboratorio):
        doc = SimpleDocTemplate("Paciente_CI:%s.pdf"%cedula, pagesize=letter)
        Story = []
        color = purple
        h1 = PS(name = 'Heading1',fontSize = 25,leading = 16,alignment=TA_CENTER,fontName="Times-Roman",textColor= magenta)
        h2 = PS(name = 'Heading1',fontSize = 14, leading = 14,fontName="Times-Roman",textColor= color)
        h3 = PS(name='parrafos_normales',fontSize=12,fontName="Times-Roman",alignment=TA_JUSTIFY)
        h4 = PS(name='parrafos_centrados',fontSize=12,fontName="Times-Roman",alignment=TA_CENTER)
        h5 = PS(name='parrafos_derechos',fontSize=12,fontName="Times-Roman",alignment=TA_RIGHT)
        
        texto = 'Hospital "Pablo Acosta Ortiz"'
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1, 0))
        texto =  "Servicio de Sala de Parto 5to Piso"
        Story.append(Paragraph(texto, h5))
        texto = '%s' % fecha
        Story.append(Paragraph(texto,h5))
        logotipo = "imagenes/logo1.png"    
        imagen = Image(logotipo, 2 * inch, 1 * inch, hAlign='LEFT')    
        Story.append(imagen)


        texto = 'Historia Clinica'

        Story.append(Paragraph(texto, h1))
        Story.append(Spacer(1, 12))

        
        """texto = '%s' % direccion
        Story.append(Paragraph(texto, estiloN))
        Story.append(Spacer(1, 12))
        # Se construye la dirección
        texto = '%s'% nombre
        Story.append(Paragraph(texto, estiloN))"""
        
        texto = 'Motivo de Consulta:'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 7))
        texto = '%s' % motivo
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 7))


        
        texto = 'Paciente:  %s %s \
                Cedula: %s \
                Telefono: %s ' % (nombre,apellido,cedula,telefono) 
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 7))
        
       
        texto = u'Enfermedad actual se trata de una gestante de %s años, natural y procedente:  %s \
                con FUR: %s , %s gestas, %s partos quien acude a consulta por presentar %s motivo por el \
                cual se evalua y se decide su ingreso.'%(edad,direccion,fur,gesta,parto,presenta)
        
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 7))

        texto = 'Diagnostico: '
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 7))
        texto = '%s' % diagnostico
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))

        texto = 'Antecedentes Familiares.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 7))
        t = Table([
        ['1.-Madre:'+madre+'.', '2.-Padre:'+padre+'.', '3.-Hermanos:'+hermanos+'.'],
        ['4.-Hijos:'+hijos+'.']], hAlign='LEFT')
        t.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('TEXTFONT', (0, 0), (-1, -1), 'Times-Roman'),])
        Story.append(t)
        Story.append(Spacer(0,7))
        
        texto = 'Antecedentes Personales.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 7))
        t = Table([
        ['1.-Patologia Base:'+patologias+'.', '2.-Alergias a Medicamentos:'+alergias+'.'],
        ['3.-Transfuciones Sanguineas:'+sangre+'.','4-Intervenciones Quirurgicas:'+qx+'.']], hAlign='LEFT')
        t.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('TEXTFONT', (0, 0), (-1, -1), 'Times-Roman'),])
        Story.append(t)
        Story.append(Spacer(0,7))
        texto = 'Antecedentes Gineco-Obstetricos.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 7))
        t = Table([
        [u'1.-Menarquia:'+menarquia+' anios.','2.-Sexarquia:'+sexarquia+'anios.','3.-FUR:'+fur+'.','4.-Ciclo Menstrual:'+ciclo+'.'],
        [u'5.-Numero de parejas:'+parejas+'.','6.-Aco:'+aco+'.','7.-Citologia:'+citologia+'.','8.-Its:'+its+'.']], hAlign='LEFT')
        t.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('TEXTFONT', (0, 0), (-1, -1), 'Times-Roman'),])
        Story.append(t)
        Story.append(Spacer(0,7))
        texto = 'Embarazo Anterior.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1,7))
        texto = '%s' % anteembarazo
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))  
        texto = 'Embarazo Actual.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1,7))
        t = Table([
        [u'1.-Deseado:'+deseado+'.','2.-Planificado:'+planificado+'.','3.-Itu:'+itu+'.','4.-Numero de Controles:'+controles+'.']], hAlign='LEFT')
        t.setStyle([('ALIGN', (0, 0), (-1, -1), 'LEFT'),
                    ('FONTSIZE', (0, 0), (-1, -1), 11),
                    ('TEXTFONT', (0, 0), (-1, -1), 'Times-Roman'),])
        Story.append(t)
        Story.append(Spacer(0,7))
        texto = 'Laboratorio:'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1,7))
        texto = '%s.' % laboratorio
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))
        texto = 'Dr(a). Firma y Sello'
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1,7))
        doc.build(Story)

    def generando_consentimiento(self,nombre,apellido,cedula,fecha,diagnostico):
        doc = SimpleDocTemplate("Paciente_CI:%s_consentimiento.pdf"%cedula, pagesize=letter)
        Story = []
        color = purple
        h1 = PS(name = 'Heading1',fontSize = 25,leading = 16,alignment=TA_CENTER,fontName="Times-Roman",textColor=color)
        h2 = PS(name = 'Heading1',fontSize = 14, leading = 14,fontName="Times-Roman",textColor=magenta)
        h3 = PS(name='parrafos_normales',fontSize=12,fontName="Times-Roman",alignment=TA_JUSTIFY)
        h4 = PS(name='parrafos_centrados',fontSize=12,fontName="Times-Roman",alignment=TA_CENTER)
        h5 = PS(name='parrafos_derechos',fontSize=12,fontName="Times-Roman",alignment=TA_RIGHT)
        
        texto = 'Hospital "Pablo Acosta Ortiz"'
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1, 0))
        texto =  "Servicio de Sala de Parto 5to Piso"
        Story.append(Paragraph(texto, h5))
        texto = '%s' % fecha
        Story.append(Paragraph(texto,h5))
        logotipo = "imagenes/logo1.png"    
        imagen = Image(logotipo, 2 * inch, 1 * inch, hAlign='LEFT')    
        Story.append(imagen)


        texto = 'Consentimiento Informado'
        Story.append(Paragraph(texto, h1))
        Story.append(Spacer(1, 15))
        
        texto = u'Dando Cumplimiento al articulo N# 34 de la ley \
                del ejercicio de la medicina yo : %s %s , Titular de la CI: %s . '%(nombre,apellido,cedula)
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'Habiendo sido informada de forma, clara y oportuna y suficiente \
                de las condiciones que presento y habiendo entendido los riesgos y beneficios \
                potenciales, autorizo al personal medico y de enfermeria que prestan sus servicios\
                en el Hospital Pablo Acosta Ortiz a realizar todos los actos que consideren necesarios\
                para la antencion del mismo incluyendo la administracion de medicamentos y cirugias, asi como tambien \
                el acto anestesico en caso de ser necesario '
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = 'Diagnostico.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 12))

        texto = '%s' % diagnostico
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

       
        texto = 'Paciente: %s %s' % (nombre,apellido)
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))
        texto = 'Cedula: %s' % cedula
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))
        texto = 'Firma.' 
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))

        texto = 'Familiar:'
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))
        texto = 'CI:' 
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))
        texto = 'Firma.' 
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1,7))

        doc.build(Story)
    def generando_nota_de_parto(self,nombre,apellido,cedula,fecha,nota_uno,nota_dos,nota_tres,nota_cuatro,nota_cinco,nota_seis,nota_siete,nota_ocho,nota_diagnostico):
        doc = SimpleDocTemplate("Paciente_CI:%s_notadeparto.pdf"%cedula, pagesize=letter)
        Story = []
        color = purple
        h1 = PS(name = 'Heading1',fontSize = 25,leading = 16,alignment=TA_CENTER,fontName="Times-Roman",textColor=color)
        h2 = PS(name = 'Heading1',fontSize = 14, leading = 14,fontName="Times-Roman",textColor=magenta)
        h3 = PS(name='parrafos_normales',fontSize=12,fontName="Times-Roman",alignment=TA_JUSTIFY)
        h4 = PS(name='parrafos_centrados',fontSize=12,fontName="Times-Roman",alignment=TA_CENTER)
        h5 = PS(name='parrafos_derechos',fontSize=12,fontName="Times-Roman",alignment=TA_RIGHT)
        
        texto = 'Hospital "Pablo Acosta Ortiz"'
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1, 0))
        texto =  "Servicio de Sala de Parto 5to Piso"
        Story.append(Paragraph(texto, h5))
        texto = '%s' % fecha
        Story.append(Paragraph(texto,h5))
        logotipo = "imagenes/logo1.png"    
        imagen = Image(logotipo, 2 * inch, 1 * inch, hAlign='LEFT')    
        Story.append(imagen)


        texto = 'Nota de Parto.'
        Story.append(Paragraph(texto, h1))
        Story.append(Spacer(1, 15))

        texto = 'Paciente:  %s %s \
                Cedula: %s ' % (nombre,apellido,cedula) 
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))
        
        texto = u'1.- %s .'% nota_uno
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'2.- %s .'% nota_dos
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'3.- %s .'% nota_tres
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'4.- %s .'% nota_cuatro
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'5.- %s .'% nota_cinco
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'6.- %s .'% nota_seis
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'7.- %s .'% nota_siete
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = u'8.- %s .'% nota_ocho
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = 'Diagnostico.'
        Story.append(Paragraph(texto, h2))
        Story.append(Spacer(1, 12))

        texto = '%s' % nota_diagnostico
        Story.append(Paragraph(texto, h3))
        Story.append(Spacer(1, 12))

        texto = 'Dr(a):'
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1,7))
        texto = '' 
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1,7))
        texto = 'Firma y Sello.' 
        Story.append(Paragraph(texto, h5))
        Story.append(Spacer(1,7))

        doc.build(Story)



aplicacion1 = Genera()