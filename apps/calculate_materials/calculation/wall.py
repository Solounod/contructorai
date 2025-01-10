def wall(dates_json):
    dimention = dates_json['dimensiones']
    high_wall = dimention['alto']
    widht_wall = dimention['ancho']

    wall_area = high_wall * widht_wall
    bricks_m2 = 42 * wall_area
    mortar_bag = 1 * (3 * wall_area)

    return f"Necesitas aproximadamente {bricks_m2} ladrillos y {mortar_bag} sacos de  mortero de albañileria."






    
