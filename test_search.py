import unittest
from unittest.mock import patch
import requests
from order_search import search_order

class TestSearchOrder(unittest.TestCase):
    @patch('requests.post')
    def test_search_order_success(self, mock_post):
        # Mock the response from the Orner API
        mock_response = {'status_code': 200, 'json.return_value': {'orders': [{'order': {'id': '123'}}]}}
        mock_post.return_value = Mock(**mock_response)

        order_id = search_order('1234567890')

        mock_post.assert_called_once_with('https://orner.com.ua/api/v1/public/order/search', params={'search': '1234567890', 'page': 1, 'size': 10})

        self.assertEqual(order_id, '123')

    @patch('requests.post')
    def test_search_order_no_results(self, mock_post):
        # Mock the response from the Orner API to simulate no results found
        mock_response = {'status_code': 200, 'json.return_value': {'orders': []}}
        mock_post.return_value = Mock(**mock_response)

        order_id = search_order('1234567890')

        self.assertIsNone(order_id)

    @patch('requests.post')
    def test_search_order_api_failure(self, mock_post):
        # Mock the response from the Orner API to simulate an API failure
        mock_response = {'status_code': 500}
        mock_post.return_value = Mock(**mock_response)
        order_id = search_order('1234567890')

        self.assertIsNone(order_id)

if __name__ == '__main__':
    unittest.main()
