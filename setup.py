import os
from setuptools import setup, find_packages

if __name__ == "__main__":

    base_dir = os.path.dirname(__file__)
    src_dir = os.path.join(base_dir, "src")

    about = {}
    with open(os.path.join(src_dir, "k_tour", "__about__.py")) as f:
        exec(f.read(), about)

    install_requires = ['numpy', 'click']

    setup(
        name=about['__title__'],

        description=about['__summary__'],
        url=about["__uri__"],

        author=about["__author__"],

        package_dir={'': 'src'},
        packages=find_packages(where='src'),
        include_package_data=True,
        
        install_requires=install_requires,
        entry_points="""
                [console_scripts]
                tour=k_tour.cli:tour
            """,

    )
