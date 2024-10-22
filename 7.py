import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):

    sum_counts = {i: 0 for i in range(2, 13)}

    for _ in range(num_rolls):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        roll_sum = die1 + die2
        sum_counts[roll_sum] += 1

    probabilities = {roll_sum: (count / num_rolls)
                     * 100 for roll_sum, count in sum_counts.items()}

    return sum_counts, probabilities


def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    plt.bar(sums, probs, color='skyblue')
    plt.xlabel("Сума")
    plt.ylabel("Ймовірність (%)")
    plt.title("Ймовірності сум при киданні двох кубиків (Метод Монте-Карло)")
    plt.xticks(sums)
    plt.show()


num_rolls = 100000
sum_counts, probabilities = simulate_dice_rolls(num_rolls)

print("Суми та їх ймовірності (у відсотках):")
for roll_sum, prob in probabilities.items():
    print(f"Сума: {roll_sum}, Ймовірність: {prob:.2f}%")

plot_probabilities(probabilities)
