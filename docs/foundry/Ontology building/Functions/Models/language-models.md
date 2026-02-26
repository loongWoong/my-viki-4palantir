# [](#language-models-within-functions)Language models within functions函数内的语言模型


Palantir provides a set of language models which can be used within functions. [Read more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).Palantir 提供了一套可在函数内使用的语言模型。了解更多关于 Palantir 提供的 LLMs 的信息。


Prerequisites前提条件To use Palantir-provided language models, [AIP must first be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You must also have permissions to use [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities).要使用 Palantir 提供的语言模型，您的注册必须首先启用 AIP。您还必须拥有使用 AIP 构建器功能的权限。


Palantir provides a set of language models which can be used within functions. [Read more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).Palantir 提供了一套可在函数中使用的语言模型。了解更多关于 Palantir 提供的 LLMs。


## [](#import-a-language-model)Import a language model导入语言模型


To begin using a language model, you must import the specific model into the code repository where you are writing your functions by following the steps below:要开始使用语言模型，您必须按照以下步骤将特定模型导入您编写函数的代码库：


1. Navigate and open the **Model Imports** side panel to see all existing imported models.导航并打开模型导入侧边栏，以查看所有已导入的模型。


![Model import sidebar.](v3-lms-functions-import-sidebar.png?width=400)


1. To import a new language model, select **Add** in the upper right corner of the **Resource Imports** panel, then select **Models**. This will open a new window where you will be able to see Palantir-provided models that are available to you.要导入新的语言模型，请在资源导入面板的右上角选择“添加”，然后选择“模型”。这将打开一个新窗口，您可以在其中看到可供您使用的 Palantir 提供的模型。


![Model import dialog showing a few Palantir-provided LLMs.](v3-lms-functions-import-dialog.png?width=600)


1. You will also see a tab where you can view custom models created through the Modeling Objectives application or direct model deployments previously. More information on using those models can be found in the [functions on models](/docs/foundry/functions/functions-on-models/) documentation.您还会看到一个标签，可以在其中查看通过建模目标应用程序创建的自定义模型或之前直接部署的模型。有关使用这些模型的信息，请参阅模型文档中的功能。
2. Choose the models you would like to import, then select **Confirm selection** to import these models into your repository. Task runner will execute the `localDev` task, generating code bindings to interact with these models.选择您要导入的模型，然后选择“确认选择”将这些模型导入您的仓库。任务运行器将执行 localDev 任务，生成与这些模型交互的代码绑定。
3. After importing the language models, select the model in the sidebar to view the detailed capabilities offered by this model. You can also copy code snippets to help you import and author functions with the model.导入语言模型后，请在侧边栏中选择该模型，以查看该模型提供的详细功能。您还可以复制代码片段，以帮助您使用该模型导入和编写函数。


![Model details in sidebar.](v3-lms-functions-sidebar-detail.png?width=400)


## [](#write-a-function-that-uses-a-language-model)Write a function that uses a language model编写一个使用语言模型的函数


At this stage, you can now write a function that uses the language model you imported. For this example, assume that you imported GPT-4.1.在这个阶段，你现在可以编写一个使用你导入的语言模型的函数。在这个例子中，假设你导入的是 GPT-4.1。


Begin by adding the following import statement to your file:首先，将以下导入语句添加到您的文件中：


```
Copied!`1import { Function } from "@foundry/functions-api";
2import { Gpt41 } from "@foundry/languagemodelservice/models";`
```


Each language model will have generated methods available with strongly typed inputs and outputs. For example, the GPT-4.1 model provides `createChatCompletion`, `createChatVisionCompletion`, and `createChatCompletionStreamed` as different APIs to interact with the model. The list of capabilities could expand in later versions of the imported model.每个语言模型都将提供具有强类型输入和输出的生成方法。例如，GPT-4.1 模型提供了 createChatCompletion 、 createChatVisionCompletion 和 createChatCompletionStreamed 作为与模型交互的不同 API。导入模型后续版本的功能列表可能会扩展。


In the following illustrative example, the provided GPT_4o model is used to run a simple sentiment analysis on a piece of text or image provided by a user. The function will classify the text as "Good", "Bad", or "Uncertain".在以下示例中，提供的 GPT_4o 模型用于对用户提供的文本或图像进行简单的情感分析。该函数将文本分类为"好"、"坏"或"不确定"。


```
Copied!`1const SYSTEM_PROMPT =
2    "Provide an estimation of the sentiment the text the user has provided. \
3You may respond with either Good, Bad, or Uncertain. Only choose Good or Bad if you are overwhelmingly \
4sure that the text is either good or bad. If the text is neutral, or you are unable to determine, choose Uncertain.";
5
6export class MyFunctions {
7    @Function()
8    public async llmFunction_createChatCompletion(userPrompt: string): Promise<string | undefined> {
9        const response = await Gpt41.createChatCompletion({
10            messages: [
11                {
12                    role: "SYSTEM",
13                    content: SYSTEM_PROMPT,
14                },
15                {
16                    role: "USER",
17                    content: userPrompt,
18                },
19            ],
20            params: {
21                temperature: 0,
22            },
23        });
24        return response.type === "ok" ? response.value.completion : "error";
25    }
26
27    @Function()
28    public async llmFunction_createChatVisionCompletion(
29        userPrompt: string,
30        pngBase64String: string,
31    ): Promise<string | undefined> {
32        const response = await Gpt41.createChatVisionCompletion({
33            messages: [
34                {
35                    role: "USER",
36                    content: [
37                        { type: "text", text: userPrompt },
38                        {
39                            type: "genericMedia",
40                            genericMedia: {
41                                mimeType: "IMAGE_PNG",
42                                // Base64 encoded PNG String
43                                content: pngBase64String,
44                            },
45                        },
46                    ],
47                },
48            ],
49            params: {
50                temperature: 0,
51            },
52        });
53        return response.type === "ok" ? response.value.completion : "error";
54    }
55}`
```


This function can then be used throughout the platform.这个功能可以在整个平台上使用。


## [](#embeddings)Embeddings嵌入向量


Along with generative language models, Palantir also provides models that can be used to generate embeddings. A simple example is as follows:除了生成式语言模型，Palantir 还提供可用于生成嵌入向量的模型。一个简单的例子如下：


```
Copied!`1@Function()
2public async llmFunction_embeddings(inputs: string[]): Promise<Double[][]> {
3    const response = await Textembedding3large.createEmbeddings({ inputs });
4    return response.type === "ok" ? response.value.embeddings : [[]];
5}`
```


This is most commonly used to perform [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) workflows.这通常用于执行语义搜索工作流。


## [](#upgrade-from-legacy-language-models-within-functions)Upgrade from legacy language models within functions在函数中升级到旧版语言模型


Skip this step if you are starting from a new repository with no [legacy language models](/docs/foundry/functions/language-models-legacy/) imported.如果你从一个没有导入遗留语言模型的新存储库开始，请跳过此步骤。


The following process will result in a compile-time break in your code repository, as the code syntax will be updated. Refer to the code snippets in the sidebar for each updated model to update your code.此过程将导致你的代码存储库在编译时出现中断，因为代码语法将被更新。请参考每个更新模型的侧边栏代码片段来更新你的代码。


The updated language models in functions offer more advanced capabilities, such as better support for vision and streaming. We highly recommend upgrading your repository to take advantage of the latest AIP offerings.函数中的更新语言模型提供了更高级的功能，例如更好的视觉支持和流媒体支持。我们强烈建议升级你的存储库以利用最新的 AIP 产品。


1. If you have existing [legacy language models](/docs/foundry/functions/language-models-legacy/) imported, a warning icon to upgrade will appear in the sidebar. Choose **Select imports** to open the model import dialog.如果你已经导入了现有的遗留语言模型，侧边栏将出现一个升级警告图标。选择选择导入以打开模型导入对话框。


![Model imports warning in sidebar.](v3-lms-functions-migration-sidebar.png?width=400)


1. In the model import dialog, select **Fix** to remove any deprecated legacy language models.在模型导入对话框中，选择“修复”以移除任何已弃用的旧语言模型。


![Model import dialog with warning.](v3-lms-functions-migration-dialog-warning.png?width=400)


1. Reselect the models to migrate to the updated language model versions. You can view additional capabilities supported by this version in the details panel in the center of the dialog.重新选择要迁移到更新语言模型版本的模型。您可以在对话框中心的详细信息面板中查看此版本支持的其他功能。


![Model import dialog shows removed models.](v3-lms-functions-migration-dialog-selected.png?width=400)


1. Now, you can view the updated model imports in the sidebar. Selecting a model will show you a details panel with code snippets to help you update your code to take advantage of the additional capabilities.现在，您可以在侧边栏中查看更新的模型导入。选择一个模型将显示一个详情面板，其中包含代码片段，以帮助您更新代码以利用额外的功能。


![Model details and code snippet in sidebar.](v3-lms-functions-sidebar-detail.png?width=400)


## [](#performance-considerations)Performance considerations性能考量


Certain models may have rate limits applied, limiting the number of tokens that may be passed over a certain time period. This will be enforced along with any standard limits that apply to functions.某些模型可能会应用速率限制，限制在特定时间段内可以传递的令牌数量。这将与适用于函数的标准限制一起执行。


---


Note: AIP feature availability is subject to change and may differ between customers.注意：AIP 功能可用性可能会发生变化，并且可能因客户而异。

