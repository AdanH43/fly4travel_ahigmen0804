# -*- coding: utf-8 -*-
{
    'name': "Renting",  # Titulo del módulo
    'summary': "Modulo realizado por Ahigmen0804, SGE 23-24",  # Resumen de la funcionaliadad
    'description': """
    ==============
    """,  

    #Indicamos que es una aplicación
    'application': True,
    'author': "Adán Higueras Mendoza",
    'website': "http://apuntesfpinformatica.es",
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base'],

    'data': [

      
        #Estos dos primeros ficheros:
        #1) El primero indica grupo de seguridad basado en rol
        #2) El segundo indica la politica de acceso del modelo
        #Mas información en https://www.odoo.com/documentation/14.0/es/developer/howtos/rdtraining/05_securityintro.html
        #Y en www.odoo.yenthevg.com/creating-security-groups-odoo/
        'security/groups.xml',
        'security/ir.model.access.csv',
        #Aqui distintas vistas de equipo (vistas diferentes, mismo modelo)
        'views/renting.xml',
        #Vista a un informe
        'report/liga_equipo_clasificacion_report.xml',
        
        

        
    ],
    # Fichero con data de demo si se inicializa la base de datos con "demo data" (No incluido en ejemplo)
    # 'demo': [
    #     'demo.xml'
    # ],
}
