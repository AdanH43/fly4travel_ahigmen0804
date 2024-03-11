# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class LigaPartido(models.Model):
    #Nombre y descripcion del modelo
    _name = 'renting.clientes'
    _description = 'Lista de Clientes'


    #Atributos del modelo
    nombre = fields.Char('Nombre', required=True, index=True)
    apellidos = fields.Char('Apellidos', required=True, index=True)

    vehiculos_alquilados_ids = fields.Many2many('renting.vehiculos', string='Vehículos Alquilados')

    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nombre} {record.apellidos}"
            result.append((record.id, name))
        return result
    




    
   