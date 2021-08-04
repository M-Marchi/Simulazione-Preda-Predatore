import pygame
from pygame.locals import *
from sys import exit
import random
import pandas as pd


import Ambiente as a
import Vector2D as v2
import plot as pl

# inizializzazione pygame
pygame.init()

# impostazione seed, default: 0.0
seed = 0.0

if seed == 0.0:
    seed = random.random()

random.seed(seed)

# Settings simulazione:

GRAFICA = True
REINSERIMENTO = True
EVOLUZIONE = True


NUMERO_CONIGLI = 75               # default: 75
NUMERO_VOLPI = 25                 # default: 25
NUMERO_POZZANGHERE = 200          # default: 200
NUMERO_CAROTE = 250               # default: 250


# default: 0.0005 crescita contenuta - 0.002 crescita abbondante
PROBABILITA_CRESCITA_CAROTE = 0.0005


QUANTITA_ACQUA = 3                 # default: 3


# parametri finestra
WIDTH = 1200
HEIGHT = 800
SCREEN_SIZE = (WIDTH, HEIGHT)
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
pygame.display.set_caption("Simulazione Ecosistema")
font = pygame.font.SysFont("Arial", 18)

# inizializzazione ambiente
ambiente = a.Ambiente()

# inizializzazione immagini animali
img_volpe = pygame.image.load('images/fox.png').convert_alpha()
img_coniglio = pygame.image.load('images/rabbit.png').convert_alpha()

# inizializzazione clock
clock = pygame.time.Clock()


