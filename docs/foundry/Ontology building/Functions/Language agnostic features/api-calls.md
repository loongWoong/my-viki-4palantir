# [](#make-api-calls-from-functions)Make API calls from functions从函数中调用 API


It is possible to make API calls to external sources from TypeScript v1, TypeScript v2 and Python functions, but doing so requires additional configuration. This configuration and external source usage are detailed below.从 TypeScript v1、TypeScript v2 和 Python 函数中可以调用外部 API，但这样做需要额外的配置。以下将详细说明该配置和外部源的使用。


## [](#configure-access-to-external-apis)Configure access to external APIs配置外部 API 访问


By default, functions are not allowed to call external APIs. To enable calling external systems from your function, you must [configure a source](/docs/foundry/data-connection/set-up-source/) in [Data Connection](/docs/foundry/data-connection/overview/) to allow Foundry to connect with an external system.默认情况下，函数不允许调用外部 API。要使您的函数能够调用外部系统，您必须在 Data Connection 中配置一个源，以允许 Foundry 连接到外部系统。


For functions to connect to your source's external system securely, your source must be configured to [enable exports](/docs/foundry/data-connection/export-overview/#enable-exports-for-source) and allow the [import of your source into Code Repositories](/docs/foundry/data-connection/external-transforms/#prerequisite-import-a-source-into-code). Both of these can be configured by navigating to the source in Data Connection and opening the **Connection settings** section. Here you will find the **Code import configuration** tab, where you can also configure an API name if your source does not yet have one. This API name will be used to reference your source in code.为了让函数能够安全地连接到您源的外部系统，您的源必须配置为启用导出并允许将您的源导入代码库。这两项都可以通过导航到数据连接中的源并打开连接设置部分进行配置。在这里，您将找到代码导入配置选项卡，如果您的源还没有 API 名称，您也可以在此配置一个。此 API 名称将用于在代码中引用您的源。


Make sure to fully configure the certificate chain in your source. 请确保在您的源中完全配置证书链。


Webhook and function runtime environments are not identical. Webhook 和函数运行环境并不相同。


Sometimes, a webhook will work correctly while the API call from a function might encounter an `UNABLE_TO_GET_ISSUER_CERT` error. 有时，Webhook 可能工作正常，而函数的 API 调用可能会遇到 UNABLE_TO_GET_ISSUER_CERT 错误。


