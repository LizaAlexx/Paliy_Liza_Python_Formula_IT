import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Считать содержимое csv файла
    with open(INPUT_FILENAME, 'r') as file:
        reader = csv.DictReader(file)
        data = list(reader)

    # Сериализовать в файл с отступами равными 4
    with open(OUTPUT_FILENAME, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
