class Example:
    #
    @property  # first decorate the getter method
    def value(self):  # This getter method name is *the* name
        return self._value

    #
    @value.setter  # the property decorates with `.setter` now
    def attribute(self, value):  # name, e.g. "attribute", is the same
        self._value = value  # the "value" name isn't special

    #
    @value.deleter  # decorate with `.deleter`
    def value(self):  # again, the method name is the same
        del self._value

    def __init__(self, value: int = 0) -> None:
        self._value = value
