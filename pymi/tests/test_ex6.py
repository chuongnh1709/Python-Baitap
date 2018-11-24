import unittest
from tests.base import TestExercise

import exercises.ex6_1 as ex6_1
import exercises.ex6_2 as ex6_2
import exercises.ex6_3 as ex6_3
import exercises.ex6_4 as ex6_4
import exercises.ex6_5 as ex6_5


class TestExercise6(TestExercise):
    @unittest.skip
    def test_ex6_0(self):
        pass

    def test_ex6_1(self):
        expected = [('Nam', 1230), ('Pikalong', 35670),
                    ('Phan Quan', 2165110), ('Maria', 90570),
                    ('Trump', 138000)]
        len_expected = len(expected)
        res = ex6_1.solve(
            {'usages': [('nam', '1'), ('pikalong', '29'),
                        ('phan quan', '1235'), ('maria', '69'),
                        ('trump', '100')],
             'prices': ex6_1.data}
        )
        self.assertIsInstance(res, list)
        self.assertEqual(
            len(res),
            len_expected,
            "Số lượng phần tử không đúng"
        )
        self.assertEqual(res, expected)

    def test_ex6_2(self):
        data = ['meo', 'bo', 'ga', 'cho', 'chim', 'gau', 'voi']
        # https://docs.python.org/3/library/functions.html#zip
        expected = list(zip(*[iter(data)] * 2))
        res = ex6_2.solve(data, 2)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], tuple)
        self.assertEqual(res, expected)

        self.assertEqual(ex6_2.solve(data, 3), list(zip(*[iter(data)] * 3)))

    def test_ex6_3(self):
        expected = ('2017-05-25', 76454277.83)
        res = ex6_3.solve()
        self.assertEqual(res, expected)

    def test_ex6_4(self):
        res = ex6_4.solve()
        expected = sum(range(1, 7)) + .5, sum(range(1, 7)) + 9 + .5

        self.assertEqual(res, expected)

    def test_ex6_5(self):
        res = ex6_5.solve(ex6_5.data)
        self.assertIsInstance(res, list)
        self.assertIsInstance(res[0], dict)

        self.assertIn('hvnsweeting', [n['login'] for n in res])

        self.assertIn('https://github.com/thedrow',
                      [n['html_url'] for n in res])
        self.assertIn('https://github.com/hvnsweeting',
                      [n['html_url'] for n in res])

    @unittest.skip
    def test_ex6_10(self):
        pass


if __name__ == "__main__":
    unittest.main()
