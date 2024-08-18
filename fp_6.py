# Визначаємо страви з їх вартістю та калорійністю
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


# Жадібний алгоритм
def greedy_algorithm(items, budget):
    # Обчислюємо співвідношення калорій до вартості для кожного предмету
    items_sorted = sorted(items.items(), key=lambda x: x[1]["calories"] / x[1]["cost"], reverse=True)

    total_calories = 0
    remaining_budget = budget
    chosen_items = []

    for item, details in items_sorted:
        if details["cost"] <= remaining_budget:
            # Вибираємо страву, якщо її вартість не перевищує залишковий бюджет
            total_calories += details["calories"]
            remaining_budget -= details["cost"]
            chosen_items.append(item)

    return total_calories, budget - remaining_budget, chosen_items


# Алгоритм динамічного програмування
def dynamic_programming(items, budget):
    item_names = list(items.keys())
    n = len(items)

    # Створюємо таблицю DP, де рядки — страви, стовпці — можливий бюджет
    dp_table = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]

    # Заповнюємо таблицю DP
    for i in range(1, n + 1):
        item_name = item_names[i - 1]
        item_cost = items[item_name]["cost"]
        item_calories = items[item_name]["calories"]
        
        for j in range(1, budget + 1):
            if item_cost <= j:
                # Вибираємо максимальне значення між двома варіантами:
                # 1. Не вибираємо цей елемент
                # 2. Вибираємо цей елемент і додаємо його калорії до значення dp[i-1][j-item_cost]
                dp_table[i][j] = max(dp_table[i - 1][j], dp_table[i - 1][j - item_cost] + item_calories)
            else:
                # Якщо не можемо вибрати страву через обмеження бюджету
                dp_table[i][j] = dp_table[i - 1][j]

    # Відновлюємо набір страв з таблиці DP
    chosen_items = []
    temp_budget = budget
    for i in range(n, 0, -1):
        if dp_table[i][temp_budget] != dp_table[i - 1][temp_budget]:
            chosen_items.append(item_names[i - 1])
            temp_budget -= items[item_names[i - 1]]["cost"]

    return dp_table[n][budget], budget - temp_budget, chosen_items


if __name__ == '__main__':
    # Виконання обох алгоритмів
    budget = 100

    greedy_result = greedy_algorithm(items, budget)
    dp_result = dynamic_programming(items, budget)

    print("Жадібний алгоритм: ", greedy_result)
    print("Динамічне програмування: ", dp_result)
