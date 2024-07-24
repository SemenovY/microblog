#  ["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]

# "found the needle at position 5"
def find_needle(haystack):
    """
    Find the position of the needle in the haystack.

    Parameters:
        haystack (str): The string to search in.

    Returns:
        str: The position of the needle in the haystack.

    Raises:
        ValueError: If the needle is not found in the haystack.

    Example:
        >>> find_needle("haystack")
        'found the needle at position 7'
    """
    return "found the needle at position {}".format(haystack.index("needle"))
