# [](#create-stub-objects)Create stub objects创建存根对象


You can create and define your mock objects using `Objects.create()`, which can be used the same way as if it was a regular function. You can then use these mock objects when writing unit tests. Here is an example:您可以使用 Objects.create() 创建和定义您的模拟对象，它可以用作常规函数的方式使用。然后，您可以在编写单元测试时使用这些模拟对象。以下是一个示例：


```
Copied!`1import { MyFunctions } from ".."
2
3import { Objects, ExampleDataAirport } from "@foundry/ontology-api";
4
5describe("example test suite", () => {
6    const myFunctions = new MyFunctions();
7
8    test("test created objects", () => {
9        const JFK = Objects.create().exampleDataAirport("JFK Test");
10        JFK.displayAirportName = "John F. Kennedy International";
11        expect(myFunctions.getAirportName(JFK)).toEqual("John F. Kennedy International");
12    });
13});`
```


For reference, the above example is using the Jest syntax [`expect(...).toEqual(...)` ↗](https://jestjs.io/docs/expect#toequalvalue).作为参考，上述示例使用的是 Jest 语法 expect(...).toEqual(...) ↗。

