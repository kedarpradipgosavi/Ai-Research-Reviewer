def generate_draft(analysis):
    if not analysis:
        return {
            "Abstract": "No sufficient abstract data found.",
            "Methods": "Methodology details could not be extracted.",
            "Results": "Results could not be synthesized."
        }

    combined = " ".join(analysis)
    abstract = combined[:800] + "..." if len(combined) > 800 else combined

    methods = (
        "The selected studies use experimental evaluation, comparative analysis, "
        "and benchmark-based validation techniques."
    )

    results = (
        "The reviewed papers consistently report improvements over baseline methods "
        "in terms of accuracy, efficiency, or scalability."
    )

    return {
        "Abstract": abstract,
        "Methods": methods,
        "Results": results
    }