# inizializzazione riquadro statistiche real time
stats = pygame.Surface((WIDTH // 4, HEIGHT // 4))
stats.fill((215, 215, 215))
stats.set_alpha(210)
stats_pos = ((WIDTH // 40) + 450, (HEIGHT // 40) - 20)


# inizializzazione dizionario informazioni
data = {
    'evoluzione': [],
    'reinserimento': [],
    'probabilita_riproduzione_carote': [],
    'quantita_acqua_pozzanghera':[],
    'tempo': [],
    'stagione': [],
    'num_volpi': [],
    'num_conigli': [],
    'num_carota': [],
    'num_pozzanghera': [],
    'numero_volpi_nate': [],
    'numero_conigli_nati': [],
    'numero_conigli_morti_fame': [],
    'numero_volpi_morti_fame': [],
    'numero_conigli_morti_sete': [],
    'numero_volpi_morti_sete': [],
    'numero_conigli_morti_vecchiaia': [],
    'numero_volpi_morti_vecchiaia': [],
    'numero_conigli_cacciati': [],
    'eta_media_conigli': [],
    'eta_media_volpi': [],
    'percezione_media_conigli': [],
    'percezione_media_volpi': [],
    'velocita_camminata_media_conigli': [],
    'velocita_camminata_media_volpi': [],
    'velocita_corsa_media_conigli': [],
    'velocita_corsa_media_volpi': [],
    'soglia_fame_media_conigli': [],
    'soglia_fame_media_volpi': [],
    'soglia_sete_media_conigli': [],
    'soglia_sete_media_volpi': [],
    'soglia_fertilita_media_conigli': [],
    'soglia_fertilita_media_volpi': [],
    'soglia_morte_di_fame_media_conigli': [],
    'soglia_morte_di_fame_media_volpi': [],
    'soglia_morte_di_sete_media_conigli': [],
    'soglia_morte_di_sete_media_volpi': [],
    'media_fame_conigli': [],
    'media_fame_volpi': [],
    'media_sete_conigli': [],
    'media_sete_volpi': [],
    'media_fertilita_conigli': [],
    'media_fertilita_volpi': []

}


# classe Animale
class Animale():
    def __init__(self, ambiente, nome, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 eta=0.0,
                 soglia_fame=0,
                 soglia_morte_di_fame=0,
                 soglia_sete=0,
                 soglia_morte_di_sete=0,
                 soglia_fertilita=0,
                 percezione=0,
                 velocita_camminata=0,
                 velocita_corsa=0):

        self.ambiente = ambiente
        self.nome = nome
        self.coord = coord
        self.coord_int = self.coord.int_()
        self.destinazione = destinazione
        self.vel = v2.Vector2D(0, 0)
        self.fame = False
        self.sete = False
        self.fertilita = False
        self.gravidanza = False
        self.preda = None
        self.pozzanghera = None
        self.compagno = None
        self.preda_nome = None
        self.tempo_digiuno = 150
        self.tempo_disidratazione = 0
        self.tempo_periodo_fertile = 0
        self.tempo_gestazione = 0
        self.color = None

        self.soglia_fame = soglia_fame
        self.soglia_morte_di_fame = soglia_morte_di_fame
        self.soglia_sete = soglia_sete
        self.soglia_morte_di_sete = soglia_morte_di_sete
        self.soglia_fertilita = soglia_fertilita
        self.percezione = percezione
        self.velocita_camminata = velocita_camminata
        self.velocita_corsa = velocita_corsa

        self.pixels_per_second = self.velocita_camminata

        self.img = None


    # cerca compagno fertile nel raggio percezione
    def cerca_compagno(self):
        if self.compagno is None or self.compagno.id not in self.ambiente.agenti:
            if self.eta > 4:  # gli animali vecchi hanno una percezione più debole
                self.compagno = self.ambiente.agente_vicino(self.nome, self.coord, self.percezione * 0.5)
            else:
                self.compagno = self.ambiente.agente_vicino(self.nome, self.coord, self.percezione)

        if self.compagno is None:
            if self.destinazione == None:
                self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                return None
            else:
                return None

        else:
            if self.compagno.eta < 0.5:
                self.compagno = None
                if self.destinazione == None:
                    self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                    return None
                else:
                    return None
            else:
                self.destinazione = self.compagno.coord
                self.pixels_per_second = self.velocita_corsa
                distanza_compagno = self.coord.get_distance_from_point(self.compagno.coord)
                if distanza_compagno < 5:
                    self.accoppiamento()


    # l'accomppiamento porta a gravidanza dell'animale
    def accoppiamento(self):
        self.fertilita = False
        self.tempo_periodo_fertile = 0
        self.gravidanza = True
        self.compagno.fertilita = False
        self.compagno.tempo_periodo_fertile = 0
        self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))


    # nascita del cucciolo di animale, se EVOLUZIONE == True si aggiunge offset
    def nascita(self):
        
        if EVOLUZIONE:
            if self.nome == "volpe":
                if self.tempo_gestazione >= random.randint(30, 40):
                    for i in range(random.randint(3, 5)):  # le volpi partoriscono dai 3 ai 5 cuccioli
                        self.ambiente.lista_agenti_aggiunti.add(
                            self.__class__(self.ambiente, coord=self.coord, eta=0.0,
                                           destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                           soglia_fame=random.randint((min(self.soglia_fame, self.compagno.soglia_fame)),
                                                                      (max(self.soglia_fame, self.compagno.soglia_fame)))+ random.randint(-20, 20),
                                           soglia_morte_di_fame=random.randint((min(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame)),
                                                                                (max(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame)))+ random.randint(-100, 100),
                                           soglia_sete=random.randint((min(self.soglia_sete, self.compagno.soglia_sete)),
                                                                               (max(self.soglia_sete, self.compagno.soglia_sete)))+ random.randint(-20, 20),
                                           soglia_morte_di_sete=random.randint((min(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete)),
                                                                               (max(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete)))+ random.randint(-100, 100),
                                           soglia_fertilita=random.randint((min(self.soglia_fertilita, self.compagno.soglia_fertilita)),
                                                                           (max(self.soglia_fertilita, self.compagno.soglia_fertilita)))+ random.randint(-50, 50),
                                           percezione=random.randint((min(self.percezione, self.compagno.percezione)),
                                                                     (max(self.percezione, self.compagno.percezione)))+ random.randint(-10, 10),
                                           velocita_camminata=max((random.randint((min(self.velocita_camminata, self.compagno.velocita_camminata)),
                                                                             (max(self.velocita_camminata, self.compagno.velocita_camminata)))+ random.randint(-20, 20)), 0),
                                           velocita_corsa=max((random.randint((min(self.velocita_corsa, self.compagno.velocita_corsa)),
                                                                         (max(self.velocita_corsa, self.compagno.velocita_corsa)))+ random.randint(-20, 20)), 0)))
                        self.gravidanza = False  # non è più in gravidanza dopo aver dato alla luce i cuccioli
                        self.ambiente.numero_volpi_nate += 1
                    self.compagno = None
    
    
            if self.nome == "coniglio":
                if self.tempo_gestazione >= random.randint(28, 35):
                    for i in range(random.randint(3, 14)):  # i conigli hanno dai 3 ai 14 cuccioli ad ogni parto
                        self.ambiente.lista_agenti_aggiunti.add(
                            self.__class__(self.ambiente, coord=self.coord, eta=0.0,
                                           destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                           soglia_fame=random.randint((min(self.soglia_fame, self.compagno.soglia_fame)),
                                                                      (max(self.soglia_fame, self.compagno.soglia_fame))) + random.randint(-20, 20),
                                           soglia_morte_di_fame=random.randint((min(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame)),
                                                                               (max(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame))) + random.randint(-100, 100),
                                           soglia_sete=random.randint((min(self.soglia_sete, self.compagno.soglia_sete)),
                                                                               (max(self.soglia_sete, self.compagno.soglia_sete))) + random.randint(-20, 20),
                                           soglia_morte_di_sete=random.randint((min(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete)),
                                                                               (max(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete))) + random.randint(-100, 100),
                                           soglia_fertilita=random.randint((min(self.soglia_fertilita, self.compagno.soglia_fertilita)),
                                                                           (max(self.soglia_fertilita, self.compagno.soglia_fertilita))) + random.randint(-50, 50),
                                           percezione=random.randint((min(self.percezione, self.compagno.percezione)),
                                                                     (max(self.percezione, self.compagno.percezione))) + random.randint(-10, 10),
                                           velocita_camminata=max((random.randint((min(self.velocita_camminata, self.compagno.velocita_camminata)),
                                                                             (max(self.velocita_camminata, self.compagno.velocita_camminata))) + random.randint(-20, 20)), 0),
                                           velocita_corsa=max((random.randint((min(self.velocita_corsa, self.compagno.velocita_corsa)),
                                                                         (max(self.velocita_corsa, self.compagno.velocita_corsa))) + random.randint(-20, 20)), 0)))
                        self.gravidanza = False  # non è più in gravidanza dopo aver dato alla luce i cuccioli
                        self.ambiente.numero_conigli_nati += 1
                    self.compagno = None
        
        else:
            if self.nome == "volpe":
                if self.tempo_gestazione >= random.randint(30, 40):
                    for i in range(random.randint(3, 5)):  # le volpi partoriscono dai 3 ai 5 cuccioli
                        self.ambiente.lista_agenti_aggiunti.add(
                            self.__class__(self.ambiente, coord=self.coord, eta=0.0,
                                           destinazione=v2.Vector2D(random.randint(0, WIDTH),
                                                                    random.randint(0, HEIGHT)),
                                           soglia_fame=random.randint(
                                               (min(self.soglia_fame, self.compagno.soglia_fame)),
                                               (max(self.soglia_fame, self.compagno.soglia_fame))),
                                           soglia_morte_di_fame=random.randint(
                                               (min(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame)),
                                               (max(self.soglia_morte_di_fame,
                                                    self.compagno.soglia_morte_di_fame))),
                                           soglia_sete=random.randint(
                                               (min(self.soglia_sete, self.compagno.soglia_sete)),
                                               (max(self.soglia_sete, self.compagno.soglia_sete))),
                                           soglia_morte_di_sete=random.randint(
                                               (min(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete)),
                                               (max(self.soglia_morte_di_sete,
                                                    self.compagno.soglia_morte_di_sete))),
                                           soglia_fertilita=random.randint(
                                               (min(self.soglia_fertilita, self.compagno.soglia_fertilita)),
                                               (max(self.soglia_fertilita,
                                                    self.compagno.soglia_fertilita))),
                                           percezione=random.randint((min(self.percezione, self.compagno.percezione)),
                                                                     (max(self.percezione,
                                                                          self.compagno.percezione))),
                                           velocita_camminata=random.randint(
                                               (min(self.velocita_camminata, self.compagno.velocita_camminata)),
                                               (max(self.velocita_camminata,
                                                    self.compagno.velocita_camminata))),
                                           velocita_corsa=random.randint((min(self.velocita_corsa, self.compagno.velocita_corsa)),
                                                               (max(self.velocita_corsa,
                                                                    self.compagno.velocita_corsa)))))
                        self.gravidanza = False  # non è più in gravidanza dopo aver dato alla luce i cuccioli
                        self.ambiente.numero_volpi_nate += 1
                    self.compagno = None

            if self.nome == "coniglio":
                if self.tempo_gestazione >= random.randint(28, 35):
                    for i in range(random.randint(3, 14)):  # i conigli hanno dai 3 ai 14 cuccioli ad ogni parto
                        self.ambiente.lista_agenti_aggiunti.add(
                            self.__class__(self.ambiente, coord=self.coord, eta=0.0,
                                           destinazione=v2.Vector2D(random.randint(0, WIDTH),
                                                                    random.randint(0, HEIGHT)),
                                           soglia_fame=random.randint(
                                               (min(self.soglia_fame, self.compagno.soglia_fame)),
                                               (max(self.soglia_fame, self.compagno.soglia_fame))),
                                           soglia_morte_di_fame=random.randint(
                                               (min(self.soglia_morte_di_fame, self.compagno.soglia_morte_di_fame)),
                                               (max(self.soglia_morte_di_fame,
                                                    self.compagno.soglia_morte_di_fame))),
                                           soglia_sete=random.randint(
                                               (min(self.soglia_sete, self.compagno.soglia_sete)),
                                               (max(self.soglia_sete, self.compagno.soglia_sete))),
                                           soglia_morte_di_sete=random.randint(
                                               (min(self.soglia_morte_di_sete, self.compagno.soglia_morte_di_sete)),
                                               (max(self.soglia_morte_di_sete,
                                                    self.compagno.soglia_morte_di_sete))),
                                           soglia_fertilita=random.randint(
                                               (min(self.soglia_fertilita, self.compagno.soglia_fertilita)),
                                               (max(self.soglia_fertilita,
                                                    self.compagno.soglia_fertilita))),
                                           percezione=random.randint((min(self.percezione, self.compagno.percezione)),
                                                                     (max(self.percezione,
                                                                          self.compagno.percezione))),
                                           velocita_camminata=random.randint(
                                               (min(self.velocita_camminata, self.compagno.velocita_camminata)),
                                               (max(self.velocita_camminata,
                                                    self.compagno.velocita_camminata))),
                                           velocita_corsa=random.randint((min(self.velocita_corsa, self.compagno.velocita_corsa)),
                                                               (max(self.velocita_corsa,
                                                                    self.compagno.velocita_corsa)))))

                        self.gravidanza = False  # non è più in gravidanza dopo aver dato alla luce i cuccioli
                        self.ambiente.numero_conigli_nati += 1
                    self.compagno = None
        




    # valutazione bisogni agente
    def bisogni_primari(self):
        if self.tempo_digiuno > self.soglia_morte_di_fame:
            self.morte()
            if self.nome == "coniglio":
                ambiente.numero_conigli_morti_fame += 1
            else:
                ambiente.numero_volpi_morti_fame += 1

        if self.tempo_disidratazione > self.soglia_morte_di_sete:
            self.morte()
            if self.nome == "coniglio":
                ambiente.numero_conigli_morti_sete += 1
            else:
                ambiente.numero_volpi_morti_sete += 1


        if self.tempo_digiuno > self.soglia_fame:
            self.fame = True
        if self.tempo_disidratazione > self.soglia_sete:
            self.sete = True
        if self.tempo_periodo_fertile > self.soglia_fertilita and self.eta > 0.5:
            self.fertilita = True




    # ricerca acqua
    def dissetarsi(self):
        if self.pozzanghera == None or self.pozzanghera.id not in self.ambiente.agenti:

            if self.eta < 0.5 or self.eta > 4:
                self.pozzanghera = self.ambiente.agente_vicino("acqua", self.coord, self.percezione * 0.5)
            else:
                self.pozzanghera = self.ambiente.agente_vicino("acqua", self.coord, self.percezione)

        if self.pozzanghera == None:
            if self.destinazione == None:
                self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                return None
            else:
                return None
        else:
            self.destinazione = self.pozzanghera.coord
            if self.eta < 0.5 or self.eta > 4:
                self.pixels_per_second = self.velocita_corsa * 0.5
            else:
                self.pixels_per_second = self.velocita_corsa

            distance_to_pozzanghera = self.coord.get_distance_from_point(self.pozzanghera.coord)
            if distance_to_pozzanghera < 5:
                self.sete = False
                self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                self.tempo_disidratazione = 0
                self.pozzanghera.quantita -= 1
                if (self.pozzanghera.quantita == 0):
                    self.pozzanghera.esaurita()

                self.pozzanghera = None

    # ricerca cibo
    def caccia(self):

        if self.preda is None or self.preda.id not in self.ambiente.agenti:

            if self.eta < 0.5 or self.eta > 4:
                self.preda = self.ambiente.agente_vicino(self.preda_nome, self.coord, self.percezione * 0.5)
            else:
                self.preda = self.ambiente.agente_vicino(self.preda_nome, self.coord, self.percezione)

        if self.preda is None:
            if self.destinazione == None:
                self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
                return None
            else:
                return None

        else:
            self.destinazione = self.preda.coord
            if self.eta < 0.5 or self.eta > 4:
                self.pixels_per_second = self.velocita_corsa * 0.5
            else:
                self.pixels_per_second = self.velocita_corsa

            distance_to_preda = self.coord.get_distance_from_point(self.preda.coord)
            if distance_to_preda < 5:
                self.fame = False
                self.tempo_digiuno = 0
                self.preda.morte()
                if self.preda_nome == "coniglio":
                    ambiente.numero_conigli_morti_cacciati += 1
                self.preda = None
                self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))

    # rimozione agente da ambiente
    def morte(self):
        self.ambiente.lista_agenti_rimossi.add(self)

    # se non si hanno destinazioni l'agente cammina
    def cammina(self):

        if self.eta < 0.5 or self.eta > 4:  # se sono cuccioli o vecchi allora hanno una velocità minore
            self.pixels_per_second = self.velocita_camminata * 0.5
        else:
            self.pixels_per_second = self.velocita_camminata

        if self.destinazione == None:
            self.destinazione = v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        else:
            return None

    # funzione per effettuare movimento
    # si usa il tempo per calcolare lo spostamento in base ai pixel che percorre al secondo
    def movimento(self, tempo_passato_secondi):
        distance_to_destinazione = self.coord.get_distance_from_point(self.destinazione)
        if distance_to_destinazione < 5:
            self.destinazione = None
            return None

        heading = self.coord.get_heading(self.destinazione)
        heading.normalize()
        distance = self.pixels_per_second * tempo_passato_secondi

        self.coord += heading * distance
        self.coord_int = self.coord.int_()

    # processamento degli agenti animali nel tempo
    def process(self, tempo_passato_secondi):
        self.tempo_digiuno += 1
        self.tempo_disidratazione += 1
        self.eta += 0.003

        if self.eta > 0.5:
            self.tempo_periodo_fertile += 1

        if self.nome == "coniglio":
            if self.eta > 4.5:
                self.morte()
                ambiente.numero_conigli_morti_vecchiaia += 1
                # print("coniglio morto di vecchiaia")
        else:
            if self.eta > 5:
                self.morte()
                ambiente.numero_volpi_morti_vecchiaia += 1
                # print("volpe morta di vecchiaia")

        self.bisogni_primari()

        if self.fame and self.tempo_digiuno >= self.tempo_disidratazione:
            self.caccia()
        elif self.sete:
            self.dissetarsi()
        elif self.fertilita:
            self.cerca_compagno()
        elif self.gravidanza:
            self.tempo_gestazione += 1  # aumenta il tempo dall'inizio della gestazione
            self.nascita()
            self.cammina()
        else:
            self.cammina()

        self.movimento(tempo_passato_secondi)

    # render degli animali in base a GRAFICA
    # se True si usano sprite 2D
    # se False si renderizzano dei quadrati di pixel

    def render(self, screen):
        if GRAFICA:
            if self.eta < 0.5:
                self.img = pygame.transform.scale(self.img, (20, 20))
            else:
                self.img = pygame.transform.scale(self.img, (25, 25))

            screen.blit(self.img, (self.coord_int.x, self.coord_int.y))

        else:
            if self.eta < 0.5:
                pygame.draw.circle(screen, self.color, (self.coord_int.x, self.coord_int.y), 2)
            else:
                pygame.draw.circle(screen, self.color, (self.coord_int.x, self.coord_int.y), 3)

