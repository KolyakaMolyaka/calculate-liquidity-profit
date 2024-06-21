from user_liquidity_pool import UserLiquidityPool
from token import Token


def print_lines(sign: str, elements, delimiter='=', delimiter_repeats=15):
	print(sign)
	print(elements)
	print(delimiter * delimiter_repeats)


def delim(delimiter='=', repeats=10):
	print(delimiter * repeats)


if __name__ == '__main__':
	token_a_title = input('Token A title (e.g. "wNOT"): ')
	token_a_init_amount = float(input('Token A initial liquidity pool amount (e.g. "20000000"): '))

	token_b_title = input('Token B title (e.g. "TON"): ')
	token_b_init_amount = float(input('Token B initial liquidity pool amount (e.g. "23.23"): '))

	initial_a = Token(token_a_title, token_a_init_amount)
	initial_b = Token(token_b_title, token_b_init_amount)
	delim()
	print('Initial liquidity pool')
	print(initial_a)
	print(initial_b)

	liquidity = UserLiquidityPool(initial_a, initial_b)

	delim()
	token_a_cur_amount = float(input('Token A current liquidity pool amount (e.g. "20662657.9449"): '))
	token_b_cur_amount = float(input('Token B current liquidity pool amount (e.g. "30.89"): '))

	current_a = Token(token_a_title, token_a_cur_amount)
	current_b = Token(token_b_title, token_b_cur_amount)

	tokens_pair_str = f'{token_a_title}/{token_b_title}'
	token_a_to_b_course = current_a.amount / current_b.amount
	token_b_to_a_course = current_b.amount / current_a.amount

	a_without_rewards, b_without_rewards = liquidity.get_liquidity_without_pool_rewards(token_a_to_b_course,
																						token_b_to_a_course)

	delim()
	print('Tokens liquidity without pool rewards')
	print(a_without_rewards)
	print(b_without_rewards)

	profit_a, profit_b = UserLiquidityPool.calculate_profit(current_a, current_b, a_without_rewards, b_without_rewards)
	delim()
	print('Token profit from pool')
	print(profit_a)
	print(profit_b)

	profit_a_percentage, profit_b_percentage = UserLiquidityPool.calculate_percentage_profit(a_without_rewards,
																							 profit_a,
																							 b_without_rewards,
																							 profit_b)
	delim()
	print(f'Percentage profit from pool A: {profit_a_percentage}')
	print(f'Percentage profit from pool B: {profit_b_percentage}')

	delim()
	input('Enter to exit...')
