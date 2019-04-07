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
        try:
            method()
        except(AssertionError):
            results.failCount += 1
        results.testCount += 1
        self.log = self.log + "-Running()"
        self.tearDownTemplate()
        return results

    def reportResults(self):
        results = self.run()
        print(results.resultsSummary())


class TestResults():
    def __init__(self):
        self.testCount = 0
        self.failCount = 0

    def resultsSummary(self):
        status = "FAILURE" if self.failCount > 0 else "OK"
        return "{}. {} Run, {} Failled.".format(
            status, self.testCount, self.failCount)


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

    def testPassingResults(self):
        results = self.test.run()
        assert("OK. 1 Run, 0 Failled." == results.resultsSummary())

    def testFaillingResults(self):
        results = self.test.run()
        assert("FAILURE. 1 Run, 1 Failled." == results.resultsSummary())


TestCaseTest("testRunning").reportResults()
TestCaseTest("testPassingResults").reportResults()
TestCaseTest("testFaillingResults").reportResults()
