# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Vuelos(models.Model):
    #Nombre y descripcion del modelo
    _name = 'flights.vuelos'
    _description = 'Lista de vuelos'


    #Atributos del modelo
    nombre = fields.Char('Nombre del vuelo', required=True, index=True)
    fecha_inicio = fields.Date('Fecha del vuelo', required=True)
    duracion = fields.Char('Duracion', required = True, index = True)
    numero_asientos = fields.Integer('Numero de asientos', required= True, default= 1)
    asientos_disponibles = fields.Integer('Numero de asientos disponibles', default = numero_asientos)


    @api.constrains('fecha_inicio')
    def _check_fecha_inicio(self):
        for reserva in self:
            if reserva.fecha_inicio < fields.Date.today():
                raise ValidationError("La fecha de inicio debe ser hoy o un dia posterior.")


    def name_get(self):
        result = []
        for record in self:
            name = f"{record.nombre} {record.fecha_inicio}"
            result.append((record.id, name))
        return result
    

    




    
   