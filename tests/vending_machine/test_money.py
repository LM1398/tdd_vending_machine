from vending_machine.money import M_10


def test_money_10_amount():
    actual = M_10.amount
    expected = 10
    assert actual == expected
