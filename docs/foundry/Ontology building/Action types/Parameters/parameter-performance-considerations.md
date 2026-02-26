# [](#performance-considerations-for-parameter-configuration)Performance considerations for parameter configuration参数配置的性能考虑


Dependencies between parameters, such as in the definitions of [default values](/docs/foundry/action-types/parameters-default-value/) and [multiple-choice options](/docs/foundry/action-types/parameters-filter/), can impact the time that it takes for an action form to load. For example, consider the following action parameter configuration:参数之间的依赖关系，例如默认值和多项选择选项的定义，会影响动作表单加载所需的时间。例如，考虑以下动作参数配置：


1. The first parameter is an `object reference` with a `from single result of object set` default value.第一个参数是一个带有 from single result of object set 默认值的对象引用 。
2. The second parameter is a string with a default value that is an `object parameter property` referencing the first parameter.第二个参数是一个字符串，默认值是对象参数属性 ，引用第一个参数。
3. The third parameter is also a string, with no default value, but configured as a `multiple choice` dropdown using `get options from an object set`. The object set definition references the second parameter.第三个参数同样是一个字符串，没有默认值，但通过 配置为多项选择下拉选单。 get options from an object set 对象集定义引用第二个参数。


When a user loads an action form for this action, multiple operations need to be performed iteratively.当用户加载该动作的动作表单时，需要迭代执行多个作。


1. First, the default value for the first parameter needs to be retrieved.首先，需要检索第一个参数的默认值。
2. Then, the second parameter's default value needs to be derived from the first parameter value.然后，第二个参数的默认值需要从第一个参数值推导出来。
3. Finally, the options for the third parameter need to be derived from the second parameter value.最后，第三个参数的选项需要从第二个参数值中推导出来。


When configuring action parameters, it is recommended to keep the dependency hierarchy as flat as possible. In the context of the action described above, referencing the first parameter instead of the second parameter in the third parameter's object set definition would allow the necessary information for the second and third parameter to be derived in parallel, reducing the total latency between opening the form and the form being fully interactive.在配置动作参数时，建议尽量保持依赖层级的平坦。在上述作的背景下，在第三个参数的对象集定义中引用第一个参数而非第二个参数，可以并行推导第二和第三个参数所需的信息，从而减少从表单打开到表单完全交互之间的总延迟。

