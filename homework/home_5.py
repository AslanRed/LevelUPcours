# 1 Увеличение глобальной переменной.
def add_client(client_count):
    global clients
    clients += 1
    return clients

clients = 0
add_client(clients)
add_client(clients)
print(clients)

# 2 Изменение цены с локальной и глобальной переменной
def aplly_discount(discount):
    new_price = base_price - base_price * discount / 100
    print(f'Цена со скидкой {new_price}')
    return new_price

base_price = 100
aplly_discount(20)
print(base_price)

# 3 Применение налогов через map
def apply_tax(price):
    new_price = price + price * 0.2
    return new_price

prices = [100, 200, 300, 400]
final_prices = list(map(apply_tax, prices))
print(final_prices)

# 4 Фильтр товаров по цене
def check_price(prices):
    return prices > 150

prices = [50, 120, 180, 300, 75]
expensive_items = list(filter(check_price, prices))
print(expensive_items)

# 5 Применение скидки к категории товаров
def apply_discount(products):
    if products['category'] == 'electronics':
        products['price'] = products['price'] - products['price'] * 0.1
    return products

products = [{'name': 'Laptop', 'price': 1000, 'category': 'electronics'},
            {'name': 'Shirt', 'price': 50, 'category': 'clothing'},
            {'name': 'Phone', 'price': 600, 'category': 'electronics'}]

discounted_products = list(map(apply_discount, products))
print(discounted_products)

# 6 Удаление товаров с низким рейтингом через filter
def check_rate(products):
    return products['rating'] > 4

products = [{'name': 'Laptop', 'rating': 4.5},
            {'name': 'Shirt', 'rating': 3.8},
            {'name': 'Phone', 'rating': 4.2}]
high_rating_products = list(filter(check_rate, products))
print(high_rating_products)

# 7 Перевод в рубли через map
def to_rub(price):
    price = price * 75
    return price

prices_usd = [10, 20, 30, 40]
prices_rub = list(map(to_rub, prices_usd))
print(prices_rub)

# 8 Отбор участников старше 18 лет
def check_age(participants):
    return participants["age"] > 18

participants = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 16},
    {"name": "Diana", "age": 22},]
adults = list(filter(check_age, participants))
print(adults)

# 9 Генерация строк описания товаров через map
def format_product(product):
    product_str = 'Товар:' + product['name'] + ', ' 'Цена: ' + str(product['price'])
    return product_str

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Shirt", "price": 50},
    {"name": "Phone", "price": 600}]
descriptions = list(map(format_product, products))
print(descriptions)

# 10 Фильтр по ключевому слову в названии
def check_name(product):
    return 'Phone' in product['name']

products = [
    {"name": "Laptop", "price": 1000},
    {"name": "Phone Case", "price": 30},
    {"name": "Phone", "price": 600},
]
phones = list(filter(check_name, products))
print(phones)

# 11 Сумма произвольного количества чисел (*args)
def sum_numbers(*args):
    res = 0
    for num in args:
        res += num
    return res

result = sum_numbers(1, 2, 3, 4, 5)
print(result)

# 12 Наибольшее число из *args
def max_number(*args):
    num_max = 0
    for num in args:
        if num > num_max:
            num_max = num
    return num_max

result = max_number(10, 25, 50, 5, 30)
print(result)

# 13 Приветствие произвольного количества людей (*args)
def greet_people(*args):
    for person in args:
        print(f'Привет, {person}!')
    return

greet_people("Alice", "Bob", "Charlie")

# 14 Создание словаря из ключей и значений (**kwargs)
def create_dict(**kwargs):
    res = {}
    res.update(kwargs)
    return res

result = create_dict(name="Alice", age=25, city="New York")
print(result)

# 15 Форматирование текста с помощью **kwargs
def format_text(template, **kwargs):
    res = template.format(name = kwargs['name'], city = kwargs['city'])
    return res

result = format_text("Привет, {name}! Ты живешь в {city}.", name = "Alice", city = "New York")
print(result)

# 16 Объединение списков через *args
def merge_lists(*args):
    res = []
    for i in range(len(args)):
        for element in args[i]:
            res.append(element)
    return res

result = merge_lists([1, 2], [3, 4], [5, 6])
print(result)

# 17 Фильтрация параметров через **kwargs
def filter_kwargs(**kwargs):
    res = {}
    for num in kwargs.items():
        x, y  = num
        if y > 10:
            dict = {x : y}
            res.update(dict)
    return res

result = filter_kwargs(a=5, b=15, c=25, d=8)
print(result)

# 18 Комбинация *args и **kwargs
def send_messages(*args, **kwargs):
   for name in args:
    print(f'Привет, {name} ! {kwargs["message"]}')

send_messages("Alice", "Bob", message="У вас новое уведомление!")

# 19 Сложение чисел и ключевых параметров
def sum_args_kwargs(*args, **kwargs): 
    all_val = list(str(kwargs.values()))
    res = sum(args)
    for elem in all_val:
        if elem.isdigit():
            res += int(elem)
    return res

result = sum_args_kwargs(1, 2, 3, x=4, y=5, z="не число")
print(result)

# 20 Проверка ключевых аргументов (**kwargs)
def check_required(**kwargs):
    if 'required' in kwargs:
        return kwargs['required']
    else:
        return 'Ключ не найден'

result1 = check_required(required="Это важно", optional="Это не важно")
result2 = check_required(optional="Это не важно")
print(result1)
print(result2)    