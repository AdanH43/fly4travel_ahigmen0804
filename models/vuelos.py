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
    numero_asientos = fields.Integer(default= 1)
    asientos_disponibles = fields.Integer(compute='_compute_asientos_disponibles', store=True)


    _sql_constraints = [
        ('name_uniq', 'UNIQUE (nombre)', 'El nombre debe ser unica')
    ]

    @api.depends('numero_asientos', 'reservas.asientos_reservados')
    def _compute_asientos_disponibles(self):
        for vuelo in self:
            asientos_reservados = sum(reserva.asientos_reservados for reserva in vuelo.reservas)
            vuelo.asientos_disponibles = vuelo.numero_asientos - asientos_reservados

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
    

    




    
   