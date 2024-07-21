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
- [ ] Create API Gateway boilerplate
  - Using [express gateway](https://www.express-gateway.io/)
  ```shell
  npm install -g express-gateway
  ``` 
  ```
  eg gateway create
  ```
  ```
  ➜ eg gateway create
  ? What is the name of your Express Gateway? api-gateway
  ? Where would you like to install your Express Gateway? api-gateway
  ? What type of Express Gateway do you want to create? (Use arrow keys)
  ❯ Getting Started with Express Gateway
    Basic (default pipeline with proxy)
  ```