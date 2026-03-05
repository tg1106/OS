import csv

INPUT_FILE = "metrics/window_metrics.csv"
OUTPUT_FILE = "metrics/trs_output.csv"

MAX_WORKING_SET = 50      # Max pages in system
MAX_BURSTINESS = 10       # Max faults in recent window

trs_data = []

with open(INPUT_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        window = int(row["window"])
        fault_rate = float(row["fault_rate"])
        working_set = int(row["working_set"])
        burstiness = int(row["burstiness"])

        working_set_norm = min(working_set / MAX_WORKING_SET, 1.0)
        burstiness_norm = min(burstiness / MAX_BURSTINESS, 1.0)

        trs = (
            0.5 * fault_rate +
            0.3 * working_set_norm +
            0.2 * burstiness_norm
        )

        trs = min(trs, 1.0)

        trs_data.append((window, fault_rate, working_set, burstiness, round(trs, 3)))

with open(OUTPUT_FILE, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["window", "fault_rate", "working_set", "burstiness", "TRS"])
    for row in trs_data:
        writer.writerow(row)

print("TRS computation completed successfully.")
print("Output written to metrics/trs_output.csv")
