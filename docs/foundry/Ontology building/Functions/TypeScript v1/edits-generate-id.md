# [](#generate-unique-ids-for-new-objects)Generate unique IDs for new objects为新对象生成唯一 ID


When writing an [Ontology edit function](/docs/foundry/functions/edits-overview/) that creates objects, you may want to generate a unique ID for the newly created object. You can set this up in functions by using the `@foundry/functions-utils` package to generate a globally unique identifier.在编写创建对象的本体编辑函数时，您可能希望为新创建的对象生成一个唯一 ID。您可以通过使用 @foundry/functions-utils 包来在函数中设置生成全局唯一标识符。


## [](#import-the-package)Import the package导入包


The `@foundry/functions-utils` package is installed by default, but if the package is not present in the `package.json` file:@foundry/functions-utils 包默认已安装，但如果 package.json 文件中不存在该包：


- In the `"dependencies"` section, add `"@foundry/functions-utils": "0.1.0"`在 "dependencies" 部分，添加 "@foundry/functions-utils": "0.1.0"


As mentioned in the [documentation on adding dependencies](/docs/foundry/functions/add-dependencies/), remember to restart Code Assist to have the new package available for autocomplete.如添加依赖项的文档所述，请记得重启代码辅助功能，以便新包可用于自动补全。


## [](#use-the-package-in-code)Use the package in code在代码中使用该包


To generate a unique ID, you can use the `Uuid.random()` utility function from the `@foundry/functions-utils` package. The below code example shows how you could use the `random` function in an example Ontology edit function.要生成唯一 ID，您可以使用 Uuid.random() 包中的 @foundry/functions-utils 实用函数。下面的代码示例展示了如何在示例本体编辑函数中使用 random 函数。


```
Copied!`1import { OntologyEditFunction, Timestamp } from "@foundry/functions-api";
2import { Objects } from "@foundry/ontology-api";
3import { Uuid } from "@foundry/functions-utils";
4
5export class ExampleEditFunctions {
6    @Edits(FlightScenario)
7    @OntologyEditFunction()
8    public createFlightScenario(): void {
9        const scenario = Objects.create().flightScenarios(Uuid.random());
10        scenario.scenarioName = "New scenario";
11        scenario.creationTime = Timestamp.now();
12    }
13}`
```

