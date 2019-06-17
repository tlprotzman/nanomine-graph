from . import ingest_tester
from . import test_template
from testcase import WhyisTestCase

file_under_test = "<FILENAME HERE>"

class IngestTestRunner(test_template.IngestTest):
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        cls.file_under_test = file_under_test
        super().setUpClass()