#!/usr/bin/env python
# -*- coding: utf-8 -*-

import traceback

class TestCase:
    def __init__(self, name):
        self.methodName = name
        self.results = TestResults()

    def run(self):
        self.results.collectTestExecution()
        try:
            self.setUpTemplate()
        except Exception as e:
            self.results.collectTestError(self.__class__.__name__,traceback.format_exc())
            return e
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
        except Exception as e:
            self.results.collectTestError(self.__class__.__name__,traceback.format_exc())
            return e
        self.log = self.log + "-TearDown()"

    def tearDown(self):
        pass

    def executeTestMethod(self, name):
        try:
            method = getattr(self, name)
            method()
        except AssertionError as e:
            self.results.collectTestFailure(self.__class__.__name__, traceback.format_exc())
            return e
        except Exception as e:
            self.results.collectTestError(self.__class__.__name__, traceback.format_exc())
            return e
        self.log = self.log + "-Running()"

    def reportResults(self):
        reporter = TestResultsReporter()
        self.run()
        reporter.reportResults(self.results)


class TestResults():
    def __init__(self):
        self.testCount = 0
        self.failCount = 0
        self.errorCount = 0
        self.troublesStack= []

    def collectTestExecution(self):
        self.testCount += 1

    def collectTestFailure(self, invoker, e):
        self.troublesStack.append(("FAIL", invoker, e))
        self.failCount += 1

    def collectTestError(self,invoker, e):
        self.troublesStack.append(("ERROR", invoker, e))
        self.errorCount += 1

    def resultsSummary(self):
        status = "ERROR" if self.errorCount > 0 else "FAILURE" if self.failCount > 0 else "OK"
        return "{}. {} Ran, {} Failed, {} Error(s).".format(
            status, self.testCount, self.failCount, self.errorCount)

class TestResultsReporter():
    def reportResults(self,testResults):
        for trouble in testResults.troublesStack:
            self.reportTrouble(trouble)
        self.reportSummary(testResults.resultsSummary())

    def reportTrouble(self, trouble):
        print("="*50)
        print("{}: {}".format(trouble[0], trouble[1]))
        print("-"*50)
        print(trouble[2])

    def reportSummary(self, summary):
        print("-"*50)
        print(summary)
        print()


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
TearDownExceptionTest("testRunningi").reportResults()
