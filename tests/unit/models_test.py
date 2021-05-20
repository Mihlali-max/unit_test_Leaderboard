from unittest import TestCase
from website.models import Note, Work, User, Team


class TestingModels(TestCase):
    def test_note(self):
        note = Note(data='test', date=17 / 5 / 2021, user_id=1)
        self.assertEqual(note.data, 'test', "Testing")
        self.assertEqual(note.user_id, 1, "test user id")

    def test_work(self):
        work = Work(title='test', description='working', user_id=2, status='online', points=75)
        self.assertEqual(work.title, 'test', "Testing")
        self.assertEqual(work.user_id, 2, 'user id')
        self.assertEqual(work.points, 75, 'points')

    def test_user(self):
        user = User(email='testing@gmail.com', password='testing', first_name='tester', team_leader=True,
                    points=100)

        self.assertEqual(user.email, 'testing@gmail.com', 'test email')
        self.assertEqual(user.password, 'testing', 'test password')
        self.assertEqual(user.first_name, 'tester')
        self.assertIsNotNone(user.notes)
        self.assertIsNotNone(user.work)
        self.assertEqual(user.points, 100, 'test points')

    def test_team(self):
        team = Team(name='tester')
        self.assertEqual(team.name, 'tester')
        self.assertIsNotNone(team.users)