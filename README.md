# C++ CLI
#### CLI for C++ project by Jeremy Junac

## Prerequisites
The CLI only need **Python 2.7**. But if you want to use all the functionalities, you will also need :
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

### Generating a new project with Makefile and VSCode settings file
```bash
cpp-cli new PROJECT-NAME
```
This command generate a basic main with and hello world and the setting file for build, debug and launch your project, using make, gcc and gdb.

### Generating Class
You can use the ~~`cpp-cli generate`~~ (or just `cpp-cli g`) command to generate C++ classes:
```bash
#cpp-cli generate class MyClass (not working atm)
cpp-cli g class MyClass         # using the alias
```
This command create a basic cpp and header file. **The CLI will add dependency in the Makefile automatically.**<br/>
You can also create several class with one command:
```bash
#cpp-cli generate class MyFirstClass MySecondClass MyThirdClass (not working atm)
cpp-cli g class MyFirstClass MySecondClass MyThirdClass         # using the alias
```

## VSCode shortcuts

### Building
Default is Ctrl+B.<br/>
Debugging and launching automatically launch the build task.

### Debugging
Default is F5.<br/>
Automatically launch the build task.

### Launching without debug
Default is Ctrl+F5.<br/>
Automatically launch the build task.