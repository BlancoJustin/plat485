def get_formal_name(fruit):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :return formal_name: str, the formal name for the supplied fruit
    """
    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    formal_name = fruit_dict[fruit]

    return formal_name


def get_scientific_name(fruit, default_value='Unknown'):
    """
    Get the scientific name for the supplied `fruit` common name.

    :param fruit: str, common name for a fruit
    :param default_value: str, the value to return if the fruit name is not in the dictionary
    :return scientific_name: str, the scientific name for the supplied fruit, or `default_value` if the fruit name is not in the dictionary
    """

    fruit_dict = {
        'apple': 'Malus domestica',
        'banana': 'Musa acuminata',
        'orange': 'Citrus × sinensis',
        'strawberry': 'Fragaria × ananassa',
        'grape': 'Vitis vinifera',
        'pineapple': 'Ananas comosus',
        'mango': 'Mangifera indica',
        'blueberry': 'Vaccinium corymbosum',
        'peach': 'Prunus persica',
        'watermelon': 'Citrullus lanatus',
        'cherry': 'Prunus avium',
        'pear': 'Pyrus',
        'plum': 'Prunus domestica',
        'raspberry': 'Rubus idaeus',
        'kiwi': 'Actinidia deliciosa',
        'lemon': 'Citrus limon',
        'avocado': 'Persea americana',
        'pomegranate': 'Punica granatum',
        'cranberry': 'Vaccinium macrocarpon',
        'grapefruit': 'Citrus × paradisi'
    }

    try:
        scientific_name = fruit_dict[fruit]
    except KeyError:
        scientific_name = default_value

    return scientific_name