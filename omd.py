from collections import Counter, defaultdict


def task_1():
    moscow = {201, 202, 203, 204}
    kazan = {203, 204, 205, 206}

    print(f"что можно забрать в любом из двух городов: {moscow & kazan}")
    print(f"что есть только в Москве: {moscow - kazan}")
    print(f"что есть только в Казани {kazan - moscow}")
    print(f"сколько разных товаров на обоих складах вместе: {len(moscow | kazan)}")


def task_2():
    queries = [
        "чехол",
        "iphone",
        "чехол",
        "наушники",
        "iphone",
        "iphone",
        "кабель",
        "чехол",
        "iphone",
    ]
    count_queries = Counter(queries).items()
    most_popular_query = max(count_queries, key=lambda x: x[1])
    single_queries = [query for query, count in count_queries if count == 1]
    print(f"сколько всего поисковых запросов в ленте: {len(queries)}")
    print(f"сколько раз ввели каждый запрос {count_queries}")
    print(f"какой запрос вводили чаще всего: {most_popular_query[0]}")
    print(f"какую долю всех поисков он занимает: {most_popular_query[1] / len(queries)}")
    print(f"какие запросы встретились один раз: {single_queries}")


def task_3():
    orders = [
        {"id": 1, "buyer": "anya", "status": "delivered", "amount": 900},
        {"id": 2, "buyer": "boris", "status": "returned", "amount": 4_500},
        {"id": 3, "buyer": "anya", "status": "delivered", "amount": 1_500},
        {"id": 4, "buyer": "vera", "status": "delivered", "amount": 3_200},
        {"id": 5, "buyer": "boris", "status": "delivered", "amount": 700},
        {"id": 6, "buyer": "gleb", "status": "returned", "amount": 2_100},
    ]
    sum_of_returned = sum([order["amount"] for order in orders if order["status"] == "returned"])
    users_returned_product = {order["buyer"] for order in orders if order["status"] == "returned"}
    num_of_orders_per_person = defaultdict(int)
    for order in orders:
        if order["status"] == "delivered":
            num_of_orders_per_person[order["buyer"]] += 1
    costs_of_delivered_orders = [order["amount"] for order in orders if order["status"] == "delivered"]
    print(f"на какую сумму оформили возвраты: {sum_of_returned}")
    print(f"кто хотя бы раз вернул заказ: {users_returned_product}")
    # Обернул в dict потому что выводилось defaultdict(<class 'int'> ...
    print(f"сколько заказов доставлено покупателю: {dict(num_of_orders_per_person)}")
    print(f"средний чек доставленных заказов: {sum(costs_of_delivered_orders) / len(costs_of_delivered_orders)}")


def task_4():
    days = [
        {"day": "пн", "orders": 20, "revenue": 40_000, "returns": 2},
        {"day": "вт", "orders": 16, "revenue": 19_200, "returns": 4},
        {"day": "ср", "orders": 25, "revenue": 55_000, "returns": 1},
        {"day": "чт", "orders": 10, "revenue": 12_000, "returns": 3},
        {"day": "пт", "orders": 30, "revenue": 48_000, "returns": 3},
    ]
    all_week_revenue = sum([day["revenue"] for day in days])
    biggest_revenue_day = max(days, key=lambda d: d["revenue"])["day"]
    avg_revenue_per_day = [[day["day"], day["revenue"] / day["orders"]] for day in days]
    days_of_returns = [day["day"] for day in days if day["returns"] / day["orders"] > 0.2]
    print(f"выручка за всю неделю: {all_week_revenue}")
    print(f"день с самой большой выручкой: {biggest_revenue_day}")
    print(f"средняя выручка на один заказ в каждый день: {avg_revenue_per_day}")
    print(f"дни, где возвратов больше 20% заказов: {days_of_returns}")


def task_5():
    reviews = [
        {"id": 1, "product": "Чехол", "stars": 5},
        {"id": 1, "product": "Чехол", "stars": 3},
        {"id": 1, "product": "Чехол", "stars": 4},
        {"id": 2, "product": "Наушники", "stars": 2},
        {"id": 2, "product": "наушники", "stars": 2},
        {"id": 2, "product": "НАУШНИКИ", "stars": 5},
        {"id": 3, "product": "Планшет", "stars": 5},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 4, "product": "Колонка", "stars": 4},
        {"id": 5, "product": "Кабель", "stars": 1},
    ]
    for review in reviews:
        review["product"] = review["product"].lower()

    num_of_product = defaultdict(int)
    sum_stars_of_product = defaultdict(int)
    for i in reviews:
        num_of_product[i["product"]] += 1
        sum_stars_of_product[i["product"]] += i["stars"]
    avg_mark_of_product = {i: sum_stars_of_product[i] / num_of_product[i] for i in num_of_product}
    worst_product_by_avg_mark = min(
        [(avg_mark_of_product[i], i) for i in avg_mark_of_product if num_of_product[i] >= 2]
    )
    num_product_of_one_two_star = 0
    for review in reviews:
        if review["stars"] <= 2:
            num_product_of_one_two_star += 1
    print(f"средняя оценка каждого товара: {avg_mark_of_product}")
    print(f"худший товар по средней оценке среди тех, у кого хотя бы два отзыва: {worst_product_by_avg_mark[1]}")
    print(f"сколько отзывов на 1 или 2 звезды: {num_product_of_one_two_star}")
    print(f"какую долю всех отзывов составляют отзывы на 1 или 2 звезды : {num_product_of_one_two_star / len(reviews)}")


if __name__ == "__main__":
    task_1()
    print()
    task_2()
    print()
    task_3()
    print()
    task_4()
    print()
    task_5()
