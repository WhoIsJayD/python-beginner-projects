import random

# s_char for small letters
s_char = "abcdefghijklmnopqrstuvwxyz"
# b_char for capital letters
b_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# d_char for digits
d_char = "123456789"


class Otp:
    def __init__(self, len):
        self.len = len

    # this method generate number otp
    @property
    def digits(self):
        num = 0
        result = []
        while num < self.len:
            rand_choice = "".join(random.choices(d_char, k=self.len)[:1])
            result.append(rand_choice)
            num += 1
        return "".join(result)

    # this method generate number and capital letters otp
    @property
    def bd_digits(self):
        num = 0
        result = []
        while num < self.len:
            b_choice = "".join(random.choices(b_char, k=self.len)[:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[:1])
            result.extend((b_choice, d_choice))
            num += 1
        return "".join(result[:self.len])

    # this method generate number and small letters otp
    @property
    def sd_digits(self):
        num = 0
        result = []
        while num < self.len:
            s_choice = "".join(random.choices(s_char, k=self.len)[:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[:1])
            result.extend((s_choice, d_choice))
            num += 1
        return "".join(result[:self.len])

    # this method generate both small, capital letters and number otp all together
    @property
    def sbd_digits(self):
        num = 0
        result = []
        while num < self.len:
            s_choice = "".join(random.choices(s_char, k=self.len)[:1])
            b_choice = "".join(random.choices(b_char, k=self.len)[:1])
            d_choice = "".join(random.choices(d_char, k=self.len)[:1])
            result.extend((s_choice, b_choice, d_choice))
            num += 1
        return "".join(result[:self.len])


print(f"OTP:{Otp(10).digits}")
