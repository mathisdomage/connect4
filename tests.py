import unittest
from connect4 import winning_move

class TestWinningMoveMethod(unittest.TestCase):

    def test_win(self):
        self.assertTrue(winning_move(
        [[1, 1, 1, 1],
         [2, 2, 2],
         [],
         [],
         [],
         [],
         []],
        0
        ))                
        self.assertTrue(winning_move(
        [[1, 1, 1, 2],
         [2, 1, 2],
         [1, 2, 1],
         [1, 2, 2, 1],
         [2],
         [],
         []],
        3
        ))
        self.assertTrue(winning_move(
        [[1,2],
         [1],
         [1,2],
         [1],
         [2],
         [],
         []],
        1 
        ))
        self.assertTrue(winning_move(
        [[2,1,2,1],
         [2,2,1],
         [1,1,1,2],
         [1],
         [2],
         [],
         []],
        1 
        ))
        self.assertTrue(winning_move(
        [[2,2,2,2],
         [1,1,1],
         [1,1],
         [2],
         [],
         [],
         [],
        ],
        0
        ))
        self.assertTrue(winning_move(
        [[1],
         [1],
         [1],
         [1],
         [2],
         [2],
         [2]],
        2
        ))
        self.assertTrue(winning_move(
        [[1,2],
         [1],
         [1,2],
         [1],
         [2],
         [],
         []],
        3 
        ))
        self.assertTrue(winning_move(
        [[1,2],
         [1,2],
         [1],
         [1],
         [],
         [],
         [2]],
        3 
        ))
        self.assertTrue(winning_move(
        [[2,1,2,1],
         [2,2,1,2],
         [1,1,1,2],
         [1],
         [],
         [],
         []],
        0 
        ))
        self.assertTrue(winning_move(
        [[2,1,2,1],
         [2,2,1,2],
         [1,1],
         [1],
         [],
         [],
         []],
        2 
        ))
        self.assertTrue(winning_move(
        [[2,1,2,1],
         [2,2,1,2],
         [1,1,1,2,1],
         [1],
         [2],
         [],
         []],
        3 
        ))
        self.assertTrue(winning_move(
        [[1, 1, 1, 2],
         [2, 1, 2],
         [1, 2],
         [2, 2, 1, 1],
         [2],
         [],
         []],
        2
        ))
        self.assertTrue(winning_move(
        [[1, 1, 1, 2],
         [2, 1, 2],
         [1, 2, 1],
         [2, 2, 1, 2],
         [2],
         [2],
         [1,1]],
        1
        ))
        self.assertTrue(winning_move(
            [[1, 1, 1, 2],
             [2, 1, 2],
             [1, 2, 1],
             [2, 2, 1, 2],
             [2,2],
             [1],
             [1]],
            0
        ))

    def test_lose(self):
        self.assertFalse(winning_move(
            [[],
             [],
             [],
             [],
             [],
             [],
             []],
            0
        ))
        self.assertFalse(winning_move(
            [[1,1,1],
             [2,2,2],
             [],
             [],
             [],
             [],
             []],
            0
        ))
        self.assertFalse(winning_move(
            [[1,1,1,2],
             [2,2],
             [],
             [],
             [],
             [],
             []],
            0
        ))
        self.assertFalse(winning_move(
            [[1],
             [],
             [],
             [],
             [],
             [],
             []],
            0
            ))
        self.assertFalse(winning_move(
            [[1,2],
             [],
             [],
             [],
             [],
             [],
             []],
            0
        ))
        self.assertFalse(winning_move(
            [[1],
             [2],
             [],
             [],
             [],
             [],
             []],
            1
        ))
        self.assertFalse(winning_move(
            [[1,2],
             [1],
             [],
             [],
             [],
             [],
             []],
            1
        ))
        self.assertFalse(winning_move(
            [[1,2,1],
             [],
             [],
             [],
             [],
             [],
             []],
            0
        ))

if __name__ == "__main__":
    unittest.main()