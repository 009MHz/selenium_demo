# Project Documentation

# Table of Contents
1. [Folder Descriptions](#folder-descriptions)
2. [File Summaries](#file-summaries)
   - [`browser_config.py`](#browser_configpy)
   - [`conftest.py`](#conftestpy)
   - [`dockerfile`](#dockerfile)
   - [`pytest.ini`](#pytestini)
   - [`requirements.txt`](#requirementstxt)
   - [`ci.yml`](#ciyml)
3. [Running Tests](#running-tests)
   - [1. Running a Single Test](#1-running-a-single-test)
   - [2. Running Multiple Test Files](#2-running-multiple-test-files)
   - [3. Running Tests from Multiple Folders](#3-running-tests-from-multiple-folders)
   - [4. Running Tests with Reports](#4-running-tests-with-reports)
      - [Including Test Report](#including-test-report)
      - [Generating the Report](#generating-the-report)
   - [5. Running Tests on Multiple Browsers](#5-running-tests-on-multiple-browsers)

## Folder Descriptions

- **pages**: Directory for storing E2E page object files used for testing.
- **reports**: Contains test report resource files generated during test execution.
- **source**: Contains API patterns and custom functions/methods used for testing.
- **tests**: Contains automated test files.

## File Summaries

### `browser_config.py`
This file contains the `BrowserManager` class, which is responsible for configuring Selenium WebDriver options and creating WebDriver instances for different browsers.

#### Key Class and Methods
- **`BrowserManager` Class**: Handles browser configuration and WebDriver creation.
  - **Initialization (`__init__`)**: Takes the browser name and headless mode as parameters.
  - **`get_browser_options()`**: Configures and returns WebDriver options based on the browser name and mode.
  - **`create_webdriver()`**: Initializes and returns a WebDriver instance based on the specified browser.

### `conftest.py`
This file sets up the configuration for pytest, allowing customization of test runs via command-line options. It uses the `BrowserManager` class from `browser_config.py` to configure and initialize WebDriver instances.

#### Key Functions and Fixtures
1. **`pytest_addoption(parser)`**: Adds command-line options for specifying the browser and headless mode.
2. **`driver` Fixture**: Initializes the WebDriver using `BrowserManager` and yields it for use in tests.
3. **`pytest_generate_tests(metafunc)`**: Dynamically generates tests for each specified browser.
4. **`_browser_per_test` Fixture**: Automatically assigns the WebDriver to test classes.

#### Example Usage
```bash
pytest --browsers=chrome --headless
```

### `dockerfile`
Sets up an environment for running automated tests with Selenium and pytest in a container.

#### Key Steps
1. **Base Image**: `python:3.9-slim`. *(most stable and supported version)*
2. **Working Directory**: `/app`.
3. **Copy Project Files**: Copies contents to `/app`.
4. **Install System Packages**: Installs essential utilities.
5. **Install Google Chrome**: Adds Google Chrome repository and installs Chrome.
6. **Install Python Dependencies**: Installs required Python packages.
7. **Install `chromedriver_autoinstaller`**: Handles ChromeDriver installation.
8. **Run Tests**: Executes pytest on E2E test scripts with options to rerun failed tests.

```dockerfile
CMD ["pytest", "./tests/", "--reruns", "2", "--reruns-delay", "3"]
```
- **`pytest`**: Required commands to run the test
- **`./tests/E2E`**: Specifies the target directory to run the test file
- **`--reruns`**: Specifies the number of times to rerun failed tests (2 in this case).
- **`--reruns-delay`**: Specifies the delay in seconds between reruns (5 seconds in this case).

### `pytest.ini`
Configures pytest settings for the test automation framework.

#### Key Sections
- **Markers**: Defines custom markers for test categorization.
- **Warning Filters**: Specifies warnings to ignore.
- **Logging Configuration**: Sets log level and enables CLI logging.
- **Additional Pytest Options**: Includes options like `-p no:warnings`, `-v`, and `--clean-alluredir`.

### `requirements.txt`
Lists Python dependencies needed for the project, including libraries for pytest, Selenium, and other utilities required for test execution and reporting.

#### Dependencies and Their Usage
1. **`allure-pytest`**: Integrates Allure reporting with pytest.
2. **`allure-python-commons`**: Core Allure integration.
3. **`pytest`**: Core framework for writing and running tests.
4. **`pytest-rerunfailures`**: Allows tests to be rerun automatically if they fail.
5. **`pytest-xdist`**: Enables parallel test execution.
6. **`python-dotenv`**: Loads environment variables from a `.env` file.
7. **`requests`**: Simplifies making HTTP requests for API testing.
8. **`selenium`**: Provides tools for web browser automation.
9. **`webdriver-manager`**: Automatically manages WebDriver binaries.

### `ci.yml`
This config is used for running Selenium E2E tests in a CI/CD pipeline.

#### Triggers
The workflow is triggered on push and pull request events targeting the `py_base` branch.

```yaml
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]
```

#### Job Configuration
Defines a job named `test` that runs on the latest Ubuntu environment.

##### Services
Sets up a Docker container running Selenium Standalone Chrome, exposing port `4444`.

```yaml
services:
  selenium:
    image: selenium/standalone-chrome:latest
    ports:
      - 4444:4444
```

#### Steps

##### Checkout Repository
```yaml
- name: Checkout repository
  uses: actions/checkout@v2
```

##### Set Up Python
```yaml
- name: Set up Python
  uses: actions/setup-python@v2
  with:
    python-version: 3.9
```

##### Cache pip
```yaml
- name: Cache pip
  uses: actions/cache@v2
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('**/requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

##### Install Dependencies
```yaml
- name: Install dependencies
  run: pip install -r requirements.txt
```

##### Build Docker Image
```yaml
- name: Build Docker image
  run: docker build . -t my-app
```

##### Run Tests
```yaml
- name: Run tests
  run: |
    docker run \
      -e execution_type=pipeline \
      -e browser=chrome-headless \
      my-app
```

## Running Tests

### 1. Running a Single Test
To run a single test using pytest:
```sh
pytest path/to/test_file.py::test_name
```
***Example Usage***
```shell
pytest .\tests\scripts\disappearing\test_dissapearing_element.py 
```

### 2. Running Multiple Test Files
Run multiple specific tests by providing multiple paths:
```sh
pytest path/to/test_file1.py::test_name1 path/to/test_file2.py::test_name2
```
***Example Usage***
```shell
pytest .\tests\scripts\disappearing\test_dissapearing_element.py  .\tests\scripts\login\test_valid_login.py   
```

### 3. Running Tests from Multiple Folders
To run tests from multiple folders, specify each folder path:
```sh
pytest path/to/folder1 path/to/folder2
```
This command executes all tests found within `folder1` and `folder2`. Adjust paths based on your project structure.

***Example Usage***
```shell
pytest .\tests\scripts\disappearing\ .\tests\scripts\login\ 
```
To simplify, use:
```sh
pytest .\tests\ 
```

### 4. Running Tests with Reports

#### Including Test Report
Generate Allure reports while running tests:
```sh
pytest path/to/tests --alluredir=<allure-results-directory>
```
Replace `<allure-results-directory>` with the directory path where Allure results should be stored.

***Example Usage***
```sh
pytest .\tests\ --alluredir=reports/
```

#### Generating the Report
To view the generated Allure report:
```sh
allure serve <allure-results-directory>
```
Starts a local web server to display the Allure report in your default browser.

***Example Usage***
```sh
allure serve reports/
```

### 5. Running Tests on Multiple Browsers

The test suite supports running tests on multiple browsers by specifying the `--browsers` command-line option. This allows you to test cross-browser compatibility by running your tests sequentially on each specified browser.

#### Supported Browsers
The following browsers are supported:
- **Chrome**
- **Firefox**
- **Edge**

#### Example Commands

- **Single Browser**: Run tests on Chrome:
  ```sh
  pytest --browsers=firefox
  ```

- **Multiple Browsers**: Run tests on Chrome, Firefox, and Edge sequentially:
  ```sh
  pytest --browsers=chrome,firefox,edge
  ```

- **Headless Mode**: Run tests on Chrome and Firefox in headless mode:
  ```sh
  pytest --browsers=chrome,firefox --headless
  ```

- **All Browsers**: Run tests across all supported browsers:
  ```sh
  pytest --browsers=chrome,firefox,edge
  ```

#### Parallel Execution with Multiple Browsers

For faster test execution, you can run tests in parallel across multiple browsers using `pytest-xdist`. Specify the number of parallel workers with `-n`:

```sh
pytest --browsers=chrome,firefox --headless -n 2
```

This command runs the tests on Chrome and Firefox in parallel using two workers.

#### Considerations
- **Cross-Browser Testing**: Running tests on multiple browsers ensures your application behaves consistently across different environments.
- **Performance**: Parallel execution with multiple browsers can reduce overall test time, especially in CI/CD pipelines.

---
