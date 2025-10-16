import random



def make_rand_figs():
    rand_age = random.randint(18, 110)
    rand_height = random.uniform(1.00, 2.40)
    rand_height = round(rand_height, 2)
    rand_weight = random.uniform(20.00, 150.00)
    rand_weight = round(rand_weight, 2)

    return [rand_age, rand_height, rand_weight]
