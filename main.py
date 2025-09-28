from test_runner import TestRunner
from test_loader_test import TestLoaderTest
from test_loader import TestLoader


loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)