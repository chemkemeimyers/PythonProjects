from Counter import Counter

def run_counter():

    c1 = Counter()

    c2 = Counter.from_string("10")

    c1.increment(5)
    c2.reset()

    print(f"Counter 1 has value:  {c1.value}")
    print(f"Counter 2 has value:  {c2.value}")

if __name__ == "__main__":
    run_counter()
 