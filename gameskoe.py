import pygame
LIGHT_BLUE = (50, 150, 0)
pygame.init()
FPS = 30
sc = pygame.display.set_mode((850, 850))
e = 5


def builder_rec(a, b, c, d):
    """Рисует прямоугольник, для дома
    :param a: x координата середины объекта,
    :param b: y координата объекта,
    :param c: width для объекта,
    :param d: height для объекта
    :return None
    """
    pygame.draw.rect(sc, LIGHT_BLUE, (a, b, c, d), e)


def builder_lin(a, b, c, d):
    pygame.draw.line(sc, LIGHT_BLUE,
                     [a, b],
                     [c, d], e)


def main():

    x, y = 300, 200
    width, height = 500, 150
    foundation_house_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_house_height - walls_height
    draw_house_foundation(x - width/2, y + walls_height, width, foundation_house_height)
    draw_house_walls(x - walls_width/2, y, walls_width, walls_height)
    draw_house_roof(x - width/2, y + roof_height/20, x, y - roof_height/2)
    draw_house_roof2(x + width/2, y + roof_height/20, x, y - roof_height/2)

    pygame.display.update()


def draw_house_foundation(x, y, width, height):
    """Рисует foundation в опорной точке (х,у) с высотой foundation_house_height и шириной width,
        :param x: кординота середины foundation,
        :param y: кордината низа фундамента,
        :param width: ширена foundation до краёв,
        :param height: длинна foundation,
        :return :None.
        """
    print("рисую foundation..", x, y, width, height)
    builder_rec(x, y, width, height)
    pass


def draw_house_walls(x, y, width, height):

    """Рисует house_walls в опорной точке (х,у) с высотой walls_height и шириной walls_width,
        :param x: кординота середины house_walls,
        :param y: кордината низа house_walls,
        :param width: ширена walls до краёв,
        :param height: длинна walls,
        :return :None.
    """

    print("рисую стены ..", x, y, width, height)
    builder_rec(x, y, width, height)
    pass


def draw_house_roof(x, y, x1, y1):
    """Рисует в  house_roof опорной точке (х,у) с высотой height и шириной width,
            :param x: кординота х начала house_roof,
            :param y: кордината у конца house_roof,
            :param x1: кординота x начала house_roof,
            :param y1: кординота у конца house_roof,
            :return :None.
        """
    print("рисую крышу ..", x, y, x1, y1)
    builder_lin(x, y, x1, y1)

    pass


def draw_house_roof2(x, y, x1, y1):
    """Рисует в  house_roof опорной точке (х,у) с высотой height и шириной width,
                :param x: кординота х начала house_roof,
                :param y: кордината у конца house_roof,
                :param x1: кординота x начала house_roof,
                :param y1: кординота у конца house_roof,
                :return :None.
            """
    print("рисую крышу ..", x, y, x1, y1)
    builder_lin(x, y, x1, y1)

    pass


main()

clock = pygame.time.Clock()

finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
