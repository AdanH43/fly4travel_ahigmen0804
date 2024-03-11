from odoo import models, fields, api
from datetime import datetime, timedelta

class Reservas(models.Model):

    _name = 'flights.reservas'
    _description = 'Reservas de vuelos'

    cliente_id = fields.Many2one('flights.clientes', string='Cliente', required=True)
    fecha_reserva = fields.Date('Fecha  de la reserva', required=True)
    asientos_reservados = fields.Integer('asientos de la reserva', default = 1)






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


    @api.constrains('fecha_reserva')
    def _check_fecha_inicio(self):
        for reserva in self:
            if reserva.fecha_reserva < fields.Date.today():
                raise ValidationError("La fecha de reserva debe ser hoy o un dia posterior.")