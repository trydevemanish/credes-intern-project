# Task Management Api
A small **role-based access control (RBAC)** task management api with **custom permission**, **JWT authentication**, and **soft delete** functionality.

## Features
- **Custom User Model** with email login (Admin/User roles).  
- **JWT Authentication** (`djangorestframework-simplejwt`).  
- **RBAC**:
  - Admin → Create, update, delete, view all tasks & comments.  
  - User → View assigned tasks, update status, comment on tasks.  
- **Soft Delete Users** → inactive users can’t log in, but their data is preserved.  
- **Tasks & Comments** with visibility rules.  
- **Filtering** by task status & task assigned to users.
  
<br/>

## Project Setup
1. First, clone the repo:

```bash

git clone https://github.com/trydevemanish/credes-intern-project.git

```

2. Create a virtual environment in the root dir & start the virtual environment .<br />
Depending on your machine.

3. Install all the neccessary dependency through requirements.txt

```bash

pip install -r requirements.txt

```

4. Move to the working dir

```bash

cd src

```

5. Run migrations

```bash

python manage.py makemigrations

```

6. migrate 

```bash

python manage.py migrate

```

7. Create super user aka(Admin)

```bash

python manage.py createsuperuser

```


8. Start the server by this command

```bash

python manage.py runserver

```

#### You are good to go.
 <br />

## Authentication flow.
**-- For Register user with role user** <br/>

POST u/auth/register/ <br />

sample data
```bash
{
  "email":"Raj@gmail.com",
  "full_name":"Raj",
  "password":"newpassword"
}
```
sample reponse
```bash
{
  "message": "User registerd"
}
```
<br />

**-- For Login user** 
<br/>
*when users is_active=false then user can not login*
<br />

POST u/auth/token/ <br />

sample data
```bash
{
  "email":"Raj@gmail.com",
  "password":"newpassword"
}
```
sample reponse
```bash
{
  "refresh": "generated refresh token...........",
  "access": "generated access token ............",
  "email": "Raj@gmail.com",
  "role": "newpassword"
}
```

**-- For Generating Access tokens** <br/>

POST u/auth/token/refresh/ <br />

sample data
```bash
{
  "refresh" : "put your refresh token here..........."
}
```
sample reponse
```bash
{
  "access": "newly generated access token............",
}
```
