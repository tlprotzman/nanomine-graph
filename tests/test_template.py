from . import ingest_tester
from testcase import WhyisTestCase

file_under_test = "<FILENAME HERE>"

class IngestTest(WhyisTestCase):
    create_app_once = True
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        print("Setting Up Class")
        IngestTest.first_run = True
        cls.expected_data = ingest_tester.autoparse(file_under_test)

    def setUp(self):
        if not IngestTest.first_run:
            return
        IngestTest.first_run = False
        ingest_tester.setUp(self, file_under_test)
        
    def test_nanocomposites(self):
        ingest_tester.test_nanocomposites(self)

    def test_authors(self):
        ingest_tester.test_authors(self, self.expected_data["authors"])

    def test_language(self):
        ingest_tester.test_language(self, self.expected_data["language"])

    def test_keywords(self):
        ingest_tester.test_keywords(self, self.expected_data["keywords"])

    def test_devices(self):
        ingest_tester.test_devices(self, self.expected_data["equipment"])


