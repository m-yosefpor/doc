# designing an API for contacts

user stories
apis
data format
data base
Architecture (micorservice, monolothic, services): search, cache, mq, api, auth, api-gw
communication: grpc vs http
language for each component
impelment:
  repo structure
  libraries


## User stories

0. is it a multi-tenant multi-contact application? or is it only a single application
  security: can I store the info? or should it be encrypted
  load?

1. data format:

  id
  first name
  last name
  phone number [] ?
  email
  address

?? is it the first name + last name? usually id is a better approach
Using a separate, unique identifier (such as contactId) for each contact is generally a better approach than using a combination of firstName and lastName as the ID for several reasons:

    Uniqueness: Different contacts may have the same first and last name, leading to conflicts. A unique ID (like a UUID) ensures each contact is distinct.

    Consistency: If a contact's name changes (due to marriage, legal name change, etc.), their identifier remains consistent. This is important for maintaining data integrity.

    Privacy and Security: Exposing names in URLs or API calls (if the name is used as an ID) can be a privacy concern. A non-descriptive unique identifier mitigates this issue.

    Flexibility: Using a unique ID allows for more flexibility in your application. For example, if you decide to allow contacts without a last name, or if you want to introduce features like duplicate contact detection, having a separate ID makes these tasks

phoneNubmer[]
1. postgres text[]
2. serialize
3. Use a Join Table
4. Store as Delimited String (not good, instead do no.2 with csv serialize)

1. create: user wants to create a record in contacts
  first name
  last name
  phone number []
  address
  q: which fields are optional?

  except for the id, which should be calculated with the server and returned
import uuid
unique_id = str(uuid.uuid4())

Is It Necessary to Check for Collisions? (uuid-v4)
In most practical applications, especially where UUIDs are used as database keys or identifiers in a web application, it is not standard practice to explicitly check for collisions because the probability is so low. The design and size of the UUID space effectively make collisions so rare that they are often disregarded.

import "github.com/google/uuid"
newUUID, err := uuid.NewRandom()


Success Response (200 OK) (be more explicit 201)

full json vs only return the id

efficiency: This approach is more bandwidth-efficient, especially if the resource is large and the client already has most of the information (having just sent it).
Simplicity: It provides a clear and straightforward response indicating the successful creation of the resource.
Usage Pattern: If the typical workflow in your application involves creating a resource and then performing subsequent operations based on its ID, returning only the ID might be sufficien
----
Completeness: This approach immediately gives the client the full, server-validated resource, including any modifications or additional fields the server might add (like timestamps, computed fields, or default values).
Convenience: It saves an additional request from the client to fetch the complete resource after creation.
Clarity: It provides immediate feedback to the client about the result of the create operation, which can be useful for debugging and validation purposes.

201 Created
{
  "contactId": "generated_unique_identifier",
  "firstName": "John",
  "lastName": "Doe",
  "phoneNumber": "123-456-7890",
  "email": "john.doe@example.com",
  "address": "123 Main St, Anytown, AN 12345",
  "notes": "Met at conference in 2023"
}

Error Response (e.g., 400 Bad Request):
{
  "error": "Error message describing what went wrong"
}

2. read


3. update: user wants to update a record in contacts:

    PUT or PATCH /contacts/{contactId}

The choice between PUT and PATCH depends on how you want to handle updates:

    Use PUT if the request is expected to provide the full updated entity. This is idempotent, meaning that making the same PUT request multiple times will result in the same state of the resource.
    Use PATCH if the request may contain only the changes to the entity. This is also idempotent in the context of the changes being applied.


  first name
  last name
  any other fields present
  q: does user want to remove a field


{
  "phoneNumbers": [
    {
      "action": "add",
      "number": "555-123-4567"
    },
    {
      "action": "remove",
      "number": "123-456-7890"
    }
  ]
}

{
  "message": "Contact updated successfully",
  "updatedContact": {
    "contactId": "123e4567-e89b-12d3-a456-426614174000",
    "phoneNumbers": ["555-123-4567", "987-654-3210"]
  }
}

204 No Content

no changes made: 304 Not Modified: This is less common and might not be necessary unless you have a specific reason to inform the client that no changes occurred


400 Bad Request: If the request body is invalid.
404 Not Found: If no contact with the specified contactId exists.

409 Conflict: This might be used if the requested changes conflict with the current state of the resource. For example, trying to remove a phone number that doesn't exist.

Concurrency: Consider how your API will handle concurrent updates to the same contact.


