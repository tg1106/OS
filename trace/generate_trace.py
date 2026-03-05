import random

TOTAL_ACCESSES = 1000
MAX_PAGE = 50
LOCALITY_PROB = 0.8

trace = []
current_base = random.randint(0, MAX_PAGE - 5)

for i in range(TOTAL_ACCESSES):
    if random.random() < LOCALITY_PROB:
        page = current_base + random.randint(0, 4)
    else:
        page = random.randint(0, MAX_PAGE)

    if page >= MAX_PAGE:
        page = random.randint(0, MAX_PAGE - 1)

    trace.append(page)

    if random.random() < 0.05:
        current_base = random.randint(0, MAX_PAGE - 5)

with open("trace/memory_trace.txt", "w") as f:
    for p in trace:
        f.write(str(p) + "\n")

print("Memory access trace generated successfully.")
