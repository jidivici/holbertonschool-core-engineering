Class Hierarchy in This Project
Throughout this project you will progressively build the following class hierarchy:

BaseGeometry
      │
      ▼
   Rectangle
      │
      ▼
     Square
Interpretation
BaseGeometry defines behavior shared by geometric shapes.
Rectangle inherits from BaseGeometry and implements concrete behavior.
Square inherits from Rectangle and represents a more specialized shape.
Because Square inherits from Rectangle, and Rectangle inherits from BaseGeometry, a Square object can also be treated as:

a Rectangle
a BaseGeometry
This relationship enables code reuse and polymorphism, allowing programs to work with related objects through a shared interface.
