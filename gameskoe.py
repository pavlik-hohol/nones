import pygame
LIGHT_BLUE = (64, 128, 255)
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
    pygame.draw.rect(sc, (LIGHT_BLUE), (a, b, c, d), e)


def builder_lin(a, b, c, d):
    pygame.draw.line(sc, (LIGHT_BLUE),
                     [a, b],
                     [c, d], e)


def builder_lin_inert(c, d, a, b):
    pygame.draw.line(sc, (LIGHT_BLUE),
                     [a, b],
                     [c, d], e)


def main():

    x, y = 300, 200
    width, height = 50, 75
    foundation_house_height = 0.05 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_house_height - walls_height - walls_width/2
    draw_dom(x, y, width, height)
    draw_house_foundation(x - width/2, y + walls_height, width, foundation_house_height)
    draw_house_walls(x - walls_width/2, y, walls_width, walls_height)

    pygame.display.update()


def draw_dom(x, y, width, height):
    """Рисует домик в опорной точке (х,у) с высотой height и шириной width,
    :param x: кординота середины домика,
    :param y: кордината низа фундамента,
    :param width: ширена домика между краёв,
    :param height: высота до крайней точки домика,
    :return :None.
    """
    print("рисую домик ..", x, y, width, height)


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

    """Рисует в house_walls опорной точке (х,у) с высотой walls_height и шириной walls_width,
        :param x: кординота середины house_walls,
        :param y: кордината низа house_walls,
        :param width: ширена walls до краёв,
        :param height: длинна walls,
        :return :None.
    """

    print("рисую стены ..", x, y, width, height)
    builder_rec(x, y, width, height)
    pass


def draw_house_roof(x, y, width, height):
    """Рисует в  house_roof опорной точке (х,у) с высотой height и шириной width,
            :param x: кординота середины house_roof,
            :param y: кордината низа house_roof,
            :param height: длинна house_roof,
            :param width: ширена house_roof до краёв,
            :return :None.
        """
    print("рисую крышу ..", x, y, width, height)

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
