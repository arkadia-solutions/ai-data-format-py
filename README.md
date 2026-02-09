# ARKADIA AI.DATA-FORMAT

```text
                             :SB@MMWBZSr,
                         ,irXX7ri, iaBWMMMMM@a:    :,
                    i2WMMMMMMMMMMMM@a:7ZZWMMMMM@7 :i,02,
                 ,7S7;i::i;72Z2S0@ZZWMW;r7iBWWM@M2 rM0BM;
                   ia@@08Z0B2:  :,i0r rBZ,: XSBMZM: 2MMMMi
                 iBZ7i:,   iXZZSi   i;  ia   ;:@22: ;M@MMS
                 ,:    ,, ,7:  ,Xi  ;r,   :   ,SS,  rBZ8MiX7,
             r8WZ: XW@0Z8WMZ: rX: :M2;BZ ;r:   ;,   ::Si;ii   :7
          :8MM@a,:@0:      XM2  , i@WZMZ 28MMMBr     , :ZW@a  iB@;
        ,Z0MMWZi BB  ,aZ8i      S7,,  ;SXZMMMMMMMa::r ,         7M8,
        :;MMZ:   8Z  :07Z7   @X XaSa,:8MMMM2ZMMMMMMM@MS   i2 ,BX :WW:
        iM0:  ,X,i8r        XM:,S7a; XZWMMMM2,8MMMMMWr8M2, iS,    ,B@:
        87  iB0:,,,XZX,  XW S@    ,;aZ00ZZ2SX7,:S8082,iM00, :i  ar ,WW,
        : :0MB@Zi,,      iM2 Sr :;Xriirr:  ZM8      ,XBM@X   :   ,: i@a
         rMMMW0X:  8Z     : ;a00Z7,,2BMMWBZXi  :,   iaWMMMMB7    :;  2Wi
        rMMBr     ZW ,i   rW7a00Z702 78@MMMMMMMM0@MMM@@@MMMMMM0r     iWS
       :MZ,  ,7: ;M2;Zii,:MrB,   2S07 ZZ8BZ,XB0WMMMMMMMMW280BWWWW8i   8Z
       S:  ,ZZ   XMZW:rr, Z;B:  ,ZXSi S2222XXX7ZBZ;:BMMM@X:   irr:    ZZ
          ;MZ;   rMMX   : ,27XZZS;S;     ii    ,i,ZMMMMMMMMM@7  ,8Z   aa
         ;MM0: ,  BMi  iS   ,irr;:;, :7,,Wa S8Z,,aXMZWBBMMMMMMS:MM8  ,ZX
        ,WMM0,2   :@,  0rr        ;@Br2,7S ::r7,ir;rr8ZZMMMMMMSiMMa  ;ai
        rMMM8a7    ,:  @0:  ,:    ,   ,         ,Z222X77@MW02i iZW: ,SX
        X@SM0@:        BB   ;r   :S     ,;7XS77; ,XZZZZ82r, :;i ,,  ;X:
        ;riMMM:  , r , ;0 ,:7Z  ;SS   ;     ,       ,:  iZ@MMMMM2
           8MM;  ; Z ;i ;, XrMi  B8   X7 , ,7        ,XZWMMMMMM@B
           ,WM2  7;87:8    XXMW, ,Bi ;7@i i Z     ,;2aa8MWWMMMM02
            ,B@, :ZaMiBX   :ZBMWr, ;  XB@iiXX2::     Xa7;80Z@0a :
              X8  r8WMaMr   iZ0MM0,    ,X@;;ZWX8       :S; 7:
               ,i  rBWMMMr   :X;WM@r      ir:0@W0
                    ,0@MMM2    : ;BMWi        7@MW:
                      :0MMMWi       ;aBS:       i8MZ:
                         XBMMW;                    ,;r,
                            iS0@8;

```

---

> **The High-Density, Token-Efficient Data Protocol for Large Language Models.**
> Stop wasting context window on JSON braces. `AI.DATA` is a unified, schema-first data format designed specifically for AI understanding. It offers up to **25% token savings**, faster parsing, and human-readable structure that LLMs love.

---

## 📦 Installation

Get started immediately with pip:

```bash
pip install arkadia-ai-data-format
```

## 🚀 Fast Example

**Encoding to AI.DATA:**

```bash
echo '{ "data": 2}' | aid enc - -c
# Output: <data:number>(2)

```

