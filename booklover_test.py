import unittest
from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):
    
    def test_1_add_book(self): 
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        bl.add_book('Book A', 3)
        self.assertIn('Book A', bl.book_list['book_name'].values)
                      
    def test_2_add_book(self):
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        bl.add_book('Book A', 3)
        bl.add_book('Book A', 3)
        self.assertEqual(1, len(bl.book_list)) 

    def test_3_has_read(self):
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        bl.add_book('Book A', 3)
        self.assertTrue(bl.has_read('Book A'))

    def test_4_has_read(self):
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        self.assertFalse(bl.has_read('Book B'))

    def test_5_num_books_read(self):
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        bl.add_book('Book A', 3)
        bl.add_book('Book B', 4)
        self.assertEqual(2, bl.num_books_read())

    def test_6_fav_books(self):
        bl = BookLover('Test User', 'test@gmail.com', 'Romance')
        bl.add_book('Book W', 4)
        bl.add_book('Book X', 2)
        bl.add_book('Book Y', 1)
        bl.add_book('Book Z', 5)
        result = bl.fav_books()
        self.assertTrue(all(rating > 3 for rating in result['book_rating'].values))

if __name__ == '__main__':
    unittest.main(verbosity=3)
    
    