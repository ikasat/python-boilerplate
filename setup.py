import ast
import os
import re
import subprocess

from setuptools import Command, setup

PACKAGE_NAME = 'python_boilerplate'

with open(os.path.join(PACKAGE_NAME, '__init__.py')) as f:
    match = re.search(r'__version__\s+=\s+(.*)', f.read())
version = str(ast.literal_eval(match.group(1)))


class SimpleCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass


class VetCommand(SimpleCommand):
    def run(self):
        subprocess.check_call(["mypy", PACKAGE_NAME])
        subprocess.check_call(["flake8"])


class FmtCommand(SimpleCommand):
    def run(self):
        subprocess.call(["isort", "-y"])
        subprocess.call(["autopep8", "-ri", PACKAGE_NAME, "tests", "setup.py"])


class DocCommand(SimpleCommand):
    def run(self):
        opt = "-f" if os.path.exists(os.path.join("docs", "conf.py")) else "-F"
        subprocess.call(["sphinx-apidoc", opt, "-o", "docs", PACKAGE_NAME])
        if os.name == 'nt':
            subprocess.call([os.path.join("docs", "make.bat"), "html"])  # for Windows
        else:
            subprocess.call(["make", "-C", "docs", "html"])


setup(
    # metadata
    name=PACKAGE_NAME,
    version=version,

    # options
    packages=[PACKAGE_NAME],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.4',
    install_requires=[
        'typing; python_version<"3.5"',
    ],
    entry_points='''
        [console_scripts]
        {app}={pkg}.cli:main
    '''.format(app=PACKAGE_NAME.replace('_', '-'), pkg=PACKAGE_NAME),
    cmdclass={
        "vet": VetCommand,
        "fmt": FmtCommand,
        "doc": DocCommand,
    },
)
