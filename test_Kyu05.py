import Kyu05 as k5

def test_prefill():
    assert k5.prefill(3,1) == [1,1,1]
    assert k5.prefill(2,'abc') == ['abc','abc']
    assert k5.prefill('1',1)== [1]
    assert k5.prefill(3, k5.prefill(2,'2d')) == [['2d','2d'],['2d','2d'],['2d','2d']]

def test_nico():
    assert k5.nico("crazy", "secretinformation") == "cseerntiofarmit on  "
    assert k5.nico("abc", "abcd") == "abcd  "
    assert k5.nico("ba", "1234567890") == "2143658709"
    assert k5.nico("a", "message") == "message"
    assert k5.nico("key", "key") == "eky"
    assert k5.nico("abcdefgh", "abcd") == "abcd    "

def test_rot13():
    assert k5.rot13("EBG13 rknzcyr.") == "ROT13 example."
    assert k5.rot13("This is my first ROT13 excercise!") == "Guvf vf zl svefg EBG13 rkprepvfr!"

