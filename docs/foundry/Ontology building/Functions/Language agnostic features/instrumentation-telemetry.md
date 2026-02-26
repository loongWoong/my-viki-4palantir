# [](#instrumentation-and-telemetry-in-functions)Instrumentation and telemetry in functions函数中的监控和遥测


It is possible to emit certain types of telemetry from your functions to allow for monitoring and debugging of production workflows.您可以从函数中发出某些类型的遥测数据，以允许监控和调试生产工作流。


To learn how to view telemetry emitted by your functions, see our [AIP Observability documentation](/docs/foundry/aip-observability/overview/).要了解如何查看您的函数发出的遥测数据，请参阅我们的 AIP 可观测性文档。


## [](#supported-telemetry-types)Supported telemetry types支持的遥测类型


The following table provides an overview of the types of telemetry supported by each function language. Note that a single span over the total execution duration of the function, along with a single request log, is automatically created for all function types.以下表格概述了每种函数语言支持的遥测类型。请注意，对于所有函数类型，都会在函数的总执行期间自动创建一个跨越整个执行时长的单个跨度，以及一个单个请求日志。































| Language语言 | Logs日志 | Spans跨度 | Metrics指标 |
| --- | --- | --- | --- |
| TypeScript v1 | Yes是 | Only product-defined spans[1]仅产品定义的跨度[1] | Only product-defined metrics[2]仅产品定义的指标[2] |
| TypeScript v2 | Yes是 | Yes[3]是[3] | Only product-defined metrics[2]仅产品定义的指标[2] |
| Python | No否 | No否 | Only product-defined metrics[2]仅产品定义的指标[2] |


[1] Product-defined spans in TypeScript v1 functions include operations like object loads and query executions.[1] TypeScript v1 函数中的产品定义跨度包括对象加载和查询执行等操作。


[2] Foundry records the total execution duration for all types of functions.[2] Foundry 记录所有类型函数的总执行持续时间。


[3] TypeScript v2 functions automatically instrument all outbound network requests, but custom spans can also be added.[3] TypeScript v2 函数自动对所有出站网络请求进行监控，但也可以添加自定义跨度。


### [](#logs)Logs日志


You can emit custom logs from functions and view them retroactively. The following examples demonstrate how to emit logs from both TypeScript v1 and v2 functions.您可以从函数中发出自定义日志，并可以事后查看它们。以下示例展示了如何从 TypeScript v1 和 v2 函数中发出日志。


In TypeScript v2 functions, Foundry will set up the OpenTelemetry SDK's global logger provider, and you will be able to retrieve a logger from it. If you want to use third-party libraries for logging, you must configure them to emit logs through a logger obtained from the global logger provider.在 TypeScript v2 函数中，Foundry 将设置 OpenTelemetry SDK 的全局日志记录器提供程序，您将能够从中获取一个日志记录器。如果您想使用第三方库进行日志记录，您必须将它们配置为通过从全局日志记录器提供程序获取的日志记录器发出日志。


TypeScript v1TypeScript v2```
Copied!`1export class MyFunctions {
2    @Function()
3    public myFunction(name: string): string {
4        console.log(`This is a custom log line ${name}.`);
5        return `Hello, ${name}!`;
6    }
7}`
```

```
Copied!`1import { logs } from "@opentelemetry/api-logs";
2
3const logger = logs.getLogger("my-function");
4
5export default function myFunction(): string {
6    logger.emit({
7        attributes: { LOG_MESSAGE: "This is a custom log line." },
8        body: { name }
9    });
10
11    return `Hello, ${name}!`;
12}`
```


### [](#spans)Spans跨度


You can also create custom spans in TypeScript v2 functions to track the duration of specific operations. The following example demonstrates how to create a custom span.您也可以在 TypeScript v2 函数中创建自定义跨度来跟踪特定操作的持续时间。以下示例演示了如何创建自定义跨度。


In TypeScript v2 functions, Foundry will set up the OpenTelemetry SDK's global tracer provider, and you will be able to retrieve a tracer from it. If you want to use third-party libraries for tracing, you must configure them to emit traces through a tracer obtained from the global tracer provider.在 TypeScript v2 函数中，Foundry 将设置 OpenTelemetry SDK 的全局追踪器提供程序，您将能够从中获取一个追踪器。如果您想使用第三方库进行追踪，您必须将它们配置为通过从全局追踪器提供程序获取的追踪器来发出追踪。


TypeScript v2```
Copied!`1import { trace } from "@opentelemetry/api";
2import { Integer } from "@osdk/functions";
3
4const tracer = trace.getTracer("my-function");
5
6export default function sqrt(n: Integer): Integer {
7    const sqrt = tracer.startActiveSpan("my-custom-span", (span) => {
8        try {
9            return Math.sqrt(n);
10        } finally {
11            span.end();
12        }
13    });
14
15    return sqrt;
16}`
```

