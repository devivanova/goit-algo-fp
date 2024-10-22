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
    ratio = [(name, info['calories'] / info['cost'])
             for name, info in items.items()]

    ratio.sort(key=lambda x: x[1], reverse=True)

    total_calories = 0
    selected_items = []

    for name, _ in ratio:
        cost = items[name]['cost']
        calories = items[name]['calories']

        if budget >= cost:
            selected_items.append(name)
            total_calories += calories
            budget -= cost

    return selected_items, total_calories


# Динамічне програмування
def dynamic_programming(items, budget):

    n = len(items)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    item_list = list(items.keys())

    for i in range(1, n + 1):
        item_name = item_list[i - 1]
        cost = items[item_name]['cost']
        calories = items[item_name]['calories']

        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]

            if b >= cost:
                dp[i][b] = max(dp[i][b], dp[i - 1][b - cost] + calories)

    total_calories = dp[n][budget]
    selected_items = []
    b = budget
    for i in range(n, 0, -1):
        if dp[i][b] != dp[i - 1][b]:
            selected_items.append(item_list[i - 1])
            b -= items[item_list[i - 1]]['cost']

    return selected_items, total_calories


budget = 100

selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print(f"Жадібний алгоритм вибрав: {
      selected_items_greedy}, сумарна калорійність: {total_calories_greedy}")

selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print(f"Динамічне програмування вибрало: {
      selected_items_dp}, сумарна калорійність: {total_calories_dp}")
