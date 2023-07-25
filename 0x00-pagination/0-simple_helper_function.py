#!/usr/bin/env python3
""" Pagination - Simple helper function """

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ returns tuple of size two containing  start index and an end index 
    """
    return ((page - 1) * page_size, ((page - 1) * page_size) + page_size)

