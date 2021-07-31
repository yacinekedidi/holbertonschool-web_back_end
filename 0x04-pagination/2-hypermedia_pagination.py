#!/usr/bin/env python3
"""[summary]"""
import csv
import math
from typing import List, Dict, Union
index_range = __import__('0-simple_helper_function').index_range


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
        """[summary]

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            List[List]: [description]
        """
        assert all([type(page) is int, type(page_size) is int]) and\
            page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        dataset = self.dataset()
        try:
            return dataset[start:end]
        except Exception:
            return []

    def get_hyper(self, page: int = 1, page_size: int = 10):
        """[summary]

        Args:
            page (int, optional): [description]. Defaults to 1.
            page_size (int, optional): [description]. Defaults to 10.

        Returns:
            Dict[int, int, List[List], Union[int, None],
            Union[int, None], int]: [description]
        """
        dataset = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        return {
            "page_size": page_size,
            "page": page,
            "data": dataset,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
