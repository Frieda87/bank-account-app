import unittest
from account import Account

'''class TestAccount(unittest.TestCase):

    def test_wrong_user_first_function(self):
        wrong_user = display_balance(1234, "user_two")
        self.assertEqual(wrong_user, "Your pin is incorrect.")
    
    def test_right_input_first_function(self):
        right_user_pin = display_balance(2222, "user_two")
        self.assertEqual(right_user_pin, "Your balance is 100 Euro.")
    
    def test_error_second_function(self):
        with self.assertRaises(TypeError):
            withdraw_money(1234, "user_one")
    
    def test_full_input_one_wrong_second_function(self):
        wrong_pin = withdraw_money(1233, "user_one", 30)
        self.assertEqual(wrong_pin, "Your pin is incorrect.")
    
    def test_all_correct_second_function(self):
        all_corr = withdraw_money(2222, "user_two", 40)
        self.assertEqual(all_corr, "Withdrew 40 EUR. New balance is: 1237 EUR.")'''

class TestAccountTwo(unittest.TestCase):

    def test_balance_class(self):
        account1 = Account("user_one", 1234)
        balance_user_class = account1.display_balance()
        self.assertEqual(balance_user_class, "Your balance is 2000 Euro.")
    
    def test_withdraw_class(self):
        account1 = Account("user_one", 1234)
        withdraw_money_class = account1.withdraw_money(40)
        self.assertEqual(withdraw_money_class, "Withdrew 40 EUR. New balance is: 1960 EUR.")
    
    def test_error_withdraw_class(self):
        account1 = Account("user_one", 1234)
        with self.assertRaises(TypeError):
            account1.withdraw_money("hello error")
    
    def test_too_greedy(self):
        account1 = Account("user_one", 1234)
        too_greedy_withdrawl = account1.withdraw_money(3000)
        self.assertEqual(too_greedy_withdrawl, "You are not allowed to withdraw more money than you have on your account!")

if __name__ == '__main__':
    unittest.main()