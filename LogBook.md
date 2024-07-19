# Log book

## 2024/07/18 (4am)
I think I will probably start by developing a common application often used as an example for microservices, like a blog or an e-commerce application (but probably more like a personal blog with funky features, haha). I will start by making a small monolith and deploy it on AWS, so I can have a running application. Then I will gradually split it into microservices by introducing a message broker, multiple databases, and all the challenging aspects related to microservices.

## 2024/07/18 (1pm)
- I created a boilerplate for the frontend using ReactJS in TypeScript. Even though the frontend is not my priority, it's better to have a cool website that interacts with the API rather than just using Postman. It will also allow me to learn about the connection between the frontend and the backend, and all the issues I might encounter when deploying in the cloud.
- I still don't know yet what kind of features I want to implement, but for sure there will be user registration and login/logout, so I will start with that.
- ~~ While writing this, I realized that I could definitely make a blog instead of just a logbook like this, where I can post my various research, advancements, and thoughts. ~~
- I should develop this feature quite fast, so I will use Django Rest Framework for the backend since I already have some experience with it. I plan to do something like this first:
  - Use the admin interface created byt Django to manage my posts
  - Create a web page that only shows the posts for now. So I don't need to manage user authentication for now
- For this I am following [this tutorial](https://www.youtube.com/watch?v=c-QsfbznSXI)

## 2024/07/19
I think I'm gonna build like a forum similar to Reddit, where people can created topics, create posts in it an interact with comments, like, reports, etc.
