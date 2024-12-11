def ceramic_floor(dates_json):
    dimention = dates_json['dimensiones']
    large = dimention['largo']
    width = dimention['ancho']

    feature = dates_json['dimensiones']['dimensiones_baldosas']
    large_ceramic = feature['largo']
    width_ceramic = feature['ancho']

    room_area = large * width

    tiled_area = large_ceramic * width_ceramic

    numbers_tiled = (room_area / tiled_area) * 1.10



    print(f"largo: {large}, ancho: {width}, baldosas {width_ceramic} x {large_ceramic}")

    return f"Necesitas aproximadamente {numbers_tiled:.0f} baldosas de {large_ceramic} por {width_ceramic} mt para cubrir {room_area} m²."
