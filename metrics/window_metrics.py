WINDOW_SIZE = 50

log_file = "logs/vm_log.txt"
output_file = "metrics/window_metrics.csv"

steps = []
faults = []
pages = []

with open(log_file, "r") as f:
    for line in f:
        step, page, fault, frames = line.strip().split(",", 3)
        steps.append(int(step))
        pages.append(int(page))
        faults.append(int(fault))

windows = []

for i in range(0, len(steps), WINDOW_SIZE):
    window_faults = faults[i:i+WINDOW_SIZE]
    window_pages = pages[i:i+WINDOW_SIZE]

    if len(window_faults) == 0:
        continue

    fault_rate = sum(window_faults) / len(window_faults)
    working_set = len(set(window_pages))
    burstiness = sum(window_faults[-10:]) if len(window_faults) >= 10 else sum(window_faults)

    windows.append((i//WINDOW_SIZE, fault_rate, working_set, burstiness))

with open(output_file, "w") as f:
    f.write("window,fault_rate,working_set,burstiness\n")
    for w in windows:
        f.write(f"{w[0]},{w[1]:.3f},{w[2]},{w[3]}\n")

print("Windowed metrics generated successfully.")
print("Output written to metrics/window_metrics.csv")
