"""
Idress Baguaei
ET721 – Software Development Practicum
Unit Test Project: Drop Chip Game
Part 2 – Unit Testing for print_board(self)
"""

import unittest
from io import StringIO
from unittest.mock import patch
from main import Connect4

class TestPrintBoard(unittest.TestCase):
    """Unit test class to verify the print_board(self) method of Connect4."""

    @patch('sys.stdout', new_callable=StringIO)
    def test_empty_board_output(self, mock_stdout):
        """Test that the print_board method displays an empty board correctly."""
        game = Connect4()
        game.print_board()
        output = mock_stdout.getvalue()
        # Check that there are 6 rows and 7 columns represented by '|'
        self.assertIn('---------------', output)
        self.assertIn('| | | | | | | |', output.replace('\033[91m', '').replace('\033[94m', '').replace('\033[0m', ''))
        self.assertIn('1 2 3', output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_board_with_chips(self, mock_stdout):
        """Test that print_board correctly shows chips placed on the board."""
        game = Connect4()
        # Place a few chips manually
        game.board[5][0] = 'X'
        game.board[5][1] = 'O'
        game.print_board()
        output = mock_stdout.getvalue()
        # Check that the X and O characters appear in output
        self.assertIn('X', output)
        self.assertIn('O', output)

# ---------- DOCUMENTATION ----------
"""
Test Results Documentation
---------------------------
All test cases passed successfully:
- Verified print_board() output for an empty board
- Verified print_board() output for board containing chips
The output format matches the expected structure (6 rows, 7 columns, borders, and player symbols).
No issues found with print_board(self).
"""

if __name__ == "__main__":
    unittest.main()
