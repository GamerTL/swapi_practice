# swapi_practice

## Init Docker by Dockerfile and run it
Build Docker image by Dockerfile:
```bash
/swapi_practice>$ docker build -t gtl_swapi_practice .
```
Run the image by tty mode:
```bash
$ docker run -it --name gtl_swapi_practice gtl_swapi_practice /bin/sh
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
