**Conditional formatting** enables the configuration of rules for any property and dictates how that property’s values will be rendered (e.g. coloring, alignment, etc.) in user facing applications. When you configure conditional formatting in the Ontology Manager, the formatting rules will apply in Object Explorer, Object Views, Quiver, and Workshop.条件格式允许为任何属性配置规则，并决定该属性的值在面向用户的应用中如何呈现（例如着色、对齐等）。当你在 Ontology Manager 中配置条件格式时，格式规则会在 Object Explorer、Object Views、Quiver 和 Workshop 中应用。


![Example](conditional-formatting-cond-form-example.png?width=600)


For the example `Aircraft` object type in Object Explorer, pictured above, the `type` and `wifi` properties have their values in colored boxes that are applied based on certain conditions. The main benefit of adding these is to make information easier to understand quickly. If an analyst was looking for all “A320” planes without wifi in “JFK”, just by glancing at the results above, we could tell that “Q-AAY” is the plane we’re after.以 Object Explorer 中的 Aircraft 对象类型为例，如上图所示， 类型和 WiFi 属性的值都以彩色框形式显示，这些框是根据特定条件应用的。添加这些信息的主要好处是让信息更容易快速理解。如果分析师想查找“JFK”中所有没有 WiFi 的“A320”飞机，仅凭上面的结果就能判断“Q-AAY”就是我们要找的飞机。


Let’s take a look at how these conditions are applied.让我们来看看这些条件是如何被应用的。


- For property `wifi`, we assign green if the value of the property is “true” for each object in the table, and red if it is “false."对于属性 WiFi，如果属性值为“true”，我们会为表中每个对象分配绿色，如果值为“false”则为红色。


![Example rules](conditional-formatting-wifi-rules.png?width=250)


- For property `type`, we assign colors based on exact match between “A320”, “A321” and “A330”.对于房产类型 ，我们根据“A320”、“A321”和“A330”之间的完全匹配来分配颜色。


![Example type colors](conditional-formatting-type-rules.png?width=250)


## [](#add-conditional-formatting)Add conditional formatting添加条件格式


In the property editor:在属性编辑器中：


1. Select the property to which you want to add conditional formatting.选择你想添加条件格式的属性。
2. You will see conditional formatting on the properties pane; select the **Add a rule** button.你会在属性面板看到条件格式;选择添加规则按钮。


![Add a rule](conditional-formatting-cond-form-oma.png?width=600)


