class CompoundInterest:
    # A = principal(1 + rate/number of iterations)**number of iterations, time in years
    def __init__(self, principal, rate, time_in_years):
        
        self.principal = principal
        self.rate = rate
        self.number_of_iterations = 12
        self.time_in_years = time_in_years
    
    def rate_divided_by_years(self):
        return self.rate / self.time_in_years
    
    def principal_multiply_rate_and_years(self):
        return self.principal * (1 + self.rate_divided_by_years())
    
    def number_of_iterations_multiply_time_in_years(self):
        return self.number_of_iterations * self.time_in_years
    
    def compound_interest(self):
        return (self.compound_interest.principal_multiply_rate_and_years) pow(self.compound_interest.number_of_iterations_multiply_time_in_years)
    
