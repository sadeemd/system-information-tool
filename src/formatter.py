def format_system_info(data: dict) -> str:
    """
    Format system information into a readable text layout.
    """

    lines = []

    for section, values in data.items():
        lines.append(f"{'=' * 20} {section} {'=' * 20}")

        for key, value in values.items():
            lines.append(f"{key:18}: {value}")

        lines.append("")

    return "\n".join(lines)