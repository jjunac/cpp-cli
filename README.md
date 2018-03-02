# C++ CLI

CLI for C++ projects by Jeremy Junac

## Prerequisites

The CLI only needs **Python 2.7**. But if you want to use all the functionalities, you will also need :

* make
* gcc/g++
* gdb
* VSCode

## Installation

```bash
git clone https://github.com/Taken0711/cpp-cli.git
```

If you want to use the CLI from anywhere, you can put a link in your $PATH (assuming that ~/bin is in your $PATH):

```bash
ln -s ./cpp-cli.py ~/bin/cpp-cli
```

## Usage

### Generating a new project with Makefile and VSCode settings files

```bash
cpp-cli new <PROJECT-NAME>
```

This command generates a project containing :

* A basic `main` with a `cout`.
* Its `Makefile`.
* The .json settings files for vscode (`settings.json`, `launch.json`, `c_cpp_properties.json` and `tasks.json`) to build, debug and launch your project, using make, gcc and gdb.

### Generating Class

You can use the `cpp-cli g class` command to generate C++ classes:

```bash
cpp-cli g class <MyClass>
```

Note : the PATH must be your newly created project.

This command creates a basic cpp and a header file. **The CLI will automatically add dependency in the Makefile.**<br/>
You can also create several classes in one command:

```bash
cpp-cli g class MyFirstClass MySecondClass MyThirdClass
```

## VSCode shortcuts

### Building

Default is Ctrl+B.<br/>
Debugging and launching automatically launch the build task.

### Debugging

Default is F5.<br/>
Automatically launches the build task.

### Launching without debug

Default is Ctrl+F5.<br/>
Automatically launches the build task.