"""
Module contains class to test department model.
"""
# pylint: disable=no-member
from department_app import db
from department_app.models.department_model import Department
from department_app.tests.conftest import BaseTest


class TestDepartment(BaseTest):
    """
    Class for department model test cases
    """

    def test_department_model(self):
        """
        Testing if the string representation of
        department is correct
        """
        department = Department(uuid="2", name='test_department', description='test')
        db.session.add(department)
        db.session.commit()
        self.assertEqual('test_department', repr(department))
