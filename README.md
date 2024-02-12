# Gym Employee Management API Documentation
This documentation provides details about the Gym Employee Management API endpoints, including their usage and examples.


## Basic Url

 https://gym-employee-management.onrender.com

## Authentication
### Login

    Method: POST
    Endpoint: /login

    Description: Authenticates a user and generates an access token.

Request Body:

```json
{
    "username": "test1",
    "password": "123@123"
}

```

E.g :
```json
POST https://gym-employee-management.onrender.com/login
Content-Type: application/json
{"username":"test1","password":"123@123"}
 
```
    Response: Returns a token if authentication is successful.

## Logout

    Method: POST

    Endpoint: /logout

    Description: Logs out the user by invalidating the access token.

    Request Headers: Authorization: Token <token>

E.g:

```json

POST https://gym-employee-management.onrender.com/logout
Content-Type: application/json
Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345 
```

    Response: Indicates a successful logout.

## Signup

    Method: POST

    Endpoint: /signup

    Description: Registers a new user.

Request Body:

```json
{
    "username": "test1",
    "password": "123@123",
    "email": "test1@gmail.com"
}

```

E.g:

```json
POST https://gym-employee-management.onrender.com/signup
Content-Type: application/json
{"username":"test1","password":"123@123","email":"test1@gmail.com"}
```

    Response: Returns user details if registration is successful.

# Employee Management

## List Employees

    Method: GET

    Endpoint: /api/employees/

    Description: Retrieves a list of all employees.

    Request Headers:

        Authorization: Token <token>

    Response: Returns a list of employee objects.

E.g:

````json
 GET https://gym-employee-management.onrender.com/api/employees/
 Content-Type: application/json
 Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345
````

## Create Employee

    Method: POST
    Endpoint: /api/employees/create/

    Description: Creates a new employee record.

    Request Body:
```json
{
    "name": "jacksonWarrior",
    "position": "Sde",
    "department": "Testing"
}

```

    Request Headers:
    Authorization: Token <token>

    Response: Returns the created employee object.

E.g:

```json
POST https://gym-employee-management.onrender.com/api/employees/create/
Content-Type: application/json
Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345

{"name":"jacksonWarrior","position":"SDET","department":"TESTING"}
 
```

## Delete Employee
    Method: DELETE

    Endpoint: /api/employees/<employee_id>/delete/

    Description: Deletes an employee record.

    Request Headers:
        Authorization: Token <token>

    Response: Indicates a successful deletion.

E.g:

```json
 DELETE  https://gym-employee-management.onrender.com/api/employees/2/delete/
 Content-Type: application/json
 Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345
{}
```

## Update Employee

    Method: PUT

    Endpoint: /api/employees/<employee_id>/update/

    Description: Updates an existing employee's information.

    Request Body:

```json
{
    "name": "Gabriel Jonas"
}
````
    Request Headers:

    Authorization: Token <token>

    Response: Returns the updated employee object.

E.g:

```json
 PUT https://gym-employee-management.onrender.com/api/employees/1/update/
 Content-Type: application/json
 Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345
{"name":"Gabriel Jonas"}
```

## Retrieve Employee by Id

    Method: GET

    Endpoint: /api/employees/<employee_id>/

    Description: Retrieves details of a specific employee.

    Request Headers:
        Authorization: Token <token>

    Response: Returns the employee object with the specified ID.

E.g:

```json
 GET  https://gym-employee-management.onrender.com/api/employees/2/
 Content-Type: application/json
 Authorization: Token f68f1adbf7e45678ed134f153dd09306c6d12345


{}
```

## Note
Replace <token> with the actual user token obtained during authentication.

Replace <employee_id> with the ID of the employee for the respective endpoints
