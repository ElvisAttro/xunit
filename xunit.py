#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WasRun:
    def __init__(self):
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True

    def run(self):
        self.testMethod()


test = WasRun()
print(test.wasRun)
test.run()
print(test.wasRun)
