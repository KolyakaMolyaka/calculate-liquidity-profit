from user_liquidity_pool import UserLiquidityPool
from token import Token


def print_lines(sign: str, elements, delimiter='=', delimiter_repeats=15):
	print(sign)
	print(elements)
	print(delimiter * delimiter_repeats)


if __name__ == '__main__':
	initial_a = Token('wNOT', float(20_000_000))  # wNOT 20_000_000
	initial_b = Token('TON', 23.23)  # TON 23.34
	print('Initial Pool', [initial_a, initial_b])

	liquidity = UserLiquidityPool(initial_a, initial_b)
	tokens_course = {'wNOT/TON': 20_662_657 / 30.89}
	a_without_rewards, b_without_rewards = liquidity.get_liquidity_without_pool_rewards(tokens_course)
	print('Pool without rewards', [a_without_rewards, b_without_rewards, tokens_course])

	current_a = Token('wNOT', 20_662_657.9449)
	current_b = Token('TON', 30.8939)

	profit_a, profit_b = UserLiquidityPool.calculate_profit(current_a, current_b, a_without_rewards, b_without_rewards)
	print('Profit from pool', [profit_a, profit_b])

	profit_a_percentage, profit_b_percentage = UserLiquidityPool.calculate_percentage_profit(a_without_rewards,
																							 profit_a,
																							 b_without_rewards,
																							 profit_b)
	print('Percentage profit from pool', [profit_a_percentage, profit_b_percentage])
