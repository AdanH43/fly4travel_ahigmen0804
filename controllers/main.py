# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
import json

#Clase del controlador web
class Main(http.Controller):
    #Decorador que indica que la url "/ligafutbol/equipo/json" atendera por HTTP, sin autentificacion
    #Devolvera texto que estará en formato JSON
    #Se puede probar accediendo a http://localhost:8069/ligafutbol/equipo/json
    @http.route('/ligafutbol/equipo/json', type='http', auth='none')
    def obtenerDatosEquiposJSON(self):
        #Obtenemos la referencia al modelo de Equipo
        equipos = request.env['liga.equipo'].sudo().search([])
        
        #Generamos una lista con informacion que queremos sacar en JSON
        listaDatosEquipos=[]
        for equipo in equipos:
             listaDatosEquipos.append([equipo.nombre,str(equipo.fecha_fundacion),equipo.jugados,equipo.puntos,equipo.victorias,equipo.empates,equipo.derrotas])
        #Convertimos la lista generada a JSON
        json_result=json.dumps(listaDatosEquipos)

        return json_result
    
    @http.route('/eliminarempates', type='http', auth='none')
    def eliminarempates(self):
        # Obtiene la referencia al modelo de Partido
        partidos = request.env['liga.partido'].sudo().search([])
        
        # Busca los partidos empatados
        partidos_empatados = []

        for juego in partidos:
            if juego.goles_fuera == juego.goles_casa:
                partidos_empatados.append(juego)

        for empatado in partidos_empatados:
            empatado.unlink()  
        

        # Elimina los partidos empatados
        num_partidos_eliminados = len(partidos_empatados)
        
        # Devuelve el número de partidos eliminados como respuesta HTTP
        return f'Número de partidos eliminados: {num_partidos_eliminados}'
