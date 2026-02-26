# [](#legacy-language-models-within-functions)Legacy language models within functions函数内的传统语言模型


Legacy传统This is documentation for the **legacy** language models within functions. The [updated language models in functions](/docs/foundry/functions/language-models/) offer more robust capabilities, such as vision and streaming. [Upgrade your language models in functions](/docs/foundry/functions/language-models/#upgrade-from-legacy-language-models-within-functions) to take advantage of the latest AIP offerings.这是关于函数内传统语言模型的文档。函数中的更新语言模型提供了更强大的功能，如视觉和流式传输。升级函数中的语言模型，以利用最新的 AIP 服务。


Palantir provides a set of language models which can be used within functions. [Read more about Palantir-provided LLMs](/docs/foundry/aip/supported-llms/).Palantir 提供了一套可在函数内使用的语言模型。了解更多关于 Palantir 提供的 LLMs 的信息。


Prerequisites先决条件To use Palantir-provided language models, [AIP must first be enabled on your enrollment](/docs/foundry/aip/enable-aip-features/). You also must have permissions to use [AIP builder capabilities](/docs/foundry/aip/aip-features/#aip-applications-and-builder-capabilities).要使用 Palantir 提供的语言模型，您必须在注册时启用 AIP。您还必须拥有使用 AIP 构建器功能的权限。


## [](#import-a-language-model)Import a language model导入语言模型


To begin using a language model, you must import the specific model into the code repository where you are writing your functions by following the steps below:要开始使用语言模型，您必须按照以下步骤将特定模型导入您编写函数的代码库：


1. Navigate and open the **Model Imports** side panel to view all existing imported models.导航并打开模型导入的侧边栏，以查看所有已导入的模型。


![Model import sidebar.](language-model-import-sidebar.png?width=400)


1. To import a new language model, select **Add** in the top-right corner of the **Resource Imports** panel and select **Models**. This will open a new window where you will be able to view the Palantir-provided models that are available to you.要导入新的语言模型，请在资源导入面板的右上角选择添加，然后选择模型。这将打开一个新窗口，您可以在其中查看可供您使用的 Palantir 提供的模型。


![Model import dialog showing a few Palantir-provided LLMs.](language-model-import-dialog.png?width=600)


1. You will also see a tab where you can view custom models which have been created through the Modeling Objectives app or direct model deployments previously. More information on using those models can be found in the [functions on models](/docs/foundry/functions/functions-on-models/) documentation.你还将看到一个选项卡，可以在其中查看通过建模目标应用程序创建的自定义模型或之前直接部署的模型。有关使用这些模型的信息，可以在模型文档中的功能上找到。
2. Select the models you would like to import, then select **Confirm selection** to import these models into your repository. Task runner will execute the `localDev` task, generating code bindings to interact with these models.选择您想要导入的模型，然后选择“确认选择”将这些模型导入到您的仓库中。任务运行器将执行 localDev 任务，生成与这些模型交互的代码绑定。
3. After importing the language models, you can now use them in your repository by adding the following import statement, replacing GPT_4o with the name of the language model you have imported into your repository:导入语言模型后，您可以通过添加以下导入语句在您的仓库中使用它们，将 GPT_4o 替换为您导入到仓库中的语言模型的名称：


```
Copied!`1import { GPT_4o } from "@foundry/models-api/language-models"`
```


## [](#writing-a-function-that-uses-a-language-model)Writing a function that uses a language model编写一个使用语言模型的函数


At this stage, we can now write a function that uses a language model we imported. For this example, we assume that we have imported GPT_4o as described above.在这个阶段，我们现在可以编写一个使用我们导入的语言模型的函数。在这个例子中，我们假设我们按照上述方法导入了 GPT_4o。


We begin by adding the following import statement to our file:我们首先在文件中添加以下导入语句：


```
Copied!`1import { GPT_4o } from "@foundry/models-api/language-models"`
```


Each language model will have generated methods available with strongly typed inputs and outputs. For example, the GPT_4o model provides a createChatCompletion method which allows the user to pass a set of messages along with additional parameters to modify the model’s behavior, such as the temperature or maximum number of tokens.每个语言模型都将提供生成方法，这些方法具有强类型的输入和输出。例如，GPT_4o 模型提供了一个 createChatCompletion 方法，允许用户传递一组消息以及额外的参数来修改模型的行为，例如温度或最大令牌数。


In the following illustrative example, we use the provided GPT_4o model to run a simple sentiment analysis on a piece of text provided by a user. The function will classify the text as "Good", "Bad", or "Uncertain".在以下示例中，我们使用提供的 GPT_4o 模型对用户提供的文本进行简单的情感分析。该函数将文本分类为 "Good"、"Bad" 或 "Uncertain"。


```
Copied!`1@Function()
2public async sentimentAnalysis(userPrompt: string): Promise<string> {
3    const systemPrompt = "Provide an estimation of the sentiment the text the user has provided. \
4    You may respond with either Good, Bad, or Uncertain. Only choose Good or Bad if you are overwhelmingly \
5    sure that the text is either good or bad. If the text is neutral, or you are unable to determine, choose Uncertain."
6
7    const systemMessage = { role: "SYSTEM", contents: [{ text: systemPrompt }] };
8    const userMessage = { role: "USER", contents: [{ text: userPrompt }] };
9    const gptResponse = await GPT_4o.createChatCompletion({messages: [systemMessage, userMessage], params: { temperature: 0.7 } });
10    return gptResponse.choices[0].message.content ?? "Uncertain";
11}`
```


This function can then be used throughout the platform.这个功能可以在整个平台上使用。


## [](#embeddings)Embeddings嵌入向量


Along with generative language models, Palantir also provides models which can be used to generate embeddings. A simple example is as follows:除了生成式语言模型，Palantir 还提供可用于生成嵌入的模型。一个简单的例子如下：


```
Copied!`1@Function()
2public async generateEmbeddingsForText(inputs: string[]): Promise<Double[][]> {
3    const response = await TextEmbeddingAda_002.createEmbeddings({ inputs });
4    return response.embeddings;
5}`
```


This is most commonly used to perform [semantic search](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/) workflows.这通常用于执行语义搜索工作流。


## [](#performance-considerations)Performance considerations性能考量


Certain models may have rate limits applied to them, limiting the number of tokens which may be passed over a certain time period. This will be enforced along with any standard limits that apply to functions.某些模型可能受到速率限制，限制在特定时间段内可以传递的 token 数量。这将和适用于函数的标准限制一起执行。


---


Note: AIP feature availability is subject to change and may differ between customers.注意：AIP 功能可用性可能会发生变化，并且可能因客户而异。

