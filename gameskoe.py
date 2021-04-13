def main():
    x, y = 400, 500
    width, height = 200, 300
    foundation_house_height = 0.07 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_house_height - walls_height
    draw_dom(x, y, width, height)


def draw_dom(x, y, width, height):
    """Рисует домик в опорной точке (х,у) с высотой height и шириной width,
    :param x: кординота середины домика,
    :param y: кордината низа фундамента,
    :param height: высота до крайней точки домика,
    :param width: ширена домика между краёв,
    :return :None.
    """
    print("рисую домик ..", x, y, width, height)
    foundation_house_height = 0.06 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_house_height - walls_height
    draw_house_foundation(x, y, width, foundation_house_height)
    draw_house_walls(x, y, width, foundation_house_height)
    draw_house_roof(x, y, width, foundation_house_height)

def draw_house_foundation (x, y, width, height):
    """Рисует foundation в опорной точке (х,у) с высотой foundation_house_height и шириной width,
        :param x: кординота середины foundation,
        :param y: кордината низа фундамента,
        :param height: длинна foundation,
        :param width: ширена foundation до краёв,
        :return :None.
        """
    print("рисую foundation..", x, y, width, height)
    pass

def draw_house_walls(x, y, walls_width, height):

    """Рисует в house_walls опорной точке (х,у) с высотой walls_height и шириной walls_width,
        :param x: кординота середины house_walls,
        :param y: кордината низа house_walls,
        :param height: длинна walls,
        :param walls_width: ширена walls до краёв,
        :return :None.
    """

    print("рисую стены ..", x, y, walls_width, height)
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






