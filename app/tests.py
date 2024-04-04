from django.test import SimpleTestCase

class TestCountHi(SimpleTestCase):
    def test_count_hi_abc_hi_ho(self):
        response = self.client.get("/string-2/abc hi ho")
        self.assertContains(response, 1)

    def test_count_hi_ABChi_hi(self):
        response = self.client.get("/string-2/ABChi hi")
        self.assertContains(response, 2)

    def test_count_hihi(self):
        response = self.client.get("/string-2/hihi")
        self.assertContains(response, 2)

class TestStringMatch(SimpleTestCase):
    def test_string_match_xxcaazz_xxbaaz(self):
        response = self.client.get("/warmup-2/xxcaazz/xxbaaz")
        self.assertContains(response, 3)

    def test_string_match_abc_abc(self):
        response = self.client.get("/warmup-2/abc/abc")
        self.assertContains(response, 2)

    def test_string_match_abc_axc(self):
        response = self.client.get("/warmup-2/abc/axc")
        self.assertContains(response, 0)

class TestRoundSum(SimpleTestCase):
    def test_round_sum_16_17_18(self):
        response = self.client.get("/logic-2/16/17/18")
        self.assertContains(response, 66)

    def test_round_sum_12_13_14(self):
        response = self.client.get("/logic-2/12/13/14")
        self.assertContains(response, 54)

    def test_round_sum_6_4_4(self):
        response = self.client.get("/logic-2/6/4/4")
        self.assertContains(response, 29)