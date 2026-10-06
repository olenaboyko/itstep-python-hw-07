from datetime import datetime


# 1. Поточна дата та час
def current_datetime():
    return datetime.now()


print("Поточна дата та час:")
print(current_datetime())


# 2. Перевірка введеної дати
def check_date(date_string):
    try:
        datetime.strptime(date_string, "%d.%m.%Y")
        return True
    except ValueError:
        return False


date_input = input("\nВведіть дату у форматі дд.мм.рррр: ")

if check_date(date_input):
    print("Дата коректна.")
else:
    print("Дата некоректна.")


# 3. Обчислення віку
def calculate_age(birth_date):
    today = datetime.now().date()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age


birth_input = input("\nВведіть дату народження у форматі дд.мм.рррр: ")

try:
    birth_date = datetime.strptime(birth_input, "%d.%m.%Y").date()
    print("Ваш вік:", calculate_age(birth_date), "років")
except ValueError:
    print("Некоректна дата народження.")


# 4. Різниця між двома датами
def date_difference(date1, date2):
    difference = abs(date2 - date1)
    return difference.days


date1_input = input("\nВведіть першу дату (дд.мм.рррр): ")
date2_input = input("Введіть другу дату (дд.мм.рррр): ")

try:
    date1 = datetime.strptime(date1_input, "%d.%m.%Y").date()
    date2 = datetime.strptime(date2_input, "%d.%m.%Y").date()

    print("Різниця між датами:", date_difference(date1, date2), "днів")
except ValueError:
    print("Одна або обидві дати некоректні.")


# 5. Привітання залежно від часу
def greeting(current_time):
    hour = current_time.hour

    if 5 <= hour < 12:
        return "Доброго ранку"
    elif 12 <= hour < 18:
        return "Доброго дня"
    elif 18 <= hour < 23:
        return "Доброго вечора"
    else:
        return "Доброї ночі"


now = datetime.now()
print("\nПривітання:")
print(greeting(now))


# 6. Перетворення рядка на datetime
def string_to_datetime(date_string):
    return datetime.strptime(date_string, "%d.%m.%Y")


date_string = input("\nВведіть дату для перетворення (дд.мм.рррр): ")

try:
    converted_date = string_to_datetime(date_string)
    print("Об'єкт datetime:", converted_date)
except ValueError:
    print("Некоректний формат дати.")


# 7. Скільки днів залишилося до заданої дати
def days_until(target_date):
    today = datetime.now().date()
    difference = target_date - today
    return difference.days


target_input = input("\nВведіть майбутню дату (дд.мм.рррр): ")

try:
    target_date = datetime.strptime(target_input, "%d.%m.%Y").date()
    days = days_until(target_date)

    if days > 0:
        print("До заданої дати залишилося:", days, "днів.")
    elif days == 0:
        print("Ця дата сьогодні.")
    else:
        print("Ця дата вже минула.")
except ValueError:
    print("Некоректна дата.")