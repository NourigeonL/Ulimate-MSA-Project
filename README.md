# Ulimate-MSA-Project
Project used to practice MSA with many differentes languages/framework/technologies

## Working environment
- OS : Windows 11
- IDE : VS Code


## Languages/framework/technologies I plan to use
- Languages
    - [ ] Python
    - [ ] Typescipt
    - [ ] Java
    - [ ] Go
    - [ ] C#
- Frameworks
  - [ ] FastAPI
  - [ ] Django
  - [ ] Spring Boot
  - [ ] .NET
  - [ ] Nextjs
  - [ ] Reactjs
- Technologies
  - Databases
    - [ ] EventStoreDB
    - [ ] Redis
    - [ ] PostgreSQL
    - [ ] MongoDB
    - [ ] Neo4j
  - Containerization
    - [ ] Docker
    - [ ] Kubernetes
  - Cloud
    - [ ] AWS
  - DevOps
    - [ ] Github Action

## Steps
- [x] Create frontend boilerplate
  - Using Reactjs Typescript
    ```shell
    npm install @types/react @types/react-dom
    npx create-react-app frontend --template typescript
    ```
- [ ] Create personal blog to use as a logbook
  - [ ] Implement the backend
    - [ ] Create backend boilerplat 
      - Using Django Rest Framework
      ```shell
      python -m venv venv
      .\venv\Scripts\activate
      pip install -r requirements.txt
      django-admin startproject backend
      cd .\backend\
      python .\manage.py startapp blog
      ```