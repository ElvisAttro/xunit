#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.methodName = name

    def run(self):
        self.setUpTemplate()
        results = self.executeTestMethod(self.methodName)
        self.tearDownTemplate()
        return results

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

    def executeTestMethod(self, name):
        results = TestResults()
        method = getattr(self, name)
        try:
            method()
        except(AssertionError):
            results.collectTestFailure()
        results.collectTestExecution()
        self.log = self.log + "-Running()"
        return results

    def reportResults(self):
        results = self.run()
        print(results.resultsSummary())


class TestResults():
    def __init__(self):
        self.testCount = 0
        self.failCount = 0

    def collectTestExecution(self):
        self.testCount += 1

    def collectTestFailure(self):
        self.failCount += 1

    def resultsSummary(self):
        status = "FAILURE" if self.failCount > 0 else "OK"
        return "{}. {} Run, {} Failed.".format(
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

    def testFaillingResults(self):
        self.test.run()
        assert(self.test.wasRun is False)


TestCaseTest("testRunning").reportResults()
TestCaseTest("testFaillingResults").reportResults()
