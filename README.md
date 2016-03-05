# Hello-World-Genetic-or-Evolutionary-Algorithm
https://www.reddit.com/r/dailyprogrammer/comments/40rs67/20160113_challenge_249_intermediate_hello_world/

## Usage
```sh
$ python test.py
```

OR for a little extra boost in performance, use cython


```sh
$ virtualenv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ python setup.py build_ext --inplace  # This takes a while if building cython for the first time
(venv) $ python test.py  # Now run
```
