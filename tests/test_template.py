import ingest_test_template
from testcase import WhyisTestCase

file_under_test = <FILENAME HERE>

class IngestTest(WhyisTestCase):
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        print("Setting Up Class")
        IngestTest.first_run = True
        cls.expected_data = ingest_test_template.autoparse(file_under_test)

    def setUp(self):
        if not IngestTest.first_run:
            return
        IngestTest.first_run = False
        ingest_test_template.setUp(self, file_under_test)
        
    def test_nanocomposites(self):
        ingest_test_template.test_nanocomposites(self)

    def test_authors(self):
        ingest_test_template.test_authors(self, self.expected_data["authors"])

    def test_language(self):
        ingest_test_template.test_language(self, self.expected_data["language"])

    def test_keywords(self):
        ingest_test_template.test_keywords(self, self.expected_data["keywords"])

    def test_devices(self):
        ingest_test_template.test_devices(self, self.expected_data["equipment"])


