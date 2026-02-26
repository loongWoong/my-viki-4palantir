# [](#use-platform-apis-with-the-foundry-platform-sdk)Use platform APIs with the Foundry platform SDK使用 Foundry 平台 SDK 调用平台 API


Foundry APIs expose a variety of functionality that you can leverage with the [Foundry platform SDK](/docs/foundry/api/v2/general/overview/sdks/#foundry-platform-software-development-kits) library through functions. You can use the platform SDK to build functions for administrative or governance workflows, interact with schedules and builds, access media sets, and more.Foundry API 提供了多种功能，您可以通过函数使用 Foundry 平台 SDK 库来利用这些功能。您可以使用平台 SDK 构建用于管理或治理工作流的函数，与日程和构建进行交互，访问媒体集等。


First-class authentication is not supported for TypeScript v1 functions. We recommend using Python functions and TypeScript v2 functions for these workflows.TypeScript v1 函数不支持一级认证。我们建议使用 Python 函数和 TypeScript v2 函数来处理这些工作流。


## [](#install-the-sdk)Install the SDK安装 SDK


To install the Foundry platform SDK, navigate to the **Libraries** side panel in your code repository and search for the SDK name: `foundry-platform-sdk` for Python, or `@osdk/foundry` for TypeScript.要安装 Foundry 平台 SDK，请导航到代码存储库中的 Libraries 侧边栏，并搜索 SDK 名称：对于 Python，使用 foundry-platform-sdk ，对于 TypeScript，使用 @osdk/foundry 。


![The Libraries search panel, searching for the Python platform SDK.](platform-sdk-lib-panel-py.png?width=400)


![The Libraries search panel, searching for the TypeScript platform SDK.](platform-sdk-lib-panel-ts.png?width=400)


## [](#initialize-your-client)Initialize your client初始化客户端


Your function requires authentication to interact with Foundry APIs. This process involves instantiating an authenticated “client” through which you can make requests to the Foundry APIs through the SDK. In TypeScript v2 repositories, this requires the `@osdk/client` library, which should be pre-installed. You can verify this by looking for the green pin:您的函数需要认证才能与 Foundry API 交互。此过程涉及通过 SDK 实例化一个认证的“客户端”，您可以通过该客户端向 Foundry API 发起请求。在 TypeScript v2 存储库中，这需要 @osdk/client 库，该库应已预安装。您可以通过查找绿色图钉来验证这一点：


![The authentication library for TypeScript.](platform-sdk-lib-panel-client-ts.png?width=400)


## [](#use-platform-apis)Use platform APIs使用平台 API


Once your function is authenticated, you can start using Foundry APIs. The examples below show how to call a language model or query media sets in both Python and TypeScript:一旦您的函数通过身份验证，您就可以开始使用 Foundry API。下面的示例展示了如何在 Python 和 TypeScript 中调用语言模型或查询媒体集：


TypeScript v2Python```
Copied!`1import { Client } from "@osdk/client";
2import { Functions } from "@osdk/foundry";
3
4export default async function useLlm(
5    client: Client, // This parameter gets populated by Foundry at runtime
6    prompt: string
7): Promise<string> {
8
9    const promptMessage = [
10        {
11            role: "USER",
12            content: prompt
13        }
14    ];
15    const result = await Functions.Queries.execute(
16        client,
17        "com.foundry.languagemodelservice.models.gpt41.CreateChatCompletion",
18        {
19            parameters: {
20                messages: promptMessage
21            }
22        },
23        {
24            preview: true, // Required only for unstable endpoints, see API reference
25        }
26    );
27    return result.value["completion"] as string;
28}`
```

```
Copied!`1from foundry_sdk import FoundryClient
2
3@function
4def media_item_to_base64(media_item_rid: str, media_set_rid: str) -> str:
5    foundry_client = FoundryClient()
6
7    result = foundry_client.media_sets.MediaSet.read(
8        media_set_rid=media_set_rid,
9        media_item_rid=media_item_rid,
10        preview=True  # Required only for unstable endpoints, see API reference
11    )
12
13    # Convert the binary stream to a base64 encoded string
14    base64_encoded = base64.b64encode(result).decode('utf-8')
15
16    return base64_encoded`
```


### [](#client-permissions)Client permissions客户端权限


The TypeScript v2 client (passed to the function by Foundry at runtime) and the Python client initialized in code have the following permissions scope:TypeScript v2 客户端（由 Foundry 在运行时传递给函数）和代码中初始化的 Python 客户端具有以下权限范围：


- `api:admin-read`
- `api:functions-read`
- `api:ontologies-read`
- `api:orchestration-read`
- `api:usage:mediasets-read`
- `api:usage:ontologies-write`


Each platform API endpoint requires certain scopes to hit the endpoint. Documentation on these scopes can be found in the [API reference](/docs/foundry/api/v2)每个平台 API 端点需要特定的权限才能访问。这些权限的文档可以在 API 参考中找到。