Refer to our documentation on the [`openssl` command in the source terminal](/docs/foundry/data-connection/set-up-source/#openssl) to verify certificates.参考源终端中 openssl 命令的文档来验证证书。


## [](#use-an-external-source-in-a-function)Use an external source in a function在函数中使用外部源


To make API calls from a function, you must first import your source using the [resource imports sidebar](/docs/foundry/functions/resource-imports-sidebar/) in a functions repository. You must then declare that your function uses the source.要从函数中调用 API，您必须首先使用函数存储库中的资源导入侧边栏导入您的源。然后，您必须声明您的函数使用该源。


Examples of this are shown below:以下展示了示例：


TypeScript v1TypeScript v2Python```
Copied!`1import { ExternalSystems } from "@foundry/functions-api";
2import { MySource } from "@foundry/external-systems/sources";
3
4export class MyExternalFunctions {
5    @ExternalSystems({ sources: [MySource] })
6    @Function()
7    public async myExternalFunction(): Promise<string> {
8        const { url } = MySource.getHttpsConnection();
9        const response = await MySource.fetch(url);
10
11        return response.text();
12    }
13}`
```

```
Copied!`1import { getSource, getHttpsConnection, getFetch } from "@palantir/functions-sources";
2
3export const config = {
4    sources: ["MySource"]
5}
6
7async function MyExternalFunction(): Promise<string> {
8    const source = await getSource("MySource");
9    const { url } = getHttpsConnection(source);
10    const fetch = await getFetch(source);
11
12    const response = await fetch(url);
13
14    return response.text();
15}`
```

```
Copied!`1from functions.api import function
2from functions.sources import get_source
3
4
5@function(sources=["MySource"])
6def my_external_function() -> str:
7    source = get_source("MySource")
8    url = source.get_https_connection().url
9    client = source.get_https_connection().get_client()
10    response = client.get(url)
11    return response.text`
```


You can test your function in live preview and use it to make external calls once published.您可以在实时预览中测试您的函数，并在发布后使用它进行外部调用。


**Third-party clients are not yet supported for serverless execution or live preview without overriding the fetch function or HTTP agent.** To ensure your API calls function properly across all environments, you must use the relevant library methods to make requests with the correct configuration. Direct API calls to external sources or internal Foundry URLs are not guaranteed to work in all environments.在不重写 fetch 函数或 HTTP 代理的情况下，第三方客户端目前不支持无服务器执行或实时预览。为确保您的 API 调用在所有环境中都能正常工作，您必须使用相关的库方法以正确的配置进行请求。直接向外部源或内部 Foundry URL 发起的 API 调用在所有环境中都不一定能正常工作。


## [](#access-source-attributes-and-credentials)Access source attributes and credentials访问源属性和凭证


You can access source attributes provided by each function type's corresponding library.您可以访问每个函数类型对应的库提供的源属性。


The example below shows how to obtain the base URL of the source in the example above.下面的示例展示了如何获取上面示例中源的基本 URL。


TypeScript v1TypeScript v2Python```
Copied!`1const { url } = MySource.getHttpsConnection();`
```

```
Copied!`1const { url } = getHttpsConnection(source);`
```

```
Copied!`1url = get_source("MySource").get_https_connection().url`
```


You can also access additional secrets or credentials stored on the source by using the following syntax to access secrets:您也可以通过使用以下语法访问源上存储的额外秘密或凭证：


TypeScript v1TypeScript v2Python```
Copied!`1const secret = MySource.getSecret("MySecret");`
```

```
Copied!`1const secret = source.secrets["MySecret"];`
```

```
Copied!`1secret = get_source("MySource").get_secret("MySecret")`
```


## [](#use-the-pre-configured-clients)Use the pre-configured clients使用预配置客户端


For sources that provide a REST API, the source object allows you to retrieve a client. This client will be pre-configured with the server and client certificates specified on the source. It will also include additional proxy configurations which allow egress from the environment functions are executed in. You should always use this client, if possible, to guarantee your function can egress to the source from all environments.对于提供 REST API 的源，源对象允许您获取一个客户端。该客户端将预配置为使用源上指定的服务器和客户端证书。它还将包含允许从执行环境函数的环境中进行出站访问的额外代理配置。如果可能，您应该始终使用此客户端，以确保您的函数可以从所有环境中出站访问源。


TypeScript v1TypeScript v2Python```
Copied!`1const fetch = MySource.fetch;`
```

```
Copied!`1const fetch = await getFetch(source);`
```

```
Copied!`1client = source.get_https_connection().get_client()`
```


Alternatively, you can use your own client or third-party libraries which make external requests, and use the source object to [retrieve attributes and credentials](#access-source-attributes-and-credentials).或者，您可以使用自己的客户端或第三方库，这些库用于发起外部请求，并使用源对象来获取属性和凭证。


TypeScript v2 functions provide a pre-configured HTTP agent as an additional integration point for usage with third party libraries which accept a custom HTTP agent.TypeScript v2 函数提供了一个预配置的 HTTP 代理，作为与接受自定义 HTTP 代理的第三方库集成的附加集成点。


The following example demonstrates retrieving this agent and using it with [axios ↗](https://github.com/axios/axios).以下示例演示了获取此代理并使用 axios ↗。


TypeScript v2```
Copied!`1import { getHttpAgent, getHttpsConnection } from "@palantir/functions-sources";
2import axios from 'axios';
3
4const agent = await getHttpAgent(source);
5const { url } = getHttpsConnection(source);
6
7const response = await axios.get(url, {
8    httpsAgent: agent,
9});`
```


Currently, it is impossible to access source attributes that are not credentials unless the source provides an HTTPS client. For example, you will not be able to access the `hostname` or other non-secret attributes on a [PostgreSQL source](/docs/foundry/available-connectors/postgresql/).目前，除非源提供 HTTPS 客户端，否则无法访问非凭证的源属性。例如，您将无法访问 PostgreSQL 源上的 hostname 或其他非秘密属性。

