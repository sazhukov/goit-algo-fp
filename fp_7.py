import random
import matplotlib.pyplot as plt


def simulate_dice_rolls(num_rolls):
    # Ініціалізація словника для підрахунку появ кожної суми
    sum_counts = {i: 0 for i in range(2, 13)}

    # Симуляція кидків
    for _ in range(num_rolls):
        # Кидок двох кубиків
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        dice_sum = dice1 + dice2

        # Підрахунок кількості появ кожної суми
        sum_counts[dice_sum] += 1

    # Обчислення ймовірності появ кожної суми
    probabilities = {s: count / num_rolls for s, count in sum_counts.items()}

    return probabilities

def plot_probabilities(probabilities):
    sums = list(probabilities.keys())
    probs = list(probabilities.values())

    # Створення графіка
    plt.bar(sums, probs, tick_label=sums)
    plt.xlabel('Сума чисел на кубиках')
    plt.ylabel('Ймовірність')
    plt.title('Ймовірність суми чисел на двох кубиках')

    # Додавання відсотків випадання на графік
    for i, prob in enumerate(probs):
        plt.text(sums[i], prob, f"{prob*100:.2f}%", ha='center')

    plt.show()
    
def analytical_probabilities():
    analytical_prob = {
        2: 1 / 36 * 100,
        3: 2 / 36 * 100,
        4: 3 / 36 * 100,
        5: 4 / 36 * 100,
        6: 5 / 36 * 100,
        7: 6 / 36 * 100,
        8: 5 / 36 * 100,
        9: 4 / 36 * 100,
        10: 3 / 36 * 100,
        11: 2 / 36 * 100,
        12: 1 / 36 * 100,
    }

    return analytical_prob

def compare_results(simulation_prob, analytical_prob):
    print("\nПорівняння імовірностей:")
    for outcome, prob in analytical_prob.items():
        simulation_prob_percentage = simulation_prob[outcome]
        print(
            f"Сума {outcome}: Метод Монте-Карло - {simulation_prob_percentage*100:.2f}%, Аналітичний розрахунок - {prob:.2f}%"
        )

if __name__ == "__main__":
    # Виведення результатів для різної кількості кидків
    for accuracy in [100, 1000, 10000, 100000]:
        print(f"Симуляція для {accuracy} кидків:")
        probabilities = simulate_dice_rolls(accuracy)
        for dice_sum, prob in probabilities.items():
            print(f"Сума: {dice_sum}, Ймовірність: {prob*100:.2f}%")

        # Побудова графіку
        plot_probabilities(probabilities)
        
    analytical_probabilities = analytical_probabilities()
    compare_results(probabilities, analytical_probabilities)