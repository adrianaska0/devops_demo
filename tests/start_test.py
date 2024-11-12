'''Startup Testing'''
from app import start

def test_start():
    '''Testing the Start func'''
    assert start() == True