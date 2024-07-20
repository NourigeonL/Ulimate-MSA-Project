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
- Handles user data, registration, and profile management.
### Components
- User API: REST endpoints for user registration, login, profile updates.
- Authentication: Handles user login using OAuth, JWT.
- User Repository: Interface for database interactions.
- Event Publisher: Publishes events like UserRegistered, UserLoggedIn.
### Endpoints
- /register
- /profile
- /updateProfile
### Events
- UserRegistered
- UserLoggedIn
- UserActivityUpdated
## Authentication Service
### Responsibilities
- Handles login, logout, and token management.
### Endpoints
- /login
- /logout
- /refreshToken
### Events
- UserLoggedIn
- UserLoggedOut

## Post Service
### Responsibilities
- Handling the creation, retrieval, and management of posts.
### Endpoints

### Events
- PostCreated
- PostUpdated
- PostDeleted

## Comment Service
### Responsibilities
- Managing comments on posts.
### Events
- CommentCreated
- CommentUpdated
- CommentDeleted

## Vote Service
### Responsibilities
- Managing upvotes and downvotes on posts and comments.
### Events
- VoteSubmitted
- VoteUpdated

## Feed Service
### Responsibilities
- Aggregating posts and comments to generate user feeds.

### Events
- FeedUpdated

## Notification Service
### Responsibilities
- Sending notifications to users for various events (new comments, upvotes, etc.).

### Events
- NotificationSent

## Media Service
### Responsibilities
- Handling media uploads and storage (images, videos).

### Events

##  Gateway Service
### Responsibilities
- Acts as a reverse proxy to route requests to the appropriate microservices.
- Handles API Gateway logic and security (e.g., verifying tokens).

### Events