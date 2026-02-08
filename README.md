# AI.DATA-FORMAT

This document describes the **actual**, **implemented**, **non-future** syntax of AI.DATA-FORMAT.

Only the following features are included:

* Type definitions
* Positional records
* Named records
* Lists
* Multiline text
* Comments 

Nothing else exists in the current version.

---

## 1. Type Definition

A type defines a name and an ordered list of fields.

```aid
User</comment/ ={(23,"A",3) #tag1 #tag2} %[{ id: 4, b: "a", c: 43}]: id:number,
b: string , c:number, >
@Users
<
 @list 
 a: number,
 b: string
>
[
  @size=5
  /example list of values/

  (1,`text`,5)
  (2,`Text can be

multiline
`,5)
  {
    id:3,
    b: "text"
  }
]
```



Rules:

* The type name (`Name`) is optional but recommended.
* The header `<...>` defines field names and their order.
* Comments (`/.../`) are **allowed here**.
* After the header, the type may contain a list of values.

---

## 2. Data Structures

### 2.1 Positional Record

```
(a,b,c)
```

* Must follow the exact order of fields in the type header.

### 2.2 Named Record

```
{key:value}
```

* May be used wherever the type is known (declared or inline).
* Keys must match field names.
* Must contain **no spaces**.

### 2.3 List

```
[ ... ]
```

* Contains positional or named records.

### 2.4 Multiline Text

```
`
line
line
`
```

* Ends with a line containing only a backtick.
* Allowed as a string value.

---

## 3. Comments

```
/ comment /
```

Rules:

* Allowed only inside type definitions.
* Forbidden in data.

---

## 4. General Rules

* **Data must contain NO spaces.**
* Schema may contain spaces and comments.
* Named fields always use `key:value` without spaces.
* Positional order must exactly match the declared order.

---

## 5. Inline Type Usage

### Type used after declaration

```aid
@User<id:number name:string desc:string>

value:@User(2,"Alice","Hello")
value2:@User(3,"Bob","World")
```


---

## 6. Nested Types — Current Allowed Form

Nested types are allowed **only as pure structural definitions**, without modifiers or validators.

```
@User<
  id:string
  name:string
  profile: < level:number, score:number >
>
[
  ("u1","Aga",{level:5,score:82})
  ("u2","Marek",{level:7,score:91})
]
```



## 7. Data Example (fully valid)

```
[
@User<id,name,age,profile,score,active>
("u1","Aga",31,{level:5,prefs:{color:red,badge:{code:"X21",exp:1800000000}}},82,true)
("u2","Marek",28,{level:7,prefs:{color:blue,badge:{code:"D55",exp:1850000000}}},91,false)
]
```

This uses **only the currently implemented features**.


# FUTURES

This is planned futures for the format


* Modifiers applied inside type definitions:

```
!required                 field must be included
?empty                    field must not be "", [] or {}
=value                    default value for optional fields
N..M                      numeric range
lenN..M                   string length range
in(a,b,c)                 enumeration
re"pattern"               regular expression
$key=value                metadata attribute
#["tag1","tag2"]          tags (schema only)
%[ 4, 32, 12]             Examples
```

* If a field has no `?optional`, it is required unless default behavior is overridden.
* `!empty` forbids explicit empty values.
* `=value` applies only when the field is omitted.

* BINARY DATA

```
<me: binary>
{
  me: ~<bin:3>0F 0A B3~
}
```

* HEX DATA

```
<me: binary>
{
  me: ~[hex]1A0F4F~
}
```


* BASE64 DATA

```
<me: binary>
{
  me: ~[b64]ADFKDXKZK56434~
}
```


* Pointers:


```
[
  @User<id: number, name: string, friend *@User>
 (1, "Alex", *User[2])
 (2, "Alice", *User[1])
]

```

* Points to previously defined value whose `id` equals `id`.
* Type hint is optional but recommended.

* Named initialization:

```
@User<id: string, name: string>
users: [
  @User

]

```

---


### Inline type + value

```aid
value: @User<id:number name:string desc:string>(2,"Alice","Hello")
```

Both forms are valid.