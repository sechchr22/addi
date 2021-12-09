# LEAD VALIDATOR

This is an API for validating a lead to check if it could become a prospect.

Core Functionality:
  - Getting lead information from national registry and judicial records from national registry
  - if everything is ok, call qualification system to get an score.
  - if score > 60 lead could become a prospect.

## Enviroment

Just a virtual enviroment is needed.

## Installation
Clone the repository
```sh
git clone git@github.com:sechchr22/addi.git
```
Build the environment
```sh
pipenv shell (for example)
```
install requirements
```sh
pip install -r requirements.txt
```
or
```sh
pip install -r requirements-dev.txt
```
if you are going to use developing functionalities

## RUN
being in main folder

Run the app
```sh
python -m infrastructure.delivery.strategy.strategy
```
Run the tests
```sh
python -m pytest -s tests/bussines_logic_tests.py
```

## USE
To use it. Is just and /evaluation/ endpoint with this payload(example) on it

```sh
{
    "nin": 12345,
    "birthdate": "22/05/1994",
    "first_name": "sergio",
    "last_name": "rueda",
}
```

curl example (if running on localhost port 8080)
```sh
curl -v -X POST "http://0.0.0.0:8080/evaluation" -H "Content-Type: application/json" -d '{"nin":12345, "birthdate": "22/05/1994", "first_name": "sergio", "last_name": "rueda"'
```

You will recieve a response with the lead nin, the evaluation and the score
```sh
{"validation":{"lead_nin":12345,"evaluation":"lead"}}
```


## FILE STRUCTURE

### Folder: bussines

#### subfolder: usecases
| File | Description |
| ------ | ------ |
| national_archives_use_case.py | use case for national archives service |
| national_registry_use_case.py | use case for national registry service |
| qualification_use_case.py | use case for qualification service |

### Folder: infrastructure

#### subfolder: delivery
##### subfolder: api
| File | Description |
| ------ | ------ |
| __init__.py | App initialization |
##### subfolder: handler
| File | Description |
| ------ | ------ |
| error_handler.py | to handle app errors |
| validation_handler.py | to handle lead validation |
###### subfloder: utils
| File | Description |
| ------ | ------ |
| utils.py | evaluation handler utilities|
##### subfolder: strategy
| File | Description |
| ------ | ------ |
| strategy.py | App starting strategy |


#### subfolder: middleware
| File | Description |
| ------ | ------ |
| here would be a middleware in order to use dependencies inyection |

### subfolder: services
| File | Description |
| ------ | ------ |
| mock_response.py | to mock services responses |
| national_archives.py | request to national archives service |
| national_registry.py | request to national registry service |
| qualification_system.py | request to qualification service |

### Folder: tests
| File | Description |
| ------ | ------ |
| bussines_logic_tests.py | testing bussines logic |
| conftest.py | common config for testing |


### TODO:
- Dependency inyection.
- Start() to lunch app.
- CLI.
- Exception handling: improve.
- Improve: Repeated code.
- Improve: ReadME
- More on clean architecture.

# Development
Sergio Andrés Rueda Castro
Backend engineer

##### Contact me:
https://www.linkedin.com/in/sergio-rueda-backend-dev/


License
----
**Free Software, Hell Yeah!**
