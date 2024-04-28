#!/usr/bin/env python3
"""
function to return a tuple with start and end index
"""


def index_range(page, page_size):
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
