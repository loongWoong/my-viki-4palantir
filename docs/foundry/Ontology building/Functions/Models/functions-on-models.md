# [](#functions-on-models)Functions on models模型上的函数


You can deploy models in the context of the Ontology by using functions that invoke models during their runtime. Model functions are automatically generated wrappers around live model deployments that can be imported into a functions repository and called from your code. This enables you to add custom business logic around model predictions, integrate models with Ontology objects, or orchestrate multiple model calls.您可以通过使用在运行时调用模型的函数，在 Ontology 的上下文中部署模型。模型函数是自动生成的、围绕实时模型部署的包装器，可以导入到函数仓库中，并在您的代码中调用。这使您能够在模型预测周围添加自定义业务逻辑，将模型与 Ontology 对象集成，或协调多个模型调用。


## [](#overview)Overview概述


Model functions can be published from two types of deployments:模型函数可以从两种类型的部署中发布：


- **[Direct model deployments](/docs/foundry/manage-models/create-a-model-deployment/):** Published directly from the model page.直接模型部署：直接从模型页面发布。
- **[Modeling Objective live deployments](/docs/foundry/manage-models/set-up-live/):** Published from the deployment details page in a Modeling Objective.建模目标实时部署：从建模目标中的部署详情页面发布。


Both methods create a function with the same input and output API as your model. For details on function behavior, version upgrades, and configuration options, see the [Model functions developer guide](/docs/foundry/model-integration/model-functions-guide/).这两种方法都会创建一个与您的模型具有相同输入和输出 API 的函数。有关函数行为、版本升级和配置选项的详细信息，请参阅模型函数开发者指南。


Model functions are fully supported in TypeScript v1, TypeScript v2, and Python functions.模型函数在 TypeScript v1、TypeScript v2 和 Python 函数中完全受支持。


## [](#import-a-live-deployment-in-a-repository)Import a live deployment in a repository导入仓库中的实时部署


