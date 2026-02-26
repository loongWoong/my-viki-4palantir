# [](#types-reference)Types reference类型参考


In order to be published to the registry, a TypeScript function must have explicit type annotations on all input parameters and specify an explicit return type. Below is the full list of currently supported function registry types and their corresponding language types.为了发布到注册表中，TypeScript 函数必须在所有输入参数上具有明确的类型注解，并指定明确的返回类型。以下是当前支持的函数注册表类型及其对应的语言类型列表。



































































































































































































































































| Function registry type函数注册表类型 | TypeScript v1 typeTypeScript v1 类型 | TypeScript v2 typeTypeScript v2 类型 | Python typePython 类型 |  |
| --- | --- | --- | --- | --- |
| Attachment附件 | `Attachment` | `Attachment` | `Attachment` | [Example](#attachment) |
| Boolean布尔值 | `boolean` | `boolean` | `bool` | [Example](#boolean) |
| Binary二进制 | Not supported不支持 | Not supported不支持 | `bytes` | [Example](#binary) |
| Byte字节 | Not supported不支持 | Not supported不支持 | `int*` | [Example](#byte) |
| Classification marking分类标记 | `ClassificationMarking` | `ClassificationMarking` | Not supported不支持 | [Example](#classification-marking) |
| Date日期 | `LocalDate` | `DateISOString` | `datetime.date` | [Example](#date) |
| Decimal十进制 | Not supported不支持 | Not supported不支持 | `decimal.Decimal` | [Example](#decimal) |
| Double双倍 | `Double` | `Double` | `float*` | [Example](#double) |
| Float单精度浮点数 | `Float` | `Float` | `float` | [Example](#float) |
| GeoPoint | `GeoPoint` | `Point` | `GeoPoint` | [Example](#geopoint) |
| GeoShape | `GeoShape` | `Geometry` | `GeoShape` | [Example](#geoshape) |
| Group | `Group` | `GroupId` | `GroupId` | [Example](#group) |
| Integer整数 | `Integer` | `Integer` | `int` | [Example](#integer) |
| Interface | Not supported不支持 | `Osdk.Instance<MyInterface>` | Not supported不支持 | [Example](#interface) |
| Interface object set接口对象集 | Not supported不支持 | `ObjectSet<MyInterface>` | Not supported不支持 | [Example](#interface-object-set) |
| List列表 | `T[]` or `Array<T>`T[] 或 Array<T> | `T[]` or `Array<T>`T[] 或 Array<T> | `list[T]` | [Example](#list) |
| Long长整型 | `Long` | `Long` | `int*` | [Example](#long) |
| Mandatory marking强制标记 | `MandatoryMarking` | `MandatoryMarking` | Not supported不支持 | [Example](#mandatory-marking) |
| Map地图 | `FunctionsMap<K, V>` | `Record<K, V>` | `dict[K, V]` | [Example](#map) |
| Media reference媒体引用 | `MediaItem` | Not supported不支持 | Not supported不支持 | [Example](#media-references) |
| Notification通知 | `Notification` | `Notification` | `Notification` | [Example](#notification) |
| Object对象 | `MyObjectType` | `Osdk.Instance<MyObjectType>` | `MyObjectType` | [Example](#object) |
| Object set对象集 | `ObjectSet<MyObjectType>` | `ObjectSet<MyObjectType>` | `MyObjectTypeObjectSet` | [Example](#object-set) |
| Ontology edit本体编辑 | `void` | `Edits` | `OntologyEdit` | [Example](#ontology-edit) |
| Optional可选 | `T | undefined` | `T | undefined` | `typing.Optional` or `T | None`typing.Optional 或 T | None | [Example](#optional) |
| Principal主要 | `Principal` | `Principal` | `Principal` | [Example](#principal) |
| Range范围 | `IRange<T>` | `Range<T>` | `Range[T]` | [Example](#range) |
| Set集合 | `Set<T>` | Not supported不支持 | `set[T]` | [Example](#set) |
| Short短 | Not supported不支持 | Not supported不支持 | `int*` | [Example](#short) |
| String字符串 | `string` | `string` | `str` | [Example](#string) |
| Struct/custom type结构/自定义类型 | `interface` | `interface` | `dataclasses.dataclass` | [Example](#structcustom-type) |
| Timestamp时间戳 | `Timestamp` | `TimestampISOString` | `datetime.datetime` | [Example](#timestamp) |
| Two-dimensional aggregation二维聚合 | `TwoDimensionalAggregation<K, V>` | `TwoDimensionalAggregation<K, V>` | `TwoDimensionalAggregation[K, V]` | [Example](#two-dimensional-aggregation) |
| Three-dimensional aggregation三维聚合 | `ThreeDimensionalAggregation<K, S, V>` | `ThreeDimensionalAggregation<K, S, V>` | `ThreeDimensionalAggregation[K, S, V]` | [Example](#three-dimensional-aggregation) |
| User用户 | `User` | `UserId` | `UserId` | [Example](#user) |


Although both `Integer` and `Long` correspond to the Python type `int`, any fields marked as `int` directly in your function signature will be registered with type `Integer`. Therefore, we instead recommend using either the `Integer` or `Long` types from the API to register numerical data types. Similar guidelines apply to `Float` and `Double`; if  the Python type `float` is directly in your function signature, it will be registered as `Float` by default.尽管 Integer 和 Long 都对应 Python 类型 int ，但如果在函数签名中直接标记为 int ，则会注册为类型 Integer 。因此，我们建议使用 API 中的 Integer 或 Long 类型来注册数值数据类型。对于 Float 和 Double 也适用相同的规则；如果 Python 类型 float 直接出现在函数签名中，它将默认注册为 Float 。


## [](#scalar-types)Scalar types标量类型


Scalar types represent a single value and are commonly used to hold textual, numeric, or temporal data.标量类型表示单个值，通常用于存储文本、数值或时间数据。


In JavaScript and TypeScript, there is one `number` type that is commonly used to represent both integer and floating-point values. In order to provide further type validation and structure, we only support the numeric aliases exported from the `@foundry/functions-api` package for TypeScript v1 functions and the `@osdk/functions` package for TypeScript v2 functions. Similarly, when working with numeric types in Python functions we recommend using the type aliases exported from the `functions.api` module.在 JavaScript 和 TypeScript 中，有一个 number 类型通常用于表示整数和浮点数。为了提供进一步的类型验证和结构，我们仅支持从 @foundry/functions-api 包中导出的数值别名，用于 TypeScript v1 函数，以及从 @osdk/functions 包中导出的数值别名，用于 TypeScript v2 函数。同样，在 Python 函数中使用数值类型时，我们建议使用从 functions.api 模块中导出的类型别名。


### [](#boolean)Boolean布尔值


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public isEven(num: Integer): boolean {
6        return num % 2 === 0;
7    }
8}`
```

```
Copied!`1import { Integer } from "@osdk/functions";
2
3function isEven(num: Integer): boolean {
4    return num % 2 === 0;
5}
6
7export default isEven;`
```

```
Copied!`1from functions.api import function, Integer
2
3@function
4def is_even(num: Integer) -> bool:
5    return n % 2 == 0`
```


### [](#string)String字符串


TypeScript v1TypeScript v2Python```
Copied!`1import { Function } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public greet(name: string): string {
6        return `Hello, ${name}!`;
7    }
8}`
```

```
Copied!`1function greet(name: string): string {
2    return `Hello, ${name}!`;
3}
4
5export default greet;`
```

```
Copied!`1from functions.api import function
2
3@function
4def greet(name: str) -> str:
5    return f"Hello, {name}!"`
```


### [](#short)Short


Represents integer values from -32,768 to 32,767.表示从-32,768 到 32,767 的整数值。


In Python functions, the `Short` type is an alias for the built-in `int` type.在 Python 函数中， Short 类型是内置 int 类型的别名。


Python```
Copied!`1from functions.api import function, Short
2
3@function
4def increment(num: Short) -> Short:
5    return num + 1`
```


### [](#integer)Integer整数


Represents integer values from (-231) to (231 - 1).表示从 (-2 31 ) 到 (2 31 - 1) 的整数值。


- In both TypeScript v1 and v2 functions, the `Integer` type is an alias for the built-in `number` type.在 TypeScript v1 和 v2 函数中， Integer 类型是内置 number 类型的别名。
- In Python functions, the `Integer` type is an alias for the built-in `int` type.在 Python 函数中， Integer 类型是内置 int 类型的别名。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public sum(a: Integer, b: Integer): Integer {
6        return a + b;
7    }
8}`
```

```
Copied!`1import { Integer } from "@osdk/functions";
2
3function sum(a: Integer, b: Integer): Integer {
4    return a + b;
5}
6
7export default sum;`
```

```
Copied!`1from functions.api import function, Integer
2
3@function
4def sum(a: Integer, b: Integer) -> Integer:
5    return a + b`
```


### [](#long)Long长


Represents integer values from -(253 - 1) to (253 - 1). These bounds are equivalent to `Number.MIN_SAFE_INTEGER` and `Number.MAX_SAFE_INTEGER` in JavaScript to prevent precision loss when functions are called from browser contexts.表示从 -(2 53 - 1) 到 (2 53 - 1) 的整数值。这些边界与 JavaScript 中的 Number.MIN_SAFE_INTEGER 和 Number.MAX_SAFE_INTEGER 相当，以防止从浏览器上下文中调用函数时精度损失。


- In TypeScript v1 functions, the `Long` type is an alias for the built-in `number` type. In TypeScript v2 functions, the `Long` type is an alias for the built-in `string` type.在 TypeScript v1 函数中， Long 类型是内置 number 类型的别名。在 TypeScript v2 函数中， Long 类型是内置 string 类型的别名。
- In Python functions, the `Long` type is an alias for the built-in `int` type.在 Python 函数中， Long 类型是内置 int 类型的别名。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Long } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public subtract(a: Long, b: Long): string {
6        return (BigInt(a) - BigInt(b)).toString();
7    }
8}`
```

```
Copied!`1import { Long } from "@osdk/functions";
2
3function subtract(a: Long, b: Long): string {
4    return (BigInt(a) - BigInt(b)).toString();
5}
6
7export default subtract;`
```

```
Copied!`1from functions.api import function, Long
2
3@function
4def subtract(a: Long, b: Long) -> str:
5    return str(a - b)`
```


### [](#float)Float浮点数


Represents a 32-bit floating-point number.表示一个 32 位浮点数。


- In both TypeScript v1 and v2 functions, the `Float` type is an alias for the built-in `number` type.在 TypeScript v1 和 v2 函数中， Float 类型是内置 number 类型的别名。
- In Python functions, the `Float` type is an alias for the built-in `float` type.在 Python 函数中， Float 类型是内置 float 类型的别名。


TypeScript v1TypeScript v2Python```
Copied!`1import { Float, Function } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public multiply(a: Float, b: Float): Float {
6        return a * b;
7    }
8}`
```

```
Copied!`1import { Float } from "@osdk/functions";
2
3function multiply(a: Float, b: Float): Float {
4    return a * b;
5}
6
7export default multiply;`
```

```
Copied!`1from functions.api import function, Float
2
3@function
4def multiply(a: Float, b: Float) -> Float:
5    return a * b`
```


### [](#double)Double双倍


Represents a 64-bit floating-point number.表示一个 64 位浮点数。


- In both TypeScript v1 and v2 functions, the `Double` type is an alias for the built-in `number` type.在 TypeScript v1 和 v2 函数中， Double 类型是内置 number 类型的别名。
- In Python functions, the `Double` type is an alias for the built-in `float` type.在 Python 函数中， Double 类型是内置 float 类型的别名。


TypeScript v1TypeScript v2Python```
Copied!`1import { Double, Function } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public divide(a: Double, b: Double): Double {
6        return a / b;
7    }
8}`
```

```
Copied!`1import { Double } from "@osdk/functions";
2
3function divide(a: Double, b: Double): Double {
4    return a / b;
5}
6
7export default divide;`
```

```
Copied!`1from functions.api import function, Double
2
3@function
4def divide(a: Double, b: Double) -> Double:
5    return a / b`
```


### [](#decimal)Decimal十进制


Python```
Copied!`1from decimal import Decimal
2from functions.api import function
3
4@function
5def return_pi() -> Decimal:
6    return Decimal('3.1415926535')`
```


### [](#date)Date日期


Represents a calendar date.表示日历日期。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, LocalDate } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public returnDate(): LocalDate {
6        return LocalDate.fromISOString("1999-10-17");
7    }
8}`
```

```
Copied!`1import { DateISOString } from "@osdk/functions";
2
3function returnDate(): DateISOString {
4    return "1999-10-17";
5}
6
7export default returnDate;`
```

```
Copied!`1from datetime import date
2from functions.api import function, Date
3
4@function
5def return_date() -> Date:
6    return date.fromisoformat('1999-10-17')`
```


### [](#timestamp)Timestamp时间戳


Represents an instant in time.表示一个时间点。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Timestamp } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getCurrentTimestamp(): Timestamp {
6        return Timestamp.now();
7    }
8}`
```

```
Copied!`1import { TimestampISOString } from "@osdk/functions";
2
3function getCurrentTimestamp(): TimestampISOString {
4    const now = new Date();
5    return now.toISOString();
6}
7
8export default getCurrentTimestamp;`
```

```
Copied!`1from datetime import datetime
2from functions.api import function, Timestamp
3
4@function
5def get_current_timestamp() -> Timestamp:
6    return datetime.now()`
```


### [](#binary)Binary二进制


In Python functions, the `Binary` type is an alias for the built-in `bytes` type.在 Python 函数中， Binary 类型是内置 bytes 类型的别名。


Python```
Copied!`1from functions.api import function
2
3@function
4def encode_utf8(param: str) -> bytes:
5    return param.encode('utf-8')`
```


### [](#byte)Byte字节


In Python functions, the `Byte` type is an alias for the built-in `int` type.在 Python 函数中， Byte 类型是内置 int 类型的别名。


Python```
Copied!`1from functions.api import function, Byte
2
3@function
4def get_first_byte(param: str) -> Byte:
5    if len(param) == 0:
6        raise Exception("String length cannot be zero.")
7    return param.encode('utf-8')[0]`
```


### [](#mandatory-marking)Mandatory marking强制标记


Markings are mandatory controls that restrict access by requiring a user to have a particular marking in order to access data.标记是强制性的控制措施，通过要求用户必须拥有特定标记才能访问数据来限制访问。


TypeScript v1TypeScript v2```
Copied!`1import { OntologyEditFunction, MandatoryMarking } from "@foundry/functions-api";
2import { Employee, Objects } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Edits(Employee)
6    @OntologyEditFunction()
7    public async editMandatoryMarkings(markings: MandatoryMarking[]): Promise<void> {
8        const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
9        employeeOne.markingsProperty = markings;
10    }
11}`
```

```
Copied!`1import { Client } from "@osdk/client";
2import { Employee } from "@ontology/sdk";
3import { Edits, createEditBatch, MandatoryMarking } from "@osdk/functions";
4
5type OntologyEdit = Edits.Object<Employee>;
6
7function editMandatoryMarkings(markings: MandatoryMarking[]): OntologyEdit[] {
8    const batch = createEditBatch<OntologyEdit>(client);
9
10    const employeeOne = await client(Employee).fetchOne(1);
11    batch.update(employeeOne, { markingsProperty: markings });
12
13    return batch.getEdits();
14}
15
16export default editMandatoryMarkings;`
```


### [](#classification-marking)Classification marking分类标记


Classification-based access controls (CBAC) are mandatory controls used to protect sensitive government information. They restrict access by requiring a user to have a particular classification marking in order to access information.基于分类的访问控制（CBAC）是用于保护敏感政府信息的强制性控制措施。它们通过要求用户必须具有特定的分类标记才能访问信息来限制访问。


TypeScript v1TypeScript v2```
Copied!`1import { OntologyEditFunction, ClassificationMarking } from "@foundry/functions-api";
2import { Employee, Objects } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Edits(Employee)
6    @OntologyEditFunction()
7    public async editClassificationMarkings(markings: ClassificationMarking[]): Promise<void> {
8        const employeeOne = Objects.search().employee().filter(e => e.id.exactMatch(1)).all()[0];
9        employeeOne.markingsProperty = markings;
10    }
11}`
```

```
Copied!`1import { Client } from "@osdk/client";
2import { Employee } from "@ontology/sdk";
3import { Edits, createEditBatch, ClassificationMarking } from "@osdk/functions";
4
5type OntologyEdit = Edits.Object<Employee>;
6
7function editClassificationMarkings(markings: ClassificationMarking[]): OntologyEdit[] {
8    const batch = createEditBatch<OntologyEdit>(client);
9
10    const employeeOne = await client(Employee).fetchOne(1);
11    batch.update(employeeOne, { markingsProperty: markings });
12
13    return batch.getEdits();
14}
15
16export default editClassificationMarkings;`
```


## [](#collection-types)Collection types集合类型


Collection types are parameterized by other types. For example, Array[String] is a list of strings and Map[String, Integer] is a dictionary with string keys and integer values. The parameterized types must be specified, and the type must be another supported type. Map keys can only be scalar types or an Ontology object type.集合类型由其他类型参数化。例如，Array[String] 是一个字符串列表，而 Map[String, Integer] 是一个具有字符串键和整数值的字典。参数化类型必须指定，并且类型必须是另一个支持类型。Map 键只能是标量类型或 Ontology 对象类型。


### [](#list)List列表


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public filterForEvenIntegers(nums: Integer[]): Integer[] {
6        return nums.filter(num => num % 2 === 0);
7    }
8}`
```

```
Copied!`1import { Integer } from "@osdk/functions";
2
3function filterForEvenIntegers(nums: Integer[]): Integer[] {
4    return nums.filter(num => num % 2 === 0);
5}
6
7export default filterForEvenIntegers;`
```

```
Copied!`1from functions.api import function, Integer
2
3@function
4def filter_for_even_integers(nums: list[Integer]) -> list[Integer]:
5    return [n for n in nums if n % 2 == 0]`
```


### [](#map)Map映射


Maps are commonly used to key by a scalar type and access an associated value that can be of any other function registry type.映射通常用于通过标量类型作为键来访问一个关联值，该关联值可以是任何其他函数注册类型。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, FunctionsMap } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getMap(): FunctionsMap<string, string> {
6        const myMap = new FunctionsMap<string, string>();
7
8        myMap.set("Name", "Phil");
9        myMap.set("Favorite Color", "Blue");
10
11        return myMap;
12    }
13}`
```

```
Copied!`1function getMap(): Record<string, string> {
2    const myMap: Record<string, string> = {};
3
4    myMap["Name"] = "Phil";
5    myMap["Favorite Color"] = "Blue";
6
7    return myMap;
8}
9
10export default getMap;`
```

```
Copied!`1from functions.api import function
2
3@function
4def get_map() -> dict[str, str]:
5    my_map = {}
6
7    my_map["Name"] = "Phil"
8    my_map["Favorite Color"] = "Blue"
9
10    return my_map`
```


Additionally, maps support Ontology objects as keys.此外，地图还支持本体对象作为键。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, FunctionsMap } from "@foundry/functions-api";
2import { Airplane } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Function()
6    public getObjectMap(aircraft: Airplane[]): FunctionsMap<Airplane, Integer | undefined> {
7        const myMap = new FunctionsMap<Airplane, Integer | undefined>();
8
9        aircraft.forEach(obj => {
10            myMap.set(obj, obj.capacity);
11        });
12
13        return myMap;
14    }
15}`
```

```
Copied!`1import { ObjectSpecifier, Osdk } from "@osdk/client";
2import { Integer } from "@osdk/functions";
3import { Airplane } from "@ontology/sdk";
4
5function getObjectMap(aircraft: Osdk.Instance<Airplane>[]): Record<ObjectSpecifier<Airplane>, Integer | undefined> {
6    const myMap: Record<ObjectSpecifier<Airplane>, Integer | undefined> = {};
7
8    aircraft.forEach(obj => {
9        myMap[obj.$objectSpecifier] = obj.capacity;
10    });
11
12    return myMap;
13}
14
15export default getObjectMap;`
```

```
Copied!`1from functions.api import function, Integer
2from ontology_sdk.ontology.objects import Airplane
3
4@function
5def get_object_map(aircraft: list[Airplane]) -> dict[Airplane, Integer | None]:
6    my_map = {}
7
8    for a in aircraft:
9        my_map[a] = a.capacity
10
11    return my_map`
```


### [](#set)Set设置


TypeScript v1Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getSizeOfSet(mySet: Set<Integer>): Integer {
6        return mySet.size;
7    }
8}`
```

```
Copied!`1from functions.api import function, Integer
2
3@function
4def get_size_of_set(my_set: set[Integer]) -> Integer:
5    return len(my_set)`
```


### [](#optional)Optional可选


- In TypeScript functions, optional parameters are declared as `varName?: T` or `varName: T | undefined`. For example, a function that has an optional integer parameter named `value` could be declared as either `value?: Integer` or `value: Integer | undefined`. TypeScript functions can also declare an optional return type by specifying a type of `T | undefined`. For example, a function that may return either an `Integer` or no value would have a return type of `Integer | undefined`.在 TypeScript 函数中，可选参数声明为 varName?: T 或 varName: T | undefined 。例如，一个具有名为 value 的可选整数参数的函数可以声明为 value?: Integer 或 value: Integer | undefined 。TypeScript 函数还可以通过指定类型为 T | undefined 来声明可选的返回类型。例如，一个可能返回 Integer 或无值的函数将具有返回类型 Integer | undefined 。
- In Python functions, optional parameters and return values can be declared using `typing.Optional[T]` or `T | None`. The `T | None` syntax requires Python 3.10 or greater.在 Python 函数中，可选参数和返回值可以使用 typing.Optional[T] 或 T | None 声明。 T | None 语法需要 Python 3.10 或更高版本。
- In both TypeScript and Python functions, the parameterized type `T` must be specified, and it must be another supported type.在 TypeScript 和 Python 函数中，参数化类型 T 必须指定，并且必须是另一个受支持类型。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function } from "@foundry/functions-api";
2
3export class MyFunction {
4    @Function()
5    public greet(name?: string): string | undefined {
6        if (name === undefined) {
7            return undefined;
8        }
9        return `Hello, ${name}!`;
10    }
11}`
```

```
Copied!`1function greet(name?: string): string | undefined {
2    if (name === undefined) {
3        return undefined;
4    }
5    return `Hello, ${name}!`;
6}
7
8export default greet;`
```

```
Copied!`1from functions.api import function
2
3@function
4def greet(name: str | None) -> str | None:
5    if name is None:
6        return None
7    return f"Hello, {name}!"`
```


Functions also support default values in the function signature.函数在函数签名中也支持默认值。


TypeScript v1TypeScript v2Python```
Copied!`1import { Double, Function } from "@foundry/functions-api";
2import { Customer } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Function()
6    public computeRiskFactor(customer: Customer, weight: Double = 0.75): Double {
7        // ...
8    }
9}`
```

```
Copied!`1import { Double } from "@osdk/functions";
2import { Osdk } from "@osdk/client";
3import { Customer } from "@ontology/sdk";
4
5function computeRiskFactor(customer: Osdk.Instance<Customer>, weight: Double = 0.75): Double {
6    // ...
7}
8
9export default computeRiskFactor;`
```

```
Copied!`1from functions.api import function, Double
2from ontology_sdk.ontology.objects import Customer
3
4@function
5def compute_risk_factor(customer: Customer, weight: Double = 0.75) -> Double:
6    # ...`
```


### [](#structcustom-type)Struct/custom type结构/自定义类型


Custom types are composed of other supported types (including other custom types) and can be used in function signatures.自定义类型由其他支持类型（包括其他自定义类型）组成，并可用于函数签名。


- In TypeScript functions, custom types are user-defined TypeScript interfaces using the `interface` keyword.在 TypeScript 函数中，自定义类型是使用 interface 关键字定义的用户自定义 TypeScript 接口。


- Optional fields are supported through either the `?` optional token or a union with `undefined`.可选字段通过 ? 可选标记或与 undefined 的联合来支持。
  - Optional fields are supported through either the `?` optional token or a union with `undefined`.可选字段通过 ? 可选标记或与 undefined 的联合来支持。
  
  - In Python functions, custom types are user-defined Python classes.在 Python 函数中，自定义类型是用户定义的 Python 类。


- To be a valid custom type, the class must adhere to the following:
要成为有效的自定义类型，类必须遵循以下规则：- The class must have type annotations on all of its fields.类的所有字段都必须有类型注解。
- The field types must be supported types; either the primitive API types or native Python types (as defined in the table above) may be used.字段类型必须是支持的类型；可以使用原始 API 类型或原生 Python 类型（如上表所定义）。
- The `__init__` method must accept only named arguments with the same names and type annotations as the fields.__init__ 方法必须只接受与字段同名且类型注解相同的命名参数。
  - The class must have type annotations on all of its fields.类的所有字段都必须有类型注解。
  - The field types must be supported types; either the primitive API types or native Python types (as defined in the table above) may be used.字段类型必须是支持的类型；可以使用原始 API 类型或原生 Python 类型（如上表所定义）。
  - The `__init__` method must accept only named arguments with the same names and type annotations as the fields.__init__ 方法必须只接受与字段同名且类型注解相同的命名参数。
  
  - The [`dataclasses.dataclass` ↗](https://docs.python.org/3/library/dataclasses.html) decorator can be used to automatically generate an `__init__` method that conforms with these requirements.dataclasses.dataclass ↗ 装饰器可用于自动生成符合这些要求的 __init__ 方法。
  - To be a valid custom type, the class must adhere to the following:
  要成为有效的自定义类型，类必须遵循以下规则：- The class must have type annotations on all of its fields.类的所有字段都必须有类型注解。
  - The field types must be supported types; either the primitive API types or native Python types (as defined in the table above) may be used.字段类型必须是支持的类型；可以使用原始 API 类型或原生 Python 类型（如上表所定义）。
  - The `__init__` method must accept only named arguments with the same names and type annotations as the fields.__init__ 方法必须只接受与字段同名且类型注解相同的命名参数。
    - The class must have type annotations on all of its fields.类的所有字段都必须有类型注解。
    - The field types must be supported types; either the primitive API types or native Python types (as defined in the table above) may be used.字段类型必须是支持的类型；可以使用原始 API 类型或原生 Python 类型（如上表所定义）。
    - The `__init__` method must accept only named arguments with the same names and type annotations as the fields.__init__ 方法必须只接受与字段同名且类型注解相同的命名参数。
    
    - The [`dataclasses.dataclass` ↗](https://docs.python.org/3/library/dataclasses.html) decorator can be used to automatically generate an `__init__` method that conforms with these requirements.dataclasses.dataclass ↗ 装饰器可用于自动生成符合这些要求的 __init__ 方法。
  
  

TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2import { Passenger } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Function()
6    public getPassengerInfo(passenger: Passenger): PassengerInfo {
7        return {
8            name: passenger.name,
9            age: passenger.age,
10        };
11    }
12}`
```

```
Copied!`1import { Osdk } from "@osdk/client";
2import { Integer } from "@osdk/functions";
3import { Passenger } from "@ontology/sdk";
4
5interface PassengerInfo {
6    name?: string;
7    age?: Integer;
8}
9
10function getPassengerInfo(passenger: Osdk.Instance<Passenger>): PassengerInfo {
11    return {
12        name: passenger.name,
13        age: passenger.age,
14    };
15}
16
17export default getPassengerInfo;`
```

```
Copied!`1from dataclasses import dataclass
2from functions.api import function, Integer
3from ontology_sdk.ontology.objects import Passenger
4
5@dataclass
6class PassengerInfo:
7    name: str | None
8    age: Integer | None
9
10@function
11def get_passenger_info(passenger) -> PassengerInfo:
12    return PassengerInfo(
13        name=passenger.name,
14        age=passenger.age
15    )`
```


## [](#aggregation-types)Aggregation types聚合类型


Aggregation types can be returned from functions for use in other parts of the platform, such as Charts in [Workshop](/docs/foundry/workshop/overview/).聚合类型可以从函数中返回，用于平台的其他部分，例如 Workshop 中的图表。


There are two supported aggregation types:有两种支持的聚合类型：


- A [two-dimensional aggregation](#two-dimensional-aggregation) maps from a single bucket key to a numeric value. For example, this could be used to represent an aggregation such as a count of employees with a specific job title.一个二维聚合从单个桶键映射到一个数值。例如，这可以用来表示一个聚合，比如具有特定职位的员工数量。
- A [three-dimensional aggregation](#three-dimensional-aggregation) maps from two bucket keys to a numeric value. This could be used to represent an aggregation such as a count of employees by each employee's job title and home office.一个三维聚合从两个桶键映射到一个数值。这可以用来表示一个聚合，比如按每位员工的职位和总部办公室统计的员工数量。


Aggregations can be keyed by several types:聚合可以按多种类型进行键控：


- [Boolean](#boolean) buckets represent values that are either `true` or `false`.布尔桶表示值为 true 或 false 的值。
- [String](#string) buckets can be used to represent categorical values.字符串桶可用于表示分类值。
- [Range](#range) buckets represent aggregations where the bucket key is a range of values. These can be used to represent a histogram or date axis in a chart.
范围桶表示聚合，其中桶键是一组值。这些可用于在图表中表示直方图或日期轴。- Numeric ranges, including [Integer](#integer) and [Double](#double), represent bucketed aggregations on numeric values.数值范围，包括整数和双精度浮点数，表示对数值的分组聚合。
- Date and time ranges, including on [Date](#date) and [Timestamp](#timestamp), represent bucketed aggregations on date ranges.日期和时间范围，包括日期和时间戳，表示对日期范围的分组聚合。
  - Numeric ranges, including [Integer](#integer) and [Double](#double), represent bucketed aggregations on numeric values.数值范围，包括整数和双精度浮点数，表示对数值的分组聚合。
  - Date and time ranges, including on [Date](#date) and [Timestamp](#timestamp), represent bucketed aggregations on date ranges.日期和时间范围，包括日期和时间戳，表示对日期范围的分组聚合。
  
  

### [](#range)Range范围


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer, IRange } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getRange(min: Integer, max: Integer): IRange<Integer> {
6        return {
7            min,
8            max,
9        };
10    }
11}`
```

```
Copied!`1import { Integer, Range } from "@osdk/functions";
2
3function getRange(min: Integer, max: Integer): Range<Integer> {
4    return {
5        min,
6        max,
7    };
8}
9
10export default getRange;`
```

```
Copied!`1from functions.api import function, Integer, Range
2
3@function
4def get_range(min: Integer, max: Integer) -> Range[Integer]:
5    return Range(
6        min=min,
7        max=max
8    )`
```


### [](#two-dimensional-aggregation)Two-dimensional aggregation二维聚合


TypeScript v1TypeScript v2Python```
Copied!`1import { Double, Function, TwoDimensionalAggregation } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public myTwoDimensionalAggregation(): TwoDimensionalAggregation<string, Double> {
6        return {
7            buckets: [
8                { key: "bucket1", value: 5.0 },
9                { key: "bucket2", value: 6.0 },
10            ],
11        };
12    }
13}`
```

```
Copied!`1import { Double, TwoDimensionalAggregation } from "@osdk/functions";
2
3function myTwoDimensionalAggregationFunction(): TwoDimensionalAggregation<string, Double> {
4    return [
5        { key: "bucket1", value: 5.0 },
6        { key: "bucket2", value: 6.0 },
7    ];
8}
9
10export default myTwoDimensionalAggregationFunction;`
```

```
Copied!`1from functions.api import (
2    function,
3    Double,
4    TwoDimensionalAggregation,
5    SingleBucket
6)
7
8@function
9def my_two_dimensional_aggregation_function() -> TwoDimensionalAggregation[str, Double]:
10    return TwoDimensionalAggregation(
11        buckets=[
12            SingleBucket(key="bucket1", value=Double(5.0)),
13            SingleBucket(key="bucket2", value=Double(6.0)),
14        ]
15    )`
```


### [](#three-dimensional-aggregation)Three-dimensional aggregation三维聚合


TypeScript v1TypeScript v2Python```
Copied!`1import { Double, Function, ThreeDimensionalAggregation } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public myThreeDimensionalAggregation(): ThreeDimensionalAggregation<string, string, Double> {
6        return {
7            buckets: [
8                {
9                    key: "group-by-1",
10                    value: [
11                        { key: "partition-by-1", value: 5.0 },
12                        { key: "partition-by-2", value: 6.0 },
13                    ],
14                },
15                {
16                    key: "group-by-2",
17                    value: [
18                        { key: "partition-by-1", value: 7.0 },
19                        { key: "partition-by-2", value: 8.0 },
20                    ],
21                },
22            ]
23        };
24    }
25}`
```

```
Copied!`1import { Double, ThreeDimensionalAggregation } from "@osdk/functions";
2
3function myThreeDimensionalAggregation(): ThreeDimensionalAggregation<string, string, Double> {
4    return [
5        {
6            key: "group-by-1",
7            value: [
8                { key: "partition-by-1", value: 5.0 },
9                { key: "partition-by-2", value: 6.0 },
10            ],
11        },
12        {
13            key: "group-by-2",
14            value: [
15                { key: "partition-by-1", value: 7.0 },
16                { key: "partition-by-2", value: 8.0 },
17            ],
18        },
19    ];
20}
21
22export default myThreeDimensionalAggregation;`
```

```
Copied!`1from functions.api import (
2    function,
3    Double,
4    ThreeDimensionalAggregation,
5    SingleBucket,
6    NestedBucket,
7)
8
9@function
10def my_three_dimensional_aggregation_function() -> (
11    ThreeDimensionalAggregation[str, str, Double]
12):
13    return ThreeDimensionalAggregation(
14        buckets=[
15            NestedBucket(key="group-by-1", buckets=[
16                SingleBucket(key="partition-by-1", value=Double(5.0)),
17                SingleBucket(key="partition-by-2", value=Double(6.0)),
18            ]),
19            NestedBucket(key="group-by-2", buckets=[
20                SingleBucket(key="partition-by-1", value=Double(7.0)),
21                SingleBucket(key="partition-by-2", value=Double(8.0)),
22            ])
23        ]
24    )`
```


## [](#ontology-types)Ontology types本体类型


Ontology imports本体导入Object types must be imported into your repository to use them in function signatures. [Learn more about Ontology imports.](/docs/foundry/functions/ontology-imports/)对象类型必须导入到您的存储库中，才能在函数签名中使用。了解更多关于本体导入的信息。


### [](#object)Object对象


Object types from your ontology can be used as both inputs and outputs in your function signature. To either accept or return a single instance of an object type, import the object type from your Ontology SDK and use that type to annotate your function.您本体的对象类型可以用作函数签名中的输入和输出。要接受或返回单个对象类型的实例，请从您的本体 SDK 导入对象类型，并使用该类型来标注您的函数。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Integer } from "@foundry/functions-api";
2import { Airplane } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Function()
6    public getCapacity(airplane: Airplane): Integer {
7        return airplane.capacity;
8    }
9}`
```

```
Copied!`1import { Osdk } from "@osdk/client";
2import { Integer } from "@osdk/functions";
3import { Airplane } from "@ontology/sdk";
4
5function getCapacity(airplane: Osdk.Instance<Airplane>): Integer {
6    return airplane.capacity;
7}
8
9export default getCapacity;`
```

```
Copied!`1from functions.api import function, Integer
2from ontology_sdk.ontology.objects import Airplane
3
4@function
5def get_capacity(airplane: Airplane) -> Integer:
6    return airplane.capacity`
```


In TypeScript v2, references to object types are supported as [struct](#structcustom-type) parameter fields. To accept a struct or struct list with object type instances, create a custom type input with an object type field from your Ontology SDK. This can be paired with [Ontology Edits](#ontology-edit) to support workflows such as creating multiple instances of an object type derived from other object types.在 TypeScript v2 中，对象类型的引用被支持为结构参数字段。要接受具有对象类型实例的结构或结构列表，请使用您的 Ontology SDK 创建一个具有对象类型字段的自定义类型输入。这可以与 Ontology Edits 配合使用，以支持创建从其他对象类型派生的对象类型的多个实例等工作流程。


TypeScript v2```
Copied!`1import { Osdk } from "@osdk/client";
2import { Integer } from "@osdk/functions";
3import { Airplane, Passenger, Ticket } from "@ontology/sdk";
4
5type TicketEdit = Edits.Object<Ticket>
6
7interface TicketInfo {
8    airplane?: Osdk.Instance<Airplane>;
9    passenger?: Osdk.Instance<Passenger>;
10    seat?: String;
11}
12
13function createTickets(ticketInfo: TicketInfo[]): TicketEdit[] {
14    const batch = createEditBatch<TicketEdit>(client);
15
16    ticketInfo.forEach(i => batch.create(TicketEdit, {
17        flightNumber: i.airplane.flightNumber,
18        passengerName: i.passenger.name,
19        seat: i.seat}))
20
21    return batch.getEdits();
22}
23
24export default createTickets;`
```


### [](#object-set)Object set对象集


There are two ways to pass a collection of objects into and out of a function: concrete collections of objects (such as arrays), or object sets.将一组对象传入和传出函数有两种方式：具体的对象集合（如数组），或对象集。


Passing an array of objects to a function enables executing logic over a concrete list of objects at the expense of loading the objects into the function execution environment up front. An object set, however, allows you to perform filtering, search-around, and aggregation operations and only load the final result when you request it.将对象数组传入函数可以在函数执行环境中预先加载对象，从而执行对具体对象列表的逻辑操作。然而，对象集允许你进行过滤、搜索和聚合操作，并且仅在请求时才加载最终结果。


We recommend using an object set instead of an array because an object set often achieves better performance and allows more than 10,000 objects to be passed into the function.我们推荐使用对象集而不是数组，因为对象集通常能实现更好的性能，并允许将超过 10,000 个对象传入函数。


The below example shows how to filter an object set without loading the objects into memory, allowing you to return the filtered object set to a different part of the application.下面的示例展示了如何在不需要将对象加载到内存的情况下过滤对象集，从而可以将过滤后的对象集返回给应用程序的其他部分。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function } from "@foundry/functions-api";
2import { Airplane, ObjectSet } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Function()
6    public filterAircraft(aircraft: ObjectSet<Airplane>): ObjectSet<Airplane> {
7        return aircraft.filter(a => a.capacity.range().gt(200));
8    }
9}`
```

```
Copied!`1import { ObjectSet } from "@osdk/client";
2import { Airplane } from "@ontology/sdk";
3
4function filterAircraft(aircraft: ObjectSet<Airplane>): ObjectSet<Airplane> {
5    return aircraft
6        .where({
7            capacity: {
8                $gt: 200,
9            }
10        });
11}
12
13export default filterAircraft;`
```

```
Copied!`1from functions.api import function
2from ontology_sdk.ontology.objects import Airplane
3from ontology_sdk.ontology.object_sets import AirplaneObjectSet
4
5@function
6def filter_aircraft(aircraft: AirplaneObjectSet) -> AirplaneObjectSet:
7    return aircraft.where(Airplane.capacity > 200)`
```


### [](#interface)Interface接口


Interface types from your Ontology can be used as both inputs and outputs in TypeScript v2 function signatures. They are not supported in TypeScript v1 or Python.来自您本体（Ontology）的接口类型可以用作 TypeScript v2 函数签名中的输入和输出。它们在 TypeScript v1 或 Python 中不受支持。


TypeScript v2```
Copied!`1import { Osdk } from "@osdk/client";
2import { Integer } from "@osdk/functions";
3import { Person } from "@ontology/sdk";
4
5function getAge(person: Osdk.Instance<Person>): Integer {
6    return person.age;
7}
8
9export default getAge;`
```


### [](#interface-object-set)Interface object set接口对象集


Interface object sets can be both inputs and outputs in TypeScript v2 function signatures.接口对象集可以用作 TypeScript v2 函数签名中的输入和输出。


TypeScript v2```
Copied!`1import { ObjectSet } from "@osdk/client";
2import { Person } from "@ontology/sdk";
3
4function filterPeople(people: ObjectSet<Person>): ObjectSet<Person> {
5    return people
6        .where({
7            age: {
8                $gt: 200,
9            }
10        });
11}
12
13export default filterPeople;`
```


### [](#ontology-edit)Ontology edit本体编辑


In addition to writing functions that read data from the Ontology, you can also write functions that create objects and edit the properties and links between objects. For more details about how edit functions work, refer to the [overview page](/docs/foundry/functions/edits-overview/).除了编写从本体中读取数据的函数外，您还可以编写创建对象以及编辑对象属性和对象间链接的函数。有关编辑函数如何工作的更多详细信息，请参阅概述页面。


To be registered as edit functions, TypeScript v1 functions require a `void` return type in the signature. TypeScript v2 and Python functions, however, require explicitly returning a list of Ontology edits.要注册为编辑函数，TypeScript v1 函数需要在签名中指定 void 返回类型。而 TypeScript v2 和 Python 函数则需要显式返回一组本体编辑。


TypeScript v1TypeScript v2Python```
Copied!`1import { Edits, OntologyEditFunction } from "@foundry/functions-api";
2import { Employee, LaptopRequest, Objects } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(Employee, LaptopRequest)
7    @OntologyEditFunction()
8    public assignEmployee(newEmployee: Employee, leadEmployee: Employee): void {
9
10        const newLaptopRequest = Objects.create().laptopRequest(Date.now().toString());
11        newLaptopRequest.employeeName = newEmployee.name;
12
13        newEmployee.lead.set(leadEmployee);
14    }
15}`
```

```
Copied!`1import { Client } from "@osdk/client";
2import { createEditBatch, Edits } from "@osdk/functions";
3import { Employee, LaptopRequest } from "@ontology/sdk";
4
5type EmployeeEdit =
6    | Edits.Object<Employee>
7    | Edits.Object<LaptopRequest>
8    | Edits.Link<Employee, "lead">;
9
10function assignEmployee(
11    client: Client,
12    newEmployee: Osdk.Instance<Employee>,
13    leadEmployee: Osdk.Instance<Employee>
14): EmployeeEdit[] {
15
16    const batch = createEditBatch<EmployeeEdit>(client);
17
18    batch.create(LaptopRequest, {
19        id: Date.now().toString(),
20        employeeName: newEmployee.name,
21    });
22    batch.link(newEmployee, "lead", leadEmployee);
23
24    return batch.getEdits();
25}
26
27export default assignEmployee;`
```

```
Copied!`1from functions.api import function, OntologyEdit
2from ontology_sdk import FoundryClient
3from ontology_sdk.ontology.objects import Employee, LaptopRequest
4from time import time
5
6@function
7def assign_employee(new_employee: Employee, lead_employee: Employee) -> list[OntologyEdit]:
8
9    ontology_edits = FoundryClient().ontology.edits()
10
11    new_laptop_request = ontology_edits.objects.LaptopRequest.create(str(int(time() * 1000)))
12    new_laptop_request.employee_name = new_employee.name
13
14    new_employee.lead.set(lead_employee)
15
16    return ontology_edits.get_edits()`
```


### [](#attachment)Attachment附件


TypeScript v1TypeScript v2Python```
Copied!`1import { Attachment, Function } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public loadAttachmentContents(attachment: Attachment): Promise<string> {
6        return attachment.readAsync().then(blob => blob.text());
7    }
8}`
```

```
Copied!`1import { Attachment } from "@osdk/functions";
2
3function loadAttachmentContents(attachment: Attachment): Promise<string> {
4    return attachment.fetchContents().then(response => response.text());
5}
6
7export default loadAttachmentContents;`
```

```
Copied!`1from functions.api import function, Attachment
2
3@function
4def load_attachment_contents(attachment: Attachment) -> str:
5    return attachment.read().getvalue().decode('utf-8')`
```


### [](#notification)Notification通知


Notification types can be returned from a function to flexibly configure notifications that should be sent in the platform. For example, you can author a function that takes in parameters such as a `User` and an object type and returns a Notification with a configured message.通知类型可以从函数中返回，以便灵活配置平台中应发送的通知。例如，您可以编写一个函数，该函数接收诸如 User 和对象类型等参数，并返回一个配置了消息的通知。


- A `Notification` consists of two fields: a `ShortNotification` and `EmailNotificationContent`.一个 Notification 包含两个字段：一个 ShortNotification 和 EmailNotificationContent 。
- A `ShortNotification` represents a summarized version of the notification, which will be shown within the Foundry platform. It includes a short `heading`, `content`, and a collection of `Link`s.一个 ShortNotification 代表通知的摘要版本，将在 Foundry 平台内显示。它包括一个简短的 heading 、 content 以及一组 Link 。
- `EmailNotificationContent` represents a rich version of the notification which can be sent externally via email. It includes a `subject`, a `body` consisting of headless HTML, and a collection of `Link`s.EmailNotificationContent 代表通知的丰富版本，可以通过电子邮件外部发送。它包括一个 subject 、一个由无头 HTML 组成的 body 以及一组 Link 。
- A `Link` has a user-facing `label` and a `linkTarget`. The `LinkTarget` can be a URL, an `OntologyObject`, or a `rid` of any resource within Foundry.一个 Link 具有面向用户的 label 和 linkTarget 。 LinkTarget 可以是一个 URL、一个 OntologyObject 或 Foundry 内任何资源的 rid 。


For an example of how to use the Notifications API, review [our guide](/docs/foundry/functions/configure-notifications/).使用通知 API 的示例，请参阅我们的指南。


TypeScript v1TypeScript v2Python```
Copied!`1import {
2    EmailNotificationContent,
3    Function,
4    Notification,
5    ShortNotification,
6} from "@foundry/functions-api";
7
8export class MyFunctions {
9    @Function()
10    public buildNotification(): Notification {
11        return Notification.builder()
12            .shortNotification(ShortNotification.builder()
13                .heading("Issue reminder")
14                .content("Investigate this issue.")
15                .build())
16            .emailNotificationContent(EmailNotificationContent.builder()
17                .subject("New issue")
18                .body("hello")
19                .build())
20            .build();
21    }
22}`
```

```
Copied!`1import {
2    Notification
3} from "@osdk/functions";
4
5export default function buildNotification(): Notification {
6    return {
7        platformNotification: {
8            heading: "Issue reminder",
9            content: "Investigate this issue.",
10            links: []
11        },
12        emailNotification: {
13            subject: "New issue"
14            body: "hello",
15            links: []
16        }
17    };
18}`
```

```
Copied!`1from functions.api import function, Notification, PlatformNotification, EmailNotification
2
3@function()
4def buildNotification() -> Notification:
5    return Notification(
6        platform_notification=PlatformNotification(
7            heading="Issue reminder",
8            content="Investigate this issue.",
9            links=[]
10        ),
11        email_notification=EmailNotification(
12            subject="New issue",
13            body="hello",
14            links=[]
15        ),
16    )`
```


## [](#media-types)Media types媒体类型


### [](#media-references)Media references媒体引用


Functions can accept and return media items. For more information, review the guide on [media](/docs/foundry/functions/media/).函数可以接受和返回媒体项。有关更多信息，请查阅媒体指南。


TypeScript v1```
Copied!`1import { Function, MediaItem } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public transcribeAudioFile(file: MediaItem): Promise<string | undefined> {
6        if (MediaItem.isAudio(file.mediaReference)) {
7            return await file.mediaReference.transcribeAsync({
8                language: TranscriptionLanguage.ENGLISH,
9                performanceMode: TranscriptionPerformanceMode.MORE_ECONOMICAL,
10                outputFormat: {type: "plainTextNoSegmentData", addTimestamps: true}
11            });
12        }
13
14        return undefined;
15    }
16}`
```


## [](#users-groups-and-principals)Users, groups, and principals用户、组和主体


A Principal represents either a Foundry user account or group. These types can be passed into a function to allow accessing information associated with a user or group, such as a group's name or a user's first and last name or email address. All Principal types are exported from the `@foundry/functions-api` package.主体代表 Foundry 用户账户或组。这些类型可以传递到函数中，以访问与用户或组关联的信息，例如组的名称或用户的名、姓或电子邮件地址。所有主体类型都从 @foundry/functions-api 包中导出。


- A `User` always has a username, and may have a `firstName`, `lastName`, or `email`. It also includes all fields associated with a `Principal`.User 总是有一个用户名，并且可能有一个 firstName 、 lastName 或 email 。它还包括所有与 Principal 关联的字段。
- A `Group` has a name. It also includes all fields associated with a `Principal`.一个 Group 有一个名称。它还包括与一个 Principal 关联的所有字段。
- A `Principal` can be either a `User` or a `Group`. You can inspect the `type` field to determine whether a given `Principal` is a `User` or a `Group`. In addition to `User` and `Group`-specific fields, a `Principal` has an `id`, `realm`, and dictionary of `attributes`.一个 Principal 可以是 User 或 Group 。你可以检查 type 字段来确定给定的 Principal 是 User 还是 Group 。除了 User 和 Group 特定字段外，一个 Principal 还有一个 id 、 realm 以及 attributes 的字典。


### [](#user)User用户


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, User } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getUserEmail(user: User): string {
6        return user.email;
7    }
8}`
```

```
Copied!`1import { UserId } from "@osdk/functions";
2import { Users } from "@osdk/foundry.admin";
3import { Client } from "@osdk/client";
4
5export default function getUserEmail(client:Client, userId: UserId): string {
6    const user = Users.get(client, userId)
7    return user.email;
8}`
```

```
Copied!`1from functions.api import function, UserId
2from foundry_sdk import FoundryClient
3import foundry_sdk
4
5@function()
6def getUserEmail(user_id: UserId) -> string:
7    client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
8    user = client.admin.User.get(user_id)
9    return user.email`
```


### [](#group)Group组


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Group } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getGroupName(group: Group): string {
6        return group.name;
7    }
8}`
```

```
Copied!`1import { GroupId } from "@osdk/functions";
2import { Groups } from "@osdk/foundry.admin";
3import { Client } from "@osdk/client";
4
5export default function getGroupName(client: Client, groupId: GroupId): string {
6    const group = Groups.get(client, groupId)
7    return group.name;
8}`
```

```
Copied!`1from functions.api import function, GroupId
2from foundry_sdk import FoundryClient
3import foundry_sdk
4
5@function()
6def getGroupName(group_id: GroupId) -> string:
7    client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
8    group = client.admin.Group.get(group_id)
9    return group.name`
```


### [](#principal)Principal主体


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Principal } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public getPrincipalType(principal: Principal): string {
6
7        switch (principal.type) {
8            case "user":
9                return "User";
10            case "group":
11                return "Group";
12            default:
13                return "Unknown";
14        }
15    }
16}`
```

```
Copied!`1import { GroupId, Principal, UserId } from "@osdk/functions";
2
3export default async function getPrincipals(client: Client, userId: UserId, groupId: GroupId): Principal[] {
4    return [{type: "user", id: userId}, {type: "group", id: groupId}];
5}`
```

```
Copied!`1from functions.api import Array, function, GroupId, Principal, UserId
2
3@function()
4def getPrincipals(user_id: UserId, group_id: GroupId) -> Array[Principal]:
5    return [Principal.user(user_id), Principal.group(group_id)]`
```


## [](#geometry-types)Geometry types几何类型


Geometry types represent spatial data and geographic shapes in your functions. Two geometry types are supported:几何类型表示函数中的空间数据和地理形状。支持两种几何类型：


- **GeoPoint** represents a single geographic point with latitude and longitude coordinates.GeoPoint 表示具有纬度和经度坐标的单个地理点。
- **GeoShape** represents any valid GeoJSON geometry, including Points, Polygons, LineStrings, and other shapes.GeoShape 表示任何有效的 GeoJSON 几何形状，包括点、多边形、线串和其他形状。


These types follow the [GeoJSON specification ↗](https://geojson.org/) and can be used for spatial operations, mapping, and geographic analysis. Note that positional arguments follow longitude, latitude order as per the GeoJSON spec.这些类型遵循 GeoJSON 规范 ↗，可用于空间操作、制图和地理分析。请注意，位置参数按照 GeoJSON 规范遵循经度、纬度的顺序。


### [](#geopoint)GeoPoint


The following example shows how to create and return a GeoPoint.以下示例展示了如何创建和返回一个 GeoPoint。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, GeoPoint } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public createPoint(): GeoPoint {
6        return GeoPoint.fromCoordinates({
7            latitude: 37.7749,
8            longitude: -22.4194
9        });
10    }
11}`
```

```
Copied!`1import { Point } from "@osdk/functions";
2
3function createPoint(): Point {
4    return {
5        type: "Point",
6        coordinates: [-22.4194, 37.7749]
7    };
8}
9
10export default createPoint;`
```

```
Copied!`1from functions.api import function, GeoPoint
2
3@function
4def create_point() -> GeoPoint:
5    return GeoPoint(type="Point", coordinates=[-22.4194, 37.7749])`
```


### [](#geoshape)GeoShape


The following example shows how to create and return a Polygon.以下示例展示了如何创建并返回一个多边形。


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, Polygon, GeoPoint } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public createPolygon(): Polygon {
6        const ring: GeoPoint[] = [
7            GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.4 }),
8            GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.5 }),
9            GeoPoint.fromCoordinates({ latitude: 37.7, longitude: -22.5 }),
10            GeoPoint.fromCoordinates({ latitude: 37.7, longitude: -22.4 }),
11            GeoPoint.fromCoordinates({ latitude: 37.8, longitude: -22.4 })
12        ];
13        return Polygon.fromLinearRings([ring]);
14    }
15}`
```

```
Copied!`1import { Geometry } from "@osdk/functions";
2
3function createPolygon(): Geometry {
4    return {
5        type: "Polygon",
6        coordinates: [[
7            [-22.4, 37.8],
8            [-22.5, 37.8],
9            [-22.5, 37.7],
10            [-22.4, 37.7],
11            [-22.4, 37.8]
12        ]]
13    };
14}
15
16export default createPolygon;`
```

```
Copied!`1from functions.api import function, Polygon
2
3@function
4def create_polygon() -> Polygon:
5    return Polygon(
6        type="Polygon",
7        coordinates=[[
8            [-22.4, 37.8],
9            [-22.5, 37.8],
10            [-22.5, 37.7],
11            [-22.4, 37.7],
12            [-22.4, 37.8]
13        ]])`
```

