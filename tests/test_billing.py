from screens.bill import format_brl, parse_brl_to_cents


def test_parse_brl_values():
    assert parse_brl_to_cents("350,00") == 35000
    assert parse_brl_to_cents("R$ 1.234,56") == 123456
    assert parse_brl_to_cents("0,99") == 99
    assert parse_brl_to_cents("-10,00") is None
    assert parse_brl_to_cents("abc") is None


def test_format_brl():
    assert format_brl(123456) == "R$ 1234,56"
