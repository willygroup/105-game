class CardSlot:
    """ """

    def __init__(self, id: int):
        if type(id) != int or (id not in range(0, 6)):
            raise TypeError("id should be an integer between 0 and 5")
        self._id = id
        self.showed_value = 0
        self.real_value = 0
        self.n_cards = 0
        self.flashing = False
        self.busted = False

    def _add_card_on_flashing(self, card_value: int):
        """
        Add a card to the CardBox
        when the box is flashing
        """
        if self.real_value == 11:
            if card_value == 11:
                card_value = 1
            self.real_value += card_value
            self.flashing = True
        elif card_value == 10:
            self.flashing = False
        elif card_value < 10:
            if self.real_value + card_value <= 21:
                self.real_value += card_value
            else:
                self.real_value = self.real_value - 10 + card_value
            self.flashing = False
        elif card_value == 11:
            if self.real_value + 1 <= 21:
                self.real_value += 1
            else:
                self.real_value = self.real_value + 1 - 10
            self.flashing = False

    def add_card(self, card_value: int):
        """
        Add a card to the CardBox
        """
        if self.flashing:
            self._add_card_on_flashing(card_value)
        elif not self.flashing and card_value <= 10:
            self.real_value += card_value
        elif not self.flashing and card_value == 11:
            if self.real_value <= 10:
                self.real_value += 11
                self.flashing = True
            else:
                self.real_value += 1

        self.showed_value = self.real_value
        self.n_cards += 1

        if self.real_value > 21:
            self.busted = True
        elif self.n_cards >= 5 and self.real_value <= 21:
            self.showed_value = 21

    def is_busted(self):
        """
        Check if the box is busted or not
        """
        return self.busted
