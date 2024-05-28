import pytest
import random
from memory_profiler import memory_usage
from hormigas_muertas import dead_ant_count, dead_ant_count_v2

def generate_text(length):
    return ''.join(random.choices('.ant', k = length))

n_range = [32] #numero de caracteres en la cadena

@pytest.mark.parametrize("size", n_range)
def test_dead_ant_count(benchmark,size):
    text = generate_text(size)
    memoria_usada = memory_usage((dead_ant_count, (text,)))
    benchmark(dead_ant_count, text)
    print(f"Memoria usada por dead_ant_count con {size} caracteres: {max(memoria_usada)}")

@pytest.mark.parametrize("size", n_range)
def test_dead_ant_count_v2(benchmark,size):
    text = generate_text(size)
    memoria_usada = memory_usage((dead_ant_count_v2, (text,)))
    benchmark(dead_ant_count_v2, text)
    print(f"Memoria usada por dead_ant_count_v2 con {size} caracteres: {max(memoria_usada)}")
