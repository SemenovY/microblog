def determine_sequence(series_array):
    """
    series_array = [2, 5, 8, 11, 14]   #should return 0
    series_array = [1, 2, 4, 8, 16]    #should return 1
    series_array = [1, 2, 1, 3, 4, 5]  #should return -1
    series_array = [1, 1, 1, 1, 1]     #should return 2
    series_array = [0, 0, 0, 0, 0]     #should return 0
    """
    try:
        for i in range(1, len(series_array)):
            if (
                series_array[-i] - series_array[-i - 1]
                == series_array[-i - 1] - series_array[-i - 2]
                and series_array[i + 2] - series_array[i + 1]
                == series_array[i + 1] - series_array[i]
            ):
                if (
                    series_array[-i] / series_array[-i - 1]
                    == series_array[-i - 1] / series_array[-i - 2]
                ):
                    return 2
                else:
                    return 0
            elif (
                series_array[-i] / series_array[-i - 1]
                == series_array[-i - 1] / series_array[-i - 2]
            ):
                return 1
            else:
                return -1
    except:
        return -1


series_array = [1, 0, 0, 0, 0]
print(determine_sequence(series_array))


def test_determine_sequence():
    assert_equals(determine_sequence([2, 5, 8, 11, 14]), 0)  # It is an AP
    assert_equals(determine_sequence([1, 2, 4, 8, 16]), 1)  # It is a GP
    assert_equals(determine_sequence([1, 2, 1, 3, 4, 5]), -1)  # It is not a series
    assert_equals(determine_sequence([1, 1, 1, 1, 1]), 2)  # It is both an AP and GP
    assert_equals(determine_sequence([1, 0, 0, 0, 0]), -1)
    assert_equals(determine_sequence([100, 0, 0, 0, 0]), -1)
