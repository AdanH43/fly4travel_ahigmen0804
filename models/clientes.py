# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Liga Equipo, que almacenara información de cada equipo
class Clientes(models.Model):

    #Nombre y descripcion del modelo
    _name = 'flights.clientes'

    _description = 'Clientes'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    
    #Campo con HTML (Sanitizado) donde se guarda la descripción del comic
    nombre = fields.Char('Nombre', required=True, index=True)
    apellidos = fields.Char('Apellidos', required=True, index=True)
    identificacion = fields.Char('Identificacion', required = True, index = True)

    #Constraints de SQL del modelo

    _sql_constraints = [
        ('name_uniq', 'UNIQUE (identificacion)', 'La identificacion debe ser unica')
    ]
  
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.apellidos} {record.identificacion}"
            result.append((record.id, name))
        return result
            