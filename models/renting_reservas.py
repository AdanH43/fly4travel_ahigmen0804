from odoo import models, fields, api
from datetime import datetime, timedelta

class RentingReservas(models.Model):

    _name = 'renting.reservas'
    _description = 'Reservas de vehículos'

    cliente_id = fields.Many2one('renting.clientes', string='Cliente', required=True)
    vehiculo_id = fields.Many2one('renting.vehiculos', string='Vehículo', required=True)
    fecha_inicio = fields.Date('Fecha de inicio', required=True)

    @api.model
    def create(self, vals):
        # Cambiar el estado del vehículo a alquilado al crear una reserva
        reserva = super(RentingReservas, self).create(vals)
        reserva.vehiculo_id.write({'estado': 'alquilado'})
        return reserva

    def unlink(self):
        # Cambiar el estado del vehículo a disponible al eliminar una reserva
        for reserva in self:
            reserva.vehiculo_id.write({'estado': 'disponible'})
        return super(RentingReservas, self).unlink()


    @api.constrains('fecha_inicio')
    def _check_fecha_inicio(self):
        today = fields.Date.today()
        for reserva in self:
            if reserva.fecha_inicio < today:
                raise ValidationError("La fecha de inicio debe ser hoy o un dia posterior.")