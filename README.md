# py-diff

py-diff is a Python package which compares two files line by line and outputs the difference between the files. No output shall be produced if the files are identical.
It works together with [py-patch](https://pip.pypa.io/en/stable/)

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install py-diff.

```bash
pip install ./dist/py_diff-0.1.0-py3-none-any.whl
```

## Usage

```bash
py-diff file1 file2
```
To generete output , redirect the output to a patch file as below:

```bash
py-diff file1 file2 > out.patch
```

Sample Output is as below:

```bash
Diff: Use ternary operator '>' to generate patch file
----------- file1.txt
+++++++++++ file2.txt
Difference in total lines: 0
Line: 1
 - new
 + newaaa
Line: 2
 - chetto
 + my dog ate
```


## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)