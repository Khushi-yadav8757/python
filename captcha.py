#Program to Generate a Random CAPTCHA List
import random, string

captcha_list = [''.join(random.choices(string.ascii_letters + string.digits, k=6)) for _ in range(10)]

print("CAPTCHA List:", captcha_list)
