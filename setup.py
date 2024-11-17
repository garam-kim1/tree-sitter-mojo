from os.path import isdir, join
from platform import system

from setuptools import Extension, find_packages, setup
from setuptools.command.build import build
from wheel.bdist_wheel import bdist_wheel


class Build(build):
    def run(self):
        if isdir("queries"):
            dest = join(self.build_lib, "tree_sitter_mojo", "queries")
            self.copy_tree("queries", dest)
        super().run()


class BdistWheel(bdist_wheel):
    def get_tag(self):
        mojo, abi, platform = super().get_tag()
        if mojo.startswith("cp"):
            mojo, abi = "cp39", "abi3"
        return mojo, abi, platform


setup(
    packages=find_packages("bindings/mojo"),
    package_dir={"": "bindings/mojo"},
    package_data={
        "tree_sitter_mojo": ["*.pyi", "py.typed"],
        "tree_sitter_mojo.queries": ["*.scm"],
    },
    ext_package="tree_sitter_mojo",
    ext_modules=[
        Extension(
            name="_binding",
            sources=[
                "bindings/mojo/tree_sitter_mojo/binding.c",
                "src/parser.c",
                "src/scanner.c",
            ],
            extra_compile_args=[
                "-std=c11",
                "-fvisibility=hidden",
            ] if system() != "Windows" else [
                "/std:c11",
                "/utf-8",
            ],
            define_macros=[
                ("Py_LIMITED_API", "0x03090000"),
                ("PY_SSIZE_T_CLEAN", None),
                ("TREE_SITTER_HIDE_SYMBOLS", None),
            ],
            include_dirs=["src"],
            py_limited_api=True,
        )
    ],
    cmdclass={
        "build": Build,
        "bdist_wheel": BdistWheel
    },
    zip_safe=False
)