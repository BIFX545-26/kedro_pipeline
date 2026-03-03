# GC Content Analysis

[![Powered by Kedro](https://img.shields.io/badge/powered_by-kedro-ffc900?logo=kedro)](https://kedro.org)
[![Powered by GitHub Copilot](https://img.shields.io/badge/powered_by-GitHub_Copilot-ffc900?logo=kedro)](https://github.com/features/copilot)

## Overview

This project demonstrates a core Kedro concept: **separation of concerns**. The Python code that performs analysis never mentions a file path. Data is wired to code through a central configuration file called the Data Catalog. The goal of this exercise is to run the same pipeline on two different datasets by changing a single line of configuration — without touching any Python.

---

## Project structure

### The data: `data/01_raw/`

Two small CSV files are provided, each containing a `sequence_id` column and a `sequence` column with DNA sequences:

- **`sample_alpha.csv`** — sequences representative of a human gene (moderate GC content)
- **`sample_beta.csv`** — sequences from an extremophile organism (high GC content)

Pipeline output is written to `data/07_model_output/results.csv`.

---

### The logic: `src/gc_content_analysis/pipelines/dna_analysis/nodes.py`

Contains a single Python function, `calculate_gc_content`, that accepts a DataFrame of sequences and adds a `gc_content` column with the GC percentage for each sequence. This file has no knowledge of where the data comes from or where results are saved.

---

### The wiring: `src/gc_content_analysis/pipelines/dna_analysis/pipeline.py`

Defines the pipeline by connecting the `calculate_gc_content` function to named datasets (`raw_sequences` → `analyzed_sequences`). These names are placeholders — their actual file paths are defined in the catalog.

---

### The catalog: `conf/base/catalog.yml`

This is the key file for the exercise. It maps the dataset names used in the pipeline to real file paths:

```yaml
raw_sequences:
  type: pandas.CSVDataset
  filepath: data/01_raw/sample_alpha.csv

analyzed_sequences:
  type: pandas.CSVDataset
  filepath: data/07_model_output/results.csv
```

---

## In-class exercise

### Setup

-   You'll need `python` and `kedro` for this exercise - recommended options:
    -   https://shell.cloud.google.com
    -   Use your own, local installation

-   Clone the Kedro pipeline and `cd` into the cloned directory

```bash
# only run this once
git clone https://github.com/BIFX545-26/kedro_pipeline

# run this every time you restart the terminal
cd kedro_pipeline
```

-   Create a virtual python environment

```bash
# only run this once
python -m venv kedro-env

# run one of these every time you restart the terminal
source kedro-env/bin/activate # (linux)
kedro-env/Scripts/activate    # (Windows)
```

### Install dependencies

After activating the virtual environment inside of `kedro_pipeline/` run

```bash
# only do this once
pip install -r requirements.txt
```

### Try it out!

We should be ready to run the pipeline on the provided data with

```bash
kedro run
```

Open `data/07_model_output/results.csv` and note the `gc_content` values for each sequence with

```bash
less data/07_model_output/results.csv # exit `less` with 'q'
```

#### Swap the input data

Open `conf/base/catalog.yml` and change the `raw_sequences` path on line 8

```yaml
  filepath: data/01_raw/sample_beta.csv
```

and run the pipeline again with

```
kedro run
```

Open `results.csv` again. The GC content values should be noticeably higher — you processed an entirely different dataset without modifying a single line of Python code.

### Discussion

- What was the only file you changed between the two runs?
- Why is it useful to separate *what the code does* from *what data it operates on*?
- How would this pattern scale if you had dozens of input files or needed to re-run an analysis on updated data?

### Assignment

Submit the output from `data/07_model_output/results.csv` on Blackboard.

---

## Rules and guidelines

In order to get the best out of the template:

* Don't remove any lines from the `.gitignore` file we provide
* Make sure your results can be reproduced by following a data engineering convention
* Don't commit data to your repository
* Don't commit any credentials or your local configuration to your repository. Keep all your credentials and local configuration in `conf/local/`

## How to install dependencies

Declare any dependencies in `requirements.txt` for `pip` installation.

To install them, run:

```
pip install -r requirements.txt
```

## How to run your Kedro pipeline

You can run your Kedro project with:

```
kedro run
```

## How to test your Kedro project

Have a look at the file `tests/test_run.py` for instructions on how to write your tests. You can run your tests as follows:

```
pytest
```

You can configure the coverage threshold in your project's `pyproject.toml` file under the `[tool.coverage.report]` section.


## Project dependencies

To see and update the dependency requirements for your project use `requirements.txt`. You can install the project requirements with `pip install -r requirements.txt`.

[Further information about project dependencies](https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html#project-specific-dependencies)

## How to work with Kedro and notebooks

> Note: Using `kedro jupyter` or `kedro ipython` to run your notebook provides these variables in scope: `context`, 'session', `catalog`, and `pipelines`.
>
> Jupyter, JupyterLab, and IPython are already included in the project requirements by default, so once you have run `pip install -r requirements.txt` you will not need to take any extra steps before you use them.

### Jupyter
To use Jupyter notebooks in your Kedro project, you need to install Jupyter:

```
pip install jupyter
```

After installing Jupyter, you can start a local notebook server:

```
kedro jupyter notebook
```

### JupyterLab
To use JupyterLab, you need to install it:

```
pip install jupyterlab
```

You can also start JupyterLab:

```
kedro jupyter lab
```

### IPython
And if you want to run an IPython session:

```
kedro ipython
```

### How to ignore notebook output cells in `git`
To automatically strip out all output cell contents before committing to `git`, you can use tools like [`nbstripout`](https://github.com/kynan/nbstripout). For example, you can add a hook in `.git/config` with `nbstripout --install`. This will run `nbstripout` before anything is committed to `git`.

> *Note:* Your output cells will be retained locally.

## Package your Kedro project

[Further information about building project documentation and packaging your project](https://docs.kedro.org/en/stable/deploy/package_a_project/#package-an-entire-kedro-project)
