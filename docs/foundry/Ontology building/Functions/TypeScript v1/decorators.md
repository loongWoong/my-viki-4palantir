# [](#decorators)Decorators装饰器


[TypeScript ↗](https://www.typescriptlang.org/docs/handbook/basic-types.html) functions are declared as methods of a [TypeScript class ↗](https://www.typescriptlang.org/docs/handbook/classes.html). There are a few requirements for a function to be discovered and published:TypeScript ↗ 函数被声明为 TypeScript 类 ↗ 的方法。一个函数要被发现和发布，有几个要求：


- The method must be `public`该方法必须是 public
- The class the method belongs to must be exported from the `functions-typescript/src/index.ts` file该方法所属的类必须从 functions-typescript/src/index.ts 文件中导出
- The method must be decorated with one of the following decorators imported from the `@foundry/functions-api` package:
该方法必须使用 @foundry/functions-api 包中导入的以下装饰器之一进行装饰：- `@Function()` for generic functions.@Function() 用于通用函数。
- [`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) for functions that will back an Action.
@OntologyEditFunction() 用于将支持 Action 的函数。- Object provenance information may be optionally specified with the `@Edits([object type])` decorator when using the[`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) method.在使用 @OntologyEditFunction() 方法时，可选择使用 @Edits([object type]) 装饰器指定对象来源信息。
- Object provenance information will be inferred on a best-efforts basis using the static analysis of code if the `@Edits([object type])` decorator is absent.如果没有 @Edits([object type]) 装饰器，将基于代码的静态分析以最佳努力方式推断对象来源信息。
  - Object provenance information may be optionally specified with the `@Edits([object type])` decorator when using the[`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) method.在使用 @OntologyEditFunction() 方法时，可选择使用 @Edits([object type]) 装饰器指定对象来源信息。
  - Object provenance information will be inferred on a best-efforts basis using the static analysis of code if the `@Edits([object type])` decorator is absent.如果没有 @Edits([object type]) 装饰器，将基于代码的静态分析以最佳努力方式推断对象来源信息。
  
  - `@Query({ apiName: "userDefinedAPIName"})` for read-only queries that you want to execute through [Foundry API](/docs/foundry/api/general/overview/introduction/). Note that this decorator should not be used in addition to the `@Function` decorator; it should be used on its own.@Query({ apiName: "userDefinedAPIName"}) 用于需要通过 Foundry API 执行的只读查询。请注意，此装饰器不应与 @Function 装饰器一起使用；它应该单独使用。
  - `@Function()` for generic functions.@Function() 用于通用函数。
  - [`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) for functions that will back an Action.
  @OntologyEditFunction() 用于将支持 Action 的函数。- Object provenance information may be optionally specified with the `@Edits([object type])` decorator when using the[`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) method.在使用 @OntologyEditFunction() 方法时，可选择使用 @Edits([object type]) 装饰器指定对象来源信息。
  - Object provenance information will be inferred on a best-efforts basis using the static analysis of code if the `@Edits([object type])` decorator is absent.如果没有 @Edits([object type]) 装饰器，将基于代码的静态分析以最佳努力方式推断对象来源信息。
    - Object provenance information may be optionally specified with the `@Edits([object type])` decorator when using the[`@OntologyEditFunction()`](/docs/foundry/functions/api-ontology-edits/) method.在使用 @OntologyEditFunction() 方法时，可选择使用 @Edits([object type]) 装饰器指定对象来源信息。
    - Object provenance information will be inferred on a best-efforts basis using the static analysis of code if the `@Edits([object type])` decorator is absent.如果没有 @Edits([object type]) 装饰器，将基于代码的静态分析以最佳努力方式推断对象来源信息。
    
    - `@Query({ apiName: "userDefinedAPIName"})` for read-only queries that you want to execute through [Foundry API](/docs/foundry/api/general/overview/introduction/). Note that this decorator should not be used in addition to the `@Function` decorator; it should be used on its own.@Query({ apiName: "userDefinedAPIName"}) 用于需要通过 Foundry API 执行的只读查询。请注意，此装饰器不应与 @Function 装饰器一起使用；它应该单独使用。
  
  

Here are examples of functions that are correctly exported in this way:以下是正确以这种方式导出的函数示例：


```
Copied!`1import { Function, OntologyEditFunction, Query, Integer, Edits } from "@foundry/functions-api";
2import { Employee } from "@foundry/ontology-api";
3
4export class MyUsefulFunctions {
5    @Function()
6    public incrementNumber(x: Integer): Integer {
7        return x + 1;
8    }
9
10    @Edits(Employee)
11    @OntologyEditFunction()
12    public updateName(employee: Employee, newName: string): void {
13        employee.firstName = newName;
14    }
15
16    @Query({ apiName: "getEmployeesByName" })
17    public async getEmployeesByName(name: string): Promise<ObjectSet<Employee>> {
18        return Objects.search().employee().filter(employee => employee.firstName.exactMatch(name));
19    }
20}`
```


Any method that is private or not decorated with the relevant decorations will not be published to the function registry. This allows users to create helper functions and utilities for reuse or organization.任何私有方法或未使用相关装饰器装饰的方法都不会发布到函数注册表中。这允许用户创建辅助函数和工具以供重用或组织。


Republishing重新发布Note that each function in a TypeScript repository is uniquely defined by its class name and method name—if you change the name of the class or method, the function will be published under a new identifier.请注意，TypeScript 存储库中的每个函数都由其类名和方法名唯一定义——如果你更改类名或方法名，该函数将在新的标识符下发布。

