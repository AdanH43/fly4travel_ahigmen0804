# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError



#Definimos modelo Liga Equipo, que almacenara información de cada equipo
class RentingVehiculos(models.Model):

    #Nombre y descripcion del modelo
    _name = 'renting.vehiculos'

    _description = 'Vehiculos'

    #Parametros de ordenacion por defecto
    _order = 'marca'

    #ATRIBUTOS

    #PARA CUANDO NO HAY UN ATRIBUTO LLAMADO NAME PARA MOSTRAR NOMBRE DE UN REGISTRO
    # https://www.odoo.com/es_ES/forum/ayuda-1/how-defined-display-name-in-custom-many2one-91657
    

    #Dato binario, para guardar un binario (en la vista indicaremos que es una imagen) con la portada del comic
    foto = fields.Image('Foto del vehiculo',max_width=50,max_height=50)
    #Campo con HTML (Sanitizado) donde se guarda la descripción del comic
    marca = fields.Char('Marca del vehiculo', requires=True, index=True)
    matricula = fields.Char('Matricula del vehiculo', requires=True, index=True)
    estado = fields.Selection([
        ('averiado', 'Averiado'),
        ('alquilado', 'Alquilado'),
        ('disponible', 'Disponible'),
        ('robado', 'Robado'),
    ], string='Estado del vehiculo', required=True, index=True)
    
    alquileres_ids = fields.One2many('renting.reservas', 'vehiculo_id', string='Alquileres')
    

    #Constraints de SQL del modelo
    __sql_constraints = [ 
    ('estado_check', 'CHECK (estado IN (\'averiado\', \'alquilado\', \'disponible\', \'robado\'))', 'El estado del vehículo debe ser uno de: averiado, alquilado, disponible o robado.')
]
    
    def name_get(self):
        result = []
        for record in self:
            name = f"{record.marca} {record.matricula}"
            result.append((record.id, name))
        return result
            