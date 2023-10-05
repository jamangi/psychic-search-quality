import util

GARDEVOIR_DATA = [
    {"date": "2023-10-05", "tasks_completed": 1}
]

GARDEVOIR_CONSISTENCY_TUPLES = [(datum['tasks_completed'], util.to_date(datum['date'])) for datum in GARDEVOIR_DATA]