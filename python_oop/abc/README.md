Concept Guide
Abstract Classes and Concrete Classes
An abstract class defines behavior that subclasses must implement.

For example, a class may define a method that all subclasses must provide, while leaving the actual implementation to each subclass.

A simplified relationship looks like this:

          Animal (Abstract Class)
                 │
        ┌────────┴────────┐
        │                 │
       Dog               Cat
   (Concrete Class)  (Concrete Class)
Interpretation:

Animal defines required behavior
Dog and Cat provide concrete implementations
all subclasses share the same contract
Duck Typing
In Python, objects are often used based on what they can do, not only on what they inherit from.

Example idea:

if an object provides a method named draw(), it may be usable in a function that expects something drawable
the object does not always need to inherit from a specific class for that use case
This approach is often called duck typing.

