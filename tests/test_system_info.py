from src.system_info import get_system_info


def test_get_system_info_returns_dictionary():
    info = get_system_info()

    assert isinstance(info, dict)


def test_system_info_contains_required_sections():
    info = get_system_info()

    expected_sections = [
        "General",
        "Operating System",
        "Hardware",
        "Network",
        "Battery",
        "Software",
    ]

    for section in expected_sections:
        assert section in info