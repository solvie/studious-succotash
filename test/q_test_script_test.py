import unittest
from src import q_test_script
import numpy as np

class QTestTester(unittest.TestCase):

    def test_make_q_table(self):
        #Reading a few selected points
        q_table = q_test_script.make_q_table()
        self.assertEqual(q_table['3']['0.90'], '0.941')
        self.assertEqual(q_table['11']['0.99'], '0.542')
        self.assertEqual(q_table['30']['0.95'], '0.298')

    def test_find_q_crit(self):
        self.assertEqual(q_test_script.find_q_crit(3, 0.9), 0.941)

    def test_returns_original_dataset_as_if_no_outlier_is_found(self):
        inputArray = [1,1,1,1,1]
        result = q_test_script.remove_outlier_via_q_test(inputArray)
        self.assertEqual(np.array_equal(inputArray, result), True)

    def test_remove_outlier_via_q_test_size_n_7(self):
        # SAMPLE SIZE 7
        # Lower outlier
        dataset = [1, 177, 180, 181, 185, 188, 189]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, [177, 180, 181, 185, 188, 189]), True)
        # Upper outlier
        dataset = [177, 180, 181, 185, 188, 189, 250]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, [177, 180, 181, 185, 188, 189]), True)
        # No outlier
        dataset = [177, 180, 181, 185, 188, 189, 200]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, [177, 180, 181, 185, 188, 189, 200]), True)
        # Scrambled order
        dataset = [180, 250, 181, 185, 177, 188, 189]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, [177, 180, 181, 185, 188, 189]), True)

    def test_remove_outlier_via_q_test_size_n_30(self):
        # SAMPLE SIZE 30
        # Lower outlier
        dataset = [1, 177, 177, 180, 180,180,180,180,180, 181,181,181,181,181,181,181,185, 185,185,185,185,185,185,185,188, 188,188,188,188,189]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, dataset[1:]), True)
        # Upper outlier
        dataset = [177, 177, 180, 180,180,180,180,180, 181,181,181,181,181,181,181,185, 185,185,185,185,185,185,185,188, 188,188,188,188,189, 1000]
        result = q_test_script.remove_outlier_via_q_test(dataset)
        self.assertEqual(np.array_equal(result, dataset[:-1]), True)


if __name__ == '__main__':
    unittest.main()