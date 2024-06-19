from token import Token


class UserLiquidityPool:
	@property
	def initial_amm(self):
		return self._initial_amm

	def __init__(self, initial_a: Token, initial_b: Token, pool_share: float = None, lp_tokens: float = None):
		self._pool_share = pool_share
		self._lp_tokens = lp_tokens

		self._initial_token_a = initial_a
		self._initial_token_b = initial_b
		self._initial_amm = self.get_amm(initial_a, initial_b)

	def get_liquidity_without_pool_rewards(self, token_a_to_b_course: dict):
		token_a_to_b_course_str = self._initial_token_a.title + '/' + self._initial_token_b.title
		a_to_b_course: float | None = token_a_to_b_course.get(token_a_to_b_course_str, None)
		if not a_to_b_course:
			raise f'Нет передан курс {token_a_to_b_course_str} токенов.'

		b_to_a_course = 1 / a_to_b_course

		b_token_amount = (self.initial_amm * b_to_a_course) ** .5
		a_token_amount = b_token_amount * a_to_b_course

		a = Token(self._initial_token_a.title, a_token_amount)
		b = Token(self._initial_token_b.title, b_token_amount)

		return a, b

	@staticmethod
	def calculate_profit(current_a: Token, current_b: Token, a_without_rewards: Token, b_without_rewards: Token):
		profit_a_amount = current_a.amount - a_without_rewards.amount
		profit_b_amount = current_b.amount - b_without_rewards.amount

		profit_a = Token(current_a.title, profit_a_amount)
		profit_b = Token(current_b.title, profit_b_amount)

		return profit_a, profit_b

	@staticmethod
	def calculate_percentage_profit(a_without_rewards, profit_a, b_without_rewards, profit_b):

		a_percentage_profit = profit_a.amount / a_without_rewards.amount * 100
		b_percentage_profit = profit_b.amount / b_without_rewards.amount * 100

		return a_percentage_profit, b_percentage_profit
	@staticmethod
	def get_amm(a: Token, b: Token) -> float:
		""" AMM: k = x * y """
		k = a.amount * b.amount
		return k
