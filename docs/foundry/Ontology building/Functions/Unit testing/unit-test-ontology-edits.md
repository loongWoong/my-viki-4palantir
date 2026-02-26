# [](#verify-ontology-edits)Verify Ontology edits验证本体编辑


You can use the `verifyOntologyEditFunction()` API to verify edits performed by your function. You need to import it from `"@foundry/functions-testing-lib"`. This allows you to create unit tests around the workflows listed below.您可以使用 verifyOntologyEditFunction() API 来验证您的函数执行的编辑。您需要从 "@foundry/functions-testing-lib" 中导入它。这使您能够围绕以下工作流创建单元测试。


#### [](#verify-object-creation)Verify object creation验证对象创建


You can use the `.createsObjects` method to verify an object creation. Here's an example:您可以使用 .createsObjects 方法来验证对象创建。这里有一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataAirport } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("create airport", () => { 
10        verifyOntologyEditFunction(() => myFunctions.createAirport("airportCode", "airportDisplayName"))
11            .createsObject(
12                {
13                    objectType: ExampleDataAirport,
14                    properties: {
15                        airport: "airportCode",
16                        displayAirportName: "airportDisplayName",
17                    },
18                });
19    });
20});`
```


This can be used to test the following function:这可用于测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataAirport } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataAirport)
7    @OntologyEditFunction()
8    public createAirport(airport: string, displayName: string): void {
9        const newAirport = Objects.create().exampleDataAirport(airport);
10        newAirport.displayAirportName = displayName;
11    }
12}`
```


#### [](#verify-edits-on-a-newly-created-object)Verify edits on a newly created object验证对新建对象的编辑


You can verify edits that are created involving a newly created object. For example, you may want to create a new `ExampleDataFlight` objects and verify that the link is created to the `new-flight-delay-0`. Here's an example:您可以验证涉及新建对象的编辑。例如，您可能想要创建新的 ExampleDataFlight 对象并验证链接是否创建到 new-flight-delay-0 。这里有一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("single key with single created object", () => {
10            const flight = Objects.create().exampleDataFlight("flightTest");
11            verifyOntologyEditFunction(() => myFunctions.createAndLinkDelays(flight, 1))
12                .createsObject({
13                    objectType: ExampleFlightDelayEvent,
14                    properties: {
15                        eventId: "new-flight-delay-0",
16                    },
17                })
18                .addsLink(edits => ({
19                    link: flight.flightDelayEvent,
20                    linkedObject: edits.createdObjects.byObjectType(ExampleFlightDelayEvent)[0],
21                }))
22        });
23});`
```


This can be used to test the following function:这可用于测试以下功能：


```
Copied!`1import { Function, Integer, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight, ExampleFlightDelayEvent )
7    @OntologyEditFunction()
8    public createAndLinkDelays(flight: ExampleDataFlight, numDelay: Integer): void {
9        for (let n = 0; n < numDelay; n++) {
10            const delay = Objects.create().exampleFlightDelayEvent(`new-flight-delay-${n}`);
11            flight.flightDelayEvent.add(delay);
12        }
13    }
14}`
```


#### [](#verify-object-property-edits)Verify object property edits验证对象属性编辑


You can verify edits to the property using `.modifiesObjects`. Here's an example:你可以使用 .modifiesObjects 来验证属性编辑。这里有一个例子：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("modifies aircraft of the flight", () => {
10        const flight = Objects.create().exampleDataFlight("NY -> LA");
11        const oldAircraft = Objects.create().exampleDataAircraft("N11111");
12        flight.aircraft.set(oldAircraft);
13        const newAircraft = Objects.create().exampleDataAircraft("A00000");
14        verifyOntologyEditFunction(() => myFunctions.assignAircraftToFlight(flight, newAircraft))
15            .modifiesObject(
16                { 
17                    object: flight, 
18                    properties: { 
19                        tailNumber: "A00000" 
20                    } 
21                })
22        });
23});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight)
7    @OntologyEditFunction()
8    public assignAircraftToFlight(flight: ExampleDataFlight, aircraft: ExampleDataAircraft): void {
9        flight.aircraft.clear();
10        aircraft.flight.set(flight);
11        flight.tailNumber = aircraft.tailNumber;
12    }
13}`
```


#### [](#verify-no-other-edits-to-an-object)Verify no other edits to an object验证对象未进行其他修改


You can ensure there are no other edits using the optional `.hasNoMoreEdits()`. This means that only the specified edits are allowed, and the verification will fail if other edits are detected. Here's an example:您可以使用可选的 .hasNoMoreEdits() 来确保没有其他修改。这意味着仅允许指定的修改，如果检测到其他修改，验证将失败。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("single key with linked object", () => {
10            const flight = Objects.create().exampleDataFlight("flightAnotherTest");
11            const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
12            verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
13                .addsLink({link: flight.flightDelayEvent, linkedObject: delay })
14                .hasNoMoreEdits();
15        });
16});`
```


When using `.hasNoMoreEdits()`, you can ignore specific kinds of edits that take place. You do this by passing an object with some or all of the following:当使用 .hasNoMoreEdits() 时，你可以忽略特定类型的编辑。你可以通过传递一个包含以下部分或全部属性的对象来实现：


- `ignoreExtraCreatedObjects: true`
- `ignoreExtraModifiedObjects: true`
- `ignoreExtraDeletedObjects: true`
- `ignoreExtraLinkedObjects: true`
- `ignoreExtraUnlinkedObjects: true`


#### [](#verify-link-creation-to-an-object)Verify link creation to an object验证与对象的链接创建


