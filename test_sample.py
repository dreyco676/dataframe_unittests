from Functions import *

def test_unique_values():
    f = get_df()
    d = unique_values(f)
    assert d['Age']['NaN'] == 177
    assert d['Cabin']['NaN'] == 687
    assert d['Embarked']['NaN'] == 2

def test_one():
    hist = get_hist_df()
    new = get_new_df()
    # print(hist.shape)
    # print(new.shape)
    assert shape_check(hist, new)

def test_two():
    hist = get_hist_df()
    new = get_new_df()
    assert NaN_check(hist, new, 'Cabin', 0.05)

def test_three():
    hist = get_hist_df()
    new = get_new_df()
    assert NaN_check_all(hist,new,0.05)

test_unique_values()
test_one()
test_two()
test_three()