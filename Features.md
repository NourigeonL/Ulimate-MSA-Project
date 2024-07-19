# Ideas of features to implement

- [ ] User account creation
- [ ] Login/logout
- [ ] chatbot using LLM
- [ ] Personnal blog
  - [ ] Create a new post
  - [ ] Update post
  - [ ] Comment

# List of microservices

## User Service
### Responsibilities
- User authentication, profile management, and user data.
### Components
- User API: REST endpoints for user registration, login, profile updates.
- Authentication: Handles user login using OAuth, JWT.
- User Repository: Interface for database interactions.
- Event Publisher: Publishes events like UserRegistered, UserLoggedIn.
### Events
- UserRegistered
- UserLoggedIn
- UserActivityUpdated
## Post Service
### Responsibilities
- Handling the creation, retrieval, and management of posts.
### Components
- Post API: REST endpoints for creating, reading, updating, and deleting posts.
- Post Repository: Interface for database interactions.
- Event Publisher: Publishes events such as PostCreated and PostUpdated.
### Events
- PostCreated
- PostUpdated
- PostDeleted

## Comment Service
### Responsibilities
- Managing comments on posts.
### Components
- Comment API: REST endpoints for creating, reading, updating, and deleting comments.
- Comment Repository: Interface for database interactions.
- Event Publisher: Publishes events such as CommentCreated, CommentUpdated.
### Events
- CommentCreated
- CommentUpdated
- CommentDeleted

## Vote Service
### Responsibilities
- Managing upvotes and downvotes on posts and comments.
### Components
- Vote API: REST endpoints for submitting votes.
- Vote Repository: Interface for database interactions.
- Event Publisher: Publishes events like VoteSubmitted.
### Events
- VoteSubmitted
- VoteUpdated

## Feed Service
### Responsibilities
- Aggregating posts and comments to generate user feeds.
### Components
- Feed API: REST endpoints for retrieving user feeds.
- Feed Generator: Logic for generating personalized feeds.
- Event Listener: Listens to events like PostCreated, CommentCreated.
- Event Publisher: Publishes events like FeedUpdated.
### Events
- FeedUpdated

## Notification Service
### Responsibilities
- Sending notifications to users for various events (new comments, upvotes, etc.).
### Components
- Notification API: REST endpoints for managing notification settings.
- Notification Generator: Logic for generating notifications.
- Notification Delivery: Sends notifications via email, SMS, in-app.
- Event Listener: Listens to events like PostCreated, CommentCreated, VoteSubmitted.
- Event Publisher: Publishes events like NotificationSent.
### Events
- NotificationSent

## Media Service
### Responsibilities
- Handling media uploads and storage (images, videos).
### Components
- Media API: REST endpoints for uploading and retrieving media.
- Media Processor: Logic for processing media (thumbnails, compression).
- Media Storage: Interface for interacting with object storage.
- Event Listener: Listens to events like PostCreated.
- - Event Publisher: Publishes events like MediaProcessed.
### Events

##  Gateway Service
### Responsibilities
- API Gateway to route requests to appropriate services.
### Components
- API Gateway: Handles routing, load balancing, and rate limiting.
- Authentication: Manages API authentication.
- Monitoring: Logs requests and responses for monitoring and debugging.
### Events