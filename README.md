`underpants` - Or, using Pants as an embedded rule engine
=========================================================

DISCLAIMER: This is not in any way to show how to use Pants, or recommended patterns of
use. Provided here AS-IS. No gurantees of any kind, as this may break with any future release of
Pants.

This is a toy POC testing out the feasability of using the [Pants Build
System](https://www.pantsbuild.org/) as a rule engine in your Python application.

It's also a test-bed for exploring the intricacies of rule caching etc.


Expected output along the lines of:
```
$ ./pants run src/pr:main
12:32:31.96 [INFO] Starting: pr.demo.basic.answer_to_life_universe_and_everything
12:32:31.96 [INFO] Starting: pr.demo.basic.reverse_input
== in reverse_input: InputData(text='answer')
12:32:31.96 [INFO] Completed: pr.demo.basic.reverse_input
== data: OutputData(text='rewsna')
12:32:31.96 [INFO] Completed: pr.demo.basic.answer_to_life_universe_and_everything
The result is: SimpleResult(answer=41)
12:32:32.47 [INFO] Starting: pr.demo.basic.answer_to_life_universe_and_everything
== data: OutputData(text='rewsna')
12:32:32.47 [INFO] Completed: pr.demo.basic.answer_to_life_universe_and_everything
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

The lock file uses the currently under development lockfile features of `pex3`, and as such, is not
yet integrated in the Pants build flow, and requires manual intervention. To update the
`3rdparty/constraints.txt` file run the following two commands:

```
pex3 lock update 3rdparty/requirements.lock
pex3 lock export -o 3rdparty/constraints.txt 3rdparty/requirements.lock
```

To add/change the requirements, re-create the lockfile from `3rdparty/requirements.txt`:

```
pex3 lock create -r 3rdparty/requirements.txt -o 3rdparty/requirements.lock
```
