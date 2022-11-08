import pytest
import sys
sys.path.append('../lab3')
from index import Record, CashCalculator, CaloriesCalculator


@pytest.fixture()
def cal_calc():
    calories_calculator = CaloriesCalculator(3220)
    calories_calculator.add_record(
        Record(amount=2000, comment='Pizza'))
    calories_calculator.add_record(
        Record(amount=1000, comment='Coffee', ))
    return calories_calculator.get_calories_remained()


@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(500)
    cash_calculator.add_record(Record(amount=228, comment='tea'))
    cash_calculator.add_record(Record(amount=322, comment='CHIMICHUNGUS'))
    return cash_calculator.get_today_cash_remained()


def test_cashCalc(cash_calc):
    assert cash_calc == 'Cash left (Currency: Rub)'


def test_CalCalc(cal_calc):
    assert cal_calc == 'Calories left: 220.'
