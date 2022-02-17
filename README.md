# Enzyme Sphinx Theme based on the  PyTorch Sphinx Theme

Sphinx theme for [Enzyme Docs](https://enzyme.mit.edu)  based on the [PyTorch Sphinx Theme](https://github.com/pytorch/pytorch_sphinx_theme).

## Local Development

Run python setup:

```
python setup.py install
```

and install the dependencies using `pip install -r docs/requirements.txt`

In the root directory install the `package.json`:

```
# node version 8.4.0
yarn install

```

If you have `npm` installed then run:

```
npm install
```

- If you want to see generated documentation for `docs/demo` then create
`.env.json` file and make it empty json file. Means `.env.json file` will
contain

```
{}
```

Run grunt to build the html site and enable live reloading of the demo app at `localhost:1919`:

```
grunt
```

- If you want to specify the project folder then you need to specify it into `.env.json`
file:

```
{
    "DOCS_DIR": "docs/",
}
```

Run grunt to build the html site for docs:

```
grunt --project=docs
```

The resulting site is a demo.

## Testing your changes and submitting a PR

When you are ready to submit a PR with your changes you can first test that your changes have been applied correctly against either the Enzyme Docs:

1. Run the `grunt build` task on your branch and commit the build to Github.
2. In your local docs, remove any existing `enzyme_sphinx_theme` packages in the `src` folder (there should be a `pip-delete-this-directory.txt` file there)
3. In `requirements.txt` replace the existing git link with a link pointing to your commit or branch, e.g. `-e git+git://github.com/{ your repo }/enzyme_sphinx_theme.git@{ your commit hash }#egg=enzyme_sphinx_theme`
4. Install the requirements `pip install -r requirements.txt`
5. Remove the current build. In the docs this is `make clean`.
6. Build the static site. In the docs this is `make html`.
7. Open the site and look around. In the docs open `docs/build/html/index.html`.

If your changes have been applied successfully, remove the build commit from your branch and submit your PR.

## Publishing the theme

Before the new changes are visible in the theme the maintainer will need to run the build process:

```
grunt build
```

Once that is successful commit the change to Github.
