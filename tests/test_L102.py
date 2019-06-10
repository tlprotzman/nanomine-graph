import ingest_tester
from testcase import WhyisTestCase

file_under_test = "L102_S3_Hu_2007"

class L102Test(WhyisTestCase):
    first_run = bool()
    @classmethod
    def setUpClass(cls):
        print("Setting Up Class")
        L102Test.first_run = True
        cls.expected_data = ingest_tester.autoparse(file_under_test)

    def setUp(self):
        if not L102Test.first_run:
            return
        L102Test.first_run = False
        ingest_tester.setUp(self, file_under_test)
        
    def test_nanocomposites(self):
        ingest_tester.test_nanocomposites(self)

    def test_authors(self):
        expected_authors = ["Hu, Tao", 
                            "Juuti, Jari",
                            "Vilkman, Taisto",
                            "Jantunen, Heli"]
        ingest_tester.test_authors(self, expected_authors)
        ingest_tester.test_authors(self, self.expected_data["authors"])

    def test_language(self):
        ingest_tester.test_language(self, ["http://nanomine.org/language/english"])
        ingest_tester.test_language(self, self.expected_data["language"])

    def test_keywords(self):
        expected_keywords = ["Composites",
                             "Dielectric Properties",
                             "Microstructure-Final",
                             "Bst-Coc"]
        ingest_tester.test_keywords(self, expected_keywords)
        ingest_tester.test_keywords(self, self.expected_data["keywords"])

    def test_devices(self):
        expected_devices = ["http://nanomine.org/ns/jeol-jsm-6400",
                            "http://nanomine.org/ns/agilent-e4991a",
                            "http://nanomine.org/ns/siemens-d5000"]
        ingest_tester.test_devices(self, expected_devices)
        ingest_tester.test_devices(self, self.expected_data["equipment"])

    def test_print_triples(self):
        ingest_tester.print_triples(self)


