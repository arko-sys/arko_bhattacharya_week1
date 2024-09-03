import os
import sys
import numpy as np
import pandas as pd
import unittest
from io import StringIO


sys.path.append(os.path.join(os.path.dirname(__file__), "../src"))
from main import add_2_arr, create_df, df_to_csv


class Test(unittest.TestCase):

    def test_add_2_arr(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        res_arr = np.array([5, 7, 9])
        np.testing.assert_array_equal(add_2_arr(arr1, arr2), res_arr)

    def test_create_df(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        arr3 = np.array([5, 7, 9])
        df = create_df(arr1, arr2, arr3)
        res_df = pd.DataFrame(
            {"Array 1": [1, 2, 3], "Array 2": [4, 5, 6], "Array 3": [5, 7, 9]}
        )
        pd.testing.assert_frame_equal(df, res_df)

    def test_df_to_csv(self):
        arr1 = np.array([1, 2, 3])
        arr2 = np.array([4, 5, 6])
        arr3 = np.array([5, 7, 9])
        df = create_df(arr1, arr2, arr3)

        # ensuring the tests are isolated and don't depend on the filesystem.
        buffer = StringIO()
        df_to_csv(df, buffer)
        buffer.seek(0)
        res_df = pd.read_csv(buffer)

        expected_df = pd.DataFrame(
            {"Array 1": [1, 2, 3], "Array 2": [4, 5, 6], "Array 3": [5, 7, 9]}
        )

        pd.testing.assert_frame_equal(res_df, expected_df)


if __name__ == "__main__":
    unittest.main()