1. Click on the newly created default rule to open the **Edit conditional formatting rule** editor. [Read on for more information about the components of the Rule editor](#edit-rules-using-the-rule-editor).点击新创建的默认规则以打开 “编辑条件格式规则编辑器”。 请继续阅读，了解更多关于规则编辑器组件的信息 。
2. Modify the rule.修改规则。


![Modifying a rule](conditional-formatting-rule.png?width=600)


## [](#edit-rules-using-the-rule-editor)Edit rules using the Rule editor使用规则编辑器编辑规则


![Rule editor](conditional-formatting-rule-editor-string.png?width=700)




















































| Label厂牌 | Description描述 | Usage用途 |
| --- | --- | --- |
| A | Switch between a **Standard** rule, an **Always true** rule, or a **Math** rule.在标准规则、 恒真规则或数学规则之间切换。 | Use **Always true** as a fallback in case your other rules don't match. In the example above, we could have grey as the fallback case when neither of the `type` values match.如果其他规则不匹配，可以用 “始终为真 ”作为备选。在上述例子中，当两种类型值都不匹配时，我们可以用灰色作为备用情况。

Use a **Math** rule when you want to run math operators on some of your properties.当你想对某些属性运行数学算子时，可以使用数学规则。 |
| B | The rule will always be applied to the property from which you selected **Add a rule**; however, this dropdown allows you to choose to apply the rule based on the value of another property.该规则始终应用到你选择的属性上 ，添加规则 ;不过，这个下拉菜单允许你根据另一处房产的价值选择应用该规则。 | In the case above, assume we want to color the value for `Type` in red when the value of `Performance factor` drops underneath a certain threshold. We would choose `Performance factor` in our logic instead of `Type`; however, the color would still show on `Type`.在上述情况下，假设当性能因子值低于某个阈值时，我们想将 Type 的值涂成红色。我们在逻辑中选择性能因子而非类型 ;但颜色仍会显示在 Type 上。 |
| C | Types of comparisons available are based on the type of the property. For example, for strings **String comparison** and **Is null** are available. For numeric types, **Numeric range** or **Exact numeric match** are available.可比较的类型取决于房产类型。例如，字符串可使用字符串比较和 Is null 功能。对于数字类型，可以选择数值范围或精确数值匹配 。 | To color the `type` in grey if the value is null, select this dropdown and choose **Is null** instead of **String comparison**.如果值为空，要将类型涂成灰色，选择此下拉菜单并选择 “是空 ”而不是字符串比较 。 |
| D | Subtypes of comparisons, **String comparison** has **Is exactly**, **Contains**, **Starts with**, etc.比较的子类型， 字符串比较有 I.actly、 包含 、以 Starting 等 。 | Use this to color all plane `type` values that **Start with** "A32".用它来给所有以“A32”开头的平面类型值涂色。 |
| E | Compare against a constant or a property reference.与常数或属性参考进行比较。 | In this case, we are specifically looking for the constant "A320", but we could also add a reference from another property from the same object type.在这种情况下，我们特别寻找常量“A320”，但也可以添加同一对象类型中其他属性的引用。 |
| F | Toggle between a **True** or **False** rule.在真规则和假规则之间切换。 | To color all planes in blue that are **not** A320, switch this to **False**.要将所有非 A320 飞机涂成蓝色，请将此标记为 False。 |
| Formatting格式 | Use Blueprint colors and intents or add your own custom color. You can also switch alignment.使用蓝图颜色和意图，或者添加你自己的自定义颜色。你也可以切换对齐。 | Switch between hex, RGB or Blueprint colors based on need; you can also align the boxes on the right hand side for easier readability for numbers.根据需要在六进制、RGB 或蓝图颜色之间切换;你也可以把右侧的方框对齐，这样数字更容易辨认。 |
| Preview预览 | View how conditional formatting appears in various contexts.查看条件格式在不同语境中的表现。 | Preview an **Objects table** or a **Property card.**预览对象表或属性卡。 |


## [](#copy-rules)Copy rules复制规则


In the property editor:在属性编辑器中：


1. Select the property from which you want to copy the conditional formatting rule.选择你想复制条件格式规则的属性。
2. You will see conditional formatting on the properties pane; select the **Copy rules** button to open the **Copy rule** dialog.你会在属性面板看到条件格式;选择复制规则按钮以打开复制规则对话框。


![Property editor](conditional-formatting-copy-rule-select-annotated.png?width=600)


1. Select the properties to which you want to copy the conditional formatting rules.选择你想复制条件格式规则的属性。


If the properties you are copying to already have their own conditional formatting rules, they will be overwritten by the new rules.如果你复制的属性已经有自己的条件格式规则，它们会被新规则覆盖。


![Copy rule](conditional-formatting-copy-rule.png?width=600)


Copied rules will continue referencing their original properties. For example, if a rule states that `wifi` values should appear green when “true,” and that rule is copied to the `customer experience` property, values of the `customer experience` property will also be green when the object’s `wifi` value is “true.” To change the property a rule references, simply select the rule and choose a new property from the **Property** dropdown in the rule editor.复制的规则将继续引用其原始属性。例如，如果一条规则指出当 “true”时 WiFi 值应显示绿色，且该规则被复制到客户体验属性中，那么当对象的 WiFi 值为“true”时， 客户体验属性的值也会显示绿色。要更改规则所引用的属性，只需选择该规则，然后在规则编辑器的属性下拉菜单中选择新的属性。


## [](#faq)FAQ常见问题


### [](#will-this-work-with-existing-type-classes)Will this work with existing type classes?这对现有类型类有效吗？


Conditional formatting takes precedence over existing type classes (with one exception detailed in the [following question](#will-this-work-with-editable-properties-in-object-views)). If you have both configured, conditional formatting will be displayed. You can however, use conditional formatting on one property and type classes on another.条件格式优先于现有类型类（一个例外，详见下文问题）。如果两者都配置好了，将显示条件格式。不过，你可以在一个属性上使用条件格式，在另一个属性上用类型类型。


### [](#will-this-work-with-editable-properties-in-object-views)Will this work with editable properties in Object Views?这对对象视图中的可编辑属性有效吗？


Conditional formatting is supported for properties configured for [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits). Conditional formatting is disabled for properties with the legacy `hubble:editable` property type class.对于为内联编辑配置的属性，支持条件格式化。对于使用旧有 hubble：editable property 类型类的属性，禁用了条件格式。

