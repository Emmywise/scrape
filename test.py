from typing import List
import unittest
from main import parse_page_content, fetch_page_content

class PageContent(unittest.TestCase):


    def test_case1(self):
        result = fetch_page_content('https://webscraper.io/test-sites/e-commerce/allinone')
        parsed_content= parse_page_content(result)
        self.assertIsNotNone(result)
        self.assertIsInstance(parsed_content, List)
        for product in parsed_content:
            self.assertIn('title', product)
            self.assertIn('review', product)
            self.assertIn('price', product)
            self.assertIn('description', product)
            self.assertIn('image', product)




    

    
  
if __name__ == '__main__':
    unittest.main()