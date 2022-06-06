#! /usr/bin/env python
"""
MyProject Description
"""

import gettext
import locale
import logging
import os
import sys


__project_name__ = "myproject"

if getattr(sys, "frozen", False):
    # If the application is run as a bundle, the PyInstaller bootloader
    # extends the sys module by a flag frozen=True and sets the app
    # path into variable _MEIPASS'.
    dirname = sys._MEIPASS
else:
    dirname = os.path.dirname(os.path.abspath(__file__))


current_locale, _ = locale.getlocale()
if current_locale == "Italian_Italy":
    current_locale = "it_IT"
locale_path = os.path.join("files", "locale")
dictionary = gettext.translation("main", locale_path, [current_locale])
dictionary.install()
_ = dictionary.gettext


"""




# Funzione che controlla se c'è una casella sballata
def checkDeckBusted(cards):
    for i in range(0, 5):
        if cards[i].checkBusted():
            return True
    return False


# Funzione che controlla se ho vinto
def checkWin(cards):
    global total_value
    if checkDeckBusted(cards):
        return -1
    if total_value == 104:
        return 8
    elif total_value == 105:
        return 10
    elif total_value >= 100:
        return 1
    return 0


# funzione che controlla se ci sono carte lampeggianti
def checkFlashingCard():
    global cardBoxes_cells
    for i in range(0, len(cardBoxes_cells)):
        if cardBoxes_cells[i].flashing:
            print("i: %d is Flashing" % i)
            return True
    return False


# Funzione che estrae una carta dal mazzo
def drawCard(deck):
    return random.choice(deck)


# Funzione che controlla se è possibile aggiungere la carta estratta al gioco corrente
def checkCardAdd(card):
    global cardBoxes_cells
    Log = ""
    if checkFlashingCard():
        Log = "Ci sono carte che lampeggiano"
        return True
    else:
        Log = "Non lampaggia alcuna carta"
    for i in range(0, 5):
        value = card[1]
        if value == 11:
            value = 1
        if (
            cardBoxes_cells[i].showValue + value <= 21
            or cardBoxes_cells[i].realValue + value <= 21
        ):
            return True
    print(Log)
    return False


# Ridisegna il contenuto della casella una volta aggiunta la carta corrente
def redrawCellContent(cell, content):
    image = Gtk.Image()
    image.set_from_file("./img/" + str(content) + ".png")
    cell.set_image(image)


# Calcola il totale e lo mostra nella casella di testo in basso
def calculateTotal():
    global total_label
    global total_value
    t_sum = 0
    for i in range(0, len(cardBoxes_cells)):
        t_sum += cardBoxes_cells[i].showValue
    total_value = t_sum
    # Scrivo la somma nella casella di testo
    total_label.set_text(str(total_value))


def setAlert(msg):
    global alert_label
    alert_label.set_text(msg)


# Pulsante di stop serve per fermarsi
def handle_stop_button(self):
    global shutDown
    shutDown = True
    print("STOP!!!")


# Aggiunge la carta estratta alla casella di testo
def addCardToCells(self, arg):
    global cardBoxes_cells
    global cardBoxes_btns
    global currentCard
    global nextCard
    global shutDown
    global stop_button
    if shutDown != True:
        cardBoxes_cells[arg].addCard(currentCard)
        redrawCellContent(cardBoxes_btns[arg], cardBoxes_cells[arg].showValue)
        res = checkWin(cardBoxes_cells)

        # Rivedere tutta la gestione dell'uscita
        if res == -1:
            #         redrawCellContent(cardBoxes_btns[arg], cardBoxes_cells[arg].showValue)
            print("Sballato")
            setAlert("GAME OVER: Sballato")
            shutDown = True
        #         elif(res == 0):
        #             pass
        elif res == 8 or res == 1:
            #         redrawCellContent(cardBoxes_btns[arg], cardBoxes_cells[arg].showValue)
            print("Puoi ritirare %d monete" % res)
            setAlert("Puoi ritirare %d monete" % res)
            # Mostro il pulsante di STOP
            #             stop_button.set_visible(True)
            stop_button.set_sensitive(True)

        elif res == 10:
            #         redrawCellContent(cardBoxes_btns[arg], cardBoxes_cells[arg].showValue)
            setAlert("Hai vinto %d monete" % res)
            print("Hai vinto %d monete" % res)
        redrawCellContent(cardBoxes_btns[arg], cardBoxes_cells[arg].showValue)

        # Metto il retro delle carte come sfondo

        filename_str = "./img/cards/back.png"
        cardBoxes_btns[5].set_from_file(filename_str)

        calculateTotal()
        nextCard = False

        print(
            "R: %d - S: %d - N: %d"
            % (
                cardBoxes_cells[arg].realValue,
                cardBoxes_cells[arg].showValue,
                cardBoxes_cells[arg].n_cards,
            )
        )


# Crea e mostra le caselle con le immagini
def paintCardBox():

    global cardBoxes_btns

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    image_last = Gtk.Image()
    image_last.set_from_file("./img/cards/back.png")
    hbox.add(image_last)
    button = Gtk.Button()
    image = Gtk.Image()
    image.set_from_file("./img/0.png")
    button.set_image(image)
    cardBoxes_btns.append(button)
    hbox.add(button)
    button = Gtk.Button()
    image = Gtk.Image()
    image.set_from_file("./img/0.png")
    button.set_image(image)
    cardBoxes_btns.append(button)
    hbox.add(button)
    button = Gtk.Button()
    image = Gtk.Image()
    image.set_from_file("./img/0.png")
    button.set_image(image)
    cardBoxes_btns.append(button)
    hbox.add(button)
    button = Gtk.Button()
    image = Gtk.Image()
    image.set_from_file("./img/0.png")
    button.set_image(image)
    cardBoxes_btns.append(button)
    hbox.add(button)
    button = Gtk.Button()
    image = Gtk.Image()
    image.set_from_file("./img/0.png")
    button.set_image(image)
    cardBoxes_btns.append(button)
    hbox.add(button)

    cardBoxes_btns.append(image_last)

    return hbox


# Imposta l'immagine della carta corrente
def setDeckCard():
    if currentCard != None:
        filename_str = "./img/cards/" + currentCard[0] + ".png"
        cardBoxes_btns[5].set_from_file(filename_str)
    return


# Crea la struttura con le cardBox (sarebbe da integrare con le caselle con le immagini)
def createCardCells():
    global cardBoxes_cells
    for i in range(0, 5):
        cardBoxes_cells.append(cardBox(i))


# Task principale
def mainTask():
    import time

    global currentCard
    global cardBoxes_cells
    global cardBoxes_btns
    global nextCard
    global shutDown
    global total_value
    nextCard = False
    deck = [
        ["A", 11],  #  0
        ["2", 2],  #  1
        ["3", 3],  #  2
        ["4", 4],  #  3
        ["5", 5],  #  4
        ["6", 6],  #  5
        ["7", 7],  #  6
        ["8", 8],  #  7
        ["9", 9],  #  8
        ["10", 10],  #  9
        ["J", 10],  # 10
        ["Q", 10],  # 11
        ["K", 10],  # 12
    ]

    # temp
    cardToExtract = [
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['3',   3],    # 12
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['2',   2],    #  0
        #     ['A',   11],    #  0
        #     ['3',   3],    # 12
        #     ['A',   11],    #  0
        #     ['2',   2],    #  0
        #     ['3',   3],    # 12
        ["A", 11],  #  0
        ["K", 10],  # 12
        ["A", 11],  #  0
        ["K", 10],  # 12
        ["A", 11],  #  0
        ["K", 10],  # 12
        ["A", 11],  #  0
        ["K", 10],  # 12
        ["K", 10],  #  0
        ["K", 10],  # 12
        ["K", 10],  # 12
        ["K", 10],  #  0
        ["K", 10],  # 12
        ["K", 10],  # 12
        ["K", 10],  #  0
        ["K", 10],  # 12
        ["K", 10],  # 12
        ["K", 10],  #  0
        ["K", 10],  # 12
        ["K", 10],  # 12
        #     ['A',   11],    #  0
        #     ['K',   10],    # 12
        #     ['A',   11],    #  0
        #     ['K',   10],    # 12
    ]
    cardCounter = 0

    #     exit_loop = False
    while not shutDown:
        currentCard = drawCard(deck)
        #        currentCard = cardToExtract[cardCounter]
        #        cardCounter += 1

        setDeckCard()
        nextCard = True
        if checkCardAdd(currentCard) and total_value != 105:
            while nextCard == True:
                time.sleep(0.2)  # 0% CPU
        else:
            #             exit_loop = True
            # Messaggio GameOver
            res = checkWin(cardBoxes_cells)

            # Rivedere tutta la gestione dell'uscita

            text = "GAME OVER"

            if res > 0:
                text += ": Hai vinto %d monete" % res
            print(text)
            setAlert(text)
            shutDown = True
    # Avviso a video
    res = checkWin(cardBoxes_cells)

    # Rivedere tutta la gestione dell'uscita

    text = "GAME OVER"

    if res > 0:
        text += ": Hai vinto %d monete" % res
    print(text)
    setAlert(text)

    return


# Disegna la carta che lampeggia
def paintCard(card, cell, on):
    image = Gtk.Image()
    if on:
        image.set_from_file("./img/" + str(cell.showValue) + ".png")
    else:
        image.set_from_file("./img/empty.png")
    card.set_image(image)


# Task che si occupa di far lampeggiare le carte
def flashingCards():
    import time
    from gi.repository import GLib

    global cardBoxes_btns
    global cardBoxes_cells
    global shutDown

    on = True

    while shutDown == False:
        for i in range(0, len(cardBoxes_btns) - 1):
            if cardBoxes_cells[i].flashing:
                # L'uso della seguente funzione previene crash del programma
                GLib.idle_add(paintCard, cardBoxes_btns[i], cardBoxes_cells[i], on)
            else:
                GLib.idle_add(paintCard, cardBoxes_btns[i], cardBoxes_cells[i], True)
        on = not on
        time.sleep(0.35)
    # Mostro tutte le carte
    for i in range(0, len(cardBoxes_btns) - 1):
        # L'uso della seguente funzione previene crash del programma
        GLib.idle_add(paintCard, cardBoxes_btns[i], cardBoxes_cells[i], True)


def main():
    import threading
    import gi

    gi.require_version("Gtk", "3.0")
    from gi.repository import Gtk

    global shutDown
    global cardBoxes_cells
    global cardBoxes_btns
    global currentCard
    global alert_label
    global total_label
    global total_value
    global stop_button

    shutDown = False
    nextCard = False

    total_value = 0

    win = Gtk.Window()
    win.connect("delete-event", Gtk.main_quit)

    cardBoxes_cells = []
    cardBoxes_btns = []
    currentCard = None

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)

    # creo le celle
    vbox.add(paintCardBox())

    for i in range(0, len(cardBoxes_btns) - 1):
        cardBoxes_btns[i].connect("clicked", addCardToCells, i)

    createCardCells()

    hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=500)

    #     button = Gtk.Button("START")
    #     hbox.add(button)

    alert_label = Gtk.Label("PLAY")
    hbox.add(alert_label)
    total_label = Gtk.Label(0)
    hbox.add(total_label)
    stop_button = Gtk.Button("STOP")
    hbox.add(stop_button)
    stop_button.connect("clicked", handle_stop_button)
    #     stop_button.set_visible(False)
    stop_button.set_sensitive(False)

    vbox.add(hbox)

    win.add(vbox)

    win.show_all()

    t = threading.Thread(target=mainTask)
    t.start()
    t2 = threading.Thread(target=flashingCards)
    t2.start()

    Gtk.main()

    shutDown = True

    sys.exit(0)


if __name__ == "__main__":

    FORMAT = "%(asctime)-15s `%(name)s` => '%(message)s'"
    log_file = os.path.join("files", f"{__project_name__}.log")
    logging.basicConfig(filename=log_file, level=logging.INFO, format=FORMAT)
    logger = logging.getLogger("main")

    logger.info("App Started")

    main()

    logger.info("App Closed")

    sys.exit(0)
"""
