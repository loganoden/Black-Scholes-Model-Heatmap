from numpy import exp, sqrt, log
from scipy.stats import norm

class BlackScholesModel:
    def __init__(self, time_to_maturity, strike, current_price, volatility, interest_rate):
        self.time_to_maturity = time_to_maturity
        self.strike = strike
        self.current_price = current_price
        self.volatility = volatility
        self.interest_rate = interest_rate

    def calculate(self):
        first_term = norm.cdf(self.d1()) * self.current_price
        second_term = norm.cdf(self.d2()) * self.strike * exp(-self.interest_rate * self.time_to_maturity)
        return first_term - second_term

    def d1(self):
        first_term_num = log(self.current_price / self.strike)
        second_term_num = (self.interest_rate + ((self.volatility ** 2) / 2)) * self.time_to_maturity
        first_term_denom = self.volatility * sqrt(self.time_to_maturity)
        return (first_term_num + second_term_num) / first_term_denom

    def d2(self):
        return self.d1() - self.volatility * sqrt(self.volatility)

B = BlackScholesModel(1, 100, 100, .2, .05)
print(B.calculate())

# Output: 7.965567455405891