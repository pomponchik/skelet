# skelet
Collect all the settings in one place


One object with a configuration for your project. This can take settings away from:

- The specified sections in the `pyproject.toml` file
- One or more separate `toml` files
- Default values specified in the class
- Values that are set during operation for class attributes (if the field is not marked as read only)

Additional features:

- The ability to validate any fields (+ a set of standard validators for basic field types)
- The ability to set a callback to change any of the fields + a mutex to a mutable field to ensure thread safety)
- Shared mutexes for multiple fields
- Typing support
- Checking fields for conflicts
- Converting types from one to another
- Subtraction of environment variables
- Nested classes
- Reading parameters from the CLI
- Context manager like https://confz.readthedocs.io/en/latest/usage/context_manager.html
