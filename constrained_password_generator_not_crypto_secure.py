import random
from string import ascii_lowercase, ascii_uppercase, punctuation, digits


def password_generator(*,
                       num_lower,
                       num_upper,
                       num_symbols,
                       num_digits,
                       required_length=None):
    num_choices = num_lower + num_upper + num_symbols + num_digits
    if required_length is None:
        required_length = num_choices
    assert required_length >= num_choices

    all_chars = ascii_lowercase + ascii_uppercase + punctuation + digits
    while True:
        filler = random.sample(all_chars, k=required_length - num_choices)
        lower = random.sample(ascii_lowercase, k=num_lower)
        upper = random.sample(ascii_uppercase, k=num_upper)
        symbols = random.sample(punctuation, k=num_symbols)
        numbers = random.sample(digits, k=num_digits)
        chars = lower + upper + symbols + numbers + filler
        yield "".join(random.sample(chars, k=required_length))


constraints = dict(num_lower=10,
                   num_upper=5,
                   num_symbols=2,
                   num_digits=2)
constrained_passwords = password_generator(**constraints)
for _ in range(10):
    print(next(constrained_passwords))
