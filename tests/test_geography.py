import re
import unittest

from alphabet_detector import AlphabetDetector
from faker import Faker

from faker_geoscience.geography.el_GR import Provider as ElGrGeographyProvider


class ElGrGeographyProviderTest(unittest.TestCase):
    """This class contains tests for greek provider about geography"""
    def setUp(self):
        self.fake = Faker()
        Faker.seed(0)
        self.fake.add_provider(ElGrGeographyProvider)

        self.ad = AlphabetDetector()

    def test_mountain_name(self):
        """
        Test for 100 random mountain names
        - if  characters are greek
        - if first character is capital
        """
        for _ in range(100):
            output = self.fake.mountain_name()
            self.assertTrue(self.ad.only_alphabet_chars(output, "GREEK"))
            self.assertTrue(re.search(r'^[Α-ΩΆΈΉΊΌΎΏ]', output))
