# [](#scale-and-property-limits)Scale and property limits规模和属性限制


Several limits are in place to ensure edited object types can quickly process edits and update user-facing data without slowing down live applications. Actions submitted that exceed these limits will not succeed and will display an error message to the user.为了确保编辑的对象类型能够快速处理编辑并更新面向用户的数据，而不会减慢实时应用程序的速度，设置了几个限制。提交的超出这些限制的操作将不会成功，并向用户显示错误消息。


## [](#configuration-limits)Configuration limits配置限制


The `Allow multiple values` toggle allows users to pass in a list of values to a parameter.Allow multiple values 开关允许用户将一组值传递给参数。























| Limit限制 | Maximum最大值 |
| --- | --- |
| Number of elements in a primitive list parameter原始列表参数中的元素数量 | 10,000 |
| Number of elements in an object reference list parameter对象引用列表参数中的元素数量 | 1,000 |
| Number of elements in a list parameter when used in submission criteria列表参数在提交标准中使用时包含的元素数量 | 1,000 |


## [](#edit-limits)Edit limits编辑限制























| Limit限制 | Maximum最大值 |
| --- | --- |
| Number of **object types** you can edit in a single action submission单个操作提交中可编辑的对象类型数量 | 50 |
| Number of **objects** you can edit in a single action submission单个操作提交中可编辑的对象数量 | 10,000 |
| Each individual edit of an **object** in an action submission单个操作提交中对对象的每个独立编辑 | 32KB (OSv1), 3MB (OSv2) |


## [](#batch-call-limits)Batch call limits批量调用限制


An action can be called a maximum of 10,000 times in a batch. This limit is reduced to 20 when the action is function-backed and the function is not configured to use [batched execution](/docs/foundry/action-types/function-actions-batched-execution/).一个操作在批量中最多可被调用 10,000 次。当操作由函数支持且该函数未配置为使用批量执行时，此限制会减少到 20。


The edits applied in a batched action call are treated as a single group when enforcing [edit limits](#edit-limits), regardless of which request in the batch was the cause of the edits.在执行编辑限制时，批量调用中应用的编辑被视为一个单一组，无论批量中的哪个请求导致了这些编辑。


Additional limits may apply, depending on the calling application.可能存在额外的限制，具体取决于调用应用程序。


## [](#supported-property-types)Supported property types支持的属性类型


Below are specifications for supported single and array property types. Note that some property types are only supported by object storage v2 (OSv2).以下是支持的单一和数组属性类型的规范。请注意，某些属性类型仅由对象存储 v2（OSv2）支持。


### [](#single-property-types)Single property types单一属性类型





















































































































| Property type属性类型 | Parameter type参数类型 | Supported支持 |
| --- | --- | --- |
| Attachment附件 | Attachment附件 | Yes是 |
| Boolean布尔值 | Boolean布尔值 | Yes是 |
| Byte字节 | Integer整数 | Yes是 |
| Cipher text密文 | String字符串 | Yes是 |
| Date日期 | Date日期 | Yes是 |
| Decimal十进制 | Decimal十进制 | Yes是 |
| Double双精度 | Double双精度 | Yes是 |
| Float浮点数 | Double双倍 | Yes是 |
| Geopoint地理点 | Geopoint地理点 | Yes是 |
| Geoshape地理形状 | Geoshape地理形状 | Yes是 |
| Geotime series reference地质时间序列参考 | Geotime series reference地质时间序列参考 | Yes (OSv2 only)是（仅限 OSv2） |
| Integer整数 | Integer整数 | Yes是 |
| Long长 | Long长 | Yes是 |
| Mandatory control强制控制 | - | Not supported as a property or in actions不作为属性或操作支持 |
| Media reference媒体参考 | Media reference媒体引用 | Yes (OSv2 only)是（仅限 OSv2） |
| String字符串 | String字符串 | Yes是 |
| Short短 | Integer整数 | Yes是 |
| Struct结构体 | Struct结构体 | Yes (OSv2 only)是（仅限 OSv2） |
| Timestamp时间戳 | Timestamp时间戳 | Yes是 |
| Time series reference时间序列参考 | Time series reference时间序列参考 | Yes (OSv2 only)是（仅限 OSv2） |
| Vector向量 | Double list双列表 | Yes (OSv2 only)是（仅限 OSv2） |


### [](#array-property-types)Array property types数组属性类型





















































































































| Array property type数组属性类型 | List parameter type列表参数类型 | Supported支持 |
| --- | --- | --- |
| Attachment附件 | Attachment附件 | Yes是 |
| Boolean布尔值 | Boolean布尔值 | Yes是 |
| Byte字节 | Integer整数 | Yes是 |
| Cipher text密文 | String字符串 | Yes是 |
| Date日期 | Date日期 | Yes是 |
| Decimal十进制 | Decimal十进制 | Yes是 |
| Double双精度浮点数 | Double双精度浮点数 | Yes是 |
| Float单精度浮点数 | Double双倍 | Yes是 |
| Geopoint地理点 | Geopoint地理点 | Yes是 |
| Geoshape地理形状 | Geoshape地理形状 | Yes是 |
| Geotime series reference地理时间序列参考 | Geotime series reference地理时间序列参考 | Yes (OSv2 only)是（仅限 OSv2） |
| Integer整数 | Integer整数 | Yes是 |
| Long长整型 | Long长整型 | Yes是 |
| Mandatory control强制控制 | Mandatory control强制控制 | Yes是 |
| Media reference媒体参考 | - | Not supported in actions在操作中不受支持 |
| String字符串 | String字符串 | Yes是 |
| Short短 | Integer整数 | Yes是 |
| Struct结构体 | Struct结构 | Yes (OSv2 only)是（仅限 OSv2） |
| Timestamp时间戳 | Timestamp时间戳 | Yes是 |
| Time series reference时间序列参考 | - | Not supported as a property or in actions不支持作为属性或用于操作 |
| Vector向量 | - | Not supported as a property or in actions不支持作为属性或用于操作 |


## [](#supported-properties)Supported properties支持的属性


Currently, actions cannot be used to edit the **primary key** of an object. Modifying the primary key is equivalent to deleting an object and then adding a new object; instead of editing the primary key with an action, you can create or delete an object directly using [rules](/docs/foundry/action-types/rules/#ontology-rules).目前，无法使用操作来编辑对象的主键。修改主键等同于删除对象然后添加新对象；您可以直接使用规则来创建或删除对象，而不是通过操作编辑主键。


## [](#notification-recipients)Notification recipients通知接收者


When using [side effect notifications](/docs/foundry/action-types/notifications/), a maximum of 500 recipients can notified in a single action. This limit is reduced to fifty recipients when notifications content is rendered "From a function". For further information about limits to account for when generating notifications, see the documentation on [maximum recipient limits for notifications](/docs/foundry/action-types/notifications/#maximum-recipient-limits).在使用副作用通知时，单个操作最多可通知 500 名接收者。当通知内容渲染为"从函数"时，此限制减少到 50 名接收者。有关生成通知时需要考虑的限制的更多信息，请参阅关于通知最大接收者限制的文档。

