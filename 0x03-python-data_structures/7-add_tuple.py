#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = tuple(sum(pair) for pair in zip_longest(tuple_a, tuple_b, fillvalue=0))
    return new_tuple