# Agente Volpe
class Volpe(Animale):
    def __init__(self, ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 eta=0.0,
                 soglia_fame=0,
                 soglia_morte_di_fame=0,
                 soglia_sete=0,
                 soglia_morte_di_sete=0,
                 soglia_fertilita=0,
                 percezione=0,
                 velocita_camminata=0,
                 velocita_corsa=0):
        Animale.__init__(self, ambiente, nome='volpe', coord=coord, destinazione=destinazione,
                         eta=0.0,
                         soglia_fame=soglia_fame,
                         soglia_morte_di_fame=soglia_morte_di_fame,
                         soglia_sete=soglia_sete,
                         soglia_morte_di_sete=soglia_morte_di_sete,
                         soglia_fertilita=soglia_fertilita,
                         percezione=percezione,
                         velocita_camminata=velocita_camminata,
                         velocita_corsa=velocita_corsa)
        self.preda_nome = 'coniglio'
        if GRAFICA:
            self.img = img_volpe
        else:
            self.color = (0, 0, 0)




# Agente Coniglio
class Coniglio(Animale):
    def __init__(self, ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                 eta=0.0,
                 soglia_fame=0,
                 soglia_morte_di_fame=0,
                 soglia_sete=0,
                 soglia_morte_di_sete=0,
                 soglia_fertilita=0,
                 percezione=0,
                 velocita_camminata=0,
                 velocita_corsa=0):
        Animale.__init__(self, ambiente, nome='coniglio', coord=coord, destinazione=destinazione,
                         eta=0.0,
                         soglia_fame=soglia_fame,
                         soglia_morte_di_fame=soglia_morte_di_fame,
                         soglia_sete=soglia_sete,
                         soglia_morte_di_sete=soglia_morte_di_sete,
                         soglia_fertilita=soglia_fertilita,
                         percezione=percezione,
                         velocita_camminata=velocita_camminata,
                         velocita_corsa=velocita_corsa)
        self.preda_nome = 'carota'
        if GRAFICA:
            self.img = img_coniglio
        else:
            self.color = (200, 200, 200)





