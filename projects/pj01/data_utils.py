"""Utility functions for wrangling data."""

__author__ = "730272774"

from csv import DictReader


def read_csv_rows(csv_file: str) -> list[dict[str, str]]:
    """Read a CSV file's contents into a list of rows."""
    rows: list[dict[str, str]] = []

    # TODO 0.1) Complete the implementation of this function here.
    file_handle = open(csv_file, "r", encoding="utf8")
    csv_reader = DictReader(file_handle)
    for row in csv_reader:
        rows.append(row)
    file_handle.close()
    return rows


# TODO: Define the other functions here.
def column_values(rows: list[dict[str, str]], column: str) -> list[str]:
    """Producing a list of column values."""
    columns: list[str] = []
    for row in rows:
        columns.append(row[column])
    return columns


def columnar(rows: list[dict[str, str]]) -> dict[str, list[str]]:
    """Making a column based table."""
    columns: dict[str, list[str]] = {}
    for column in rows[0]:
        columns[column] = column_values(rows, column)
    return columns


def head(columns: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Making sure column based table is working."""
    head_columns: dict[str, list[str]] = {}
    if n > len(columns):
        n = len(columns)
    for column in columns:
        n_values: list[str] = []
        for row in range(n):
            n_values.append(columns[column][row])
        head_columns[column] = n_values
    return head_columns


def select(columns: dict[str, list[str]], names: list[str]) -> dict[str, list[str]]:
    """Selects a subset of column names."""
    select_columns: dict[str, list[str]] = {}
    for column in names:
        select_columns[column] = columns[column]
    return select_columns


def count(selected_data: list[str]) -> dict[str, int]:
    """Counts frequency of column values."""
    counts: dict[str, int] = {}
    for item in selected_data:
        if item in counts:
            counts[item] += 1
        else:
            counts[item]: int = 1
    return counts
