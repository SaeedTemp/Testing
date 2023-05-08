import unittest
from unittest.mock import patch
import main

class TestJobSeekerPortal(unittest.TestCase):
    @patch('main.pymongo.MongoClient')
    def test_dataConnectivity(self, mock_mongo_client):
        # Mock the MongoClient and assert that it is called with the correct connection string
        main.dataConnectivity()
        mock_mongo_client.assert_called_with(main.conn_str, serverSelectionTimeoutMS=5000)
    
    @patch('main.pdfplumber.open')
    def test_extract_text_from_pdf(self, mock_pdf_open):
        # Mock the pdfplumber.open function and assert that it is called with the correct file
        mock_pdf = mock_pdf_open.return_value.__enter__.return_value
        mock_pdf.pages.__iter__.return_value = [mock_pdf.pages.__getitem__.return_value]
        mock_pdf.extract_text.return_value = 'Sample resume text'
        file = 'sample_resume.pdf'
        text = main.extract_text_from_pdf(file)
        self.assertEqual(text, 'Sample resume text')

if __name__ == '__main__':
    unittest.main()
