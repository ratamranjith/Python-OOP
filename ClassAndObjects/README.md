# Python: Class and Objects

## Description

This script provides an example of how to use classes and objects in Python. It defines a class named `Television` with various attributes and a method to display the attributes. The script then creates two instances of the `Television` class and uses the method to print the attributes of each instance.

## Code Explanation

The script demonstrates the following concepts:

1. **Class Definition**: The `Television` class is defined with the `__init__` constructor method to initialize its attributes: `brand`, `dimensions`, `warranty`, and `price`. Initially, these attributes are set to `None`.

2. **Class Instance Creation**: Two instances of the `Television` class (`tv` and `tv1`) are created. Each instance represents a different television with its own unique set of attribute values.

3. **Assigning Attribute Values**: After creating the instances, the script assigns values to the attributes of each instance. For example, `tv.brand` is set to `"onida"` and `tv1.brand` is set to `"MI"`.

4. **Method Definition and Usage**: The `Television` class includes a method called `print_data()`. This method iterates over the instance's attributes (using the built-in `__dict__` method) and prints out the attribute names and their corresponding values.

5. **Method Invocation**: The `print_data()` method is called on both `tv` and `tv1` instances to print the details of each television.

## Example Output

When the script is executed, it produces the following output:

```
brand : onida
dimensions : 2040x1028
warranty : 1 Year
price : 30000
-------------
brand : MI
dimensions : 2040x1028
warranty : 1 Year
price : 30000
-------------
```

## Additional Notes

- The `__dict__` attribute in Python is a built-in attribute that stores an object's (instance's) writable attributes as a dictionary. This attribute is used within the `print_data()` method to access and print the values of the class's attributes.

This example provides a clear demonstration of how to define a class, create instances, assign attributes, and use methods in Python.
