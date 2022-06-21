import unittest
from city_functions import city_country

class CityCountryTestCase(unittest.TestCase):
    """Tests for city_functions.py."""

    def test_city_country_population(self):
        "Do city, country, population strings display properly, with capitalization?"
        formatted_name = city_country('santiago','chile','5000000')
        self.assertEqual(formatted_name,'Santiago, Chile - Population: 5000000')

if __name__ == '__main__':
    unittest.main()

