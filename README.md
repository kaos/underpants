`underpants` - Or, using Pants as an embedded rule engine
=========================================================

DISCLAIMER: This is not in any way to show how to use Pants, or recommended patterns of
use. Provided here AS-IS. No gurantees of any kind, as this may break with any future release of
Pants.

This is a toy POC testing out the feasability of using the [Pants Build
System](https://www.pantsbuild.org/) as a rule engine in your Python application.

It's also a test-bed for me to explore the intricacies of rule caching etc.


Expected output along the lines of:
```
$ ./pants run src/pants_rules/main.py
14:00:05.78 [INFO] Starting: pants_rules.demo.basic.answer_to_life_universe_and_everything
14:00:05.78 [INFO] Starting: pants_rules.demo.basic.reverse_input
== in reverse_input: InputData(text='answer')
14:00:05.78 [INFO] Completed: pants_rules.demo.basic.reverse_input
== data: OutputData(text='rewsna')
14:00:05.78 [INFO] Completed: pants_rules.demo.basic.answer_to_life_universe_and_everything
The result is: SimpleResult(answer=41)
14:00:06.29 [INFO] Starting: pants_rules.demo.basic.answer_to_life_universe_and_everything
== data: OutputData(text='rewsna')
14:00:06.29 [INFO] Completed: pants_rules.demo.basic.answer_to_life_universe_and_everything
The result is: SimpleResult(answer=42)
The result is: ProcResult(code=0, err=None)
The result is: ProcResult(code=1, err="proc 'fail' failed")
```


License
=======

Provided under the [MIT](https://opensource.org/licenses/MIT) license, as "public domain" is not an
OSI approved license.


Lockfile
========

To update the `3rdparty/requirements.lock` file run:

```
./pants generate-lockfiles
```


Version
=======

Use at your own peril:
[![version](https://img.shields.io/pypi/v/underpants.svg)](https://pypi.org/project/underpants)
