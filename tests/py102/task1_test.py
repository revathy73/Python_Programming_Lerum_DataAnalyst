import pytest

from src.py102.task1 import task1
from tests.helper.custom_assertions import assert_equals
from tests.helper.TestCase import TestCase3


class TestTask1:
    # given1 is country, given2 is capital, given3 is currency
    test_cases = [
        TestCase3(
            given1="Panama",
            given2="Panama",
            given3="USD",
            expected="The capital of Panama is Panama. They use the USD",
        ),
        TestCase3(
            given1="Sweden",
            given2="Stockholm",
            given3="SEK",
            expected="The capital of Sweden is Stockholm. They use the SEK",
        ),
        TestCase3(
            given1="Colombia",
            given2="Bogota",
            given3="Colombian Peso",
            expected="The capital of Colombia is Bogota. They use the Colombian Peso",
        ),
    ]

    @pytest.mark.parametrize("test_case", test_cases)
    def test_task_is_implemented(self, test_case):
        country = test_case.given1
        capital = test_case.given2
        currency = test_case.given3

        assert_equals(
            message=f"> country= {country}\n> capital= {capital}\n> currency = {currency}",
            expected=test_case.expected,
            actual=task1(country=country, capital=capital, currency=currency),
        )
