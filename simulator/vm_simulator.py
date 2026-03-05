from collections import OrderedDict

FRAME_COUNT = 5
PAGE_FAULTS = 0
MEMORY = OrderedDict()

trace_file = "trace/memory_trace.txt"
log_file = "logs/vm_log.txt"

def access_page(page, step):
    global PAGE_FAULTS, MEMORY

    fault = 0

    if page in MEMORY:
        MEMORY.move_to_end(page)
    else:
        PAGE_FAULTS += 1
        fault = 1
        if len(MEMORY) >= FRAME_COUNT:
            MEMORY.popitem(last=False)
        MEMORY[page] = True

    return fault

with open(trace_file, "r") as f, open(log_file, "w") as log:
    for step, line in enumerate(f):
        page = int(line.strip())
        fault = access_page(page, step)
        log.write(f"{step},{page},{fault},{list(MEMORY.keys())}\n")

print("Simulation completed.")
print("Total Page Faults:", PAGE_FAULTS)
print("Log written to logs/vm_log.txt")

