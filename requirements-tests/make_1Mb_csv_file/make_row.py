from .make_rand_str import make_rand_str
from .make_rand_figs import make_rand_figs



def make_row():
    # headers = ['name', 'email_address', 'age', 'height', 'weight']
    row = []
    first_name = make_rand_str(5)
    last_name = make_rand_str(6)
    name = first_name + ' ' + last_name
    email = first_name + '@' + 'email.com'
    
    # [rand_age, rand_height, rand_weight]
    figs = make_rand_figs()
    age = figs[0]
    height = figs[1]
    weight = figs[2]

    return [name, email, age, height, weight]