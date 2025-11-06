# Árvore Sintática Atribuída

```json
[
  {
    "node": "op",
    "op": "/",
    "args": [
      {
        "node": "literal",
        "value": 5.5,
        "type": "real",
        "line": 1
      },
      {
        "node": "literal",
        "value": 2,
        "type": "int",
        "line": 1
      }
    ],
    "type": "unknown",
    "line": 1
  },
  {
    "node": "op",
    "op": "MEM",
    "args": [
      {
        "node": "id",
        "name": "mZ",
        "type": "unknown",
        "line": 2
      }
    ],
    "type": "unknown",
    "line": 2
  },
  {
    "node": "op",
    "op": "RES",
    "args": [
      {
        "node": "literal",
        "value": 1,
        "type": "int",
        "line": 3
      }
    ],
    "type": "unknown",
    "line": 3
  },
  {
    "node": "op",
    "op": "if",
    "args": [
      {
        "node": "literal",
        "value": 3,
        "type": "int",
        "line": 4
      },
      {
        "node": "literal",
        "value": 2,
        "type": "int",
        "line": 4
      },
      {
        "node": "op",
        "op": "MEM",
        "args": [
          {
            "node": "literal",
            "value": 10,
            "type": "int",
            "line": 4
          },
          {
            "node": "id",
            "name": "mR",
            "type": "unknown",
            "line": 4
          }
        ],
        "type": "int",
        "line": 4
      }
    ],
    "type": "int",
    "line": 4
  },
  {
    "node": "op",
    "op": "while",
    "args": [
      {
        "node": "literal",
        "value": 1,
        "type": "int",
        "line": 5
      },
      {
        "node": "literal",
        "value": 2,
        "type": "int",
        "line": 5
      },
      {
        "node": "id",
        "name": "+",
        "type": "unknown",
        "line": 5
      },
      {
        "node": "op",
        "op": "MEM",
        "args": [
          {
            "node": "id",
            "name": "mNot",
            "type": "unknown",
            "line": 5
          }
        ],
        "type": "unknown",
        "line": 5
      }
    ],
    "type": "unknown",
    "line": 5
  },
  {
    "node": "op",
    "op": "%",
    "args": [
      {
        "node": "literal",
        "value": 7,
        "type": "int",
        "line": 6
      },
      {
        "node": "literal",
        "value": 0,
        "type": "int",
        "line": 6
      }
    ],
    "type": "int",
    "line": 6
  },
  {
    "node": "op",
    "op": "MEM",
    "args": [
      {
        "node": "literal",
        "value": 10,
        "type": "int",
        "line": 7
      },
      {
        "node": "id",
        "name": "mInit",
        "type": "unknown",
        "line": 7
      }
    ],
    "type": "int",
    "line": 7
  },
  {
    "node": "op",
    "op": "MEM",
    "args": [
      {
        "node": "id",
        "name": "mInit",
        "type": "int",
        "line": 8
      }
    ],
    "type": "int",
    "line": 8
  },
  {
    "node": "op",
    "op": "==",
    "args": [
      {
        "node": "literal",
        "value": 4,
        "type": "int",
        "line": 9
      },
      {
        "node": "literal",
        "value": 4,
        "type": "int",
        "line": 9
      }
    ],
    "type": "bool",
    "line": 9
  },
  {
    "node": "op",
    "op": "+",
    "args": [
      {
        "node": "id",
        "name": "x",
        "type": "unknown",
        "line": 10
      },
      {
        "node": "id",
        "name": "y",
        "type": "unknown",
        "line": 10
      }
    ],
    "type": "unknown",
    "line": 10
  }
]
```