Once a function for a live deployment has been created either [on the model itself](/docs/foundry/manage-models/create-a-model-deployment/#3-publish-a-function-for-the-deployment) or in a [modeling objective](/docs/foundry/manage-models/set-up-live/#publish-function), it must be imported for usage in a specific repository. Select **Add** and **Query Functions** in the **Resource Imports** menu on the left side bar in the repository. Models are searchable by the function name that was chosen during publishing. Note that Python and TypeScript v2 repositories only support model functions that are tied to an ontology, as described in the section below.一旦为实时部署创建了函数，无论是在模型本身还是在建模目标中，都必须将其导入到特定仓库中以供使用。在仓库左侧栏的资源导入菜单中选择“添加和查询函数”。模型可以通过在发布时选择的函数名称进行搜索。请注意，Python 和 TypeScript v2 仓库仅支持与本体关联的模型函数，如下一节所述。


Notes注意事项For TypeScript v1 repositories, it is also possible to import a model function by selecting **Models**, which is functionally equivalent to importing it under **Query Functions**.对于 TypeScript v1 仓库，也可以通过选择“模型”来导入模型函数，其功能等效于在“查询函数”下导入。

Legacy function on models that use the **API Name** card in Modeling Objectives instead of the preferred [model publication dialog](/docs/foundry/manage-models/set-up-live/#publish-function) can still be imported under the **Modeling Objectives** section, but are being sunset.在建模目标中使用 API 名称卡而不是首选模型发布对话框的模型上的旧函数仍然可以导入到建模目标部分，但正在逐步淘汰。


## [](#ontology-or-space-bound-functions)Ontology or space-bound functions本体或空间限制函数


Starting from February 2026 onwards, all new model functions will be tied to an ontology. This is a prerequisite for usage in TypeScript v2 and Python functions, which only allow ontology resource imports. Prior to this date, model functions were tied to the model's [space](/docs/foundry/security/orgs-and-spaces/). TypeScript v1 allows importing both types of model functions, but the import and usage semantics vary slightly as [detailed below](#if-the-function-is-registered-to-an-ontology).从 2026 年 2 月开始，所有新的模型函数都将与一个本体绑定。这是在 TypeScript v2 和 Python 函数中使用的前提条件，这些函数只允许导入本体资源。在此日期之前，模型函数与模型的空間绑定。TypeScript v1 允许导入这两种类型的模型函数，但导入和使用语义略有不同，如下所述。


To check if a function is bound to an ontology, navigate to your model: model functions that are not bound to an ontology will indicate that a migration is available. [Learn more on migrating your function to be ontology-bound](#migrating-model-functions-to-ontology-bound-functions).要检查一个函数是否与本体绑定，请导航到您的模型：未与本体绑定的模型函数将显示可进行迁移。了解更多关于将您的函数迁移为与本体绑定的信息。


## [](#call-a-model-function-from-python-or-typescript-v2-functions)Call a model function from Python or TypeScript v2 functions从 Python 或 TypeScript v2 函数中调用模型函数


Once a function for a live deployment has been created, it must be imported for usage in a specific repository. It can then be queried [like any query function](/docs/foundry/functions/query-functions/#call-a-query-function).一旦为实时部署创建了函数，就必须将其导入到特定存储库中以供使用。然后，它就像任何查询函数一样可以被查询。


### [](#example-code-python)Example code: Python示例代码：Python


```
Copied!`1from functions.api import function, Double
2from foundry_sdk_runtime import AllowBetaFeatures
3from ontology_sdk import FoundryClient
4from ontology_sdk.ontology.objects import Flight
5
6
7@function
8def predict_flight_delays(flight: Flight) -> Double:
9    # Prepare the input to match the model function's API.
10    with AllowBetaFeatures():
11        model_output = FoundryClient().ontology.queries.flight_model_deployment(
12            df_in=[
13                {
14                    "lastArrivalTime": flight.last_arrival_time,
15                    "lastExpectedArrivalTime": flight.last_expected_arrival_time,
16                },
17            ]
18        )
19        return model_output.df_out[0].prediction`
```


### [](#example-code-typescript-v2)Example code: TypeScript v2示例代码：TypeScript v2


```
Copied!`1import { Client } from "@osdk/client";
2import { Double } from "@osdk/functions";
3import { flightModelDeployment, Flight } from "@ontology/sdk";
4
5async function predictFlightDelays(client: Client, flight: Flight): Promise<Double> {
6    // Prepare the input to match the model function's API.
7    const modelOutput = await client(flightModelDeployment).executeFunction({
8        "df_in": [
9            {
10                "lastArrivalTime": flight.lastArrivalTime,
11                "lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
12            },
13        ]
14    });
15    return modelOutput.df_out[0].prediction;
16}
17
18export default predictFlightDelays;`
```


## [](#write-a-model-backed-typescript-v1-function)Write a model-backed TypeScript v1 function编写一个基于模型的 TypeScript v1 函数


### [](#if-the-model-function-is-registered-to-a-space)If the model function is registered to a space如果模型函数注册到某个空间


We first need to import the function:我们首先需要导入该函数：


```
Copied!`1// If the model function is tied to a space and not to an ontology,
2// copy the import snippet from the Resource imports sidebar.`
```


Then, write a function that takes a flight, prepares data for the model, and interprets the result of the model execution. The model is imported as an asynchronous function that respects the [model's input and output specification or API](/docs/foundry/integrate-models/model-adapter-api/). From this, TypeScript can ensure, at compile time, that the correct data structure is sent to and received from the model deployment.然后，编写一个函数，该函数接收一个飞行任务，为模型准备数据，并解释模型执行的结果。模型被导入为异步函数，它遵循模型的输入和输出规范或 API。由此，TypeScript 可以在编译时确保正确的数据结构被发送到模型部署，并从模型部署中接收。


Note that if your Model's API expects a single tabular input and output, the associated function will accept single TypeScript objects with properties corresponding to the columns specified for the input if the [**Enable row-wise processing** option](/docs/foundry/model-integration/model-functions-guide/#row-wise-publishing) is enabled, which is the default. Alternatively, consider [using an Object or ObjectSet directly in the Model API](/docs/foundry/integrate-models/model-adapter-reference/#for-object-inputs) to facilitate use of your Model with Objects in functions.请注意，如果您的 Model 的 API 期望单个表格输入和输出，并且启用了按行处理选项（默认情况下已启用），则相关函数将接受具有与输入指定的列对应的属性的 TypeScript 对象。或者，您可以直接在 Model API 中使用 Object 或 ObjectSet，以方便在函数中使用您的 Model 处理对象。


```
Copied!`1@Function()
2public async predictFlightDelaysRowWise(flight: Flight): Promise<Double> {
3    // Prepare the input to match the model function's API.
4    // This model function expects a single flight.
5    // If you'd like to process multiple flights at a time,
6    // edit your model function and uncheck "Enable row-wise processing".
7
8    // Note you can also use an Object directly in the model API
9    // to avoid tedious mapping between a model API and an object type's properties.
10    const modelInput = {
11        "lastArrivalTime": flight.lastArrivalTime,
12        "lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
13    };
14    // Call the Live deployment.
15    const modelOutput = await FlightModelDeploymentRowWise(modelInput);
16    return modelOutput.prediction;
17}
18
19
20@Function()
21public async predictFlightDelays(flights: Flight): Promise<FunctionsMap<Flight, Double>> {
22    let functionsMap = new FunctionsMap();
23    // Prepare the input to match the model function's API,
24    // for the case where row-wise processing is not enabled.
25
26    // Note you can also use an ObjectSet directly in the model API
27    // to avoid tedious mapping between a model API and an object type's properties.
28    const dfIn = flights.map(flight => ({
29        "lastArrivalTime": flight.lastArrivalTime,
30        "lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
31    }));
32    // Call the Live deployment.
33    const modelOutput = await FlightModelDeployment(
34        {"df_in": dfIn}
35    );
36    for (let i = 0; i < flights.length; i++) {
37        functionsMap.set(flights[i], modelOutput.df_out[i].prediction);
38    }
39    return functionsMap;
40}`
```


Note the above example assumes the following Model API:请注意，上述示例假设以下模型 API：


```
Copied!`1import palantir_models as pm
2
3
4class ExampleModelAdapter(pm.ModelAdapter):
5    ...
6
7    @classmethod
8    def api(cls):
9        inputs = {
10            "df_in": pm.Pandas(columns=[("lastArrivalTime", datetime.datetime), ("lastExpectedArrivalTime", datetime.datetime)])
11        }
12        outputs = {
13            "df_out": pm.Pandas(columns=[("prediction", float)])
14        }
15        return inputs, outputs
16    ...`
```


### [](#if-the-function-is-registered-to-an-ontology)If the function is registered to an ontology如果该函数注册到一个本体


In this case, both the import and the query syntax need to be updated as detailed by the comments in the snippet below:在这种情况下，导入和查询语法都需要根据下面代码片段中的注释进行更新：


```
Copied!`1import { Function, Double } from "@foundry/functions-api";
2// Add the Queries import to use an ontology-bound model function
3import { Queries, Flight } from "@foundry/ontology-api";
4
5export class MyFunctions {
6    @Function()
7    public async predictFlightDelays(flight: Flight): Promise<Double> {
8        // Call your model by API Name from Queries
9        const modelOutput = await Queries.flightModelDeployment({
10            "df_in": [
11                {
12                    "lastArrivalTime": flight.lastArrivalTime,
13                    "lastExpectedArrivalTime": flight.lastExpectedArrivalTime,
14                },
15            ]
16        });
17        return modelOutput.df_out[0].prediction;
18    }
19}`
```


### [](#migrating-model-functions-to-ontology-bound-functions)Migrating model functions to ontology-bound functions将模型函数迁移到本体绑定函数


When you migrate a space-bound model function to an ontology-bound function from the user interface, existing published versions of TypeScript v1 functions that use the model will continue to work. However, the import syntax will no longer be recognized, meaning preview and tagging new releases of the repository consuming the model function will no longer work.当您从用户界面将一个空间绑定模型函数迁移到一个本体绑定函数时，使用该模型的现有已发布的 TypeScript v1 函数版本将继续正常工作。但是，导入语法将不再被识别，这意味着预览和标记使用该模型函数的存储库的新版本将不再起作用。


To update your TypeScript v1 function after migration:迁移后要更新您的 TypeScript v1 函数：


1. Open your code repository and select the **Resource imports** sidebar.打开您的代码存储库并选择资源导入侧边栏。
2. Select the newly created version of the model function, by updating the resources.json file to the new version.通过更新 resources.json 文件到新版本来选择新创建的模型函数版本。
3. Update your function code to use the query function syntax as detailed above, or see the dedicated documentation on [calling a query function](/docs/foundry/functions/query-functions/#call-a-query-function) for more details.更新您的函数代码以使用上述详细说明的查询函数语法，或查看有关调用查询函数的专用文档以获取更多详细信息。


Direct model function usage through the [Foundry Platform SDK](/docs/foundry/dev-toolchain/overview/#platform-sdks) and the [Functions.Query ↗](https://github.com/palantir/foundry-platform-python/blob/develop/docs/v2/Functions/Query.md) method will break immediately upon migration. This is because this consumption pattern refers to the function by its API name, which is migrated globally across all model function versions at once. To remediate these consumers, update the API name to its new value after the migration.通过 Foundry Platform SDK 和 Functions.Query ↗方法直接使用模型函数将在迁移时立即中断。这是因为这种使用模式通过其 API 名称引用函数，该 API 名称将在所有模型函数版本中一次性全局迁移。为解决这些消费者问题，请在迁移后更新 API 名称为其新值。


## [](#performance-considerations)Performance considerations性能考量


Models are executed as part of the runtime of the function, therefore all standard [limits](/docs/foundry/functions/manage-functions/#enforced-limits) apply.
If your function backs an Action, there are [further limits](/docs/foundry/action-types/scale-property-limits/#edit-limits) on the number of resulting edits.
When calling live deployments, model input and output data is sent through the network with an upper limit of 50 MB. Including that additional throughput, the total execution time of the function cannot exceed 30 seconds. If you wish to increase this timeout limit per function, contact your Palantir representative.模型作为函数运行时的一部分执行，因此所有标准限制都适用。如果你的函数支持一个 Action，那么生成的编辑数量还有进一步的限制。在调用实时部署时，模型输入和输出数据通过网络传输，上限为 50 MB。考虑到额外的吞吐量，函数的总执行时间不能超过 30 秒。如果你希望为每个函数增加这个超时限制，请联系你的 Palantir 代表。

