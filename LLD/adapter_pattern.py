import sqlite3
import pymongo
from abc import ABC, abstractmethod

# 1. The Target Interface (What the Client Expects)
# This is an abstract base class that defines the methods the client will use.
class Database(ABC):
    @abstractmethod
    def save_user(self, user_data: dict) -> int:
        """Saves user data and returns the user's ID."""
        pass
    
    @abstractmethod
    def get_user(self, user_id: int) -> dict:
        """Retrieves user data by ID."""
        pass

# 2. The Adaptee Classes (The Incompatible Interfaces)
# These are the actual database drivers with their own unique method signatures.

# SQLite (SQL) Adaptee
class SQLiteDriver:
    def __init__(self, db_path: str):
        print(f"Initializing SQLite driver for: {db_path}")
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                email TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def execute_insert(self, table: str, columns: tuple, values: tuple) -> int:
        """Specific method for inserting a record."""
        print(f"SQLite: Inserting into '{table}' with columns {columns} and values {values}")
        placeholders = ', '.join(['?' for _ in columns])
        sql = f"INSERT INTO {table} ({', '.join(columns)}) VALUES ({placeholders})"
        self.cursor.execute(sql, values)
        self.conn.commit()
        return self.cursor.lastrowid
    
    def execute_select(self, table: str, record_id: int) -> tuple:
        """Specific method for selecting a record."""
        print(f"SQLite: Selecting from '{table}' with ID {record_id}")
        self.cursor.execute(f"SELECT * FROM {table} WHERE id = ?", (record_id,))
        return self.cursor.fetchone()

# MongoDB (NoSQL) Adaptee
class MongoDBDriver:
    def __init__(self, host: str, port: int, db_name: str):
        print(f"Initializing MongoDB driver for: {host}:{port}/{db_name}")
        self.client = pymongo.MongoClient(host, port)
        self.db = self.client[db_name]
        self.collection = self.db['users']

    def create_document(self, document: dict) -> str:
        """Specific method for creating a document."""
        print(f"MongoDB: Creating document in 'users' with data {document}")
        result = self.collection.insert_one(document)
        return str(result.inserted_id) # MongoDB IDs are complex, so we'll just return it as a string
    
    def find_document(self, doc_id: str) -> dict:
        """Specific method for finding a document."""
        print(f"MongoDB: Finding document in 'users' with ID {doc_id}")
        # Note: In a real app, we'd use ObjectId, but for this simple example, we'll assume a field exists.
        return self.collection.find_one({'_id': doc_id})

# 3. The Adapter Classes
# These classes implement the 'Database' interface and adapt the Adaptee's methods.

class SQLiteAdapter(Database):
    def __init__(self, driver: SQLiteDriver):
        self.driver = driver

    def save_user(self, user_data: dict) -> int:
        print("SQLiteAdapter: Translating 'save_user' to 'execute_insert'...")
        columns = tuple(user_data.keys())
        values = tuple(user_data.values())
        user_id = self.driver.execute_insert('users', columns, values)
        return user_id

    def get_user(self, user_id: int) -> dict:
        print("SQLiteAdapter: Translating 'get_user' to 'execute_select'...")
        user_tuple = self.driver.execute_select('users', user_id)
        if user_tuple:
            # Recreate the dictionary from the tuple
            return {'id': user_tuple[0], 'name': user_tuple[1], 'email': user_tuple[2]}
        return {}

class MongoDBAdapter(Database):
    def __init__(self, driver: MongoDBDriver):
        self.driver = driver
        self.last_user_id = 0 # Simple mock ID generation for demonstration

    def save_user(self, user_data: dict) -> int:
        print("MongoDBAdapter: Translating 'save_user' to 'create_document'...")
        # MongoDB does not have auto-incrementing integer IDs like SQL, so we'll simulate it.
        self.last_user_id += 1
        user_data['id'] = self.last_user_id
        doc_id = self.driver.create_document(user_data)
        return self.last_user_id

    def get_user(self, user_id: int) -> dict:
        print("MongoDBAdapter: Translating 'get_user' to 'find_document'...")
        # Simulating a find by our custom 'id' field
        user_data = self.driver.collection.find_one({'id': user_id})
        return user_data

# 4. The Client Code (The User of the Adapters)
# The client only knows about the 'Database' interface.

def client_app(database: Database):
    """A client function that uses the generic Database interface."""
    print("--- Client Application Running ---")
    user_data = {"name": "Alice", "email": "alice@example.com"}
    
    # Save a user
    user_id = database.save_user(user_data)
    print(f"Client: User saved with ID: {user_id}")
    
    # Get the user back
    retrieved_user = database.get_user(user_id)
    print(f"Client: Retrieved user: {retrieved_user}")
    print("----------------------------------\n")

# --- Example Usage ---

# 1. Use the SQLite adapter
print("### Running with SQLite Adapter ###")
sqlite_driver = SQLiteDriver('users.db')
sqlite_adapter = SQLiteAdapter(sqlite_driver)
client_app(sqlite_adapter)

# 2. Use the MongoDB adapter (requires a running MongoDB instance)
#    Note: You must have a MongoDB server running and the 'pymongo' library installed.
#    To install: pip install pymongo
try:
    print("### Running with MongoDB Adapter ###")
    mongo_driver = MongoDBDriver('localhost', 27017, 'mydatabase')
    mongo_adapter = MongoDBAdapter(mongo_driver)
    client_app(mongo_adapter)
except pymongo.errors.ConnectionFailure as e:
    print(f"Could not connect to MongoDB. Please ensure it is running. Error: {e}")