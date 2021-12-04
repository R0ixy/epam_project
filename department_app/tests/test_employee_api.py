"""
Module contains class to test employee api.
"""
# pylint: disable=no-member
import http
import json

from department_app.tests.conftest import BaseTest
from department_app.models.employee_model import Employee
from department_app.models.department_model import Department
from department_app.loader import db


class TestEmployeeApi(BaseTest):
    """
    Class for employees api test cases.
    """

    @staticmethod
    def create_dep():
        """
        Fill department table with test data.
        """
        department = Department(name='Test Department', description='Test Description')
        db.session.add(department)
        db.session.commit()

    def fill_db(self):
        """
        Fill database with test data.
        """
        self.create_dep()
        employee = Employee(full_name='James Johnson',
                            salary=2000,
                            date_of_birth='1982-03-14',
                            position='Developer',
                            department_id=1)
        db.session.add(employee)
        db.session.commit()

    def test_get(self):
        """
        Test get request.
        """
        self.fill_db()
        response = self.app.get('/api/employees/')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id(self):
        """
        Test get request with param id.
        """
        self.fill_db()
        response = self.app.get('/api/employees/?id=1&')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_first_date(self):
        """
        Test get request with param first_date.
        """
        self.fill_db()
        response = self.app.get('/api/employees/?first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id_and_first_date(self):
        """
        Test get request with params id and first_date.
        """
        self.fill_db()
        response = self.app.get('/api/employees/?id=1&first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_all_params(self):
        """
        Test get request with all possible params.
        """
        self.fill_db()
        response = self.app.get('/api/employees/?id=1&first_date=1982-03-14&second_date=1991-02-21')
        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        """
        Test post request.
        """
        self.create_dep()
        data = {
            'full_name': 'Jhon Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 1
        }
        response = self.app.post('/api/employees/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_wrong_post(self):
        """
        Test post request exception.
        """
        self.create_dep()
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.post('/api/employees/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put(self):
        """
        Test put request.
        """
        self.fill_db()
        data = {
            'id': 1,
            'full_name': 'Jhon Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 1
        }
        response = self.app.put('/api/employees/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_put(self):
        """
        Test put request exception.
        """
        self.create_dep()
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.put('/api/employees/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        """
        Test delete request.
        """
        self.fill_db()
        data = {
            'id': 1,
        }
        response = self.app.delete('/api/employees/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_delete_data(self):
        """
        Test delete request exception because of wrong data.
        """
        self.create_dep()
        data = {
            'id': 3423
        }
        response = self.app.delete('/api/employees/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_wrong_delete_args(self):
        """
        Test delete request exception because of wrong args.
        """
        self.create_dep()
        data = {
            'wrong_arg': 3423
        }
        response = self.app.delete('/api/employees/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST
