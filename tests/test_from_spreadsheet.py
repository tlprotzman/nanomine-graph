import functools
import rdflib
import pandas as pd

prefixes = {
    "nanomine:": "http://nanomine.org/sample/",
    "sio:": "http://semanticscience.org/resource/",
    "obo:": "http://purl.obolibrary.org/obo/",
}


def load_spreadsheet(sheet):
    df = pd.read_csv(sheet)
    if "uri" not in df.columns or "xpath" not in df.columns:
        return None
    df = df[["uri", "xpath"]].dropna()
    df["uri"] = df["uri"].apply(lambda s: functools.reduce(lambda base, p: base.replace(
        p, prefixes[p]), [s] + list(prefixes.keys())))  # Just because you can doesn't mean you should
    df["xpath"] = df["xpath"].apply(lambda s: "." + s)
    return df


def test_uri_xpath_pairs(runner, df):
    def query_graph(runner, uri):
        return runner.app.db.objects(None, rdflib.URIRef(uri))

    def query_xml(runner, xpath):
        return runner.xml.findall(xpath)

    pairs = [(query_graph(runner, row["uri"]), query_xml(runner, row["xpath"]))
             for _, row in df.iterrows()]
    graph, xml = zip(*pairs)
    runner.assertListEqual(xml, graph)


def main():
    load_spreadsheet("ontology_spreadsheet/Material.csv")


if __name__ == "__main__":
    main()
