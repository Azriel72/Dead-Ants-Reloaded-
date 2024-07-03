import pytest
from hormigas_muertas import dead_ant_count

def test_dead_ant_count():
    assert dead_ant_count("...ant...ant..nat.ant.t..ant...ant..ant..ant.anant..t") == 3

def test_dead_ant_count2():
    assert 1 == 0

def test_dead_ant_count3():
    assert dead_ant_count("...ant...ant..nat.ant.t..ant...ant..ant..ant.anant") == 2
