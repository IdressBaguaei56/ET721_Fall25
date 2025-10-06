"""
Idress Baguaei 
Lab 8, unittest
Sep 29, 2025 
"""
import unittest
from bankaccount import BankAccount

print("\n ----- Example 1: setUp with default BankAccount -----")


class TestBankAccount(unittest.TestCase):

    # Use setUp to create a default account before each test
    def setUp(self):
        self.account = BankAccount(owner="Alice", balance=100)

    print("\n ----- Example 2: initialization and basic operations -----")
    # Test that the account is initialized with the correct balance

    def test_initial_balance(self):
        self.assertEqual(self.account.get_balance(), 100)

    # Test that a deposit operation correctly adds the specified amount
    def test_deposit_adds_to_balance(self):
        self.account.deposit(50)
        self.assertEqual(self.account.get_balance(), 150)

    # Test that a withdrawal operation correctly subtracts the specified amount
    def test_withdraw_subtracts_from_balance(self):
        self.account.withdraw(40)
        self.assertEqual(self.account.get_balance(), 60)

    print("\n ----- Example 3: exception handling and sequences -----")
    # Test that attempting to withdraw more than the available balance raises the appropriate exception

    def test_withdraw_more_than_balance_raises(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(200)

    # Test a sequence of deposits and withdrawals to ensure correct balance calculations
    def test_sequence_of_transactions(self):
        # Start: 100
        self.account.deposit(25)     # 125
        self.account.withdraw(10)    # 115
        self.account.deposit(5)      # 120
        self.account.withdraw(20)    # 100
        self.assertEqual(self.account.get_balance(), 100)


if __name__ == "__main__":
    unittest.main()
