from . import ingest_tester
from . import test_template
from testcase import WhyisTestCase
import rdflib


class L102Test(test_template.IngestTest):
    @classmethod
    def setUpClass(cls):
        cls.file_under_test = "L102_S3_Hu_2007"
        super().setUpClass()

    def test_authors(self):
        expected_authors = ["Hu, Tao", 
                            "Juuti, Jari",
                            "Vilkman, Taisto",
                            "Jantunen, Heli"]
        ingest_tester.test_authors(self, expected_authors)
        ingest_tester.test_authors(self)

    def test_language(self):
        ingest_tester.test_language(self, ["http://nanomine.org/language/english"])
        ingest_tester.test_language(self)

    def test_keywords(self):
        expected_keywords = ["Composites",
                             "Dielectric Properties",
                             "Microstructure-Final",
                             "Bst-Coc"]
        ingest_tester.test_keywords(self, expected_keywords)
        ingest_tester.test_keywords(self)

    def test_devices(self):
        expected_devices = ["http://nanomine.org/ns/jeol-jsm-6400",
                            "http://nanomine.org/ns/agilent-e4991a",
                            "http://nanomine.org/ns/siemens-d5000"]
        ingest_tester.test_devices(self, expected_devices)
        ingest_tester.test_devices(self)

    def test_volume(self):
        excepted_volume = [rdflib.Literal(27)]
        ingest_tester.test_volume(self, excepted_volume)
        ingest_tester.test_volume(self)

    def test_matrix_chemical_names(self):
        expected_names = [rdflib.Literal("cyclo olefin copolymer")]
        ingest_tester.test_matrix_chemical_names(self, expected_names)
        ingest_tester.test_matrix_chemical_names(self)

    def test_matrix_trade_names(self):
        expected_names = [rdflib.Literal("Topas 8007s-04")]
        ingest_tester.test_matrix_trade_names(self, expected_names)
        ingest_tester.test_matrix_trade_names(self)

    def test_filler_chemical_names(self):
        expected_names = [rdflib.Literal("barium strontium titanate")]
        ingest_tester.test_filler_chemical_names(self, expected_names)
        ingest_tester.test_filler_chemical_names(self)

    def test_filler_trade_names(self):
        expected_names = []
        ingest_tester.test_filler_trade_names(self, expected_names)
        ingest_tester.test_filler_trade_names(self)
 



    # def test_print_triples(self):
        # ingest_tester.print_triples(self)



