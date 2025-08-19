import pytest

from src.py102.task2 import task2
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase3


class TestTask2:
    test_cases = [
        # given1 is name, given2 is country, given3 is month
        TestCase3(
            given1="Roberto",
            given2="Panama",
            given3="November",
            expected="Hello Roberto, you are from Panama and you were born in November",
        ),
        TestCase3(
            given1="Jennie",
            given2="Sweden",
            given3="July",
            expected="Hello Jennie, you are from Sweden and you were born in July",
        ),
        TestCase3(
            given1="Alberto",
            given2="Spain",
            given3="August",
            expected="Hello Alberto, you are from Spain and you were born in August",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_is_implemented(self, test_case):
        name = test_case.given1
        country = test_case.given2
        month = test_case.given3

        assert_equals(
            message=f"> name= {name}\n> country= {country}\n> month = {month}",
            expected=test_case.expected,
            actual=task2(name=name, country=country, month=month),
        )
