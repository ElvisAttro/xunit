#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.methodName = name

    def setUpTemplate(self):
        self.setUp()
        self.wasSetUp = True

    def setUp(self):
        pass

    def run(self):
        self.setUpTemplate()
        method = getattr(self, self.methodName)
        method()

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = False
        self.wasSetUp = False

    def testMethod(self):
        self.wasRun = True

class TestCaseTest(TestCase):
    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasRun)

    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert(test.wasSetUp)


TestCaseTest("testRunning").run()
TestCaseTest("testSetUp").run()
