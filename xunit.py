#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestCase:
    def __init__(self):
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True

test = TestCase()
print(test.wasRun)
test.testMethod()
print(test.wasRun)
