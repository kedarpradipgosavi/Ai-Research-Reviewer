def review_draft(draft):
    suggestions = []

    if len(draft.get("Abstract", "")) < 150:
        suggestions.append("Abstract may be too short; consider expanding it.")

    suggestions.append("Add citations and publication years for completeness.")
    suggestions.append("Consider including limitations and future work.")

    return suggestions
