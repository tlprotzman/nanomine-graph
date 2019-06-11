import os
import sys
import time
import random
from SPARQLWrapper import SPARQLWrapper, JSON

def main(argv):
    run_all = True
    to_run = 0
    if len(argv) >= 2:
        run_all = False
        to_run = int(argv[1])
    endpoint = SPARQLWrapper("https://materialsmine.org/wi/sparql")
    endpoint.setQuery(
        '''
        SELECT DISTINCT ?article WHERE {
            ?doi a <http://nanomine.org/ns/ResearchArticle> .
            ?doi <http://semanticscience.org/resource/hasPart> ?article .
        }
        '''
    )
    endpoint.setReturnFormat(JSON)
    results = endpoint.query().convert()
    files = [uri["article"]["value"].replace("http://nanomine.org/sample/", "").replace("-", "_").title()
             for uri in results["results"]["bindings"]]


    if os.path.exists("/apps/nanomine-graph/tests/output.txt"):
        os.remove("/apps/nanomine-graph/tests/output.txt")

    tests_ran = 0
    tests_failed = 0
    if "--scramble" in argv:
        random.shuffle(files)
    for uri in files:
        sys.stdout.write(uri + "...")
        tests_ran += 1
        test_text = str()
        with open("/apps/nanomine-graph/tests/test_template.py", "r") as f:
            test_text = f.read()
        test_text = test_text.replace("<FILENAME HERE>", uri)
        with open("/apps/nanomine-graph/tests/test_template_active.py", "w") as f:
            f.write(test_text)
        _, std_out, std_err = os.popen3("/apps/whyis/venv/bin/python manage.py test --test=test_template_active")
        std_out = std_out.read()
        std_err = std_err.read()
        if "FAILED" in std_err:
            print(" FAIL")
            tests_failed += 1
            with open("/apps/nanomine-graph/tests/output.txt", "a") as outfile:
                outfile.write("*" * 20 + uri + "*" * 20)
                # outfile.write("\nSTDOUT\n")
                # outfile.write(std_out)
                outfile.write("\nSTDERR\n")
                outfile.write(std_err)    
                outfile.write("\n" + "*" * 45)
                outfile.write("\n\n\n")
        else:
            print(" PASS")
        os.remove("/apps/nanomine-graph/tests/test_template_active.py")
        if not run_all and tests_ran >= to_run:
            break
    return tests_ran, tests_failed


if __name__ == "__main__":
    start = time.time()
    tests_ran, tests_failed = main(sys.argv)
    end = time.time()
    print("{}/{} tests passed in {:.1} seconds".format(tests_ran - tests_failed, tests_ran, end - start))