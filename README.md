# DDF Load Test

A simple load testing tool taking advantage of locust.io.

![](http://ddf.slackexception.com/weight.png)

## Setup

#### This requires python 3.5+ to run.

1. Ensure python 3.5+ is installed on your system.
2. Install requirements by running `pip install -r requirements.txt`
    1. `pip` may be aliased to `pip3` on macOS


## Running
1. Run `python main.py --host=https://localhost:8993` to start the application
    - `python` may be aliased to `python3` on macOS
    - replace `localhost:8993` with running server address
2. Navigate to [https://localhost:8089](https://localhost:8089) to open the Load Test UI.


