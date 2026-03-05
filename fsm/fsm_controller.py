import csv
from policies.policy_actions import apply_policy

TRS_FILE = "metrics/trs_output.csv"

NORMAL = "NORMAL"
WARNING = "WARNING"
HIGH_RISK = "HIGH_RISK"
THRASHING = "THRASHING_IMMINENT"
RECOVERY = "RECOVERY"

state = NORMAL

context = {
    "frames": 5,
    "base_frames": 5,
    "throttled": False
}

def trs_to_symbol(trs):
    if trs < 0.4:
        return "LOW"
    elif trs < 0.6:
        return "MEDIUM"
    elif trs < 0.75:
        return "HIGH"
    else:
        return "CRITICAL"

def transition(current_state, symbol):
    if current_state == NORMAL:
        if symbol == "MEDIUM":
            return WARNING
        elif symbol in ["HIGH", "CRITICAL"]:
            return HIGH_RISK

    elif current_state == WARNING:
        if symbol == "LOW":
            return NORMAL
        elif symbol == "HIGH":
            return HIGH_RISK

    elif current_state == HIGH_RISK:
        if symbol == "LOW":
            return RECOVERY
        elif symbol == "CRITICAL":
            return THRASHING

    elif current_state == THRASHING:
        if symbol in ["LOW", "MEDIUM"]:
            return RECOVERY

    elif current_state == RECOVERY:
        if symbol == "LOW":
            return NORMAL

    return current_state

print("\nFSM + Policy Controller Started\n")

with open(TRS_FILE, "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        window = row["window"]
        trs = float(row["TRS"])
        symbol = trs_to_symbol(trs)

        new_state = transition(state, symbol)

        print(f"Window {window} | TRS={trs:.3f} | {state} → {new_state}")

        apply_policy(new_state, context)

        state = new_state

