from django.test import TestCase
from django.urls import reverse
from .models import Result, Game, Player

# Index page : testing templates and HTML
class IndexPageTestCase(TestCase):

    def setUp(self):
        url = reverse('catalog:index')
        self.response = self.client.get(url)

    def test_indexpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_indexpage_template(self):
        self.assertTemplateUsed(self.response, 'catalog/index.html')

    def test_indexpage_contains_correct_html(self):
        self.assertContains(self.response, 'Welcome on')

    def test_indexpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'I am not on the Index page')

# List Page
class ListPageTestCase(TestCase):
    def setUp(self):
        url = reverse('catalog:list')
        self.response = self.client.get(url)

    def test_listpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_listpage_template(self):
        self.assertTemplateUsed(self.response, 'catalog/games.html')

    def test_listpage_contains_correct_html(self):
        self.assertContains(self.response, 'Games list')

    def test_listpage_does_not_contains_incorrect_html(self):
        self.assertNotContains(self.response, 'I am not on the Games list page')

#Result Model

class TestModels(TestCase):
	def setUp(self):
		game = Game.objects.create(title="Mission Impossible")
		player = Player.objects.create(email="toto@toto.fr", name="toto")
		game_id = Game.objects.get(title='Mission Impossible').id
		player_id = Player.objects.get(email="toto@toto.fr", name="toto").id
		self.result1 = Result.objects.create(
			score=200,
			game = Game(id=game_id),
			player= Player(id=player_id)
		)
		self.result2 = Result.objects.create(
			score=7500,
			game = Game(id=game_id),
			player= Player(id=player_id)
		)
		self.result3 = Result.objects.create(
			score=12000,
			game = Game(id=game_id),
			player= Player(id=player_id)
		)

	def test_project_is_assigned_level_beginner_on_create(self):
		self.assertEquals(self.result1.level, 'Beginner')

	def test_project_is_assigned_level_advanced_on_create(self):
		self.assertEquals(self.result2.level, 'Advanced')
		
	def test_project_is_assigned_level_expert_on_create(self):
		self.assertEquals(self.result3.level, 'Expert')












