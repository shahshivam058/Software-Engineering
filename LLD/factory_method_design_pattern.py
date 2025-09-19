from abc import ABC, abstractmethod

# --- 1. Product Interface and Concrete Products ---

class Query(ABC):
    """The Product interface declares the operations common to all concrete products."""
    @abstractmethod
    def execute(self, query_string: str):
        pass

class SQLQuery(Query):
    """A Concrete Product that provides an implementation for the SQL database."""
    def execute(self, query_string: str):
        print(f"Executing SQL query: '{query_string}'")

class MongoDBQuery(Query):
    """A Concrete Product that provides an implementation for the NoSQL database."""
    def execute(self, query_string: str):
        print(f"Executing MongoDB query: '{query_string}'")

# --- 2. Creator Interface and Concrete Creators ---

class Database(ABC):
    """
    The Creator interface declares the factory method, which is expected to return
    an object of a Product class. The Creator's subclasses will implement this method.
    """
    @abstractmethod
    def create_query(self) -> Query:
        pass

    def connect(self):
        print("Connecting to the database...")

    def get_version(self):
        print("Getting database version...")

    def perform_action(self, action: str):
        """
        The Creator also contains some core logic that relies on the factory method
        to produce a Product object. This code is independent of the concrete product type.
        """
        query = self.create_query()
        print("A query object has been created by the factory method.")
        query.execute(action)

class PostgreSQLDatabase(Database):
    """
    A Concrete Creator that overrides the factory method to return a specific
    type of Concrete Product, the SQLQuery.
    """
    def create_query(self) -> Query:
        return SQLQuery()

class MongoDBDatabase(Database):
    """
    Another Concrete Creator that overrides the factory method to return a different
    Concrete Product, the MongoDBQuery.
    """
    def create_query(self) -> Query:
        return MongoDBQuery()

# --- 3. Client Code ---

class UserService:
    """
    The Client code works with an instance of a Concrete Creator through its
    abstract interface. It is independent of the concrete product type that gets created.
    """
    def __init__(self, database: Database):
        self.database = database
        self.database.connect()

    def create_user(self, user_data: dict):
        print("\nUserService is creating a user.")
        query_string = f"INSERT INTO users VALUES ({user_data})"
        self.database.perform_action(query_string)

    def delete_user(self, user_id: int):
        print("\nUserService is deleting a user.")
        query_string = f"DELETE FROM users WHERE id = {user_id}"
        self.database.perform_action(query_string)

# --- Usage Example ---

if __name__ == "__main__":
    print("--- User Service using PostgreSQL ---")
    postgres_db = PostgreSQLDatabase()
    user_service_sql = UserService(postgres_db)
    user_service_sql.create_user({"name": "Alice", "email": "alice@example.com"})

    print("\n" + "="*40 + "\n")

    print("--- User Service using MongoDB ---")
    mongo_db = MongoDBDatabase()
    user_service_nosql = UserService(mongo_db)
    user_service_nosql.delete_user(123)


# --------------------------------------------------------------------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# --- 1. Abstract Products ---
# These are the interfaces for our family of related objects.

class Query(ABC):
    """Abstract Product A: Defines an interface for a database query."""
    @abstractmethod
    def execute(self, statement: str):
        pass

class Connection(ABC):
    """Abstract Product B: Defines an interface for a database connection."""
    @abstractmethod
    def connect(self):
        pass

class Transaction(ABC):
    """Abstract Product C: Defines an interface for a database transaction."""
    @abstractmethod
    def begin(self):
        pass
    
    @abstractmethod
    def commit(self):
        pass

# --- 2. Concrete Products ---
# These are the specific implementations for each product family.

# Concrete Products for the SQL family
class SQLQuery(Query):
    """Concrete Product A1: An SQL-specific query."""
    def execute(self, statement: str):
        print(f"Executing SQL query: '{statement}'")

class PostgreSQLConnection(Connection):
    """Concrete Product B1: A PostgreSQL-specific connection."""
    def connect(self):
        print("Connecting to PostgreSQL...")

class SQLTransaction(Transaction):
    """Concrete Product C1: An SQL-specific transaction."""
    def begin(self):
        print("Beginning SQL transaction...")

    def commit(self):
        print("Committing SQL transaction...")

# Concrete Products for the NoSQL family
class MongoDBQuery(Query):
    """Concrete Product A2: A MongoDB-specific query."""
    def execute(self, statement: str):
        print(f"Executing MongoDB query: '{statement}'")

class MongoDBConnection(Connection):
    """Concrete Product B2: A MongoDB-specific connection."""
    def connect(self):
        print("Connecting to MongoDB...")

class NoSQLTransaction(Transaction):
    """Concrete Product C2: A NoSQL-specific transaction."""
    def begin(self):
        print("Beginning NoSQL transaction...")

    def commit(self):
        print("Committing NoSQL transaction...")

# --- 3. Abstract Factory and Concrete Factories ---
# The factories are responsible for producing families of compatible products.

class DatabaseFactory(ABC):
    """
    Abstract Factory: Declares a set of methods for creating each abstract product.
    """
    @abstractmethod
    def create_query(self) -> Query:
        pass

    @abstractmethod
    def create_connection(self) -> Connection:
        pass

    @abstractmethod
    def create_transaction(self) -> Transaction:
        pass

class PostgreSQLFactory(DatabaseFactory):
    """
    Concrete Factory 1: Implements the creation methods to produce
    the SQL family of products.
    """
    def create_query(self) -> Query:
        return SQLQuery()

    def create_connection(self) -> Connection:
        return PostgreSQLConnection()
    
    def create_transaction(self) -> Transaction:
        return SQLTransaction()

class MongoDBFactory(DatabaseFactory):
    """
    Concrete Factory 2: Implements the creation methods to produce
    the NoSQL family of products.
    """
    def create_query(self) -> Query:
        return MongoDBQuery()

    def create_connection(self) -> Connection:
        return MongoDBConnection()

    def create_transaction(self) -> Transaction:
        return NoSQLTransaction()

# --- 4. Client Code ---
# The client uses the Abstract Factory to get a family of products without
# knowing their concrete classes.

class UserService:
    """
    The Client: Interacts with the Abstract Factory and Abstract Products,
    making it independent of the specific database family.
    """
    def __init__(self, factory: DatabaseFactory):
        self.query = factory.create_query()
        self.connection = factory.create_connection()
        self.transaction = factory.create_transaction()
        self.connection.connect()

    def create_user(self, user_data: dict):
        print("\nUserService is creating a user.")
        self.transaction.begin()
        statement = f"INSERT INTO users VALUES ({user_data})"
        self.query.execute(statement)
        self.transaction.commit()

    def delete_user(self, user_id: int):
        print("\nUserService is deleting a user.")
        self.transaction.begin()
        statement = f"DELETE FROM users WHERE id = {user_id}"
        self.query.execute(statement)
        self.transaction.commit()

# --- Usage Example ---
if __name__ == "__main__":
    print("--- Using PostgreSQL via Abstract Factory ---")
    postgres_factory = PostgreSQLFactory()
    user_service_sql = UserService(postgres_factory)
    user_service_sql.create_user({"name": "Alice", "email": "alice@example.com"})

    print("\n" + "="*40 + "\n")

    print("--- Using MongoDB via Abstract Factory ---")
    mongo_factory = MongoDBFactory()
    user_service_nosql = UserService(mongo_factory)
    user_service_nosql.delete_user(123)
