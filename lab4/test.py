import sys
import pytest
sys.path.append('../lab3')
from index import Record, CashCalculator, CaloriesCalculator


@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=145, comment='кофе'))
    cash_calculator.add_record(Record(amount=300, comment='Серёге за обед'))
    cash_calculator.add_record(Record(amount=3000, comment='бар в Танин др'))
    return cash_calculator.get_today_cash_remained()


@pytest.fixture()
def cal_calc():
    calories_calculator = CaloriesCalculator(2000)
    calories_calculator.add_record(
        Record(amount=1186, comment='Кусок тортика. И ещё один.'))
    calories_calculator.add_record(Record(amount=84, comment='Йогурт.', ))
    calories_calculator.add_record(
        Record(amount=1140, comment='Баночка чипсов.', ))
    return calories_calculator.get_calories_remained()


def test_cashCalc(cash_calc):
    assert cash_calc == 'Your debt is -2445.0 Rub'


def test_CalCalc(cal_calc):
    assert cal_calc == 'Stop eating for today'
