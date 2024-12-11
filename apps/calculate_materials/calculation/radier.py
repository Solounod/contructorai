def calculation_radier(dates_json):
    dimention = dates_json['dimensiones']
    large = dimention['largo']
    width = dimention['ancho']
    thickness = dimention['espesor']
    print()
    print()
    print(f"largo: {large}, ancho: {width}, espesor: {thickness}")
    print()
    # calculate
    volume = large * width * thickness
    bags_cement_m3 = 7
    m3_sand = 0.7
    m3_gravel = 0.7

    bag_cement = volume * bags_cement_m3
    cube_sand = volume * m3_sand
    cube_gravel = volume * m3_gravel

    return f"Necesitas aproximadamente {bag_cement:.2f} bolsas de cemento, {cube_sand:.2f} cubos de arena y {cube_gravel:.2f} cubos de grava"
