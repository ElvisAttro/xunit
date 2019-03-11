#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WasRun:
    def __init__(self, name):
        self.name = name
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True

    def run(self):
        self.testMethod()


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
