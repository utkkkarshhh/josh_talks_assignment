
#  Josh Talks Assignment

### Assumptions:
- A task is **not assigned** to any user upon creation. It remains unassigned until explicitly assigned via the `api/v1/task/assign/<user_id>` API, similar to JIRA.
- Bulk assignment of tasks to a user is supported.
- New assignments **does not overrides existing assignments** .

---

### Setup

#### Clone the Repository:
```
git clone https://github.com/utkkkarshhh/josh_talks_assignment
```

#### Create a Virtual Environment:
```
python -m venv env
source env/bin/activate
```

#### Install Dependencies:
```
pip install -r requirements.txt
```

#### Set Environment Variables:
Create a `.env` file in the project using `.env.example` as a reference:

---

### DB Setup

#### Using SQLite
Tthe app uses **SQLite** if the `USE_SQLITE=True` environment variable is set. 

#### Using PostgreSQL
If you want to use **PG SQL**:
1. Set `USE_SQLITE=False` in `.env`.
2. Add PG SQL database details in `.env`.

---

### Run Migrations
```
python manage.py makemigrations
python manage.py migrate
```

---

### Start the Server
```
python manage.py runserver
```


---

### Running Test Cases

To run the test cases:
```
python manage.py test
```

---

### API Documentation
Postman collection/contract is available on the root of the project. `./postman_contract/Josh Talks Assignment.postman_collection.json`

---


### Sample API Requests and Responses

#### 1. Create Task
- **URL:** `api/v1/task/create/<user_id>`
- **Method:** `POST`
- **Payload:**
```json
{
    "name": "Test Task",
    "description": "Sample description",
    "task_type": "development"
}
```
- **Response:**
```json
{
    "success": true,
    "message": "Task created successfully with ID 1"
}
```

---

#### 2. Assign Task
- **URL:** `api/v1/task/assign/<user_id>`
- **Method:** `PATCH`
- **Payload:**
```json
{
    "task_ids": [1, 2, 3]
}
```
- **Response:**
```json
{
    "success": true,
    "message": "Tasks successfully assigned"
}
```

---

#### 3. Fetch Task Details
- **URL:** `api/v1/task/details/<user_id>`
- **Method:** `GET`
- **Response:**
```json
{
    "success": true,
    "message": "Tasks fetched successfully",
    "data": [
        {
            "id": 1,
            "name": "Test Task",
            "description": "Sample description",
            "task_type": "development",
            "status": "pending"
        }
    ]
}
```