# [](#mock-dates-timestamps-and-uuids)Mock dates, timestamps, and UUIDs模拟日期、时间戳和 UUID


You can specify the output of non-deterministic functions by utilizing `jest.spyOn()` to inject a mock to run the test.您可以通过使用 jest.spyOn() 注入模拟对象来指定非确定性函数的输出，以运行测试。


### [](#uuid-functions)UUID functionsUUID 函数


You can specify the output of `Uuid` by injecting a mock. Here is an example:您可以通过注入模拟对象来指定 Uuid 的输出。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5import { Uuid } from "@foundry/functions-utils";
6
7describe("example test suite", () => {
8    const myFunctions = new MyFunctions();
9
10    test("creates new flight", () => {
11        const makeUuid = () => "my-uuid";
12        jest.spyOn(Uuid, "random").mockImplementation(() => makeUuid());
13
14        verifyOntologyEditFunction(() => myFunctions.createNewFlight())
15            .createsObject({
16                objectType: ExampleDataFlight,
17                properties: {
18                    flightId: makeUuid()
19                }
20            })
21    })
22});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
3import { Uuid } from "@foundry/functions-utils";
4
5export class MyFunctions {
6    @Edits(ExampleDataFlight)
7    @OntologyEditFunction()
8    public createNewFlight(): void {
9        Objects.create().exampleDataFlight(Uuid.random());
10    }
11}`
```


#### [](#advanced-uuid-functions)Advanced UUID functions高级 UUID 函数


There are certain circumstances where you may want full control over the output of the `Uuid`. This requires you to adjust the code of the function you are testing. For example, the `createNewFlight` function above is wrapped in a class `MyFunctions` and you can add a constructor to the class that takes a supplier with a default value. The updated function with the supplier looks like this:在某些情况下，你可能需要完全控制 Uuid 的输出。这需要你调整正在测试的函数的代码。例如，上面提到的 createNewFlight 函数被包装在一个类 MyFunctions 中，你可以在类中添加一个构造函数，该构造函数接受一个具有默认值的供应商。使用供应商的更新后函数如下所示：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
3import { Uuid } from "@foundry/functions-utils";
4
5export class MyFunctions {
6    constructor (private UuidSupplier: () => string = Uuid.random){} // this new constructor in the class takes a supplier
7
8    @Edits(ExampleDataFlight)
9    @OntologyEditFunction()
10    public createNewFlightWithConstructor(): void {
11        Objects.create().exampleDataFlight(this.UuidSupplier());
12    }
13}`
```


This updated function can be tested with full control of the output (in this case we set the generated `Uuid` to be `my-other-uuid`):该更新后的函数可以完全控制输出进行测试（在本例中，我们将生成的 Uuid 设置为 my-other-uuid ）：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5import { Uuid } from "@foundry/functions-utils";
6
7describe("example test suite", () => {
8    const myFunctions = new MyFunctions();
9
10    test("creates new flight with supplier", () => {
11        const myNewFunctions = new MyFunctions(() => "my-other-uuid");
12
13        verifyOntologyEditFunction(() => myNewFunctions.createNewFlightWithConstructor())
14            .createsObject({
15                objectType: ExampleDataFlight,
16                properties: {
17                    flightId: "my-other-uuid"
18                }
19            })
20
21    })
22});`
```


### [](#timestampnow-functions)Timestamp.now() functionsTimestamp.now() 函数


You can specify the output of `Timestamp.now()` by injecting a mock. Here is an example:你可以通过注入模拟对象来指定 Timestamp.now() 的输出。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5import { Timestamp } from "@foundry/functions-api";
6
7describe("example test suite", () => {
8    const myFunctions = new MyFunctions();
9
10    test("test timestamp now", () => {
11        const makeTimestamp = () => Timestamp.fromISOString("2018-06-13T12:11:13+05:00");
12        jest.spyOn(Timestamp, "now").mockImplementation(() => makeTimestamp());
13
14        const flight = Objects.create().exampleDataFlight("flightAnotherTest");
15        verifyOntologyEditFunction(() => myFunctions.startTakeoff(flight))
16            .modifiesObject({
17                object: flight,
18                properties: {
19                    takeoff: makeTimestamp()
20                }
21            })
22    })
23});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits, Timestamp } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Edits(ExampleDataFlight)
6    @OntologyEditFunction()
7    public startTakeoff(flight: ExampleDataFlight): void {
8        flight.takeoff = Timestamp.now();
9    }
10}`
```


### [](#localdatenow-functions)LocalDate.now() functionsLocalDate.now()函数


You can specify the output of `LocalDate.now()` by injecting a mock. Here is an example:你可以通过注入模拟对象来指定 LocalDate.now() 的输出。这里有一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5import { LocalDate } from "@foundry/functions-api";
6
7describe("example test suite", () => {
8    const myFunctions = new MyFunctions();
9
10    test("test LocalDate now", () => {
11        const makeLocalDate = () => LocalDate.fromISOString("2018-06-13");
12        jest.spyOn(LocalDate, "now").mockImplementation(() => makeLocalDate());
13
14        const flight = Objects.create().exampleDataFlight("flightTest");
15        verifyOntologyEditFunction(() => myFunctions.dateTakeoff(flight))
16            .modifiesObject({
17                object: flight,
18                properties: {
19                    date: makeLocalDate()
20                }
21            })
22    })
23});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits, LocalDate } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
3
4export class MyFunctions {
5    @Edits(ExampleDataFlight)
6    @OntologyEditFunction()
7    public dateTakeoff(flight: ExampleDataFlight): void {
8        flight.date = LocalDate.now();
9    }
10}`
```

