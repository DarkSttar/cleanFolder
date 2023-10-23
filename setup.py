from setuptools import setup,find_namespace_packages



setup(
    name='cleanfolder',
    version='1.0.0',
    description='Sorting and cleaning Directory',
    author='Dark Star',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean_folder=cleanfolder.main:start']}
)

