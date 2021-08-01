import matplotlib.pyplot as plt
import pandas as pd
import os
import matplotlib as matplotlib
from operator import add



def plot_and_save(seed):

    tag_reinserimento = ''
    tag_evoluzione = ''

    df = pd.read_csv(filepath_or_buffer='Volpe-Coniglio.csv', sep=';')
    if df['reinserimento'][0]:
        tag_reinserimento = 'R'
    if df['evoluzione'][0]:
        tag_evoluzione = 'E'


    path = 'plot/seed_'+str(seed)+'_'+tag_reinserimento+tag_evoluzione+'/'
    os.mkdir(path)
    print(path)



    # plot popolazioni animali a confronto
    fig = plt.figure(1, figsize=[6.6, 5.5])
    plt.plot(df['tempo'], df['num_conigli'], label = "Popolazione \n conigli", color="darkgray")
    plt.plot(df['tempo'], df['num_volpi'], label = "Popolazione \n volpi", color="indianred")
    # plt.title("popolazioni animali a confronto", y=1.9)
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Popolazioni animali a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.xlabel("Tempo (s)")
    plt.ylabel("# agenti")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.8, 1.15))
    plt.savefig(path+'popolazioni.png')
    plt.close(fig)
    # plt.show()


    # plot nascite animali a confronto
    fig = plt.figure(2)
    plt.plot(df['tempo'], df['numero_conigli_nati'], label="Numero \n nascite Conigli", color="darkgray")
    plt.plot(df['tempo'], df['numero_volpi_nate'], label="Numero \n nascite Volpi", color="indianred")
    # plt.title("nascite animali a confronto", y=1.1)
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Nascite a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("# nascite")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'nascite.png')
    plt.close(fig)
    # plt.show()


    # plot eta animali a confronto
    fig = plt.figure(3)
    plt.plot(df['tempo'], df['eta_media_conigli'], label="Eta media Conigli", color="darkgray")
    plt.plot(df['tempo'], df['eta_media_volpi'], label="Eta media Volpi", color="indianred")
    # plt.title("eta animali a confronto")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Età a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.xlabel("Tempo (s)")
    plt.ylabel("età media")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'eta.png')
    plt.close(fig)
    # plt.show()


    # plot causa morte conigli
    fig = plt.figure(4)
    plt.plot(df['tempo'], df['numero_conigli_morti_sete'], label = "Numero Conigli morti di sete")
    plt.plot(df['tempo'], df['numero_conigli_morti_fame'], label = "Numero Conigli morti di fame")
    plt.plot(df['tempo'], df['numero_conigli_morti_vecchiaia'], label = "Numero Conigli morti \n di vecchiaia")
    plt.plot(df['tempo'], df['numero_conigli_cacciati'], label = "Numero conigli cacciati")
    # plt.title("cause morte conigli")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Cause morte conigli",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("# morti")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left", ncol=1)
    plt.savefig(path+'morti_conigli.png')
    plt.close(fig)
    # plt.show()


    # plot causa morte volpi
    fig = plt.figure(5)
    plt.plot(df['tempo'], df['numero_volpi_morti_sete'], label="Numero volpi morte di sete")
    plt.plot(df['tempo'], df['numero_volpi_morti_fame'], label="Numero volpi morte di fame")
    plt.plot(df['tempo'], df['numero_volpi_morti_vecchiaia'], label="Numero volpi morte \n di vecchiaia")
    # plt.title("cause morte volpi")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Cause morte volpi",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("# morti")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    ax.xaxis.set_label_coords(0.4, -0.6)
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'morti_volpi.png')
    plt.close(fig)
    # plt.show()



    # plot caratteri
    fig = plt.figure(5)
    plt.plot(df['tempo'][0:len(df)-3], df['percezione_media_conigli'][0:len(df)-3], label="Percezione media conigli",
             color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['percezione_media_volpi'][0:len(df)-3], label="Percezione media volpi",
             color="indianred")
    # plt.title("Percezione")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Percezione",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("percezione media")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'Percezione.png')
    plt.close(fig)

    fig = plt.figure(6)
    plt.plot(df['tempo'][0:len(df)-3], df['percezione_media_conigli'][0:len(df)-3], label="Percezione media conigli",
             color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['percezione_media_volpi'][0:len(df)-3], label="Percezione media volpi",
             color="indianred")
    # plt.title("Percezione")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Percezione",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("percezione media")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'Percezione.png')
    plt.close(fig)

    fig = plt.figure(7)
    plt.plot(df['tempo'][0:len(df)-3], df['velocita_camminata_media_conigli'][0:len(df)-3],
             label="Velocità camminata media conigli", color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['velocita_camminata_media_volpi'][0:len(df)-3],
             label= "Velocità camminata media volpi", color="indianred")
    # plt.title("velocita_camminata_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Velocita camminata media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim * 0.23), y=ylim - (top * 0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media velocità camminata")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'velocita_camminata_media.png')
    plt.close(fig)

    fig = plt.figure(8)
    plt.plot(df['tempo'][0:len(df)-3], df['velocita_corsa_media_conigli'][0:len(df)-3],
             label="velocita corsa media conigli", color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['velocita_corsa_media_volpi'][0:len(df)-3],
             label="velocita corsa media volpi", color="indianred")
    # plt.title("velocita_corsa_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Velocita corsa media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    ax.xaxis.set_label_coords(0.5, -0.1)
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media velocità corsa")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'velocita_corsa_media.png')
    plt.close(fig)

    fig = plt.figure(9)
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_fame_media_conigli'][0:len(df)-3], label="soglia fame media conigli",
             color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_fame_media_volpi'][0:len(df)-3], label="soglia fame media volpi",
             color="indianred")
    # plt.title("soglia_fame_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Soglia fame media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia fame")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_fame_media.png')
    plt.close(fig)
    # plt.show()

    fig = plt.figure(10)
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_sete_media_conigli'][0:len(df)-3], label="soglia sete media conigli",
             color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_sete_media_volpi'][0:len(df)-3], label="soglia media sete volpi",
             color="indianred")
    # plt.title("soglia_sete_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Soglia sete media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia sete")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_sete_media.png')
    plt.close(fig)

    fig = plt.figure(11)
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_fertilita_media_conigli'][0:len(df)-3],
             label="soglia media fertilità conigli", color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_fertilita_media_volpi'][0:len(df)-3],
             label="soglia media fertilita volpi", color="indianred")
    # plt.title("soglia_fertilita_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Soglia media fertilità",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia fertilità")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_fertilita_media.png')
    plt.close(fig)
    # plt.show()

    fig = plt.figure(12)
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_morte_di_fame_media_conigli'][0:len(df)-3],
             label="soglia media morte \n di fame conigli", color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_morte_di_fame_media_volpi'][0:len(df)-3],
             label="soglia media morte \n di fame volpi", color="indianred")
    # plt.title("soglia_morte_di_fame_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Soglia morte di fame media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia morte")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_morte_di_fame_media.png')
    plt.close(fig)

    fig = plt.figure(13)
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_morte_di_sete_media_conigli'][0:len(df)-3],
             label="soglia media morte \n di sete conigli", color="darkgray")
    plt.plot(df['tempo'][0:len(df)-3], df['soglia_morte_di_sete_media_volpi'][0:len(df)-3],
             label="soglia media morte \n di sete volpi", color="indianred")
    # plt.title("soglia_morte_di_sete_media")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Soglia morte di sete media",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia morte di sete")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_morte_di_sete_media.png')
    plt.close(fig)
    # plt.show()




    # plot fame animali a confronto
    fig = plt.figure(14)
    plt.plot(df['tempo'], df['media_fame_conigli'], label="Media fame conigli", color="darkgray")
    plt.plot(df['tempo'], df['media_fame_volpi'], label="Media fame volpi", color="indianred")
    # plt.title("fame animali a confronto")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Fame a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media soglia fame")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'fame.png')
    plt.close(fig)
    # plt.show()


    # plot sete animali a confronto
    fig = plt.figure(15)
    plt.plot(df['tempo'], df['media_sete_conigli'], label="Media sete conigli", color="darkgray")
    plt.plot(df['tempo'], df['media_sete_volpi'], label="Media sete volpi", color="indianred")
    # plt.title("sete animali a confronto")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Sete a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media sete")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'sete.png')
    plt.close(fig)
    # plt.show()

    # plot fertilita animali a confronto
    fig = plt.figure(16)
    plt.plot(df['tempo'], df['media_fertilita_conigli'], label="Fertilita media conigli", color="darkgray")
    plt.plot(df['tempo'], df['media_fertilita_volpi'], label="Fertilita media volpi", color="indianred")
    # plt.title("fertilita animali a confronto")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Fertilità a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("media fertilità")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'fertilita.png')
    plt.close(fig)
    # plt.show()

    # plot risorse a confronto
    fig = plt.figure(17)
    plt.plot(df['tempo'], df['num_pozzanghera'], label="Numero pozzanghere", color="#0066FF")
    plt.plot(df['tempo'], df['num_carota'], label="Numero carote", color="darkorange")
    # plt.title("risorse a confronto")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Risorse a confronto",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("# agenti")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'risorse.png')
    plt.close(fig)
    # plt.show()

    # plot conigli/carote
    fig = plt.figure(18)
    plt.plot(df['tempo'], df['num_conigli'], label="Popolazione Conigli", color="darkgray")
    plt.plot(df['tempo'], df['num_carota'], label="Popolazione Carote", color="darkorange")
    # plt.title("popolazioni conigli/carote")
    ax = plt.gca()
    ax.set_ylim(0)
    plt.text(0.5, 1.1, "Popolazioni conigli e carote",
             horizontalalignment='center', fontsize=12, transform=ax.transAxes)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.yaxis.set_ticks_position('left')
    ax.xaxis.set_ticks_position('bottom')
    left, xlim = ax.get_xlim()
    ylim, top = ax.get_ylim()
    ax.text(x=xlim - (xlim*0.23), y=ylim- (top*0.135), s="seed " + str(seed), size=8)
    plt.ylabel("# agenti")
    plt.xlabel("Tempo (s)")
    plt.grid(axis="y", linewidth=0.2, alpha=1, c="black")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'conigli-carote.png')
    plt.close(fig)
    # plt.show()


    # stacked barchart cause di morte delle volpi
    # volpi
    setePrimavera = 0
    famePrimavera = 0
    vecchiaiaPrimavera = 0
    seteEstate = 0
    fameEstate = 0
    vecchiaiaEstate = 0
    seteAutunno = 0
    fameAutunno = 0
    vecchiaiaAutunno = 0
    seteInverno = 0
    fameInverno = 0
    vecchiaiaInverno = 0
    totPrimavera = 0
    totEstate = 0
    totAutunno = 0
    totInverno = 0
    for i in range(1, len(df["stagione"])):
        if (df["stagione"][i]) == "primavera":
            if df["numero_volpi_morti_fame"][i] != df["numero_volpi_morti_fame"][i - 1]:
                nuovi = df["numero_volpi_morti_fame"][i] - df["numero_volpi_morti_fame"][i - 1]
                famePrimavera += nuovi
                totPrimavera += nuovi
            if df["numero_volpi_morti_sete"][i] != df["numero_volpi_morti_sete"][i - 1]:
                nuovi = df["numero_volpi_morti_sete"][i] - df["numero_volpi_morti_sete"][i - 1]
                setePrimavera += nuovi
                totPrimavera += nuovi
            if df["numero_volpi_morti_vecchiaia"][i] != df["numero_volpi_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_volpi_morti_vecchiaia"][i] - df["numero_volpi_morti_vecchiaia"][i - 1]
                vecchiaiaPrimavera += nuovi
                totPrimavera += nuovi
        if (df["stagione"][i]) == "estate":
            if df["numero_volpi_morti_fame"][i] != df["numero_volpi_morti_fame"][i - 1]:
                nuovi = df["numero_volpi_morti_fame"][i] - df["numero_volpi_morti_fame"][i - 1]
                fameEstate += nuovi
                totEstate += nuovi
            if df["numero_volpi_morti_sete"][i] != df["numero_volpi_morti_sete"][i - 1]:
                nuovi = df["numero_volpi_morti_sete"][i] - df["numero_volpi_morti_sete"][i - 1]
                seteEstate += nuovi
                totEstate += nuovi
            if df["numero_volpi_morti_vecchiaia"][i] != df["numero_volpi_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_volpi_morti_vecchiaia"][i] - df["numero_volpi_morti_vecchiaia"][i - 1]
                vecchiaiaEstate += nuovi
                totEstate += nuovi
        if (df["stagione"][i]) == "autunno":
            if df["numero_volpi_morti_fame"][i] != df["numero_volpi_morti_fame"][i - 1]:
                nuovi = df["numero_volpi_morti_fame"][i] - df["numero_volpi_morti_fame"][i - 1]
                fameAutunno += nuovi
                totAutunno += nuovi
            if df["numero_volpi_morti_sete"][i] != df["numero_volpi_morti_sete"][i - 1]:
                nuovi = df["numero_volpi_morti_sete"][i] - df["numero_volpi_morti_sete"][i - 1]
                seteAutunno += nuovi
                totAutunno += nuovi
            if df["numero_volpi_morti_vecchiaia"][i] != df["numero_volpi_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_volpi_morti_vecchiaia"][i] - df["numero_volpi_morti_vecchiaia"][i - 1]
                vecchiaiaAutunno += nuovi
                totAutunno += nuovi
        if (df["stagione"][i]) == "inverno":
            if df["numero_volpi_morti_fame"][i] != df["numero_volpi_morti_fame"][i - 1]:
                nuovi = df["numero_volpi_morti_fame"][i] - df["numero_volpi_morti_fame"][i - 1]
                fameInverno += nuovi
                totInverno += nuovi
            if df["numero_volpi_morti_sete"][i] != df["numero_volpi_morti_sete"][i - 1]:
                nuovi = df["numero_volpi_morti_sete"][i] - df["numero_volpi_morti_sete"][i - 1]
                seteInverno += nuovi
                totInverno += nuovi
            if df["numero_volpi_morti_vecchiaia"][i] != df["numero_volpi_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_volpi_morti_vecchiaia"][i] - df["numero_volpi_morti_vecchiaia"][i - 1]
                vecchiaiaInverno += nuovi
                totInverno += nuovi
        nuovi = 0

    datiSinistra = [setePrimavera, seteEstate, seteAutunno, seteInverno]  # sono i morti di fame
    datiCentro = [famePrimavera, fameEstate, fameAutunno, fameInverno]
    datiDestra = [vecchiaiaPrimavera, vecchiaiaEstate, vecchiaiaAutunno, vecchiaiaInverno]
    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(111)
    colori = ['#00a388', '#71cc91', "#c6eb98", "#e3f59b", "#ffffae", "#f6f6ce"]
    p1 = plt.barh([1, 3, 5, 7], datiSinistra, align='center', height=1.4, zorder=1, color=colori[0],
                  edgecolor="black", alpha=0.7, label="sete")
    p2 = plt.barh([1, 3, 5, 7], datiCentro, align='center', height=1.4, left=datiSinistra, zorder=1, color=colori[1],
                  edgecolor="black", alpha=0.7, label="fame")
    p3 = plt.barh([1, 3, 5, 7], datiDestra, align='center', height=1.4, left=list(map(add, datiSinistra, datiCentro)),
                  color=colori[2], zorder=1, edgecolor="black", alpha=0.7, label="vecchiaia")
    ax.invert_yaxis()
    plt.yticks([1, 3, 5, 7], ["primavera", "estate", "autunno", "inverno"])
    plt.xlim(0, max(totEstate, totInverno, totAutunno, totPrimavera) + 100)
    plt.ylim(0, 8)
    plt.title("Cause morti volpi per stagione", fontsize=22, pad=-2)



    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.legend(handles=[p1, p2, p3])
    plt.savefig(path + 'stackedBarchart_cause_morti_volpi.png')

    # stacked barchart cause di morte conigli
    setePrimavera = 0
    cacciaPrimavera = 0
    famePrimavera = 0
    vecchiaiaPrimavera = 0
    seteEstate = 0
    cacciaEstate = 0
    fameEstate = 0
    vecchiaiaEstate = 0
    seteAutunno = 0
    cacciaAutunno = 0
    fameAutunno = 0
    vecchiaiaAutunno = 0
    seteInverno = 0
    cacciaInverno = 0
    fameInverno = 0
    vecchiaiaInverno = 0
    totPrimavera = 0
    totEstate = 0
    totAutunno = 0
    totInverno = 0
    for i in range(1, len(df["stagione"])):
        if (df["stagione"][i]) == "primavera":
            if df["numero_conigli_morti_fame"][i] != df["numero_conigli_morti_fame"][i - 1]:
                nuovi = df["numero_conigli_morti_fame"][i] - df["numero_conigli_morti_fame"][i - 1]
                famePrimavera += nuovi
                totPrimavera += nuovi
            if df["numero_conigli_cacciati"][i] != df["numero_conigli_cacciati"][i - 1]:
                nuovi = df["numero_conigli_cacciati"][i] - df["numero_conigli_cacciati"][i - 1]
                cacciaPrimavera += nuovi
                totPrimavera += nuovi
            if df["numero_conigli_morti_sete"][i] != df["numero_conigli_morti_sete"][i - 1]:
                nuovi = df["numero_conigli_morti_sete"][i] - df["numero_conigli_morti_sete"][i - 1]
                setePrimavera += nuovi
                totPrimavera += nuovi
            if df["numero_conigli_morti_vecchiaia"][i] != df["numero_conigli_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_conigli_morti_vecchiaia"][i] - df["numero_conigli_morti_vecchiaia"][i - 1]
                vecchiaiaPrimavera += nuovi
                totPrimavera += nuovi
        if (df["stagione"][i]) == "estate":
            if df["numero_conigli_morti_fame"][i] != df["numero_conigli_morti_fame"][i - 1]:
                nuovi = df["numero_conigli_morti_fame"][i] - df["numero_conigli_morti_fame"][i - 1]
                fameEstate += nuovi
                totEstate += nuovi
            if df["numero_conigli_cacciati"][i] != df["numero_conigli_cacciati"][i - 1]:
                nuovi = df["numero_conigli_cacciati"][i] - df["numero_conigli_cacciati"][i - 1]
                cacciaEstate += nuovi
                totEstate += nuovi
            if df["numero_conigli_morti_sete"][i] != df["numero_conigli_morti_sete"][i - 1]:
                nuovi = df["numero_conigli_morti_sete"][i] - df["numero_conigli_morti_sete"][i - 1]
                seteEstate += nuovi
                totEstate += nuovi
            if df["numero_conigli_morti_vecchiaia"][i] != df["numero_conigli_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_conigli_morti_vecchiaia"][i] != df["numero_conigli_morti_vecchiaia"][i - 1]
                vecchiaiaEstate += nuovi
                totEstate += nuovi
        if (df["stagione"][i]) == "autunno":
            if df["numero_conigli_morti_fame"][i] != df["numero_conigli_morti_fame"][i - 1]:
                nuovi = df["numero_conigli_morti_fame"][i] - df["numero_conigli_morti_fame"][i - 1]
                fameAutunno += nuovi
                totAutunno += nuovi
            if df["numero_conigli_cacciati"][i] != df["numero_conigli_cacciati"][i - 1]:
                nuovi = df["numero_conigli_cacciati"][i] - df["numero_conigli_cacciati"][i - 1]
                cacciaAutunno += nuovi
                totAutunno += nuovi
            if df["numero_conigli_morti_sete"][i] != df["numero_conigli_morti_sete"][i - 1]:
                nuovi = df["numero_conigli_morti_sete"][i] - df["numero_conigli_morti_sete"][i - 1]
                seteAutunno += nuovi
                totAutunno += nuovi
            if df["numero_conigli_morti_vecchiaia"][i] != df["numero_conigli_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_conigli_morti_vecchiaia"][i] - df["numero_conigli_morti_vecchiaia"][i - 1]
                vecchiaiaAutunno += nuovi
                totAutunno += nuovi
        if (df["stagione"][i]) == "inverno":
            if df["numero_conigli_morti_fame"][i] != df["numero_conigli_morti_fame"][i - 1]:
                nuovi = df["numero_conigli_morti_fame"][i] - df["numero_conigli_morti_fame"][i - 1]
                fameInverno += nuovi
                totInverno += nuovi
            if df["numero_conigli_cacciati"][i] != df["numero_conigli_cacciati"][i - 1]:
                nuovi = df["numero_conigli_cacciati"][i] - df["numero_conigli_cacciati"][i - 1]
                cacciaInverno += nuovi
                totInverno += nuovi
            if df["numero_conigli_morti_sete"][i] != df["numero_conigli_morti_sete"][i - 1]:
                nuovi = df["numero_conigli_morti_sete"][i] - df["numero_conigli_morti_sete"][i - 1]
                seteInverno += nuovi
                totInverno += nuovi
            if df["numero_conigli_morti_vecchiaia"][i] != df["numero_conigli_morti_vecchiaia"][i - 1]:
                nuovi = df["numero_conigli_morti_vecchiaia"][i] - df["numero_conigli_morti_vecchiaia"][i - 1]
                vecchiaiaInverno += nuovi
                totInverno += nuovi

    datiSinistra = [setePrimavera, seteEstate, seteAutunno, seteInverno]  # sono i morti di fame
    datiCentro = [famePrimavera, fameEstate, fameAutunno, fameInverno]
    datiDestra = [cacciaPrimavera, cacciaEstate, cacciaAutunno, cacciaInverno]
    datiDestra2 = [vecchiaiaPrimavera, vecchiaiaEstate, vecchiaiaAutunno, vecchiaiaInverno]
    fig = plt.figure(figsize=(15, 5))
    ax = fig.add_subplot(111)
    colori = ['#00a388', '#71cc91', "#c6eb98", "#e3f59b", "#ffffae", "#f6f6ce"]
    p1 = plt.barh([1, 3, 5, 7], datiSinistra, align='center', height=1.4, zorder=1, color=colori[0], edgecolor="black",
                  alpha=0.7,
                  label="sete")
    p2 = plt.barh([1, 3, 5, 7], datiCentro, align='center', height=1.4, left=datiSinistra, zorder=1, color=colori[1],
                  edgecolor="black", alpha=0.7, label="fame")
    p3 = plt.barh([1, 3, 5, 7], datiDestra, align='center', height=1.4, left=list(map(add, datiSinistra, datiCentro)),
                  color=colori[2], zorder=1, edgecolor="black", alpha=0.7, label="caccia")
    p4 = plt.barh([1, 3, 5, 7], datiDestra2, align='center', height=1.4,
                  left=list(map(add, list(map(add, datiSinistra, datiCentro)), datiDestra)),
                  color=colori[5], zorder=1, edgecolor="black", alpha=0.7, label="vecchiaia")
    ax.invert_yaxis()
    plt.yticks([1, 3, 5, 7], ["primavera", "estate", "autunno", "inverno"])
    plt.xlim(0, max(totEstate, totInverno, totAutunno, totPrimavera) + 100)
    plt.ylim(0, 8)
    plt.title("Cause morti conigli per stagione", fontsize=22, pad=-2)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.legend(handles=[p1, p2, p3, p4])
    plt.savefig(path + 'stackedBarchart_cause_morti_conigli.png')

    # plot numero conigli vs numero volpi non temporale

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    plt.scatter(df["num_conigli"], df["num_volpi"], s=1.1)
    plt.plot(df["num_conigli"], df["num_volpi"], alpha=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.xlabel("numero conigli")
    plt.ylabel("numero volpi")
    plt.savefig(path + 'conigliVsVolpi_NoTimeSeries.png')

    # plot numero carote vs numero volpi non temporale
    # questi vengono usati per la validazione

    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(111)
    plt.scatter(df["num_carota"], df["num_conigli"], s=1.1)
    plt.plot(df["num_carota"], df["num_conigli"], alpha=0.7)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.xlabel("numero carote")
    plt.ylabel("numero conigli")
    plt.savefig(path + 'caroteVsConigli_NoTimeSeries.png')
    # plt.show()


    print(path)
    df.to_csv(path+str(seed)+'.csv', sep=';')