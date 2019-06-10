import ingest_test_template
from testcase import WhyisTestCase

class L168Test(WhyisTestCase):
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        print("Setting Up Class")
        L168Test.first_run = True

    def setUp(self):
        if not L168Test.first_run:
            return
        L168Test.first_run = False
        ingest_test_template.setUp(self, "L168_S4_Luo_2013")

    def test_nanocomposites(self):
        ingest_test_template.test_nanocomposites(self)

    def test_authors(self):
        expected_authors = ["Luo, Suibin", 
                            "Yu, Shuhui",
                            "Sun, Rong",
                            "Wong, Ching-Ping"]
        ingest_test_template.test_authors(self, expected_authors)

    def test_language(self):
        ingest_test_template.test_language(self, u'<http://nanomine.org/language/english>')

    def test_keywords(self):
        expected_keywords = ["Ag-Deposited Batio3",
                             "Hetero-Epitaxial Interface",
                             "Polymer Matrix",
                             "Dielectric Composites"]
        ingest_test_template.test_keywords(self, expected_keywords)

    def test_devices(self):
        expected_devices = ["http://nanomine.org/ns/cs9912bx",
                            "http://nanomine.org/ns/agilent-4294a-impedance-analyzer",
                            "http://nanomine.org/ns/xrd-d-max-2500-pc-rigaku-co",
                            "http://nanomine.org/ns/fei-nova-nanosem450",
                            "http://nanomine.org/ns/fei-tecnai-spirit"]
        ingest_test_template.test_devices(self, expected_devices)