4. delete

DELETE /contacts/{contactId}

Success Response (200 OK or 204 No Content):
{
  "message": "Contact deleted successfully",
  "contactId": "123e4567-e89b-12d3-a456-426614174000"
}

5. list 400, 404
  Pagination and Performance: add page and limit query parameters to control pagination.

    GET /contacts
    GET /contacts?firstNameStartsWith=X&lastNameStartsWith=Y&?phoneNumber=123&
    GET /contacts?fuzzyName=Jhn


### data type (first we need to talk about data retrieval as well. also read intensive/write intensive/and all other topics in db)

f the data in your application has a document-like structure (i.e., a tree of one-to- many relationships, where typically the entire tree is loaded at once), then it’s probably a good idea to use a document model.

db normalization
However, if your application does use many-to-many relationships, the document model becomes less appealing

It’s possible to reduce the need for joins by denormal‐ izing, but then the application code needs to do additional work to keep the denor‐ malized data consistent.
Joins can be emulated in application code by making multiple requests to the database, but that also moves complexity into the application and is usually slower than a join performed by specialized code inside the database.

schema less
- There are many different types of objects, and it is not practical to put each type of object in its own table
- The structure of the data is determined by external systems over which you have no control and which may change at any time

data-locality

document based vs relational

Schema changes have a bad reputation of being slow and requiring downtime. This reputation is not entirely deserved: most relational database systems execute the ALTER TABLE statement in a few milliseconds. MySQL is a notable exception—it copies the entire table on ALTER TABLE, which can mean minutes or even hours of downtime when altering a large table—although various tools exist to work around this limitation [24, 25, 26]

  atomic: ?
  consistency:
  isolation:
  durability: yes
Relational Databases (SQL):
    PostgreSQL
    MySQL
    SQLite
    Microsoft SQL Server

Pros
    Structured Data: Ideal for structured data with relationships between different entities.
    ACID Compliance: Ensures reliable transactions, which is crucial for data integrity.
    Complex Queries: Strong at handling complex queries and relationships.
    Mature Tools and Support: Extensive support, mature tools, and a large community.

Cons

    Scaling: Can be more challenging to scale horizontally compared to NoSQL databases.
    Schema Changes: Modifying the schema can be complex and may require downtime.