You can verify link creation on an object using `.addsLink`. Here's an example:你可以使用 .addsLink 验证对象上的链接创建。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("single key with linked object", () => {
10            const flight = Objects.create().exampleDataFlight("flightAnotherTest");
11            const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
12            verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
13                .addsLink({link: flight.flightDelayEvent, linkedObject: delay })
14                .hasNoMoreEdits();
15        });
16});`
```


This test is equivalent to testing for the same link going in the opposite direction:此测试等同于测试同一链接的反方向：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("single key with linked object reverse", () => {
10            const flight = Objects.create().exampleDataFlight("flightAnotherTest");
11            const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
12            verifyOntologyEditFunction(() => myFunctions.linkDelays(flight, delay))
13                .addsLink({link: delay.flight, linkedObject: flight })
14                .hasNoMoreEdits();
15        });
16});`
```


This can be used to test the following function:这可用于测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight, ExampleFlightDelayEvent )
7    @OntologyEditFunction()
8    public linkDelays(flight: ExampleDataFlight, delay: ExampleFlightDelayEvent): void {
9        flight.flightDelayEvent.add(delay);
10    }
11}`
```


#### [](#verify-link-removal-from-an-object)Verify link removal from an object验证从对象中移除链接


You can verify link removal from an object using `.removesLink`. Here's an example:您可以使用 .removesLink 验证从对象中移除链接。这里有一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("test link removal", () => {
10            const flight = Objects.create().exampleDataFlight("flightAnotherTest");
11            const delay = Objects.create().exampleFlightDelayEvent("new-flight-delay")
12            flight.flightDelayEvent.add(delay);
13            verifyOntologyEditFunction(() => myFunctions.removeAllDelays(flight))
14                .removesLink({link: flight.flightDelayEvent, unlinkedObject: delay })
15                .hasNoMoreEdits();
16        });
17});`
```


This can be used to test the following function:这可用于测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight, ExampleFlightDelayEvent)
7    @OntologyEditFunction()
8    public removeAllDelays(flight: ExampleDataFlight): void {
9        flight.flightDelayEvent.clear();
10    }
11}`
```


#### [](#verify-deleting-an-object)Verify deleting an object验证删除对象


You can verify deleting an object using `.deletesObject`. Here's an example:您可以使用 .deletesObject 验证删除对象。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("test object deletion", () => {
10            const flight = Objects.create().exampleDataFlight("flightAnotherTest");
11            verifyOntologyEditFunction(() => myFunctions.deleteFlight(flight))
12                .deletesObject(flight)
13                .hasNoMoreEdits();
14        });
15});`
```


This can be used to test the following function:这可用于测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight)
7    @OntologyEditFunction()
8    public deleteFlight(flight: ExampleDataFlight): void {
9        flight.delete();
10    }
11}`
```


#### [](#verify-multiple-objects-were-created)Verify multiple objects were created验证已创建多个对象


You can use the `.createsObjects` method and pass in a list to create multiple objects to test on. Here's an example:您可以使用 .createsObjects 方法，并传入一个列表来创建多个用于测试的对象。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects , ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
4import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
5
6describe("example test suite", () => {
7    const myFunctions = new MyFunctions();
8
9    test("single key with many created objects", () => {
10            const flight = Objects.create().exampleDataFlight("flightTest");
11            verifyOntologyEditFunction(() => myFunctions.createAndLinkDelays(flight, 3))
12                .createsObjects(
13                    [0, 1, 2].map(i => ({
14                        objectType: ExampleFlightDelayEvent,
15                        properties: {
16                            eventId: "new-flight-delay-" + i,
17                        },
18                    })),
19                )
20                .addsLinks(edits =>
21                    edits.createdObjects.byObjectType(ExampleFlightDelayEvent).map(event => ({
22                        link: flight.flightDelayEvent,
23                        linkedObject: event,
24                    })),
25                )
26                .hasNoMoreEdits();
27        });
28});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, Integer, OntologyEditFunction, Edits } from "@foundry/functions-api";
2import { Objects, ExampleDataFlight, ExampleFlightDelayEvent } from "@foundry/ontology-api";
3
4export class MyFunctions {
5
6    @Edits(ExampleDataFlight, ExampleFlightDelayEvent )
7    @OntologyEditFunction()
8    public createAndLinkDelays(flight: ExampleDataFlight, numDelay: Integer): void {
9        for (let n = 0; n < numDelay; n++) {
10            const delay = Objects.create().exampleFlightDelayEvent(`new-flight-delay-${n}`);
11            flight.flightDelayEvent.add(delay);
12        }
13    }
14}`
```


### [](#asynchronous-ontology-edits)Asynchronous ontology edits异步本体编辑


You can verify asynchronous ontology edits as follows:你可以按以下方式验证异步本体编辑：


```
Copied!`1import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
2
3test("test async edit function", async () => {
4        const obj = Objects.create().objectWithAllPropertyTypes(1);
5        (await verifyOntologyEditFunction(() => myFunctions.setDateAndTimestampToNow(obj))).modifiesObject({
6            object: obj,
7            properties: {
8                timestampProperty: makeTimestamp(),
9            },
10        });
11    });`
```


### [](#multiple-verifications)Multiple verifications多次验证


As we have seen in the examples above, we can chain verifications. The following pattern illustrates this:如前文示例所示，我们可以串联验证。以下模式说明了这一点：


```
Copied!`1import { verifyOntologyEditFunction } from "@foundry/functions-testing-lib";
2import { Objects, ExampleDataObject } from "@foundry/ontology-api";
3
4test("multiple action edit", () => { 
5    verifyOntologyEditFunction(() => myFunctions.multistageEdits("objectId", "objectName"))
6        .createsObject({...})
7        .modifiesObjects({...})
8        .addsLinks({...})
9        .removesLinks({...})
10        .deletesObject(...)
11        .hasNoMoreEdits(); 
12});`
```

