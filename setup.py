from setuptools import setup
from io import open
from enzyme_sphinx_theme import __version__

setup(
    name = 'enzyme_sphinx_theme',
    version =__version__,
    author = 'Shift Lab',
    author_email= 'info@shiftlabny.com',
    url="https://github.com/enzymead/enzyme_sphinx_theme",
    docs_url="https://github.com/enzymead/enzyme_sphinx_theme",
    description='Enzyme Sphinx Theme',
    py_modules = ['enzyme_sphinx_theme'],
    packages = ['enzyme_sphinx_theme'],
    include_package_data=True,
    zip_safe=False,
    package_data={'enzyme_sphinx_theme': [
        'theme.conf',
        '*.html',
        'static/css/*.css',
        'static/js/*.js',
        'static/fonts/*.*',
        'static/images/*.*',
        'theme_variables.jinja'
    ]},
    entry_points = {
        'sphinx.html_themes': [
            'enzyme_sphinx_theme = enzyme_sphinx_theme',
        ]
    },
    license= 'MIT License',
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Internet",
        "Topic :: Software Development :: Documentation"
    ],
    install_requires=[
       'sphinx'
    ]
)
