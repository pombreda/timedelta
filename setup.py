from setuptools import setup
from setuptools import find_packages

setup(
    name = "timedelta-tool",
    version = "0.2.0",
    package_dir = {'' : 'src'},
    packages = find_packages('src'),
    entry_points = {
        'console_scripts': [
            'timedelta = timedelta_tool:main',
        ]
    },

    install_requires = [
        'python-dateutil'
    ],

    author = "Jean-Louis Fuchs",
    author_email = "ganwell@fangorn.ch",
    description = "Very simple timedelta tool",
    license = "Modified BSD",
    long_description = """
timedelta 1440 1500 will return 0.33 which is the delta in hours.
""",
    keywords = "timedelta timesheet worktime",
    url = "https://github.com/ganwell/timedelta",
    classifiers = [
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.3",
    ]
)
