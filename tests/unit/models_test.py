from unittest import TestCase
from website.models import Note, Work, User, Team


class TestingModels(TestCase):
    def test_note(self):
        note = Note(data='test',  user_id=1,date=5 / 20/ 2021)
        self.assertEqual(note.data, 'test', "Testing")
        self.assertEqual(note.user_id, 1, "test user id")

    def test_work(self):
        work = Work(title='test', user_id=2, points=75, status='online',description='working')
        self.assertEqual(work.title, 'test', "Testing")
        self.assertEqual(work.user_id, 2, 'user id')
        self.assertEqual(work.points, 75, 'points')

    def test_user(self):
        user = User(email='testing@gmail.com', password='testing', first_name='Mihlali', team_leader=True,
                    points=100)

        self.assertEqual(user.email, 'testing@gmail.com', 'test email')
        self.assertEqual(user.password, 'testing', 'password')
        self.assertEqual(user.first_name, 'Mihlali')
        self.assertIsNotNone(user.notes)
        self.assertIsNotNone(user.work)
        self.assertEqual(user.points, 100, 'points')

    def test_team(self):
        team = Team(name='Quality Assurance')
        self.assertEqual(team.name, 'Quality Assurance')
        self.assertIsNotNone(team.users)