**Decoding back to JSON:**

```bash
echo '<data:number>(2)' | aid dec - -f json
# Output: { "data": 2 }

```

---

## ⚡ Performance & Token Savings

Why switch? Because every token counts. `AICD` (Arkadia Compressed Data) consistently outperforms standard formats in both token efficiency.

```text
BENCHMARK SUMMARY:


   JSON  █████████████████████░░░░     6921 tok   ░░░░░░░░░░░░░░░░░░░░░░░░░     0.15 ms
   AICD  ████████████████░░░░░░░░░     5416 tok   █████████████████████████     4.40 ms
   AID   ███████████████████░░░░░░     6488 tok   ████████████████████████░     4.29 ms
   TOON  █████████████████████████     8198 tok   █████████████░░░░░░░░░░░░     2.36 ms


   FORMAT     TOKENS       TIME (Total)    AVG TIME/FILE   VS JSON
   ----------------------------------------------------------------------
   AICD       5416             4.40 ms        0.37 ms    -21.7%
   AID        6488             4.29 ms        0.36 ms    -6.3%
   JSON       6921             0.15 ms        0.01 ms    +0.0%
   TOON       8198             2.36 ms        0.20 ms    +18.5%


CONCLUSION: Switching to AICD saves 1505 tokens (21.7%) compared to JSON.
```

---

## 🛠 CLI Usage

The package comes with a powerful CLI tool `aid` for encoding, decoding, and benchmarking.

```text
   Arkadia AI DATA TOOL
   --------------------------------------------------
   Unified interface for AI Data Format operations.

USAGE:
   aid <command> [flags]

COMMANDS:
   enc             [ENCODE] Convert JSON/YAML/TOON to AI.Data format
   dec             [DECODE] Parse AI.Data format back to JSON
   benchmark       [BENCHMARK] Run performance and token usage tests
   ai-benchmark    [AI] Run AI understanding tests (not implemented yet)

GLOBAL OPTIONS:
   -h, --help       Show this help message
   -v, --version    Show version info

```

---

## 📖 Syntax Specification (Current Version)

This section describes the **actual, currently implemented** syntax of AI.DATA-FORMAT.

### 1. Type Definition

A type defines a name and an ordered list of fields. Comments are allowed within the definition to assist the LLM.

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

**Key Rules:**

* The type name (`@Name`) is optional but recommended.
* The header `<...>` defines field names and their order.
* Comments (`/ ... /`) are **allowed** in the header.

### 2. Data Structures

The format supports compact positional records and explicit named records.

| Structure | Syntax | Description |
| --- | --- | --- |
| **Positional Record** | `(a,b,c)` | Must follow the exact order of fields in the type header. |
| **Named Record** | `{key:value}` | Keys must match field names. No spaces allowed in keys/values. |
| **List** | `[ ... ]` | Contains positional or named records. |
| **Multiline Text** | ``text`` | Ends with a line containing only a backtick. |

### 3. Comments

```aid
/ this is a comment /

```

* Allowed **only** inside type definitions.
* Forbidden in raw data blocks to save space.

### 4. General Rules

1. **Data must contain NO spaces.** (Compactness is priority).
2. Schema/Type definitions **may** contain spaces and comments.
3. Named fields always use `key:value` without spaces.
4. Positional order must exactly match the declared order.

### 5. Inline Type Usage

You can declare a type and immediately use it:

```aid
@User<id:number name:string desc:string>

value:@User(2,"Alice","Hello")
value2:@User(3,"Bob","World")

```

### 6. Nested Types

Currently, nested types are allowed as structural definitions:

```aid
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

---

## 🔮 Futures / Roadmap

The following features are planned for future releases and are **not yet implemented**.

* **Modifiers:**
* `!required` - field must be included.
* `?empty` - field must not be empty.
* `=value` - default value.
* `N..M` - numeric range validation.


* **Binary Data Types:**
* Hex: `~[hex]1A0F4F~`
* Base64: `~[b64]ADFKDXKZK...~`


* **Pointers/References:**
* Reference existing objects by ID: `(1, "Alex", *User[2])`


## 📄 License

This project is licensed under the [MIT License].

---

<div align="center">
<sub>Built by <strong>Arkadia AI</strong>. Engineering the kernel of distributed intelligence.</sub>
</div>
