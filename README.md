Alexandria
==========

## 🌿 Repository structure
This repository is organized based upon the following branches:
- 🔘 [`master`](../../tree/master) contains the source code of the Alexandria Project

### 🔽 How to clone specific branches locally
```console
git clone https://github.com/icub-tech-iit/study-alexandria.git
```

## Usage
⚠️ This project is currently under development ⚠️

### Dependencies

- [Python](https://www.python.org/)
- [lxml](https://pypi.org/project/lxml/)

### Installation

If you don't have Python installed yet, follow the instructions based on your OS.

- **Linux**

    Install Python via the system package manager:

    ```console
    sudo apt install python3
    ```

- **Linux/macOS/Windows**

    Alternatively, you can install a `conda` distribution and create a conda environment with Python:

    ```console
    conda create --name myenv python=3.x
    conda activate myenv
    ```

To install Python packages instead, [`pip`](https://pip.pypa.io/en/stable/installation/) is typically used (if you want to avoid conflicts between package versions, please use a virtual environment).

```console
python3 -m venv alexandriaenv
source alexandriaenv/bin/activate
pip install lxml
pip install -e sysmlv2parser
```

### sysmlv2parser

This repository includes a parser for the SysMLv2 language, which is generated using the [ANTLR](https://www.antlr.org/) tool based on the grammar file `SysMLv2.g4`. The parser is located in the `sysmlv2parser` folder. The grammar file `SysMLv2.g4` defines the syntax and structure of the SysMLv2 language. It includes lexer and parser rules to handle various constructs such as parts, attributes, packages, and arrays. These parser files are generated with the following command:

```console
antlr4 -Dlanguage=Python3 sysmlv2parser/SysMLv2.g4 -visitor
```

The `sysmlv2parser` folder also contains a `CustomVisitor.py`: this file features a custom implementation of the visitor pattern for traversing and processing the parse tree generated, and it contains a custom logic for handling specific nodes in the parse tree.

### How it works

To generate the XML files for one or more specific robots, please run:

```console
python3 src/main.py --robot <robots-name> --config <absolute-path-to-sysml-directory>
```

where:

- `<robots-name>` is a space-separated list that contains the name of the robots (e.g., `iCubGenova11 iCubErzelli03`).
- `<absolute-path-to-sysml-directory>` is the absolute path to the directory containing the SysML files (e.g., `<path-to-study_alexandria-repository/sysml>`).

This script will create a folder for the specified robot, mirroring the architecture of [`robots-configuration`](https://github.com/robotology/robots-configuration).