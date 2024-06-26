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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """get a page list using page num and page_size"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        (start, end) = index_range(page, page_size)
        data_set = self.dataset()
        data = data_set[start:end]

        total_pages = math.ceil(len(data_set) / page_size)
        page_size = len(data)
        next_page = None if page + 1 > total_pages else page + 1
        prev_page = None if page - 1 == 0 else page - 1
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
