# importo pygames
import pygame

from pygame.locals import *
import Vector2D as v2



WIDTH = 1800
HEIGHT = 900
pygame.init()
SCREEN_SIZE = (WIDTH, HEIGHT)


class Ambiente():
    def __init__(self):
        self.agenti = {}
        self.id_agente = 0
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.colore_erba = (0, 255, 0)
        self.background.fill(self.colore_erba)
        self.lista_agenti_aggiunti = set()
        self.lista_agenti_rimossi = set()
        self.numero_volpi_nate = 0
        self.numero_conigli_nati = 0
        self.numero_conigli_morti_fame = 0
        self.numero_volpi_morti_fame = 0
        self.numero_conigli_morti_sete = 0
        self.numero_volpi_morti_sete = 0
        self.numero_conigli_morti_vecchiaia = 0
        self.numero_volpi_morti_vecchiaia = 0
        self.numero_conigli_morti_cacciati = 0
        self.stagione = "primavera"
        self.giorno = 0.0


    def aggiungi_agente(self, agente):
        self.agenti[self.id_agente] = agente
        agente.id = self.id_agente
        self.id_agente += 1
        agente.eta = 0

    def rimuovi_agente(self, agente):
        self.agenti[agente.id] = None
        del self.agenti[agente.id]

    def get(self, id_agente):
        if id_agente in self.agenti:
            return self.agenti[id_agente]
        else:
            return None

    def process(self, tempo_secondo):
        for agente in self.agenti.values():
            agente.process(tempo_secondo)

        for agente in self.lista_agenti_aggiunti:
            self.aggiungi_agente(agente)

        for agente in self.lista_agenti_rimossi:
            self.rimuovi_agente(agente)

        self.lista_agenti_aggiunti.clear()
        self.lista_agenti_rimossi.clear()

    def render(self, surface):
        self.background.fill(self.colore_erba)
        surface.blit(self.background, (0, 0))
        for agente in self.agenti.values():
            agente.render(surface)


    def agente_vicino(self, nome, coord, Range=100.):
        location = v2.Vector2D(coord.x, coord.y)
        potenziali = []
        min_dist = 100000
        target = None
        for agente in self.agenti.values():
            if agente.nome == nome:
                if agente.coord != coord:  # altrimenti considererebbe se stesso come agente più vicino
                    distanza = location.get_heading(agente.coord).get_magnitude()
                    if distanza < Range:
                        potenziali.append(agente)

        if potenziali != []:
           for a in potenziali:
               if location.get_heading(a.coord).get_magnitude() < min_dist:
                   min_dist = location.get_heading(a.coord).get_magnitude()
                   target = a

           return target
        else:
            return None
    

