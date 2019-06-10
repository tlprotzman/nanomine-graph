import ingest_test_template
from testcase import WhyisTestCase

file_under_test = "L168_S4_Luo_2013"

class L168Test(WhyisTestCase):
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        print("Setting Up Class")
        L168Test.first_run = True
        cls.expected_data = ingest_test_template.autoparse(file_under_test)

    def setUp(self):
        if not L168Test.first_run:
            return
        L168Test.first_run = False
        ingest_test_template.setUp(self, file_under_test)

    def test_nanocomposites(self):
        ingest_test_template.test_nanocomposites(self)

    def test_authors(self):
        expected_authors = ["Luo, Suibin", 
                            "Yu, Shuhui",
                            "Sun, Rong",
                            "Wong, Ching-Ping"]
        ingest_test_template.test_authors(self, expected_authors)
        ingest_test_template.test_authors(self, self.expected_data["authors"])

    def test_language(self):
        ingest_test_template.test_language(self, ["http://nanomine.org/language/english"])
        ingest_test_template.test_language(self, self.expected_data["language"])

    def test_keywords(self):
        expected_keywords = ["Ag-Deposited Batio3",
                             "Hetero-Epitaxial Interface",
                             "Polymer Matrix",
                             "Dielectric Composites"]
        ingest_test_template.test_keywords(self, expected_keywords)
        ingest_test_template.test_keywords(self, self.expected_data["keywords"])

    def test_devices(self):
        expected_devices = ["http://nanomine.org/ns/cs9912bx",
                            "http://nanomine.org/ns/agilent-4294a-impedance-analyzer",
                            "http://nanomine.org/ns/xrd-d-max-2500-pc-rigaku-co",
                            "http://nanomine.org/ns/fei-nova-nanosem450",
                            "http://nanomine.org/ns/fei-tecnai-spirit"]
        ingest_test_template.test_devices(self, expected_devices)
        ingest_test_template.test_devices(self, self.expected_data["equipment"])

