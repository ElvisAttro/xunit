#!/usr/bin/env python
# -*- coding: utf-8 -*-

class WasRun:
    def __init__(self, name):
        self.name = name
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True

    def run(self):
        testMethod = getattr(self, self.name)
        testMethod()


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