# classe Acqua
class Acqua():
    def __init__(self, ambiente, coord=v2.Vector2D(random.randint(10, WIDTH - 10), random.randint(10, HEIGHT - 10))):
        self.ambiente = ambiente
        self.coord = coord

        if self.coord.x > WIDTH - 10: self.coord.x = WIDTH - 10
        if self.coord.x < 10: self.coord.x = 10
        if self.coord.y > HEIGHT - 10: self.coord.y = HEIGHT - 10
        if self.coord.y < 10: self.coord.y = 10

        self.coord_int = self.coord.int_()
        self.colore = (0, 102, 255)
        self.nome = 'acqua'
        self.quantita = QUANTITA_ACQUA

    def esaurita(self):
        Animale.morte(self)

    def process(self, tempo_passato_secondi):
        None

    # render in base alla quantità disponibile
    def render(self, screen):
        pygame.draw.circle(screen, self.colore, (self.coord_int.x, self.coord_int.y), self.quantita * 2)

# classe Carota
class Carota():
    def __init__(self, ambiente, coord=v2.Vector2D(random.randint(20, WIDTH - 20), random.randint(20, HEIGHT - 20))):
        self.ambiente = ambiente
        self.coord = coord

        if self.coord.x > WIDTH - 10: self.coord.x = WIDTH - 10
        if self.coord.x < 10: self.coord.x = 10
        if self.coord.y > HEIGHT - 10: self.coord.y = HEIGHT - 10
        if self.coord.y < 10: self.coord.y = 10

        self.coord_int = self.coord.int_()
        self.colore = (255, 94, 19)
        self.nome = 'carota'
        self.eta = 0

    def morte(self):
        Animale.morte(self)

    # probabilità di generazione di una carota vicina
    def Crescita(self):

        if random.random() < PROBABILITA_CRESCITA_CAROTE:
            # print("Nuova carota")
            self.ambiente.lista_agenti_aggiunti.add(
                self.__class__(self.ambiente, coord=self.coord + v2.Vector2D(random.randint(-50, 50), random.randint(-50, 50))))

    def process(self, tempo_passato_secondi):
        self.Crescita()

        # le carote possono marcire
        self.eta += 0.002
        if self.eta > 2.5:
            self.colore = (150, 75, 0)
        if self.eta > 3:
            self.morte()


    def render(self, screen):
        pygame.draw.circle(screen, self.colore, (self.coord_int.x, self.coord_int.y), 2)






