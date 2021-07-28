import matplotlib.pyplot as plt
import pandas as pd
import os






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
    plt.figure(1, figsize=[6.6, 5.5])
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left", bbox_to_anchor=(0.8, 1.15))
    plt.savefig(path+'popolazioni.png')
    # plt.show()


    # plot nascite animali a confronto
    plt.figure(2)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'nascite.png')
    # plt.show()


    # plot eta animali a confronto
    plt.figure(3)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'eta.png')
    # plt.show()


    # plot causa morte conigli
    plt.figure(4)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left", ncol=1)
    plt.savefig(path+'morti_conigli.png')
    # plt.show()


    # plot causa morte volpi
    plt.figure(5)
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
    plt.xlabel("Tempo")
    ax.xaxis.set_label_coords(0.4, -0.6)
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'morti_volpi.png')
    # plt.show()



    # plot caratteri
    plt.figure(5)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'Percezione.png')

    plt.figure(6)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'Percezione.png')


    plt.figure(7)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'velocita_camminata_media.png')


    plt.figure(8)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'velocita_corsa_media.png')


    plt.figure(9)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_fame_media.png')
    # plt.show()

    plt.figure(10)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_sete_media.png')

    plt.figure(11)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_fertilita_media.png')
    # plt.show()

    plt.figure(12)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_morte_di_fame_media.png')

    plt.figure(13)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="center left")
    plt.savefig(path+'soglia_morte_di_sete_media.png')
    # plt.show()




    # plot fame animali a confronto
    plt.figure(14)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'fame.png')
    # plt.show()


    # plot sete animali a confronto
    plt.figure(15)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'sete.png')
    # plt.show()

    # plot fertilita animali a confronto
    plt.figure(16)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'fertilita.png')
    # plt.show()

    # plot risorse a confronto
    plt.figure(17)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'risorse.png')
    # plt.show()

    # plot conigli/carote
    plt.figure(18)
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
    plt.xlabel("Tempo")
    plt.legend(frameon=False, loc="upper left")
    plt.savefig(path+'conigli-carote.png')
    # plt.show()


    print(path)
    df.to_csv(path+str(seed)+'.csv', sep=';')