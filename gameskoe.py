def main():
    x, y = 400, 500
    width, height = 200, 300
    draw_dom(x, y, width, height)


def draw_dom(x, y, width, height):
    """Рисует домик в опорной точке (х,у) с высотой height и шириной width,
    :param x: кординота середины домика,
    :param y: кордината низа фундамента,
    :param height: высота до крайней точки домика,
    :param width: ширена домика между краёв,
    :return :None.
    """
    print("рисую домик .......", x, y, width, height)
    foundation_house_height = 0.07 * height
    walls_width = 0.9 * width
    walls_height = 0.5 * height
    roof_height = height - foundation_house_height - walls_height






















main()






