#!/usr/bin/env python3
__author__ = 'rohe0002'

from sp_test import tests
from sp_test import Client
from sp_test.check import factory

cli = Client(tests, factory)
cli.run()
