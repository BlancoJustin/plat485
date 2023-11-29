import pytest
from plat485.projects.hw13.pass_strength import compute_complexity
from plat485.projects.hw13.pass_strength import evaluate_strength

"""
Testable Things:

compute_complexity
-function should return float value
-complexity rating should rise with addition of complex characters
    -test every complexifier for this

evaluate_strength
-Function should return a bool
-Should raise type error if password's not a string
-Returns true for complexity > strength_threshold (50.0)
    -and returns false if not


"""


"""
Testing for compute_complexity
"""


@pytest.mark.parametrize('data, expected_complexity', [
    ('password', 0.0),
    ('PAsSwOrD', 0.0),
    ('PASS', 0.0),
    ('4820!?', 0.0),
    ('password4839', 0.0),
    ('~@#$%^&-_+=', 100.0),
    ('password!@#$', 25.0),
    ('password@$', 20.0),
    ('password&', 11.11111111111111),
    ('password', 0.0),

])
def test_compute_complexity(data, expected_complexity):
    result = compute_complexity(data)
    assert result == expected_complexity


"""
Testing for evaluate_strength
"""


@pytest.mark.parametrize('password, expected_result', [
    ('password123', False),
    ('!@#$%^&*&~~', True),
    ('password~', False),

])
def test_evaluate_strength_returns_correct_value(password, expected_result):
    result = evaluate_strength(password)
    assert isinstance(result, bool)
    assert result == expected_result


@pytest.mark.parametrize('password', [
    1.55,
    592,
    7,
    1.11111111,
    True,
    False,
    [],
    {},
])
def test_evaluate_strength_raises_TypeError_for_non_strings(password):
    with pytest.raises(TypeError):
        evaluate_strength(password)
