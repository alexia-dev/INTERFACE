from core.billing_format import format_brl, parse_decimal_amount


def test_parse_brl_values():
    assert parse_decimal_amount("350,00") == 35000
    assert parse_decimal_amount("R$ 1.234,56") == 123456
    assert parse_decimal_amount("0,99") == 99
    assert parse_decimal_amount("-10,00") is None
    assert parse_decimal_amount("abc") is None


def test_format_brl():
    assert format_brl(123456) == "R$ 1234,56"
