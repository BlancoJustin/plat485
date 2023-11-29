import pytest
from plat485.projects.hw12.pass_comp import compute_complexity

"""
Testable things:
Parameter data:
-testing complexifiers
every char in complexifiers should count towards num_complexifiers
    ~@#$PASS%^&-_+=
num_complexifiers (testing number of complexifieres in data are accurate)
testing the for loop
    password@$ (2)
    password% (1)
    pass_word+~ (3)
-without complexifiers (other unique chars not in complexifiers)
    password (0)
    PasSwOrD (0)
    PASS (0)
    5438!?> 

-length_of_data 
    string should be the accurate length
password (8)
password# (9)
pass@& (6)

-complexity calculation (rating should correlate with num_complexifiers and length_of_data)

Testing floats
-Should raise type error
Testing ints
-should raise type error
"""
print(compute_complexity('~@#$%^&-_+='))

@pytest.mark.parametrize('data, expected_complexity', [
    ('password', 0.0),
    ('PAsSwOrD', 0.0),
    ('PASS', 0.0),
    ('4820!?', 0.0),
    ('password4839', 0.0),
    ('~@#$%^&-_+=', 100),
    ('password!@#$', 25.0),
    ('password@$', 20.0),
    ('password&', 11.11111111111111),
    ('password', 0.0),


])
def test_compute_complexity(data, expected_complexity):
    result = compute_complexity(data)
    assert result == expected_complexity

def test_compute_complexity_int():
    with pytest.raises(TypeError):
        complexity = compute_complexity(1345)

def test_compute_complexity_float():
    with pytest.raises(TypeError):
        complexity = compute_complexity(43.6425)




