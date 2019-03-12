#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.methodName = name

    def run(self):
        method = getattr(self, self.methodName)
        method()

class WasRun(TestCase):
    def __init__(self, name):
        self.wasRun = False
        super().__init__(name)

    def testMethod(self):
        self.wasRun = True


test = WasRun("testMethod")
print(test.wasRun)
test.run()
print(test.wasRun)
