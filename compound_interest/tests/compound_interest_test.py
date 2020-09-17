import unittest

from src.compound_interest import CompoundInterest

class CompoundInterestTest(unittest.TestCase):
    def setUp(self):
        self.compound_interest = CompoundInterest(100, 10, 20)

    # Tests

    def test_rate_divided_by_years(self):
        self.assertEqual(0.5, self.compound_interest.rate_divided_by_years())

    def test_principal_multiply_rate_and_years(self):
        self.assertEqual(150, self.compound_interest.principal_multiply_rate_and_years())
    
    def test_number_of_iterations_multiply_time_in_years(self):
        self.assertEqual(240, self.compound_interest.number_of_iterations_multiply_time_in_years())
    
    def test_compound_interest(self):
        self.assertEqual(732.81, (self.compound_interest.principal_multiply_rate_and_years) ** self.compound_interest.number_of_iterations_multiply_time_in_years)
        
    # Should return 732.81 given 100 principal, 10 percent, 20 years

    # def test_returns(self):
    #     self.assertEqual(732.81, self.compound_interest.calculate_interest())

    # Should return 181.94 given 100 principal, 6 percent, 10 years

    # Should return 149,058.55 given 100000 principal, 5 percent, 8 years

    # Should return 0.00 given 0 principal, 10 percent, 1 year

    # Should return 100.00 given 100 principal, 0 percent, 10 years


    # Extention tests

    # Should return 118,380.16 given 100 principal, 5 percent, 8 years, 1000 per month

    # Should return 156,093.99 given 100 principal, 5 percent, 10 years, 1000 per month

    # Should return 475,442.59 given 116028.86, 7.5 percent, 8 years, 2006 per month

    # Should return 718,335.96 given 116028.86 principal, 9 percent, 12 years, 1456 per month

