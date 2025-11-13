import random

def gen_random(num_count, begin, end):
    nums = [random.randint(begin, end) for i in range(num_count)]

    return nums  

if __name__ == "__main__":
    print(gen_random(5, 1, 3))