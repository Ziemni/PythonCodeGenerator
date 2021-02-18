# PythonCodeGenerator

## Description
Python script that generates Python code based on templates. I use it in my research related to Neural Network. It's not perfect but gets the job done.

## Usage
`python pythonGenerator.py <lines> <in_file> <out_file>`
- `line` - Number of lines to generate per template.
- `in_file` - File that contains templates.

Templates in `in_file` must contain variables in the following format:
 - `$v[number]` - Variable will be inserted here. Etc: `$v1`, `$v2`, `$v3` ...
 - `$n[number]` - Number will be inserted here. Etc: `$n1`, `$n2`, `$n3` ...
 - `$s[number]` - String will be inserted here. Etc: `$s1`, `$s2`, `$s3` ...
Names must contain numbers in order starting with 1.

> idk what im doing with my life glhf