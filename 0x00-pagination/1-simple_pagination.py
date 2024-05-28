#!/usr/bin/env python3
"""
function to return a tuple with start and end index
"""

import csv
import math
from typing import List


def index_range(page, page_size):
    """ returns the start and end indices"""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Returns a list of rows for the specified page and page size."""
        assert isinstance(page, int) and page > 0, "Page must be positive."
        assert isinstance(page_size, int) and page_size > 0, "Size Positive"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        # Return the sliced data based on calculated start and end indices
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]
