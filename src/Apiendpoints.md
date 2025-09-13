## Api Endpoints to try.

*Below every route need authorization header*
*Authorization=Bearer access_token*

<br />
**-- Admin fetching all users**
<br />

GET /u/users/
<br />

sample response
```bash
{
  "message": "Users founded.",
  "data": [
    {
      "id": 5,
      "password": "*******************************",
      "last_login": null,
      "is_superuser": false,
      "email": "Adarsh@gmail.com",
      "full_name": "Adarsh",
      "date_joined": "2025-09-13",
      "role": "User",
      "is_active": true,
      "is_staff": false,
      "groups": [],
      "user_permissions": []
    }
  ]
}
```

------------------------------

<br />
**-- Admin soft delete a user**
<br />

PUT /u/users/{userid}/soft-delete/
<br />

sample response
```bash
{
  "message": "Soft deleted a user with id: {userid}."
}
```

------------------------------

<br />
**-- Admin Create task**
<br />

POST tasks/create/
<br />

sample data
```bash
{
  "title":"adarsh new task",
  "description":"must be completed till 5 pm",
  "assigned_to":5
}
```
sample response
```bash
{
  "message": "Task created.",
  "data": {
    "id": 12,
    "title": "adarsh new task",
    "description": "must be completed till 5 pm",
    "status": "todo",
    "created_at": "2025-09-13T14:13:04.136262Z",
    "updated_at": "2025-09-13T14:13:04.136300Z",
    "assigned_to": 5
  }
}
```

------------------------------

<br />
**-- Admin fetches tasks**
<br />

GET tasks/all/
<br />

sample response
```bash
{
  "message": "Fetched all tasks.",
  "data": [
    {
      "id": 12,
      "title": "adarsh new task",
      "description": "must be completed till 5 pm",
      "status": "todo",
      "created_at": "2025-09-13T14:13:04.136262Z",
      "updated_at": "2025-09-13T14:13:04.136300Z",
      "assigned_to": 5
    }
  ]
}
```

------------------

<br />
**-- Admin Delete tasks**
<br />

DELETE tasks/id/delete/
<br />

------------------

<br />
**-- Admin can update anything in tasks**
<br />

PUT tasks/id/update/
<br />

sample data
```bash
{
  "title":"new title added"
}
```

------------------

<br />
**-- Role user can fetch tasks assigned to them if is_active=true only**
<br />

GET tasks/
<br />

------------------

<br />
**-- Role user can fetch task detail assigned to him if is_active=true only**
<br />

GET tasks/
<br />

------------------

<br />
**-- Role user can fetch task detail assigned to him if is_active=true only**
<br />

PUT tasks/{task_id}/status/     ----->     like this /tasks/11/status/
<br />


------------------

<br />
**-- Admin fetching all the commments relted to a task**
<br />

GET /tasks/{put the task id here}/comments/all/     ----->     like this /tasks/10/comments/all/
<br />

sample response 

``` bash
{
  "message": "Comments on tasks with taskid:10.",
  "data": [
    {
      "id": 7,
      "text": "Raj Another comments wooh 🎉",
      "created_at": "2025-09-13T05:47:30.472430Z",
      "task": 10,
      "author": 6
    }
  ]
}
```

------------------

<br />
**-- Role user can fetch comments of a task assigned to him if is_active=true only**
<br />

GET tasks/{task_id}/comments/     ----->     like this /tasks/10/comments/
<br />


------------------

<br />
**-- Role user can add comment to a task assigned to him if is_active=true only**
<br />

POST tasks/{task_id}/comments/add/     ----->     like this /tasks/10/comments/add/
<br />

sample data
```bash
{
  "text":"Raj Another comments wooh 🎉"
}
```
