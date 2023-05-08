import unittest
from unittest.mock import patch
import main

class TestJobSeekerPortal(unittest.TestCase):
    @patch('main.pymongo.MongoClient')
    def test_dataConnectivity(self, mock_mongo_client):
        # Mock the MongoClient and assert that it is called with the correct connection string
        main.dataConnectivity()
        mock_mongo_client.assert_called_with(main.conn_str, serverSelectionTimeoutMS=5000)

        # Mock the collection and assert that the find() method is called with the expected parameters
        mock_collection = mock_mongo_client.return_value.resumeDB.candidates
        mock_collection.find.assert_called_with({'name': 'Ahmed Mohammed', 'emailId': 'jobaxa1925@ippals.com'})

if __name__ == '__main__':
    unittest.main()
