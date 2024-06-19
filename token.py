class Token:
	def __init__(self, title: str, amount: float):
		self.title = title
		self.amount = amount

	def __str__(self):
		return f'<Token: title={self.title}, amount={self.amount}>'

	def __repr__(self):
		return self.__str__()
