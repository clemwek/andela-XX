import unittest
from src.models.activities.activities import Activity


class TestActivity(unittest.TestCase):
    def test_is_type(self):
        new_activity = Activity('play pool', 'bucketlist1', 'date', False)
        self.assertIsInstance(new_activity, Activity)