MongoDB (Document-Oriented)
Cassandra (Wide-Column Store)
Redis (Key-Value Store)
Neo4j (Graph Database


In-Memory Databases
Examples

    Redis
    Memcached

NewSQL Databases
Examples

    Google Spanner
    CockroachDB

Pros

    Scalability of NoSQL + ACID Compliance of SQL: Aim to combine the best of SQL and NoSQL.
    High Availability: Built for cloud environments with high availability.
    Strong Consistency: Offers strong data consistency.

Cons

    Complexity and Cost: Can be more complex to set up and manage.
    Relative Newness: Not as battle-tested as traditional SQL databases.

----
For a straightforward contact management application like yours, both SQL and NoSQL databases could work well.

    If you anticipate complex querying needs or have a strong background in SQL, a relational database like PostgreSQL would be a solid choice.
    If you prefer schema flexibility, anticipate frequent changes to the data structure, or plan to scale horizontally, a NoSQL database like MongoDB would be more appropriate.



    Atomicity: This property ensures that all parts of a transaction are completed successfully. If one part fails, the entire transaction fails. For your application, atomicity is important when updating or adding multiple pieces of information at once, like adding a contact with multiple phone numbers.

    Consistency: This ensures that the database remains in a valid state before and after a transaction. Given that your application might involve complex operations like fuzzy searches or updates across multiple fields, maintaining consistency is crucial.

    Isolation: This property ensures that transactions are processed independently and securely, even when executed concurrently. For an application like yours, where multiple users might be searching or updating data simultaneously, isolation is important but might not be as critical as it would be in a high-transaction, multi-user system.

    Durability: This ensures that once a transaction is committed, it will remain so, even in the event of a system failure. Durability is important for your application to ensure that contact data isn’t lost or corrupted.


    Consistency (as defined in CAP, which is different from ACID's consistency): Every read receives the most recent write or an error. For your application, consistency is important but can be balanced with availability, depending on your specific requirements

    Every request receives a response, without guaranteeing that it contains the most recent write. Availability is crucial for user experience, especially for an application that handles contact information. Users expect the system to be accessible and responsive whenever they perform operations like searching or updating contacts.


- scale (reuests, data, which api)
-

ACID Compliance: PostgreSQL offers full ACID compliance, ensuring reliable and secure transactions, which is important for operations like adding or updating contacts with multiple phone numbers and associated details.

Advanced Search Capabilities: PostgreSQL supports advanced querying capabilities, including full-text search, which can be beneficial for implementing features like fuzzy name search. It also has powerful indexing options, which are crucial for optimizing search performance.

PostgreSQL allows for JSON storage,  robust full-text search

mariadb: Performance: MariaDB often has the edge in read-heavy scenarios and offers good replication features (slight edge  )

CA





- scale:
  - cockroach
  - cassandra: Good for write-heavy workloads, eventually consistent

  - mongodb: sharding


OLTP OLAP

log-structured storage engines, and page-oriented storage engines such as B-trees

### fuzzy
Using PostgreSQL for Fuzzy Search

PostgreSQL has several extensions and features, like pg_trgm and full-text search, which can be used for implementing fuzzy search.
Pros:

    Simplicity: No need for additional infrastructure or synchronization mechanisms since everything is handled within a single system.
    ACID Compliance: Maintains the ACID properties of the database.
    Cost-Effective: Generally more cost-effective as it doesn't require additional systems.
    Good for Smaller Datasets: Efficient for small to medium-sized datasets.

Cons:

    Performance: For very large datasets, the performance might not be as good as specialized search engines like Elasticsearch.
    Limited Scalability for Search: Scalability is limited to the database's overall scalability.
    Less Advanced Search Features: While PostgreSQL is powerful, it might lack some of the advanced search capabilities and optimizations available in dedicated search engines.

    Highly Optimized for Search: Elasticsearch is designed specifically for search operations, offering superior performance, especially with large datasets.
    Scalability: It scales horizontally, which can be beneficial as your dataset grows.
    Advanced Search Capabilities: Offers a wide range of search functionalities, including more advanced fuzzy search capabilities.
    Real-Time Search: Optimized for real-time search applications.

Cons:

    Complexity: Adds complexity to your system in terms of maintenance and infrastructure.
    Data Synchronization: Requires mechanisms to keep data synchronized between the primary database and the Elasticsearch index.
    Cost: Additional costs for running and maintaining another system.
    Overkill for Small Datasets: For smaller datasets, the benefits might not justify the additional complexity and cost.


- how to sync:
1. Application-Level Synchronization
Pros: Straightforward to implement and can be customized based on application logic.
Cons: Increases complexity in the application code and can lead to inconsistencies if not carefully managed
2. Database Triggers and Log-Based Synchronization
CDC
Database Triggers: Triggers in your database can call external processes or services to update Elasticsearch upon data changes.
Log-Based CDC Tools: Tools like Debezium can capture changes in your database's transaction log and stream these changes to Elasticsearch.

    Pros: Decouples data synchronization from application logic and can capture all changes made to the database.
    Cons: Can add load to the database and might be complex to set up and maintain.

3. Periodic Synchronization (Batch Process)
    How it Works: A batch process runs at regular intervals, querying the database for recent changes and updating Elasticsearch.
    Pros: Simpler to implement and can be less invasive on the primary database operations.
    Cons: There's a lag between data changes in the database and the updates in Elasticsearch, leading to temporary inconsistencies.

4. Queue-Based Synchronization

Use a message queue (like RabbitMQ, Kafka) to handle synchronization tasks.

    How it Works: When a change occurs in the database, an event is published to a queue, and a separate service consumes these events to update Elasticsearch.
    Pros: Decouples the synchronization process from both the database and application logic, offering scalability and reliability.
    Cons: Adds the complexity of managing a message queue system and additional service for consuming messages.


## caching

redis: higher capabilities, clustering,etc... memcached: simpler data
  In both cases, supplementing with a caching layer for reads can significantly improve performance.

  Choose a Caching Strategy:

    Cache-Aside (Lazy Loading): The application first checks the cache; if the data is not present, it retrieves it from the database and then stores it in the cache for subsequent access.
    Write-Through Cache: Data is written to the cache and the database simultaneously. This ensures data consistency but might be slower for write operations.
    Write-Behind (Delayed Write): Data is first written to the cache and then written to the database after a certain interval or under certain conditions.

Implement Cache Eviction Policies: Define rules for how data is removed from the cache, like Least Recently Used (LRU), Time to Live (TTL), etc.

Cache Invalidation: Implement a mechanism to update or invalidate cache entries when data in the database changes to maintain consistency

#### microservice vs monolothic
team based
language based
scope
easier deploy


mono repo vs multi-repo

TODO: chatgpt monolothic vs microservice

Monolithic Architecture

    Pros:
        Simpler to develop and deploy, especially for small to medium-sized applications.
        Easier debugging and testing since everything is in one codebase.
        Ideal for applications with a well-defined scope that are not expected to scale massively.

    Cons:
        Can become difficult to manage as the application grows.
        Scaling requires scaling the entire application.
        Tightly coupled components can impact flexibility and agility.

Microservices Architecture

    Pros:
        Scalability: Individual components can be scaled independently.
        Flexibility in technology choices and easier to introduce new technologies.
        Resilience: Failure in one service doesn’t bring down the entire application.

    Cons:
        Complexity in deployment, testing, and monitoring.
        Network latency and data consistency challenges.
        Requires a well-thought-out approach to service boundaries, data ownership, and communication.


1.Contact Management Service

Scope:

    Handles CRUD (Create, Read, Update, Delete) operations for contacts.
    Manages contact details like names, phone numbers, email, and addresses.

Interactions:

    Communicates with PostgreSQL for storing and retrieving contact data.
    Interacts with the Caching Service for cache-related operations.
    Notifies the Search Service when contact information is created, updated, or deleted.

2. Search Service

Scope:

    Manages advanced search functionalities, including fuzzy searching.
    Handles search queries and returns results based on Elasticsearch indices.

Interactions:

    Communicates with Elasticsearch for executing search queries.
    Receives updates from the Contact Management Service to keep the search index updated.

3. Caching Service??

Scope:

    Manages caching strategies for frequently accessed data.
    Reduces the load on the Contact Management Service and the PostgreSQL database.

Interactions:

    Interfaces with Redis for storing and retrieving cached data.
    Synchronizes cache with the Contact Management Service's data.

Given your architecture involving PostgreSQL for the main database, Redis for caching, and Elasticsearch for fuzzy search, breaking down your contact management application into microservices can be approached by focusing on distinct functionalities and data concerns. Here's a possible breakdown:
1. Contact Management Service

Scope:

    Handles CRUD (Create, Read, Update, Delete) operations for contacts.
    Manages contact details like names, phone numbers, email, and addresses.

Interactions:

    Communicates with PostgreSQL for storing and retrieving contact data.
    Interacts with the Caching Service for cache-related operations.
    Notifies the Search Service when contact information is created, updated, or deleted.

2. Search Service

Scope:

    Manages advanced search functionalities, including fuzzy searching.
    Handles search queries and returns results based on Elasticsearch indices.

Interactions:

    Communicates with Elasticsearch for executing search queries.
    Receives updates from the Contact Management Service to keep the search index updated.

3. Caching Service

Scope:

    Manages caching strategies for frequently accessed data.
    Reduces the load on the Contact Management Service and the PostgreSQL database.

Interactions:

    Interfaces with Redis for storing and retrieving cached data.
    Synchronizes cache with the Contact Management Service's data.

4. Authentication and Authorization Service

Scope:

    Handles user authentication and authorization.
    Manages user credentials and session tokens.

Interactions:

    Ensures secure access to the Contact Management, Search, and Caching Services

5. API Gateway

Scope:

    Acts as the single entry point for the frontend to interact with the backend services.
    Routes requests to appropriate services and aggregates responses.

Interactions:

    Communicates with all backend services.
    Handles request routing, load balancing, and potentially API rate limiting.

#### language
concurency
image build size on k8s
compile time
rapid development

go: performance, less verbose than java, strong type
---

TODO: chatGPT
TODO: merge with docs


## service communications:
crud -> search
sync
    Immediate Consistency: Ensures that the Search service processes the notification immediately, maintaining data consistency between services.
    Simplicity: Easier to implement and understand, as it follows a straightforward request-response pattern.
    Error Handling: Immediate feedback on the success or failure of the operation, allowing for immediate error handling.

Cons:

    Coupling: Creates tighter coupling between services, as the CRUD service depends on the Search service's availability and response time.
    Latency: Can introduce latency in the CRUD operations, as it needs to wait for the Search service to respond.
    Scalability: Can impact scalability, as the CRUD service's throughput is limited by the Search service's ability to handle requests.
async
Pros:

    Decoupling: Reduces coupling between services, allowing the CRUD service to operate independently of the Search service's performance and availability.
    Scalability: Improves scalability, as the CRUD service can continue processing other requests without waiting for the Search service.
    Resilience: Enhances system resilience, as the CRUD service is not directly impacted by delays or failures in the Search service.

Cons:

    Eventual Consistency: Leads to eventual consistency, as there might be a delay before the Search service processes the update.
    Complexity: Adds complexity in tracking and handling messages, especially in failure scenarios.
    Error Handling: Handling errors becomes more complex, as the response from the Search service is not immediate.


Use Asynchronous Communication if your system can tolerate eventual consistency and you prioritize scalability and decoupling.

rmq:
Pros:

    Ease of Use: Known for its simplicity and ease of setup.
    Flexibility: Supports various messaging patterns like point-to-point, publish/subscribe, etc.
    Reliability: Provides features like message acknowledgments and durable queues.
    Scalability: Efficiently handles high-throughput scenarios with clustering.

Cons:

    Performance: While highly efficient, it might lag behind Kafka in handling extremely high volumes of data. Threshold: RabbitMQ can start to struggle with tens of thousands of messages per second
    Persistence: Heavier on resources when dealing with a large number of persistent messages.

kafka:
Pros:

    High Throughput: Excellent for handling very high volumes of data.
    Scalability: Easily scalable with partitioning and replication.
    Durability: Stores streams of records in a fault-tolerant way.
    Ecosystem: Rich ecosystem and integrations, suitable for complex event-driven architectures.

Cons:

    Complexity: Higher learning curve and more complex to set up compared to RabbitMQ.
    Resource Intensive: Requires more resources, especially in a clustered setup


Pros:

    Performance: Highly performant, especially in scenarios requiring low latency.
    Simplicity: Easier to use and deploy, with a focus on simplicity and performance.
    Scalability: Scales well with support for clustering.
    Lightweight: Lower operational overhead compared to Kafka.

Cons:

    Persistence: JetStream is relatively new and might not have as mature persistence capabilities as Kafka or RabbitMQ.
    Feature Set: While powerful, it might lack some advanced features found in Kafka.


### now libraries
1. fiber / echo /gin

fiber: fast only http logic (rare). no http2

gin: (also doesn't return error for handlers)
    Too Minimalistic for Some: Might be too minimalistic for complex applications that require more built-in features.
    Less Prescriptive: Offers less guidance on application structure, which can be a con for beginners or larger teams.


echo:
  Performance: While Echo is fast, it might be slightly less performant than Gin in some benchmarks, although this difference is often negligible in real-world applications
  Complexity: The additional features and functionality might add to the learning curve compared to Gin.

    Choose Gin if:
        You prefer a minimalist framework that stays out of your way.
        You want a framework that’s easy to learn and quick to set up for smaller projects or microservices.

    Choose Echo if:
        You need built-in features.
        You are building an application that relies heavily on middleware.
        You want a framework that’s easy to use but also offers more guidance and structure.

2. gorm/ sqlx: orm or not:
  Productivity and Ease of Use
  Code Readability and Maintenance
  Reduced Boilerplate Code
  Database Abstraction
  Built-in Features
  --
  Performance Overheads (esp for complex queries)
  Loss of Control and Flexibility
  Learning Curve
  omplexity in Advanced Scenarios


      Use an ORM if:
        You prioritize rapid development and ease of maintenance.
        Your application doesn't require highly complex and optimized SQL queries.
        You want to avoid dealing directly with SQL for most of your database operations.

    Avoid an ORM if:
        You need to write highly optimized, complex SQL queries.
        You prefer having full control over the SQL and database interactions.
        Your application's performance is critically dependent on the efficiency of the database access layer.

3. ozzo vs govalidator
performance: refelct only for rule creation not evaludation / Reflection-Based
only strucutres/api vs general purpose validation

4. slog (now we have a standard which is fast enough, and structured)

5. viper / koanf / built-in(flag,os.Getenv,yaml+ioutils,json+ioutils)

viper:
  hot reload
  multiple formats and sources
  default values
  - complexity
  - size

koanf:
 light weight
 multi format
 it also constructs the duration from a string, or for instance, accepts a number from a string.


yaml:
 no dependencies
 one way to do a thing. why need multiple formats?

RocksDB:
  lsm
####

docker compose up
make run

curl -XPOST   -H "Content-Type: application/json" -d @sample-user.json localhost:8081/contacts -i


style:?
  	z := 1.0
     better than z := float64(1) or var z float64 = 1
