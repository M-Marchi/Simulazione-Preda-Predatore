# importo pygames
import pygame

from pygame.locals import *
import Vector2D as v2


# valori di inizializzazione grafica della simulazione
WIDTH = 1200
HEIGHT = 800
pygame.init()
SCREEN_SIZE = (WIDTH, HEIGHT)

# classe Ambiente
class Ambiente():
    def __init__(self):
        self.agenti = {}    # Lista degli agenti
        self.id_agente = 0  # ID incrementale per identificare ogni agente
        self.background = pygame.surface.Surface(SCREEN_SIZE).convert()
        self.colore_erba = (0, 175, 0)
        self.background.fill(self.colore_erba)
        self.lista_agenti_aggiunti = set()      # lista agenti da aggiungere all'ambiente
        self.lista_agenti_rimossi = set()       # lista agenti da rimuovere dall'ambiente
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


    # funzione che aggiunge agente all'ambiente e incrementa ID
    def aggiungi_agente(self, agente):
        self.agenti[self.id_agente] = agente
        agente.id = self.id_agente
        self.id_agente += 1
        agente.eta = 0

    # funzione che rimuove agente dall'ambiente
    def rimuovi_agente(self, agente):
        self.agenti[agente.id] = None
        del self.agenti[agente.id]

    # funzione per ottenere agente tramite ID
    def get(self, id_agente):
        if id_agente in self.agenti:
            return self.agenti[id_agente]
        else:
            return None

    # funzione per processare l'ambiente: ogni agente viene processato
    def process(self, tempo_secondo):
        for agente in self.agenti.values():
            agente.process(tempo_secondo)

        for agente in self.lista_agenti_aggiunti:
            self.aggiungi_agente(agente)

        for agente in self.lista_agenti_rimossi:
            self.rimuovi_agente(agente)

        self.lista_agenti_aggiunti.clear()
        self.lista_agenti_rimossi.clear()

    # si effettua il render del terreno e di ogni agente
    def render(self, surface):
        self.background.fill(self.colore_erba)
        surface.blit(self.background, (0, 0))
        for agente in self.agenti.values():
            agente.render(surface)


    # funzione per trovare un agente vicino nel raggio della percezione
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
    

