import pandas as pd
import numpy as np


def add_2_arr(arr1, arr2):
    return arr1 + arr2


def create_df(arr1, arr2, arr3):
    return pd.DataFrame({"Array 1": arr1, "Array 2": arr2, "Array 3": arr3})


def df_to_csv(df, filename="output.csv"):
    df.to_csv(filename, index=False)
    return filename


if __name__ == "__main__":
    first_arr = np.array([1, 2, 3])
    second_arr = np.array([4, 5, 6])

    third_arr = add_2_arr(first_arr, second_arr)

    df = create_df(first_arr, second_arr, third_arr)

    output_file = df_to_csv(df, "testfile.csv")

    print(f"DataFrame saved to {output_file}")
