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

    def testRunning(self):
        test = WasRun("testMethod")
        assert(not test.wasRun)
        test.run()
        assert(test.wasRun)

WasRun("testRunning").run()
