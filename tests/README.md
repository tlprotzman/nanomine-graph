# Nanomine Testing
* To write a custom test file, look at `test_L102.py` and `test_L168.py` as templates and modify as needed
* The autoparser currently allows for automatic testing of the following categories:
  * PNC Present
  * Language
  * Authors
  * Keywords
  * Devices
* This list will be expanded as new automated tests are developed
* Batch testing can be accomplised with `test_runner.py`
  * Run from whyis directory, `python apps/nanomine-graph/tests/test_runner.py <Number of tests to run> <--scramble>`
    * Can specify how many tests to run and if they should be selected randomly
  * Uses `test_template.py` as a template, replacing <FILENAME HERE> with the target file
  * Outputs std-err to `/apps/nanomine-graph/tests/output.txt` to allow investigation of failed tests
