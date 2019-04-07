#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.methodName = name

    def setUpTemplate(self):
        self.setUp()
        self.log = "Setup()"

    def setUp(self):
        pass

    def tearDownTemplate(self):
        self.tearDown()
        self.log = self.log + "-TearDown()"

    def tearDown(self):
        pass

    def run(self):
        results = TestResults()
        self.setUpTemplate()
        method = getattr(self, self.methodName)
        method()
        results.testCount += 1
        self.log = self.log + "-Running()"
        self.tearDownTemplate()
        return results

class TestResults():
    def __init__(self):
        self.testCount = 0

    def resultsSummary(self):
        return "OK. {} Run, 0 Failled.".format(self.testCount)

class WasRun(TestCase):
    def setUp(self):
        self.wasRun = False

    def testMethod(self):
        self.wasRun = True


class TestCaseTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def testRunning(self):
        self.test.run()
        assert(self.test.log == "Setup()-Running()-TearDown()")

    def testResults(self):
        results = self.test.run()
        assert("OK. 1 Run, 0 Failled." == results.resultsSummary())


TestCaseTest("testRunning").run()
TestCaseTest("testResults").run()
