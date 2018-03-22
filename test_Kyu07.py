import unittest
import Kyu07

class TestAccum(unittest.TestCase):
    """
    Test the accum function from the 7th Kyu library
    """
    def test_accum_01(self):
        result = Kyu07.accum("abcd")
        self.assertEqual(result, "A-Bb-Ccc-Dddd")

    def test_accum_02(self):
        result = Kyu07.accum("RqaEzty")
        self.assertEqual(result, "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy")

    def test_accum_03(self):
        result = Kyu07.accum("cwAt")
        self.assertEqual(result, "C-Ww-Aaa-Tttt")

    def test_accum_04(self):
        """
        Test output for various strings as per below
        """
        self.assertEqual(Kyu07.accum("ZpglnRxqenU"),
                           "Z-Pp-Ggg-Llll-Nnnnn-Rrrrrr-Xxxxxxx-Qqqqqqqq-Eeeeeeeee-Nnnnnnnnnn-Uuuuuuuuuuu")
        self.assertEqual(Kyu07.accum("NyffsGeyylB"),
                           "N-Yy-Fff-Ffff-Sssss-Gggggg-Eeeeeee-Yyyyyyyy-Yyyyyyyyy-Llllllllll-Bbbbbbbbbbb")
        self.assertEqual(Kyu07.accum("MjtkuBovqrU"),
                           "M-Jj-Ttt-Kkkk-Uuuuu-Bbbbbb-Ooooooo-Vvvvvvvv-Qqqqqqqqq-Rrrrrrrrrr-Uuuuuuuuuuu")
        self.assertEqual(Kyu07.accum("EvidjUnokmM"),
                           "E-Vv-Iii-Dddd-Jjjjj-Uuuuuu-Nnnnnnn-Oooooooo-Kkkkkkkkk-Mmmmmmmmmm-Mmmmmmmmmmm")
        self.assertEqual(Kyu07.accum("HbideVbxncC"),
                           "H-Bb-Iii-Dddd-Eeeee-Vvvvvv-Bbbbbbb-Xxxxxxxx-Nnnnnnnnn-Cccccccccc-Ccccccccccc")

class TestExplode(unittest.TestCase):
    """
    Test the explode function from the 7th Kyu library
    """
    def test_explode_01(self):
        result = Kyu07.explode("312")
        self.assertEqual(result, "333122")

    def test_explode_02(self):
        result = Kyu07.explode("102269")
        self.assertEqual(result, "12222666666999999999")

    def test_accum_03(self):
        """
        Test output for various strings as per below
        """
        self.assertEqual(Kyu07.explode("0"),"")
        self.assertEqual(Kyu07.explode("000"),"")
        self.assertEqual(Kyu07.explode("123"),"122333")
        self.assertEqual(Kyu07.explode("01001"),"11")
        self.assertEqual(Kyu07.explode("54321"),"555554444333221")

class TestFind_next_square(unittest.TestCase):
    """
    Test the find_next_square function from the 7th Kyu library
    """
    def test_find_next_01(self):
        self.assertEqual(Kyu07.find_next_square(121), 144)

    def test_find_next_02(self):
        self.assertEqual(Kyu07.find_next_square(625), 676)

    def test_find_next_03(self):
        self.assertEqual(Kyu07.find_next_square(114), -1)

class TestIs_isogram(unittest.TestCase):
    """
    Test the find_next_square function from the 7th Kyu library
    """
    def test_is_isogram_01(self):
        self.assertEqual(Kyu07.is_isogram("Dermatoglyphics"), True)

    def test_is_isogram_02(self):
        self.assertEqual(Kyu07.is_isogram("aba"), False)

    def test_is_isogram_03(self):
        self.assertEqual(Kyu07.is_isogram("moOse"), False)

    def test_is_isogram_04(self):
        self.assertEqual(Kyu07.is_isogram(""), True)

    def test_is_isogram_05(self):
        self.assertEqual(Kyu07.is_isogram("isogram"), True)

if __name__ == '__main__':
    unittest.main()
#    suite = unittest.TestLoader().loadTestsFromTestCase(TestAccum)
#    unittest.TextTestRunner(verbosity=2).run(suite)