# swapi_practice
This project is use to practice Star Wars API by use Requests and Pytest Library from: https://swapi.co/

## Initialize Docker by Dockerfile and run it
Build Docker image by Dockerfile:
```bash
/swapi_practice>$ docker build -t gtl_swapi_practice .
```
Run the image by tty mode:
```bash
$ docker run -it --name swapi_test gtl_swapi_practice /bin/sh
```
## Run by PyTest
In Docker container, use the command below to run test script by PyTest
```bash
/swapi_practice>$ pytest -v
```
## Run the run_action.py to see the data and status
In Docker container, use the command below to run action by python3
```bash
/swapi_practice>$ python -m action.run_action
```
