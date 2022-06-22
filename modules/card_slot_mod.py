class CardSlot:
    """
    This represents a single card slot behavior
    """

    def __init__(self, id: int):
        if type(id) != int or (id not in range(0, 5)):
            raise TypeError("id should be an integer between 0 and 4")
        self.id = id
        self.shown_value = 0
        self.real_value = 0
        self.n_cards = 0
        self.flashing = False
        self.busted = False
        self.cards_no_limit = 5

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

    def _add_card_no_flashing(self, card_value: int):
        """
        Add a card to the CardBox
        when the box is not flashing
        """
        if card_value == 11:
            if self.real_value < 11:
                if self.n_cards >= self.cards_no_limit:
                    self.real_value = self.real_value + 1
                else:
                    self.real_value += 11
                    self.flashing = True
            else:
                self.real_value = self.real_value + 1
        else:

            self.real_value += card_value

    def add_card(self, card_value: int) -> bool:
        """
        Add a card to the CardBox
        return False if busted
        """
        if self.flashing:
            self._add_card_on_flashing(card_value)
        else:
            self._add_card_no_flashing(card_value)

        self.shown_value = self.real_value
        self.n_cards += 1

        if self.real_value > 21:
            self.busted = True
        elif self.n_cards >= self.cards_no_limit and self.real_value <= 21:
            self.shown_value = 21

        return self.is_busted()

    def is_busted(self):
        """
        Check if the box is busted or not
        """
        return self.busted
