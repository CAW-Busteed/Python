import unittest

class PasswordTest(unittest.TestCase):

    def helper(self, x, y):
        return x==y

    # test names must start w/test
    def test_me(self):
        assert self.helper("roy", "joe"), "bad args"
        assert self.helper("roy", "roy"), "bad args"

if __name__=='__main__':

    import pdb; pdb.set_trace()
    unittest.main()

