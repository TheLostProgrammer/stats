#!/usr/bin/python3
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

def calculate(titles, numbers):
    titles = [i.strip() for i in titles.split(",")]
    if len(numbers) % 2 == 0:
        q2 = (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2
        q3 = numbers[len(numbers) // 2:]
    else:
        q2 = numbers[len(numbers) // 2]
        q3 = numbers[len(numbers) // 2 + 1:]
    q1 = numbers[:len(numbers) // 2]
    q1 = q1[len(q1) // 2] if len(q1) % 2 != 0 else (q1[len(q1) // 2] + q1[len(q1) // 2 - 1]) / 2
    q3 = q3[len(q3) // 2] if len(q3) % 2 != 0 else (q3[len(q3) // 2] + q3[len(q3) // 2 - 1]) / 2
    iqr = q3 - q1
    print(f"Sorted: {', '.join(str(i) for i in numbers)}\nQ1: {q1}\nQ2/Median: {q2}\nQ3: {q3}\nIQR: {iqr}\nLower Outlier(s): {', '.join(str(i) for i in [i for i in numbers if i < q1 - (1.5 * iqr)])}\nUpper Outlier(s): {', '.join(str(i) for i in [i for i in numbers if i > q3 + (1.5 * iqr)])}\nMin: {min(numbers)}\nMax: {max(numbers)}\nRange: {max(numbers) - min(numbers)}\nMean: {round(sum(numbers) / len(numbers), 2)}")

    df = pd.DataFrame(data=numbers, columns=[titles[1]])
    boxplot = sns.boxplot(y="variable", x="value", data=pd.melt(df))
    if titles[0].startswith("-v"):
        boxplot = sns.stripplot(y="variable", x="value", marker="o", alpha=0.3, color="black", data=pd.melt(df))
    boxplot.axes.set_title(titles[0], fontsize=14)
    boxplot.set_xlabel(titles[2], fontsize=12)
    boxplot.set_ylabel(titles[3], fontsize=12)
    plt.show()
    return

print(calculate(input("Enter chart title [-v for stripplot], boxplot title and x-y axis titles (seperate by commas): "), sorted([float(i.strip()) for i in input("Enter some numbers: ").replace(",", ", ").split(" ")])))
