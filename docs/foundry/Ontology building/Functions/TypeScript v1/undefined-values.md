# [](#handle-undefined-values)Handle undefined values处理未定义值


Below are two useful patterns for handling `undefined` values which may be returned from accessing properties or links.以下是两个处理从访问属性或链接可能返回的 undefined 值的实用模式。


### [](#explicit-checks)Explicit checks显式检查


```
Copied!`1@Function()
2public getFullName(employee: Employee): string {
3    if (!(employee.firstName && employee.lastName)) {
4        throw new UserFacingError("Cannot derive full name because either first or last name is undefined.");
5    }
6    return employee.firstName + " " + employee.lastName;
7}`
```


By checking that both the `firstName` and `lastName` fields are defined, the TypeScript compiler knows that the final line with the `return` statement can compile correctly. The benefit of this approach is that type checking is more explicit, and in the case where `undefined` values are present, you can throw a more explicit error about what went wrong.通过检查 firstName 和 lastName 字段都已被定义，TypeScript 编译器知道带有 return 语句的最后一行可以正确编译。这种方法的优点是类型检查更加明确，在存在 undefined 值的情况下，你可以抛出更明确的错误信息说明出了什么问题。


### [](#non-null-assertion-operator)Non-null assertion operator非空断言运算符


You can use the TypeScript [non-null assertion operator ↗](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html#non-null-assertion-operator) (`!`) to ignore the `undefined` case.你可以使用 TypeScript 的非空断言运算符 ↗ ( ! ) 来忽略 undefined 的情况。


```
Copied!`1@Function()
2public getFullName(employee: Employee): string {
3    return employee.firstName! + " " + employee.lastName!;
4}`
```


This approach simply overrides the TypeScript compiler and asserts that the fields you're accessing are defined. Although this makes for more concise code, this can lead to cryptic errors in the case when one of the fields turns out to be `undefined`. We recommend making explicit checks when possible.这种方法简单地覆盖了 TypeScript 编译器，并断言你访问的字段是已定义的。虽然这使得代码更加简洁，但在某个字段实际上是 undefined 的情况下，这可能会导致难以理解的错误。我们建议在可能的情况下进行显式检查。

