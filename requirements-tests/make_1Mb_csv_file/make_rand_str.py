import random, string







def make_rand_str(len: int):
    alphab = string.ascii_lowercase # 'abcdef...xyz'
    rand_str = ''.join(random.choice(alphab) for _ in range(len))
    return rand_str
