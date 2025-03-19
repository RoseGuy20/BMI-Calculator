import pytest
import math
from src.bmi_calc import *

class TestConvertHeight:
    def test_normal_conversion(self):
        assert convertHeight(5, 10) == 70
        assert convertHeight(6, 0) == 72
    
    def test_zero_values(self):
        assert convertHeight(0, 0) == 00
        assert convertHeight(0, 12) == 12
    
    def test_large_values(self):
        assert convertHeight(7, 11) == 95


class TestCalcBMI:
    def test_normal_bmi_calculation(self):
        bmi = calcBMI(70, 160)
        assert bmi == pytest.approx(22.9, 0.1)
        
        bmi = calcBMI(72, 180)
        assert bmi == pytest.approx(24.4, 0.1)
    
    def test_zero_values(self):
        with pytest.raises(ZeroDivisionError):
            calcBMI(0, 0)
            calcBMI(0, 100)
            calcBMI(72, 0)

    def test_boundary_values(self):
        # Underweight/Normal boundary
        bmi_boundary1 = calcBMI(72, 136.4)
        assert bmi_boundary1 == pytest.approx(18.5, 0.1)
        
        # Normal/Overweight boundary 
        bmi_boundary2 = calcBMI(66, 155) 
        assert bmi_boundary2 == pytest.approx(25.0, 0.1)
        
        # Overweight/Obese boundary
        bmi_boundary3 = calcBMI(69, 197) 
        assert bmi_boundary3 == pytest.approx(30.0, 0.1)
    
    def test_extreme_values(self):
        assert calcBMI(66, 50) < 10
    
        assert calcBMI(66, 350) > 50


class TestDetBMICategory:
    def test_underweight_category(self):
        assert detBMICategory(18.4) == "Underweight"
        assert detBMICategory(10.0) == "Underweight"
        assert detBMICategory(0.1) == "Underweight"
    
    def test_normal_weight_category(self):
        assert detBMICategory(18.5) == "Normal weight"
        assert detBMICategory(21.7) == "Normal weight"
        assert detBMICategory(24.9) == "Normal weight"
    
    def test_overweight_category(self):
        assert detBMICategory(25.0) == "Overweight"
        assert detBMICategory(27.5) == "Overweight"
        assert detBMICategory(29.9) == "Overweight"
    
    def test_obese_category(self):
        assert detBMICategory(30.0) == "Obese"
        assert detBMICategory(35.0) == "Obese"
        assert detBMICategory(40.0) == "Obese"
    

def test_cli_mock(monkeypatch, capsys):
    inputs = iter(["5, 10", "160"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    from src.bmi_calc import cli
    cli()
    
    captured = capsys.readouterr()
    assert "BMI is" in captured.out


def test_cli_beg(monkeypatch, capsys):
    inputs = iter(["-5, 10", "160"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    
    from src.bmi_calc import cli
    cli()
    
    captured = capsys.readouterr()
    assert "Error:" in captured.out
