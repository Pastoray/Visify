# Visify

Visify is an intuitive web-based application designed to visually represent data structures no matter the size in an interactive and engaginging manner. as of today Visify supports visualizing trees, linked lists and graphs.

## Usage

On the home page, there are five input fields:
- Trees
    Here you enter your input in the form of an array, This app assumes that the node values are organized following the **Depth-First Search (DFS) traversal**.

- Linked Lists
    Doubly linked lists and singly linked lists are very similar, you just simply enter an array of consecutive linked list node values, **this app will run through them one after the other**.

- Graphs
    Here you have the option to enter an array graph representation which would look like this:
    ```python
    [ [ from¹, to¹ ], [ from², to² ], ... ]
    ```

    And you also have the option to enter a graph representation of the graph which would look like this:
    ```python
    { from¹: [ to¹, to², to³ ], from²: [ to⁴, to⁵ ], ... }
    ```
    The graph implementation also uses a **Depth-First Search (DFS) traversal** approach.

## Note

- **This web application will display linked lists and graphs with cycles but once the app finds a node that it already went through it will simply stop to avoid errors and unexpected behaviour**

## Technologies
### UI
- HTML
- CSS
- SASS

### Server
- Python / Flask
- Jinja 2
- Webpack
- Docker

## Contributing

We welcome contributions from the community! If you would like to contribute to this project, simply fork the repository, make your changes, and submit a pull request.

## Installation

Everything needed to run this app is included in the package.json dependencies and the requirements.txt.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT)

- [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://opensource.org/licenses/MIT)
