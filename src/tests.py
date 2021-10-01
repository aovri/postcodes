import unittest
import postcode


class TestAA9APostCode(unittest.TestCase):
    def test_aa9a(self):
        self.assertTrue(postcode.is_valid('EC1A 1BB'))
    # The following central London single-digit districts have been further divided
    # by inserting a letter after the digit and before the space:
    # EC1–EC4 (but not EC50), SW1, W1, WC1, WC2 and parts of E1 (E1W), N1 (N1C and N1P), NW1 (NW1W) and SE1 (SE1P).
    def test_aa9a_not_ok(self):
        self.assertFalse(postcode.is_valid('BL1A 1BB'))
    # The only letters to appear in the fourth position are
    # A, B, E, H, M, N, P, R, V, W, X and Y when the structure starts with AA9A.
    def test_aa9a_fourth_position_not_ok(self):
        self.assertFalse(postcode.is_valid('EC1C 0BB'))
        self.assertFalse(postcode.is_valid('EC1D 0BB'))
        # TODO: etc. + could use loop as below

class TestA9APostCode(unittest.TestCase):
    def test_a9a(self):
        self.assertTrue(postcode.is_valid('W1A 0AX'))
    # The only letters to appear in the third position are
    # A, B, C, D, E, F, G, H, J, K, P, S, T, U and W when the structure starts with A9A.
    def test_a9a_not_ok(self):
        codes = [
            'W1I 0AX',
            'W1L 0AX',
            'W1M 0AX',
            'W1N 0AX',
            'W1O 0AX',
            'W1Q 0AX',
            'W1R 0AX',
            'W1V 0AX',
            'W1X 0AX',
            'W1Y 0AX',
            'W1Z 0AX',
        ]
        for code in codes:
            self.assertFalse(postcode.is_valid(code))

class TestA9PostCode(unittest.TestCase):
    # Only B, E, G, L, M, N, S, W
    def test_a9(self):
        codes = [
            'B8 0AX',
            'E8 0AX',
            'G8 0AX',
            'L8 0AX',
            'M8 0AX',
            'N8 0AX',
            'S8 0AX',
            'W8 0AX',
        ]
        for code in codes:
            self.assertTrue(postcode.is_valid(code))
    def test_a9_not_ok(self):
        self.assertFalse(postcode.is_valid('Y8 1PY'))

class TestA99PostCode(unittest.TestCase):
    def test_a99(self):
        self.assertTrue(postcode.is_valid('B33 8TH'))
    # TODO: Add more tests

class TestAA9PostCode(unittest.TestCase):
    def test_aa9(self):
        self.assertTrue(postcode.is_valid('CR2 6XH'))
    # Areas with only single-digit districts:
    # BR, FY, HA, HD, HG, HR, HS, HX, JE, LD, SM, SR, WC, WN, ZE
    def test_single_digit_district_only_ok(self):
        self.assertTrue(postcode.is_valid('FY1 1PY'))
    def test_single_digit_district_only_not_ok(self):
        # TODO: This is not caught is invalid due to:
        # ^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR
        # But I am not going to fix that!
        self.assertFalse(postcode.is_valid('FY11 1PY'))
    # Areas with a district '0' (zero): BL, BS, CM, CR, FY, HA, PR, SL, SS
    def test_zero_district_only_ok(self):
        self.assertTrue(postcode.is_valid('BL0 0AB'))
    def test_zero_district_only_not_ok(self):
        self.assertFalse(postcode.is_valid('BB0 1PY'))
    # The letters Q, V and X are not used in the first position.
    def test_disallowed_first_pos(self):
        self.assertFalse(postcode.is_valid('QL1 0PY'))
        self.assertFalse(postcode.is_valid('VL1 0PY'))
        self.assertFalse(postcode.is_valid('XL1 0PY'))
    # The letters I, J and Z are not used in the second position.
    def test_disallowed_second_pos(self):
        self.assertFalse(postcode.is_valid('BI1 0PY'))
        self.assertFalse(postcode.is_valid('BJ1 0PY'))
        self.assertFalse(postcode.is_valid('BZ1 0PY'))


class TestAA99PostCode(unittest.TestCase):
    def test_aa99(self):
        self.assertTrue(postcode.is_valid('DN55 1PT'))
    # Areas with only double-digit districts: AB, LL, SO
    def test_double_digit_district_only_ok(self):
        self.assertTrue(postcode.is_valid('LL15 1PY'))
    def test_double_digit_district_only_not_ok(self):
        self.assertFalse(postcode.is_valid('LL1 1PY'))

class Test9AAInwardCode(unittest.TestCase):
    def test_missing(self):
        self.assertFalse(postcode.is_valid('W1A'))
    # The final two letters do not use C, I, K, M, O or V,
    # so as not to resemble digits or each other when hand-written.
    def test_disallowed_character(self):
        codes = [
            'W1I 0CX',
            'W1L 0IX',
            'W1M 0KX',
            'W1N 0MX',
            'W1O 0OX',
            'W1Q 0VX',
            'W1I 0XC',
            'W1L 0XI',
            'W1M 0XK',
            'W1N 0XM',
            'W1O 0XO',
            'W1Q 0XV',
        ]
        for code in codes:
            self.assertFalse(postcode.is_valid(code))
    def test_inner_incomplete(self):
        self.assertFalse(postcode.is_valid('B33 8T'))


# TODO: Could split this further into classes of negative tests
class TestBadPostCode(unittest.TestCase):
    def test_empty_string(self):
        self.assertFalse(postcode.is_valid(''))
    # A99A format does not exist
    def test_a99a(self):
        self.assertFalse(postcode.is_valid('B33A 0EF'))
    def test_num(self):
        self.assertFalse(postcode.is_valid(1))
    def test_long_string(self):
        self.assertFalse(postcode.is_valid('LL8880055 1PT'))
    def test_no_space(self):
        self.assertTrue(postcode.is_valid('DN551PT'))


# TODO: Test special cases

if __name__ == '__main__':
    unittest.main()
