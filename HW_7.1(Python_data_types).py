# Используя таймер мотоцикла, рассчитайте текущее время. Возвращает ответ в виде суммы цифр,
# которую покажет цифровой таймер в формате чч:мм.
# Пример:
# Для n = 240, результат должен быть: 4
# 240 минут прошло, текущее время 04:00. Сумма чисел: 0 + 4 + 0 + 0 = 4, это и есть ответ.
# Для n = 808, результат должен быть: 14
# 808 минут прошло, и это означает что сейчас 13:28, так что ответ должен быть 1 + 3 + 2 + 8 = 14.

def get_digit_sum(n):
    bike_hours = (n // 60) % 24
    bike_minutes = n % 60
    digit_sum = sum(int(digit) for digit in f"{bike_hours:00}{bike_minutes:00}")
    print(digit_sum)


minutes1 = 240
get_digit_sum(minutes1)

minutes2 = 808
get_digit_sum(minutes2)


# Учитывая значения опыта, порога и награды, проверьте,
# достигнете ли вы следующего уровня после убийства монстра.
# Пример:
# Для experience = 10, threshold = 15, и reward = 5, результат должен быть: true
# Для experience = 10, threshold = 15, и reward = 4, результат должен быть: false

def is_next_level(experience, threshold, reward):
    if experience + reward >= threshold:
        print(True)
    else:
        print(False)


my_experience = 10
my_threshold = 15
my_reward1 = 5
my_reward2 = 4

is_next_level(my_experience, my_threshold, my_reward1)
is_next_level(my_experience, my_threshold, my_reward2)

# Ваша задача - переконвертировать время из 24-часового формата в 12-часовой,
# используя следующие правила: выходной формат должен быть 'чч:мм a.m.'
# (для часов до полудня) или 'чч:мм p.m.' (для часов после полудня),
# если часы меньше 10 - не пишите '0' перед ними. Например: '9:05 a.m.'
# Пример:
# '12:30' == '12:30 p.m.'
# '09:00' == '9:00 a.m.'
# '23:15' == '11:15 p.m.'
# '00:00' == '12:00 a.m.'

time_str = "23:15"

hours, minutes = map(int, time_str.split(":"))

if hours == 0:
    result = f"12:{minutes:02} a.m."
elif hours == 12:
    result = f"12:{minutes:02} p.m."
elif hours < 12:
    result = f"{hours}:{minutes:02} a.m."
else:
    result = f"{hours - 12}:{minutes:02} p.m."

print(result)
