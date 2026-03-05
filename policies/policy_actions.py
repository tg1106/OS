def apply_policy(state, context):
    if state == "NORMAL":
        print("Action: Default LRU | Frames =", context["frames"])

    elif state == "WARNING":
        print("Action: Monitoring | Preparing mitigation")

    elif state == "HIGH_RISK":
        context["frames"] += 2
        print("Action: Increased frames to", context["frames"])

    elif state == "THRASHING_IMMINENT":
        context["throttled"] = True
        print("Action: Throttling workload")

    elif state == "RECOVERY":
        if context["frames"] > context["base_frames"]:
            context["frames"] -= 1
        context["throttled"] = False
        print("Action: Recovery | Frames =", context["frames"])
