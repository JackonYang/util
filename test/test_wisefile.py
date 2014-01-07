import unittest
import sys

sys.path.append('..')
import wisefile


class test_wisefile(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_file_md5(self):
        md5 = wisefile.file_md5(__file__)
        self.assertEqual(len(md5), 32)
    
    def test_exclude(self):
        # pattern with or without magic characters
        patterns = '.git*, .svn, *.py[cod]'
        files = ['.git',
                 '.git/HEAD',
                 '.git/Branch',
                 '.svn/',
                 '.svn',
                 'hello.pyc',
                 'hello.py',
                 'hello.pyd',
                 'hello.pycd',
                 ]
        res = ['.svn/', 'hello.pycd', 'hello.py']
        self.assertItemsEqual(wisefile.exclude(files, patterns), res)
        # one file string
        files = 'hello.py'
        self.assertItemsEqual(wisefile.exclude(files, ' '), [files])
        # files start with space
        pat = '[ ]*'
        files = [' hello.py', 'ihello.py']
        self.assertItemsEqual(wisefile.exclude(files, pat), ['ihello.py'])


testclass = test_wisefile 

testcases = [#'test_file_md5',
             'test_exclude',
             ]

if __name__=='__main__':
    suite=unittest.TestSuite()
    for test in testcases:
        suite.addTest(testclass(test))

    runner=unittest.TextTestRunner()
    runner.run(suite)
