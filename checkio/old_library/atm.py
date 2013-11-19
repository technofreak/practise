

from decimal import Decimal, ROUND_DOWN

__author__ = 'parthan'

def checkio(inputs):
    init_bal, withdrawals = inputs[0], inputs[1]
    curr_bal = Decimal(str(init_bal))
    for amount in withdrawals:
        amount = Decimal(str(amount))
        if (amount - Decimal('0.5') - Decimal('0.01')*amount) < Decimal('5.0'):
            continue
        bal = curr_bal - amount - Decimal('0.5') - Decimal('0.01')*amount
        if bal > Decimal('0'):
            curr_bal = bal.quantize(Decimal('1.'), rounding=ROUND_DOWN)
        else:
            continue
    return int(curr_bal)

if __name__ == "__main__":
    assert checkio([120, [10 , 20, 30]]) == 57, 'First'

    # With one Insufficient Funds, and then withdraw 10 $
    assert checkio([120, [200 , 10]]) == 109, 'Second'

    #with one incorrect amount
    assert checkio([120, [3, 10]]) == 109, 'Third'

    assert checkio([120, [200, 119]]) == 120 , 'Fourth'

    assert checkio([120, [120, 10, 122, 2, 10, 10, 30, 1]]) == 56, "It's mixed all base tests"

    print 'All Ok'
