# `pyCoreWLAN`

Provides Python stubs for the Apple [CoreWLAN](https://developer.apple.com/documentation/corewlan) framework and should be used alongside the CoreWLAN wrappers provided by [PyObjC](https://github.com/ronaldoussoren/pyobjc).
Provides code completion and docstring hints equivalent to the CoreWLAN
documentation. Intended to work with VS Code Intellisense with Pylance installed.

## Installation & Usage

Install `pyCoreWLAN` as follows:

```
pip install pyCoreWLAN
```

For use with VSCode, update the settings to include the path to the package if using a virtual environment.

```json
{
  "python.analysis.stubPath": "./.venv/lib/python3.10/site-packages/pyCoreWLAN"
}
```
