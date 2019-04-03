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
        self.setUpTemplate()
        method = getattr(self, self.methodName)
        method()
        self.log = self.log + "-Running()"
        self.tearDownTemplate()


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


TestCaseTest("testRunning").run()
