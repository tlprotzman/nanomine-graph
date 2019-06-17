from . import ingest_tester
from . import test_template
from testcase import WhyisTestCase

file_under_test = "L168_S4_Luo_2013"

class L168Test(test_template.IngestTestSetup):
    @classmethod
    def setUpClass(cls):
        cls.file_under_test = file_under_test
        super().setUpClass()

    def test_authors(self):
        expected_authors = ["Luo, Suibin", 
                            "Yu, Shuhui",
                            "Sun, Rong",
                            "Wong, Ching-Ping"]
        ingest_tester.test_authors(self, expected_authors)
        ingest_tester.test_authors(self)

    def test_language(self):
        ingest_tester.test_language(self, ["http://nanomine.org/language/english"])
        ingest_tester.test_language(self)

    def test_keywords(self):
        expected_keywords = ["Ag-Deposited Batio3",
                             "Hetero-Epitaxial Interface",
                             "Polymer Matrix",
                             "Dielectric Composites"]
        ingest_tester.test_keywords(self, expected_keywords)
        ingest_tester.test_keywords(self)

    def test_devices(self):
        expected_devices = ["http://nanomine.org/ns/cs9912bx",
                            "http://nanomine.org/ns/agilent-4294a-impedance-analyzer",
                            "http://nanomine.org/ns/xrd-d-max-2500-pc-rigaku-co",
                            "http://nanomine.org/ns/fei-nova-nanosem450",
                            "http://nanomine.org/ns/fei-tecnai-spirit"]
        ingest_tester.test_devices(self, expected_devices)
        ingest_tester.test_devices(self)

