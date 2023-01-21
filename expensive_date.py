from date import Date


def expensive_and_sunny_suggest():
    return Date("conhecer um barzinho legal na praia", 'sun', 'expensive')


def expensive_and_some_clouds_suggest():
    return Date("ir ao shopping comprar presentes especiais para o parceiro", 'clouds', 'expensive')


def expensive_and_rainny_suggest():
    return Date("fazer uma skincare completa e fazer um jantar especial", 'rain', 'expensive')


def expensive_and_night_suggest():
    return Date("conhecer um bom restaurante", 'night', 'expensive')