# inizializzazione agenti
def introduzione():
    for i in range(NUMERO_CAROTE):
        ambiente.aggiungi_agente(Carota(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))
    for i in range(NUMERO_POZZANGHERE):
        ambiente.aggiungi_agente(Acqua(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))


    for i in range(NUMERO_VOLPI):
        ambiente.aggiungi_agente(Volpe(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                       destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                       eta=0.0,
                                       soglia_fame=random.randint(200, 250),
                                       soglia_morte_di_fame=random.randint(550, 650),
                                       soglia_sete=random.randint(200, 250),
                                       soglia_morte_di_sete=random.randint(550, 650),
                                       soglia_fertilita=random.randint(500, 600),
                                       percezione=random.randint(15, 20),
                                       velocita_camminata=random.randint(40, 60),
                                       velocita_corsa=random.randint(65, 75)))
    for i in range(NUMERO_CONIGLI):
        ambiente.aggiungi_agente(Coniglio(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                          destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                          eta=0.0,
                                          soglia_fame=random.randint(200, 250),
                                          soglia_morte_di_fame=random.randint(500, 600),
                                          soglia_sete=random.randint(200, 250),
                                          soglia_morte_di_sete=random.randint(500, 600),
                                          soglia_fertilita=random.randint(250, 300),
                                          percezione=random.randint(15, 20),
                                          velocita_camminata=random.randint(40, 60),
                                          velocita_corsa=random.randint(65, 75)))

# reintroduzione agenti nell'ambiente ogni cambio di stagione
def reintroduzione():
    for i in range(10):
        ambiente.aggiungi_agente(Volpe(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                       destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                                       eta=random.randint(0, 3),
                                       soglia_fame=soglia_fame_volpi,
                                       soglia_morte_di_fame=soglia_morte_di_fame_volpi,
                                       soglia_sete=soglia_sete_media_volpi,
                                       soglia_morte_di_sete=soglia_morte_di_sete_volpi,
                                       soglia_fertilita=soglia_fertilita_volpi,
                                       percezione=percezione_volpi,
                                       velocita_camminata=velocita_camminata_volpi,
                                       velocita_corsa=velocita_corsa_volpi))
    for i in range(30):
        ambiente.aggiungi_agente(
            Coniglio(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                     destinazione=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT)),
                     eta=random.randint(0, 3),
                     soglia_fame=soglia_fame_conigli,
                     soglia_morte_di_fame=soglia_morte_di_fame_conigli,
                     soglia_sete=soglia_sete_media_conigli,
                     soglia_morte_di_sete=soglia_morte_di_sete_conigli,
                     soglia_fertilita=soglia_fertilita_conigli,
                     percezione=percezione_conigli,
                     velocita_camminata=velocita_camminata_conigli,
                     velocita_corsa=velocita_corsa_conigli))







contatore_frame = 0
frame_num = 250

introduzione()

