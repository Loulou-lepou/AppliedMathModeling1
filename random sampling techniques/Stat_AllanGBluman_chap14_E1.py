""" random sampling """
import random
import pandas as pd
import os


def random_sampling_(sample_size):
    """ sample of given size will be selected without replacement """
    population = list(range(100))
    # random.shuffle(population) -> create a permutation of the population
    # randomly select numbers with replacement
    random_numbers = [random.choice(population) for _ in range(100)]
    # display random number table in columns
    for _ in range(10):
        print(" ".join([str(random_numbers[_ + 10 * col]).zfill(2) for col in range(10)]))

    status = [1 <= _ <= 50 for _ in random_numbers]
    count = 0
    # use a list to preserve insertion order, membership testing takes a longer time than using a set
    sample = []
    max_index = len(random_numbers)
    index_ = random.choice(list(range(99)))
    current_num = random_numbers[index_]
    print("sample size = ", sample_size)
    print("starting position :", "row:", index_ % 10 + 1,
          "column:", index_ // 10 + 1, ", first num:", current_num)

    while count < sample_size:
        current_num = random_numbers[index_]
        if status[index_] and current_num not in sample:
            sample.append(current_num)
            count += 1
            status[index_] = False
        # else:
        #     message = "has been chosen" if 1<= current_num <= 50 else "is out of bound"
        #     print(f"{current_num} {message}")
        if index_ < max_index - 1:
            index_ += 1
        else:
            suffix = 's' if sample_size - count > 1 else ''
            print(f"sample: {sample}\nWe'll need {sample_size - count} more number{suffix}")
            index_ = random.choice(list(range(99)))
            print("next round, starting position :", "row:", index_ % 10 + 1,
                  "column:", index_ // 10 + 1, ", first num:", random_numbers[index_])
    return sample


os.chdir(r"C:\Users\Admin\PycharmProjects\NewLoulou2021\Fundamental Python June 2021\D2021_23_24\teaching\random sampling techniques")
data_frame = pd.read_csv("Stat2_E14_1.csv")
cities = data_frame[' City name']
# random sampling:
size = 20
sample_ = random_sampling_(size)
for _ in sample_:
    print(f"{str(_).zfill(2)}.{cities[_ - 1]}")
