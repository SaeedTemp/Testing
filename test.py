import unittest
from unittest.mock import patch
import main

class TestJobSeekerPortal(unittest.TestCase):
    @patch('main.pymongo.MongoClient')
    def test_dataConnectivity(self, mock_mongo_client):
        # Mock the MongoClient and assert that it is called with the correct connection string
        mock_collection = mock_mongo_client.return_value.resumeDB.users
        mock_collection.find.return_value = [
            {
                "name": "Ahmed Mohammed",
                "emailId": "jobaxa1925@ippals.com",
                "description": "Ahmed Mohammed About Me I am passionate Backend Developer with 2 years of experience working on back end technologies such as Node Js,. PostgreSQL Express Js and Type Script. A B.Tech computer science graduate with CGPA:6.8. Experience First Tech Solutions 2022 - 2023 Junior Developer Worked on various Node js projects in the company Maintained previous code and its fixes Worked on Database management Education 2018-2022 Completed B. Tech Degree in Computer Science Crescent University with a CGPA:8.8 Vandalur Chennai B.Tech Language Expertise Contact Hindi ui/ux Old town Street, Mumbai English visual design India Phone Tamil leadership +916282459725 coaching",
                "job_description": "Job role as a Backend Developer, 2 years experience            with CGPA:8.0 . You will be required to design, develop, test, and implement effective and highly robust applications. You must be able to maintain existing systems whilst developing new solutions in line with the business requirements.You will work as part of a collaborative Agile development team, which will include Product Owners, a Scrum Master, Developers and UX/UX Design staff on the frontend, database and back-end elements of the Company product which is used by customers all over the world. A can-do attitude and be willines to grow and adapt to the changing environoment is expected. Responsibilities: Providing regular updates. Maintaining application performance. Troubleshooting issues and carrying out root cause analysis. Performing code reviews as per the code review process. Skills and Experience: experience using Backend technologies such as Nodejs, REST API , JavaScript , ES6, AWS , MongoDB. Strong organisational skills. Excellent problem-solving abilities. Experience of working in Agile delivery model using Jira as the work management too Job Type: Full-time Benefits: Health insurance"
            }
        ]

        main.dataConnectivity()

        # Assert that the expected candidate name and email are found in the database
        mock_collection.find.assert_called_with({
            "name": "Ahmed Mohammed",
            "emailId": "jobaxa1925@ippals.com"
        })

if __name__ == '__main__':
    unittest.main()