# quando si chiude la finestra pygame salva in un csv i dati
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            dataDF = pd.DataFrame.from_dict(data, orient='index')
            dataDF = dataDF.transpose()
            print(dataDF)
            dataDF.to_csv('Volpe-Coniglio.csv', sep=';')
            pl.plot_and_save(seed)
            exit()

    #---------- INIZIO GAME LOOP ----------#


    tempo_passato = clock.tick(
        150)  # valore alto: tempo passa velocemente ->troppi morti di fame e proliferazione piante
    tempo_passato_secondi = tempo_passato / 1000

    ambiente.giorno += 0.001
    # ogni volta che si raggiunge il valore 2 iniza l'anno nuovo
    giorno_anno = ambiente.giorno % 2
    # variabile utilizzata per asse X del plot real time
    giorno_grafico = ambiente.giorno % 12

    # GESTIONE STAGIONI

    # primavera
    if giorno_anno <= 0.5:
        if ambiente.stagione == "inverno":
            if REINSERIMENTO:
                reintroduzione()
        ambiente.stagione = "primavera"
        ambiente.colore_erba = (0, 175, 0)


        if random.randint(0, 3) == 1:
            ambiente.aggiungi_agente(Carota(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))

        if random.randint(0, 350) == 1:
            # print("piove")
            for i in range(random.randint(0, 10)):
                ambiente.aggiungi_agente(Acqua(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))

    # estate
    elif giorno_anno > 0.5 and giorno_anno <= 1:
        if ambiente.stagione == "primavera":
            if REINSERIMENTO:
                reintroduzione()
            for pozzanghera in ambiente.agenti.values():
                if (pozzanghera.nome == 'acqua'):
                    pozzanghera.quantita -= 1

        ambiente.stagione = "estate"
        ambiente.colore_erba = (125, 175, 0)

        if random.randint(0, 5) == 1:
            ambiente.aggiungi_agente(Carota(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))

        if random.randint(0, 1000) == 1:
            # print("piove")
            for i in range(random.randint(0, 50)):
                ambiente.aggiungi_agente(Acqua(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))


    # autunno
    elif giorno_anno > 1 and giorno_anno <= 1.5:
        if ambiente.stagione == "estate":
            if REINSERIMENTO:
                reintroduzione()
        ambiente.stagione = "autunno"
        ambiente.colore_erba = (165, 145, 0)
        if random.randint(0, 10) == 1:
            ambiente.aggiungi_agente(Carota(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))
        if random.randint(0, 200) == 1:
            # print("piove")
            for i in range(random.randint(0, 10)):
                ambiente.aggiungi_agente(Acqua(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))

    # inverno
    elif giorno_anno > 1.5 and giorno_anno <= 2:
        if ambiente.stagione == "autunno":
            if REINSERIMENTO:
                reintroduzione()
        ambiente.stagione = "inverno"
        ambiente.colore_erba = (255, 255, 255)
        if random.randint(0, 5) == 1:
            ambiente.aggiungi_agente(Carota(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))
        if random.randint(0, 250) == 1:
            # print("piove")
            for i in range(random.randint(0, 10)):
                ambiente.aggiungi_agente(Acqua(ambiente, coord=v2.Vector2D(random.randint(0, WIDTH), random.randint(0, HEIGHT))))




    # lista contenente gli animali per specie, utilizzate per collezionare dati
    conigli = [agente for agente in ambiente.agenti.values() if agente.nome == 'coniglio']
    volpi = [agente for agente in ambiente.agenti.values() if agente.nome == 'volpe']

    # processamento dell'ambiente
    ambiente.process(tempo_passato_secondi)
    ambiente.render(screen)

    frame_num += 1


    num_volpe = len([1 for agente in ambiente.agenti.values() if agente.nome == 'volpe'])
    num_coniglio = len([1 for agente in ambiente.agenti.values() if agente.nome == 'coniglio'])


    # ogniqualvolta si raggiungono i 250 frame vengono salvati i dati come nuovo record del csv
    if frame_num >= 250:
        data['reinserimento'].append(REINSERIMENTO)
        data['evoluzione'].append(EVOLUZIONE)
        data['probabilita_riproduzione_carote'].append(PROBABILITA_CRESCITA_CAROTE)
        data['quantita_acqua_pozzanghera'].append(QUANTITA_ACQUA)
        data['tempo'].append(pygame.time.get_ticks() // 1000)
        data['stagione'].append(ambiente.stagione)
        data['num_volpi'].append(num_volpe)
        data['num_conigli'].append(num_coniglio)
        data['num_carota'].append(len([1 for agente in ambiente.agenti.values() if agente.nome == 'carota']))
        data['num_pozzanghera'].append(len([1 for agente in ambiente.agenti.values() if agente.nome == 'acqua']))
        data['numero_conigli_morti_fame'].append(ambiente.numero_conigli_morti_fame)
        data['numero_volpi_morti_fame'].append(ambiente.numero_volpi_morti_fame)
        data['numero_conigli_morti_sete'].append(ambiente.numero_conigli_morti_sete)
        data['numero_volpi_morti_sete'].append(ambiente.numero_volpi_morti_sete)
        data['numero_conigli_morti_vecchiaia'].append(ambiente.numero_conigli_morti_vecchiaia)
        data['numero_volpi_morti_vecchiaia'].append(ambiente.numero_volpi_morti_vecchiaia)
        data['numero_conigli_cacciati'].append(ambiente.numero_conigli_morti_cacciati)
        data['numero_conigli_nati'].append(ambiente.numero_conigli_nati)
        data['numero_volpi_nate'].append(ambiente.numero_volpi_nate)
        conigli = [agente for agente in ambiente.agenti.values() if agente.nome == 'coniglio']
        volpi = [agente for agente in ambiente.agenti.values() if agente.nome == 'volpe']


        if len(conigli) != 0:
            data['eta_media_conigli'].append(round((sum(coniglio.eta for coniglio in conigli)) / len(conigli), 3))
            data['percezione_media_conigli'].append(
                round((sum(coniglio.percezione for coniglio in conigli)) / len(conigli), 3))
            data['velocita_camminata_media_conigli'].append(
                round((sum(coniglio.velocita_camminata for coniglio in conigli)) / len(conigli), 3))
            data['velocita_corsa_media_conigli'].append(
                round((sum(coniglio.velocita_corsa for coniglio in conigli)) / len(conigli), 3))
            data['soglia_fame_media_conigli'].append(
                round((sum(coniglio.soglia_fame for coniglio in conigli)) / len(conigli), 3))
            data['soglia_sete_media_conigli'].append(
                round((sum(coniglio.soglia_sete for coniglio in conigli)) / len(conigli), 3))
            data['soglia_fertilita_media_conigli'].append(
                round((sum(coniglio.soglia_fertilita for coniglio in conigli)) / len(conigli), 3))
            data['soglia_morte_di_fame_media_conigli'].append(
                round((sum(coniglio.soglia_morte_di_fame for coniglio in conigli)) / len(conigli), 3))
            data['soglia_morte_di_sete_media_conigli'].append(
                round((sum(coniglio.soglia_morte_di_sete for coniglio in conigli)) / len(conigli), 3))
            data['media_fame_conigli'].append(
                round((sum(coniglio.tempo_digiuno for coniglio in conigli)) / len(conigli), 3))
            data['media_sete_conigli'].append(
                round((sum(coniglio.tempo_disidratazione for coniglio in conigli)) / len(conigli), 3))
            data['media_fertilita_conigli'].append(
                round((sum(coniglio.tempo_periodo_fertile for coniglio in conigli)) / len(conigli), 3))

            soglia_fame_conigli = int(data['soglia_fame_media_conigli'][len(data['soglia_fame_media_conigli']) - 1])
            soglia_morte_di_fame_conigli = int(data['soglia_morte_di_fame_media_conigli'][len(data['soglia_morte_di_fame_media_conigli']) - 1])
            soglia_sete_media_conigli = int(data['soglia_sete_media_conigli'][len(data['soglia_sete_media_conigli']) - 1])
            soglia_morte_di_sete_conigli = int(data['soglia_morte_di_sete_media_conigli'][len(data['soglia_morte_di_sete_media_conigli']) - 1])
            soglia_fertilita_conigli = int(data['soglia_fertilita_media_conigli'][len(data['soglia_fertilita_media_conigli']) - 1])
            percezione_conigli = int(data['percezione_media_conigli'][len(data['percezione_media_conigli']) - 1])
            velocita_camminata_conigli = int(data['velocita_camminata_media_conigli'][len(data['velocita_camminata_media_conigli']) - 1])
            velocita_corsa_conigli = int(data['velocita_corsa_media_conigli'][len(data['velocita_corsa_media_conigli']) - 1])


        # se i conigli sono estinti si riutilizzano gli ultimi valori non nulli per evitare salti nei grafici
        else:
            data['eta_media_conigli'].append(0)
            data['media_fame_conigli'].append(0)
            data['media_sete_conigli'].append(0)
            data['media_fertilita_conigli'].append(0)
            data['percezione_media_conigli'].append(percezione_conigli)
            data['velocita_camminata_media_conigli'].append(velocita_camminata_conigli)
            data['velocita_corsa_media_conigli'].append(velocita_corsa_conigli)
            data['soglia_fame_media_conigli'].append(soglia_fame_conigli)
            data['soglia_sete_media_conigli'].append(soglia_sete_media_conigli)
            data['soglia_fertilita_media_conigli'].append(soglia_fertilita_conigli)
            data['soglia_morte_di_fame_media_conigli'].append(soglia_morte_di_fame_conigli)
            data['soglia_morte_di_sete_media_conigli'].append(soglia_morte_di_sete_conigli)


        if len(volpi) != 0:
            data['eta_media_volpi'].append(round(sum(volpe.eta for volpe in volpi) / len(volpi), 3))
            data['percezione_media_volpi'].append(round((sum(volpe.percezione for volpe in volpi)) / len(volpi), 3))
            data['velocita_camminata_media_volpi'].append(
                round((sum(volpe.velocita_camminata for volpe in volpi)) / len(volpi), 3))
            data['velocita_corsa_media_volpi'].append(
                round((sum(volpe.velocita_corsa for volpe in volpi)) / len(volpi), 3))
            data['soglia_fame_media_volpi'].append(round((sum(volpe.soglia_fame for volpe in volpi)) / len(volpi), 3))
            data['soglia_sete_media_volpi'].append(round((sum(volpe.soglia_sete for volpe in volpi)) / len(volpi), 3))
            data['soglia_fertilita_media_volpi'].append(
                round((sum(volpe.soglia_fertilita for volpe in volpi)) / len(volpi), 3))
            data['soglia_morte_di_fame_media_volpi'].append(
                round((sum(volpe.soglia_morte_di_fame for volpe in volpi)) / len(volpi), 3))
            data['soglia_morte_di_sete_media_volpi'].append(
                round((sum(volpe.soglia_morte_di_sete for volpe in volpi)) / len(volpi), 3))
            data['media_fame_volpi'].append(round((sum(volpe.tempo_digiuno for volpe in volpi)) / len(volpi), 3))
            data['media_sete_volpi'].append(round((sum(volpe.tempo_disidratazione for volpe in volpi)) / len(volpi), 3))
            data['media_fertilita_volpi'].append(
                round((sum(volpe.tempo_periodo_fertile for volpe in volpi)) / len(volpi), 3))


            soglia_fame_volpi = int(data['soglia_fame_media_volpi'][len(data['soglia_fame_media_volpi']) - 1])
            soglia_morte_di_fame_volpi = int(data['soglia_morte_di_fame_media_volpi'][len(data['soglia_morte_di_fame_media_volpi']) - 1])
            soglia_sete_media_volpi = int(data['soglia_sete_media_volpi'][len(data['soglia_sete_media_volpi']) - 1])
            soglia_morte_di_sete_volpi = int(data['soglia_morte_di_sete_media_volpi'][len(data['soglia_morte_di_sete_media_volpi']) - 1])
            soglia_fertilita_volpi = int(data['soglia_fertilita_media_volpi'][len(data['soglia_fertilita_media_volpi']) - 1])
            percezione_volpi = int(data['percezione_media_volpi'][len(data['percezione_media_volpi']) - 1])
            velocita_camminata_volpi = int(data['velocita_camminata_media_volpi'][len(data['velocita_camminata_media_volpi']) - 1])
            velocita_corsa_volpi = int(data['velocita_corsa_media_volpi'][len(data['velocita_corsa_media_volpi']) - 1])


        else:
            data['eta_media_volpi'].append(0)
            data['media_fame_volpi'].append(0)
            data['media_sete_volpi'].append(0)
            data['media_fertilita_volpi'].append(0)
            data['percezione_media_volpi'].append(percezione_volpi)
            data['velocita_camminata_media_volpi'].append(velocita_camminata_volpi)
            data['velocita_corsa_media_volpi'].append(velocita_corsa_volpi)
            data['soglia_fame_media_volpi'].append(soglia_fame_volpi)
            data['soglia_sete_media_volpi'].append(soglia_sete_media_volpi)
            data['soglia_fertilita_media_volpi'].append(soglia_fertilita_volpi)
            data['soglia_morte_di_fame_media_volpi'].append(soglia_morte_di_fame_volpi)
            data['soglia_morte_di_sete_media_volpi'].append(soglia_morte_di_sete_volpi)







        contatore_frame += 1
        print(str(contatore_frame)+': + 250 frames')
        frame_num = 0




    # contatori visualizzati a schermo
    str_conigli = "Numero Conigli:" + str(num_coniglio)
    str_volpi = "Numero Volpi:" + str(num_volpe)
    txt_num_conigli = font.render(str_conigli, 1, (0, 0, 0), (255, 255, 255))
    txt_num_volpi = font.render(str_volpi, 1, (0, 0, 0), (255, 255, 255))
    txt_stagione = font.render(ambiente.stagione, 1, (0, 0, 0), (255, 255, 255))
    screen.blit(txt_num_conigli, (10, 0))
    screen.blit(txt_num_volpi, (10, 21))
    screen.blit(txt_stagione, (1100, 0))




    # finché esiste un animale si visualizza a schermo il plot real time
    if(num_volpe != 0 or num_coniglio != 0):

        # Update stats
        stats_height = stats.get_height()
        stats_width = stats.get_width()



        t = int((giorno_grafico / 12) * stats_width)
        y_volpi = int(num_volpe / (num_volpe + num_coniglio) * stats_height)
        y_conigli= 200 - y_volpi

        stats_graph = pygame.PixelArray(stats)
        stats_graph[t, y_conigli:200] = pygame.Color(240, 86, 39)
        stats_graph[t, 0:y_conigli] = pygame.Color(255, 255, 255)


        del stats_graph
        stats.unlock()
        screen.blit(stats, stats_pos)

        pygame.display.update()

    else: # caso in cui sono morti tutti gli aniamli

        data['reinserimento'].append(REINSERIMENTO)
        data['evoluzione'].append(EVOLUZIONE)
        data['probabilita_riproduzione_carote'].append(PROBABILITA_CRESCITA_CAROTE)
        data['quantita_acqua_pozzanghera'].append(QUANTITA_ACQUA)
        data['tempo'].append(pygame.time.get_ticks() // 1000)
        data['stagione'].append(ambiente.stagione)
        data['num_volpi'].append(num_volpe)
        data['num_conigli'].append(num_coniglio)
        data['num_carota'].append(len([1 for agente in ambiente.agenti.values() if agente.nome == 'carota']))
        data['num_pozzanghera'].append(len([1 for agente in ambiente.agenti.values() if agente.nome == 'acqua']))
        data['numero_conigli_morti_fame'].append(ambiente.numero_conigli_morti_fame)
        data['numero_volpi_morti_fame'].append(ambiente.numero_volpi_morti_fame)
        data['numero_conigli_morti_sete'].append(ambiente.numero_conigli_morti_sete)
        data['numero_volpi_morti_sete'].append(ambiente.numero_volpi_morti_sete)
        data['numero_conigli_morti_vecchiaia'].append(ambiente.numero_conigli_morti_vecchiaia)
        data['numero_volpi_morti_vecchiaia'].append(ambiente.numero_volpi_morti_vecchiaia)
        data['numero_conigli_cacciati'].append(ambiente.numero_conigli_morti_cacciati)
        data['numero_conigli_nati'].append(ambiente.numero_conigli_nati)
        data['numero_volpi_nate'].append(ambiente.numero_volpi_nate)
        conigli = [agente for agente in ambiente.agenti.values() if agente.nome == 'coniglio']
        volpi = [agente for agente in ambiente.agenti.values() if agente.nome == 'volpe']
        data['eta_media_volpi'].append(0)
        data['percezione_media_volpi'].append(0)
        data['velocita_camminata_media_volpi'].append(0)
        data['velocita_corsa_media_volpi'].append(0)
        data['soglia_fame_media_volpi'].append(0)
        data['soglia_sete_media_volpi'].append(0)
        data['soglia_fertilita_media_volpi'].append(0)
        data['soglia_morte_di_fame_media_volpi'].append(0)
        data['soglia_morte_di_sete_media_volpi'].append(0)
        data['media_fame_volpi'].append(0)
        data['media_sete_volpi'].append(0)
        data['media_fertilita_volpi'].append(0)
        data['eta_media_conigli'].append(0)
        data['percezione_media_conigli'].append(0)
        data['velocita_camminata_media_conigli'].append(0)
        data['velocita_corsa_media_conigli'].append(0)
        data['soglia_fame_media_conigli'].append(0)
        data['soglia_sete_media_conigli'].append(0)
        data['soglia_fertilita_media_conigli'].append(0)
        data['soglia_morte_di_fame_media_conigli'].append(0)
        data['soglia_morte_di_sete_media_conigli'].append(0)
        data['media_fame_conigli'].append(0)
        data['media_sete_conigli'].append(0)
        data['media_fertilita_conigli'].append(0)




        # anche in questo caso si memorizzano i dati nel file csv
        dataDF = pd.DataFrame.from_dict(data, orient='index')
        dataDF = dataDF.transpose()
        print(dataDF)
        dataDF.to_csv('Volpe-Coniglio.csv', sep=';')
        pl.plot_and_save(seed)
        exit()


