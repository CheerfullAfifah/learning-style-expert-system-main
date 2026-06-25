from rules import (
    RULES,
    FORWARD_RULES
)

def forward_chaining(facts):

    working_memory = set(facts)

    trace = []

    fired_rules = []

    changed = True

    while changed:

        changed = False

        for rule in FORWARD_RULES:

            if all(
                cond in working_memory
                for cond in rule["if"]
            ):

                conclusion = rule["then"]

                if conclusion not in working_memory:

                    working_memory.add(
                        conclusion
                    )

                    fired_rules.append(
                        rule["id"]
                    )

                    trace.append(
                        f"{rule['id']} FIRED -> {conclusion}"
                    )

                    changed = True

    visual_count = len([
        x for x in facts
        if x in RULES["visual"]
    ])

    auditory_count = len([
        x for x in facts
        if x in RULES["auditory"]
    ])

    kinesthetic_count = len([
        x for x in facts
        if x in RULES["kinesthetic"]
    ])

    if "visual" in working_memory:

        goal = "visual"

    elif "auditory" in working_memory:

        goal = "auditory"

    elif "kinesthetic" in working_memory:

        goal = "kinesthetic"

    else:

        goal = max(
            {
                "visual": visual_count,
                "auditory": auditory_count,
                "kinesthetic": kinesthetic_count
            },
            key=lambda x: {
                "visual": visual_count,
                "auditory": auditory_count,
                "kinesthetic": kinesthetic_count
            }[x]
        )

    trace.append(
        f"\nGOAL FIRED -> {goal.upper()}"
    )

    return {

        "goal": goal,

        "visual_count": visual_count,

        "auditory_count": auditory_count,

        "kinesthetic_count": kinesthetic_count,

        "rule_trace": "\n".join(trace)

    }