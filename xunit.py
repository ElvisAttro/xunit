#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TestCase:
    def __init__(self, name):
        self.methodName = name
        self.results = TestResults()

    def run(self):
        try:
            self.setUpTemplate()
        except Exception:
            self.results.collectTestError()
        else:
            self.executeTestMethod(self.methodName)
            self.tearDownTemplate()

    def setUpTemplate(self):
        self.setUp()
        self.log = "Setup()"

    def setUp(self):
        pass

    def tearDownTemplate(self):
        try:
            self.tearDown()
        except Exception:
            self.results.collectTestError()
        self.log = self.log + "-TearDown()"

    def tearDown(self):
        pass

    def executeTestMethod(self, name):
        method = getattr(self, name)
        try:
            method()
        except AssertionError:
            self.results.collectTestFailure()
        self.results.collectTestExecution()
        self.log = self.log + "-Running()"

    def reportResults(self):
        self.run()
        print(self.results.resultsSummary())


class TestResults():
    def __init__(self):
        self.testCount = 0
        self.failCount = 0
        self.errorCount = 0

    def collectTestExecution(self):
        self.testCount += 1

    def collectTestFailure(self):
        self.failCount += 1

    def collectTestError(self):
        self.errorCount += 1

    def resultsSummary(self):
        status = "ERROR" if self.errorCount > 0 else "FAILURE" if self.failCount > 0 else "OK"
        return "{}. {} Ran, {} Failed, {} Error(s).".format(
            status, self.testCount, self.failCount, self.errorCount)


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
        assert(self.test.wasRun is True)

    def testFaillingResults(self):
        self.test.run()
        assert(self.test.wasRun is False)


class SetUpExceptionTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")
        raise Exception

    def testRunningSequence(self):
        pass


class TearDownExceptionTest(TestCase):
    def setUp(self):
        self.test = WasRun("testMethod")

    def tearDown(self):
        raise Exception

    def testRunning(self):
        self.test.run()
        assert(self.test.wasRun is True)


TestCaseTest("testRunning").reportResults()
TestCaseTest("testFaillingResults").reportResults()
SetUpExceptionTest("testRunningSequence").reportResults()
TearDownExceptionTest("testRunning").reportResults()
