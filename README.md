# Crossbar echo boilerplate

Run a crossbar router with an echo server for testing your clients.

## Usage

### Requirements
Requires Python 3.6, due to my blatant use of unnecessary features like f-strings and async/await(3.5)

### Preparation
Prepare the environment. Preferably use virtualenv to ensure isolation from other versions of the libraries.

`pip install -r requirements.txt`

### Running

To run the router and the echo server:

`crossbar start`
`python echo.py`

To run the test client, even though it's here just as an example:
`python client.py`

