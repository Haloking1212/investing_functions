purch_total_cost = 0
cur_shares_amount = 0
purch_share_amount = 0
desired_share_price = 0


def avg_share_cost(purch_total_cost, cur_shares_amount, purch_share_amount, desired_share_price):
    total_shares = 0
    total_cost = 0
    total_cost += (desired_share_price * purch_share_amount) + purch_total_cost
    total_shares += cur_shares_amount + purch_share_amount
    return f"Your new avg cost is: {total_cost / total_shares} if you purchased {purch_share_amount} shares at {desired_share_price}"

"""
input 4 numbers to use the function 
first number - how much you currently paid for all your shares
second_number - how many shares you currently have
third_number - how many shares you want to purchase
fourth_number - what price you want to buy the shares at.
"""
print(avg_share_cost(4217, 1000, 2000, 3.8))


