# [](#error-types)Error types错误类型


In addition to declaring an [output type](/docs/foundry/functions/types-reference/) on your TypeScript function, you can also declare an error type. This can be particularly useful for propagating and handling errors in the context of queries.除了在 TypeScript 函数中声明输出类型外，你还可以声明错误类型。这在查询上下文中传播和处理错误时特别有用。


## [](#define-an-error-type)Define an error type定义错误类型


You can define an error type using the `FunctionsError` type exported from `@foundry/functions-api`. It takes two type parameters; a string name and an optional type that defaults to an empty object. Any [valid output type](/docs/foundry/functions/types-reference/) for a function may be used as an error type, including objects and object sets.你可以使用从 @foundry/functions-api 导出的 FunctionsError 类型来定义错误类型。它接受两个类型参数：一个字符串名称和一个可选类型，默认为空对象。函数的任何有效输出类型都可以用作错误类型，包括对象和对象集。


You can union multiple `FunctionsError` types together to define a set of possible errors for your function. For example, you could define the following error type for a function that gets an employee's teammates:你可以将多个 FunctionsError 类型组合在一起来定义你的函数可能出现的错误集。例如，你可以为获取员工队友的函数定义以下错误类型：


```
Copied!`1import { FunctionsError } from "@foundry/functions-api";
2import { Employee } from "@foundry/ontology-api";
3
4type GetTeammatesError =
5    | FunctionsError<"EmployeeNotFoundForId", string>
6    | FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>`
```


## [](#declare-an-error-type-on-a-function)Declare an error type on a function在函数上声明错误类型


To declare an error type on a TypeScript function, you can use the `FunctionsResult` type exported from `@foundry/functions-api`. It takes two type parameters; an output type and an error type.要在 TypeScript 函数上声明错误类型，你可以使用从 @foundry/functions-api 导出的 FunctionsResult 类型。它接受两个类型参数：一个输出类型和一个错误类型。


Using the `GetTeammatesError` example from the previous section, you can declare the error type on a function like so:使用上一节中的 GetTeammatesError 示例，你可以在函数上这样声明错误类型：


```
Copied!`1import { Function, FunctionsError, FunctionsResult } from "@foundry/functions-api";
2import { Employee } from "@foundry/ontology-api";
3
4type GetTeammatesError =
5    | FunctionsError<"EmployeeNotFoundForId", string>
6    | FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>
7
8@Function()
9public getTeammates(employeeId: string): FunctionsResult<Employee[], GetTeammatesError> {
10    ...
11}`
```


Note that by default the `FunctionsResult` type includes a few errors that can be returned by the TypeScript function runtime infrastructure:请注意，默认情况下， FunctionsResult 类型包含一些 TypeScript 函数运行时基础设施可能返回的错误：


- **`FunctionsTypeScriptExecutorService:CpuTimeoutError`:** Returned when the function exceeds the CPU time limit.FunctionsTypeScriptExecutorService:CpuTimeoutError : 当函数超出 CPU 时间限制时返回。
- **`FunctionsTypeScriptExecutorService:WallTimeoutError`:** Returned when the function exceeds the wall time limit.FunctionsTypeScriptExecutorService:WallTimeoutError : 当函数超出墙时间限制时返回。
- **`FunctionsTypeScriptExecutorService:OutOfMemoryError`:** Returned when the function exceeds the memory limit.FunctionsTypeScriptExecutorService:OutOfMemoryError : 当函数超出内存限制时返回。
- **`FunctionsTypeScriptExecutorService:RuntimeError`:** Returned when the function encounters some other runtime error.FunctionsTypeScriptExecutorService:RuntimeError : 当函数遇到其他运行时错误时返回。


## [](#return-outputs-and-errors-in-your-function)Return outputs and errors in your function在函数中返回输出和错误


To return outputs and errors, you can use the `FunctionsResult.ok` and `FunctionsResult.err` methods exported from `@foundry/functions-api`:要返回输出和错误，你可以使用从 @foundry/functions-api 导出的 FunctionsResult.ok 和 FunctionsResult.err 方法：


- **`FunctionsResult.ok`:** Takes a single output value as its argument.FunctionsResult.ok : 接收一个输出值作为其参数。
- **`FunctionsResult.err`:** Takes an error name and value as its arguments.FunctionsResult.err : 接受一个错误名称和值作为其参数。


Using the `getTeammates` example from the previous section, you can return outputs and errors like so:使用上一节的 getTeammates 示例，你可以像这样返回输出和错误：


```
Copied!`1import { Function, FunctionsError, FunctionsResult } from "@foundry/functions-api";
2import { Employee } from "@foundry/ontology-api";
3
4type GetTeammatesError =
5    | FunctionsError<"EmployeeNotFoundForId", string>
6    | FunctionsError<"MultipleEmployeesFoundForId", { employees: Employee[], employeeId: string }>
7
8@Function()
9public getTeammates(employeeId: string): FunctionsResult<Employee[], GetTeammatesError> {
10    const employees = await Objects.search().employee([employeeId]).allAsync();
11    if (employees.length === 0) {
12        return FunctionsResult.err("EmployeeNotFoundForId", employeeId);
13    }
14
15    if (employees.length > 1) {
16        return FunctionsResult.err("MultipleEmployeesFoundForId", { employees, employeeId });
17    }
18
19    const employee = employees[0];
20    const teammates = await employee.teammates.allAsync();
21    return FunctionsResult.ok(teammates);
22}`
```


## [](#handle-errors-from-queries)Handle errors from queries处理查询错误


When a function with an error type is [called as a query from another repository](/docs/foundry/functions/query-functions/#call-a-query-function), it returns a `Result` type response, which can be an `ok` or `err` result.当一个带有错误类型的函数从另一个存储库作为查询调用时，它返回一个 Result 类型的响应，该响应可以是 ok 或 err 结果。


You can use the `isOk` or `isErr` type guards exported from `@foundry/functions-api` to differentiate between the two possible results. For instance, call the `getTeammates` example from the previous section, assuming you also [published it as a query](/docs/foundry/functions/query-functions/#query-decorator), and handle the response like so:您可以使用从 @foundry/functions-api 导出的 isOk 或 isErr 类型守卫来区分这两种可能的结果。例如，调用上一节的 getTeammates 示例，假设您也将其发布为查询，并像这样处理响应：


```
Copied!`1import { Function, isOk } from "@foundry/function-api";
2import { getTeammates } from "@foundry/ontology-api/queries";
3
4@Function()
5public async myFunction(employeeId: string): Promise<string> {
6    const result = await getTeammates({ employeeId });
7
8    if (isOk(result)) {
9        const teammates = result.value;
10        // Do something with "teammates" here
11        ...
12    }
13
14    // You can inspect the "name" field to case on each error by name and use the "value" field to get the error value
15    switch (result.error.name) {
16        case "EmployeeNotFoundForId": ...
17        case "MultipleEmployeesFoundForId": ...
18        case "FunctionsTypescriptExecutorService:OutOfMemoryError": ...
19        ...
20    }
21}`
```

