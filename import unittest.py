import unittest
from xmlrunner import XMLTestRunner

# Import the test case class
from openwebsitetest import TestWebpage

# Create a test suite
suite = unittest.TestSuite()

# Add the test case to the suite
suite.addTest(unittest.makeSuite(TestWebpage))

# Create an XMLTestRunner
runner = XMLTestRunner(output="test_results")

# Run the test suite
result = runner.run(suite)

# Print the results
print(f"Result: {result}")
print(f"Errors: {len(result.errors)}")
print(f"Failures: {len(result.failures)}")
print(f"Skipped: {len(result.skipped)}")
print(f"Tests run: {result.testsRun}")