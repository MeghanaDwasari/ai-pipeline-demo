from interest import calculate_interest

def test_interest_calculation():
    balance = 1000
    rate = 0.05
    expected = 50
    assert calculate_interest(balance, rate) == expected
