import random

print("Tossing a coin...")
results = [random.choice(["Heads", "Tails"]) for _ in range(3)]
for i, result in enumerate(results, 1):
    print(f"Round {i}: {result}")

heads = results.count("Heads")
tails = results.count("Tails")
print(f"Heads: {heads}, Tails: {tails}")
