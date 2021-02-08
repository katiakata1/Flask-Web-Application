from Application.app import app
import unittest


class FlaskTestCase(unittest.TestCase):

    #Ensures the the home page is set up correctly
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    #Ensures that register page loads correctly 
    def test_register_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertTrue(b'Enter your credentials bellow' in response.data)

    #Ensures that the user can login:
    def test_login_loads(self):
        tester = app.test_client(self)
        response = tester.post('/register', data = dict(username="admin", password="admin"),
        follow_redirects=True)
        self.assertTrue(response.status_code, 200)

    #Ensures that the user is able to input items into the table
    def test_table_inputs_are_accepted(self):
        tester = app.test_client(self)
        response = tester.post('/supplies', data = dict(item_name="ice", reasons_for_request="need it", quantity="5"),
        follow_redirects=True)
        self.assertTrue(response.status_code, 200)

    #Ensures that the item can be viewed by the user
    def test_item_can_be_viewed(self):
        tester = app.test_client(self)
        response = tester.get('/item/<id>', content_type='html/text')
        self.assertTrue(response.status_code, 200)

    #Ensures that the item can be deleted by the user:
    # def test_table_inputs_are_deleted(self):
    #     tester = app.test_client(self)
    #     response = tester.post('/delete_item/<int:id>', data = dict(item_name="ice", reasons_for_request="need it", quantity="5"),
    #     follow_redirects=True)
    #     self.assertTrue(response.status_code, 200)


if __name__=='__main__':
    unittest.main()



