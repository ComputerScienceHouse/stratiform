# Stratiform

An extensible end-user computing resource provisioner and management console built for Computer Science House.

## Development

Ensure you have NodeJS and Python 3 installed. Creating a Python virtualenv is optional, but recommended.

Install the dependencies:

```
pip install -r requirements.txt
cd frontend && npm install
```

If changes to the default configuration are required, you may set the environment variables noted in `config.env.py` or copy `config.env.py` to `config.py` and edit the file manually.

You can start the development servers by running: `honcho start`

Stratiform uses the Create React App build framework for the frontend. More information can be found [here](https://github.com/facebookincubator/create-react-app/blob/master/packages/react-scripts/template/README.md).

### Testing

Stratiform has unit test suites available to validate the functionality of the application.

###### Frontend

Run the tests with: `cd frontend && npm test`

###### Backend

Run the tests with: `python manage.py test`