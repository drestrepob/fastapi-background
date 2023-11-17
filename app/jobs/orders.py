import random
import time


DISHES = {
    'pizza': '🍕',
    'pasta': '🍝',
    'salad': '🥗',
    'soup': '🍲',
    'sandwich': '🥪',
    'milkshake': '🥤',
    'burger': '🍔',
}


def process_order(dish: str) -> str:
    """
    A function that takes a dish name, "cook" it with randomized timing
       and return the dish emoji with the time it took to prepare

    Args:
        dish_name (str): name of the dish/drink

    Returns:
        if the dish_name is not in the dishes dictionary, return a string response with the sorry message
        if the dish_name is in the dishes dictionary, return a string response with the dish emoji and the time it took to cook
    """
    elapsed_time = random.randint(1, 10)
    time.sleep(elapsed_time)
    try:
        cooked_dish = DISHES[dish]
    except KeyError:
        return f'🚫 Sorry, we don\'t have {dish} on the menu today.'

    return f'🍽️ Your {cooked_dish} is ready! It took {elapsed_time} seconds to prepare.'
