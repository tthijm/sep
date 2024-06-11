# Report for Assignment 1

## Project chosen

Name: <TODO>

URL: <TODO>

Number of lines of code and the tool used to count it: <TODO>

Programming language: <TODO>

## Coverage measurement

### Existing tool
The coverage tool [coverage.py](https://coverage.readthedocs.io/en/7.5.3/) was used for this project. 
After installing the dependencies and executing `coverage run -m pytest` we get the following output:
```
======================================================================== test session starts ========================================================================
platform darwin -- Python 3.12.3, pytest-8.2.2, pluggy-1.5.0
rootdir: /Users/username/sep
configfile: pyproject.toml
plugins: cov-5.0.0, asyncio-0.23.7, mock-3.14.0
asyncio: mode=Mode.STRICT
collected 169 items

tests/test_annotated_annotation.py .                                                                                                                                        [  0%]
tests/test_app_commands_autocomplete.py .......                                                                                                                             [  4%]
tests/test_app_commands_description.py ............                                                                                                                         [ 11%]
tests/test_app_commands_group.py ..................                                                                                                                         [ 22%]
tests/test_app_commands_invoke.py ................                                                                                                                          [ 31%]
tests/test_colour.py ......................                                                                                                                                 [ 44%]
tests/test_ext_commands_cog.py ...........                                                                                                                                  [ 51%]
tests/test_ext_commands_description.py .....                                                                                                                                [ 54%]
tests/test_ext_tasks.py ..........                                                                                                                                          [ 60%]
tests/test_files.py ................                                                                                                                                        [ 69%]
tests/test_utils.py ...................................................                                                                                                     [100%]

========================================================================= warnings summary =========================================================================
discord/player.py:29
  /Users/username/sep/discord/player.py:29: DeprecationWarning: 'audioop' is deprecated and slated for removal in Python 3.13
    import audioop

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
================================================================== 169 passed, 1 warning in 4.70s ==================================================================

```
Runnig `coverage html` and opening the document in the browser gives the following:
![23724](https://github.com/tthijm/sep/assets/74216566/5991a9ef-81a1-494f-8016-700ee72d375e)

### Your own coverage tool

<The following is supposed to be repeated for each group member>

<Group member name>

<Function 1 name>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the instrumented code to gather coverage measurements>

<Provide a screenshot of the coverage results output by the instrumentation>

<Function 2 name>

<Provide the same kind of information provided for Function 1>

## Coverage improvement

### Individual tests

<The following is supposed to be repeated for each group member>

<Group member name>

<Test 1>

<Show a patch (diff) or a link to a commit made in your forked repository that shows the new/enhanced test>

<Provide a screenshot of the old coverage results (the same as you already showed above)>

<Provide a screenshot of the new coverage results>

<State the coverage improvement with a number and elaborate on why the coverage is improved>

<Test 2>

<Provide the same kind of information provided for Test 1>

### Overall

<Provide a screenshot of the old coverage results by running an existing tool (the same as you already showed above)>

<Provide a screenshot of the new coverage results by running the existing tool using all test modifications made by the group>

## Statement of individual contributions

<Write what each group member did>
