# python-boilerplate

* [Pythonのパッケージングのベストプラクティスについて考える2018](https://techblog.asahi-net.co.jp/entry/2018/06/15/162951)

Please rename this package:

```sh
PACKAGE_NAME=foobar
git ls-files | xargs sed -i "s/python_boilerplate/${PACKAGE_NAME}/g"
mv python_boilerplate "$PACKAGE_NAME"
rm -rf .git
```

## Create and activate venv

```sh
python3 -m venv .venv
source .venv/bin/activate
```

## Install

```sh
pip install .
```

## Upgrade

```sh
pip install -U .  # or --upgrade
```

## Install (for developer)

```sh
pip install -e '.[dev]'
```

## Import this library

(Python)

```python
import python_boilerplate
print(python_boilerplate.add(1, 1))  # => 2
```

## Execute this application

```sh
python-boilerplate 1 1
```

## Test

```sh
pytest
```

## Test against multiple environments

```sh
tox
```

## Create a source distribution

```sh
python setup.py sdist
```

## Create a wheel package

```sh
pip install wheel
python setup.py bdist_wheel
```
