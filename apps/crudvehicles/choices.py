from dj.choices import Choices, Choice


class ModelsTypesChoices(Choices):
    motorcycle = Choice('motorcycle').extra(description='moto')
    car = Choice('car').extra(description='car')

