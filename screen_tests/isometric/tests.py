"""Unit tests for the app."""

from utils import *


def test_get_map_differences():
    map1 = [
        [1, 1, 1],
        [1, 1, 1],
        [1, 1, 1]
    ]
    map2 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 1]
    ]
    map3 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    
    assert get_map_differences(map1, map2) == [(1, 1)]
    assert get_map_differences(map1, map3) == [(1, 1), (2, 2)]
    assert get_map_differences(map2, map3) == [(2, 2)]
    assert get_map_differences(map1, map1) == []
    assert get_map_differences(map2, map2) == []
    assert get_map_differences(map3, map3) == []

def test_transpose():
    map1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    map2 = [
        [1, 1, 1],
        [0, 0, 1],
        [1, 1, 0]
    ]
    map3 = [
        [1, 0, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    
    assert transpose(map1) == map1
    assert transpose(map2) == map3
    assert transpose(map3) == map2
    
def test_reverse_rows():
    map1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    map2 = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    assert reverse_rows(map1) == map2
    assert reverse_rows(map2) == map1
    
def test_reverse_tiles():
    map1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    map2 = [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1]
    ]
    
    assert reverse_tiles(map1[0]) == map1[0]
    assert reverse_tiles(map1[1]) == map2[1]
    assert reverse_tiles(map1[2]) == map2[2]
    
def test_map_rotation():
    map1 = [
        [1, 1, 1],
        [1, 0, 1],
        [1, 1, 0]
    ]
    map1_left = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1]
    ]
    map1_right = [
        [1, 1, 1],
        [1, 0, 1],
        [0, 1, 1]
    ]
    map1_down = [
        [1, 1, 0],
        [1, 0, 1],
        [1, 1, 1]
    ]
    
    assert reverse_rows(map1) == map1_down
    assert transpose(map1) == map1_left

test_get_map_differences()
test_transpose()
test_reverse_rows()
test_reverse_tiles()
test_map_rotation()