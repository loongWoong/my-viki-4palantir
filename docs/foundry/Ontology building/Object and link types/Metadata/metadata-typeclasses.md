# [](#type-classes)Type classes类型类别


Type classes can be applied to properties, link types, and action types. With the exception of the `analyzer` type class kind, which affects [indexing](/docs/foundry/object-indexing/overview/) behavior, type classes define additional metadata that can be interpreted by user applications that interact with the Ontology. For example, the specification of some `hubble` property type classes affect how the property value is rendered in [Object Views](/docs/foundry/object-views/overview/).类型类可以应用于属性、链接类型和动作类型。除了影响索引行为的分析器类型类类型外，类型类定义了额外的元数据，用户可以在与本体交互时解释这些元数据。例如，某些哈勃属性类型类的规范会影响对象视图中属性值的渲染方式。


The chart below provides a list of known type classes. The columns in this chart are as follows:下图列出了已知类型的类别。该图表中的列如下：


- The **Deprecated** column indicates whether a type class is still supported.
弃用列表示类型类是否仍被支持。- The **Deprecated** column also indicates whether a type class should now be configured in the **Capabilities** page.
弃用列还指示是否应在能力页面配置类型类。- In the Ontology Manager, object types now have a **Capabilities** page to configure features historically defined as type classes. The configuration of all supported type classes will move to the **Capabilities** page.在本体管理器中，对象类型现在有一个能力页面，用于配置历史上定义为类型类的功能。所有支持类型类的配置将移至能力页面。
  - In the Ontology Manager, object types now have a **Capabilities** page to configure features historically defined as type classes. The configuration of all supported type classes will move to the **Capabilities** page.在本体管理器中，对象类型现在有一个能力页面，用于配置历史上定义为类型类的功能。所有支持类型类的配置将移至能力页面。
  - The **Deprecated** column also indicates whether a type class should now be configured in the **Capabilities** page.
  弃用列还指示是否应在能力页面配置类型类。- In the Ontology Manager, object types now have a **Capabilities** page to configure features historically defined as type classes. The configuration of all supported type classes will move to the **Capabilities** page.在本体管理器中，对象类型现在有一个能力页面，用于配置历史上定义为类型类的功能。所有支持类型类的配置将移至能力页面。
    - In the Ontology Manager, object types now have a **Capabilities** page to configure features historically defined as type classes. The configuration of all supported type classes will move to the **Capabilities** page.在本体管理器中，对象类型现在有一个能力页面，用于配置历史上定义为类型类的功能。所有支持类型类的配置将移至能力页面。
    
    
  - The **Type** column indicates whether the type class is applied to a property, link type (formerly known as relation), or action type.类型列表示类型类是应用于属性、链接类型（以前称为关系型）还是动作类型。
- The **Kind** and **Name** columns contain string values from two user-defined fields that are set when adding a type class in the Ontology Manager. These values are used by Foundry products to label a type class.Kind 和 Name 列包含两个用户自定义字段的字符串值，这些字段在 Ontology Manager 添加类型类时设置。这些值被 Foundry 产品用来标记类型类。


![Add Type Class - Kind and Name fields](typeclasses-kind-name.png?width=300)


- The **Description** column describes the intended behavior of user applications when interacting with a property value, link, or action for which the listed type class has been added.
描述列描述用户应用程序在与属性值、链接或已添加该类型类的动作交互时的预期行为。- [Object Explorer](/docs/foundry/object-views/overview/) is an application that consumes `hubble` type classes.对象探查器是一个使用哈勃类型类的应用程序。
- [Quiver](/docs/foundry/quiver/overview/) is an application that consumes `timeseries` type classes.Quiver 是一个消耗时间序列类的应用程序。
  - [Object Explorer](/docs/foundry/object-views/overview/) is an application that consumes `hubble` type classes.对象探查器是一个使用哈勃类型类的应用程序。
  - [Quiver](/docs/foundry/quiver/overview/) is an application that consumes `timeseries` type classes.Quiver 是一个消耗时间序列类的应用程序。
  
  


































































































































































































































































































































































































































































































| Deprecated        已弃用 | Type类型 | Kind种类 | Name名称 | Description描述 |
| --- | --- | --- | --- | --- |
|  | Property财产 | hubble哈勃 | media_url | Renders the property as a media item when it appears in an Object View.当属性出现在对象视图中时，它会以媒体项目的形式渲染该属性。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | editable可编辑 | Allows users to edit the property when it appears in an Object View. Use [inline edits](/docs/foundry/action-types/inline-edits/#object-explorer-inline-edits) instead.允许用户在属性出现在对象视图时编辑该属性。改用内联编辑 。 |
|  | Property财产 | hubble哈勃 | icon图标 | Indicates that the URL stored as property value contains the icon for an object.表示作为属性值存储的 URL 包含某个对象的图标。 |
| Deprecated已弃用 | Relation关系 | hubble哈勃 | creatable可创造 | Allows the user to create new objects of a specific link type from a Linked Objects View widget within an Object View. The type class is placed on the relation and allows the user to create objects of the type on the "many" side of a one-to-many relation. See [actions](/docs/foundry/action-types/overview/) for the supported way to allow users to create new links.允许用户在对象视图中的链接对象视图小部件中创建特定链接类型的新对象。类型类被放置在关系上，允许用户在一对多关系的“多”侧创建该类型的对象。请参见支持用户创建新链接的作 。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | endorsement_status:endorsement_status：
endorsed认可 | Marks object as `endorsed` in Object Explorer and Object Views when added to the primary key property of an object type.当添加到对象类型的主键属性时，将对象标记为在对象探索器和对象视图中被认可 。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | endorsement_status:endorsement_status：
not_endorsed | Marks object as `work in progress` in Object Explorer and Object Views when added to the primary key property of an object type.在对象探索器和对象视图中，将该对象标记为正在进行中， 当添加到某个对象类型的主键属性中时。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | thumbnail缩略图 | Uses the URL stored as the property value as a thumbnail in the search results cards. 在搜索结果卡中，将作为属性值存储的 URL 作为缩略图使用。

This was only relevant in a previous version of Object Explorer.这只在之前的 Object Explorer 版本中出现过。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | array数组 | This type class was formerly used to ensure that a property is formatted as an array, but arrays are now properly-supported property base types in the Ontology Manager.该类型类过去用于确保属性格式化为数组，但现在数组已成为本体管理器中得到妥善支持的属性基类型。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | default_sort_descending | Will automatically sort a column by descending values in Object Explorer. 在对象资源管理器中会自动按降序排序列。

This was only relevant in a previous version of Object Explorer.这只在之前的 Object Explorer 版本中出现过。 |
| Deprecated已弃用 | Property财产 | hubble哈勃 | quick_filter | In Object Explorer list view, these properties were available as default filters. 在对象浏览器列表视图中，这些属性作为默认筛选器可用。

This was only relevant in a previous version of Object Explorer.这只在之前的 Object Explorer 版本中出现过。 |
|  | Relation关系 | hierarchy等级制度 | parent家长 | Signals that the link direction in a link type represents a parent in a hierarchy. Object Views will then display breadcrumbs at the top of the Object View of the hierarchy (e.g., 'Europe -> France -> Paris -> Rue Cler').表示链路类型中的链路方向代表层级中的父节点。对象视图随后会在层级结构对象视图顶部显示面包屑（例如，“欧洲 - >法国 - > 巴黎 - > 克莱尔街”）。 |
|  | Property财产 | choropleth_map_
config_id | <map_config_id> | A choropleth can be created for any property type that contains values for geographic regions (i.e., country codes) that can be plotted on a map. The `kind` of type class necessary is `choropleth_map_config_id`, and the `name` depends on what type of region code the property contains.可以为任何包含地理区域（即国家代码）值的物业类型创建 choropleth，这些地区可以绘制在地图上。所需的类型类类型是 choropleth_map_config_id 的， 名称取决于该属性所包含的区域代码类型。

For instance:例如：
- For countries, use `countries`- 对于国家，请使用国家
- US States → `us_states`- 美国→ 州 us_states
- US Counties → `us_counties`- 美国县 →us_counties
- US Zip Codes → `us_zip_codes`- 美国邮政编码→us_zip_codes

For additional region boundary options, or additional assistance with adding this type class, contact your Palantir representative.如需更多区域边界选项，或添加此类类别的额外帮助，请联系您的 Palantir 代表。

Configuration options include changing the type of aggregation as well as the color scale used. 配置选项包括更改聚合类型以及使用的颜色比例。

 To use this type class, either the `selectable` or `sortable` render hint must be applied to the property.要使用该类型类，必须对该属性应用可选或可排序的渲染提示。 |
| Deprecated已弃用 | Property财产 | oe_home_page_
 object_type_group | <your_object_type_ 
 group_name> | Add this type class to the primary key property of an object type to add said object type to a group. 将该类型类添加到某个对象类型的主键属性中，以便将该对象类型添加到组中。

Ensure proper spelling to avoid the duplication of groups. These configured groups of object types are displayed on Object Explorer's home page. 确保拼写正确，避免组别重复。这些配置好的对象类型组显示在对象资源管理器的主页上。

If you have groups configured, any non-hidden object types you do not add to a group will be placed at the bottom of the page under “Other” group. This has been replaced with the object type groups capability.如果你已经配置了组，任何你没有添加到组中的非隐藏对象类型都会放在页面底部的“其他”组下。该功能已被对象类型组功能所取代。 |
|  | Action type动作类型 | hubble-oe哈勃-欧伊 | hide-action隐藏动作 | Hides the action type within Object Explorer & Object Views; otherwise they are automatically discovered in the `Actions` button dropdown.在对象浏览器和对象视图中隐藏动作类型;否则它们会自动在动作按钮下拉菜单中被发现。 |
|  | Action type动作类型 | hubble-oe-object-set-rid哈勃-OE-物体-设定-清除 | <object_type_RID> | Experimental feature that allows for the creation of dynamic object sets.一个允许创建动态对象集的实验性功能。 |
|  | Action type动作类型 | hubble-oe-security-rid哈勃-OE-安全-里德 | <compass_RID> | Experimental feature that allows for the creation of dynamic object sets.一个允许创建动态对象集的实验性功能。 |
|  | Action type动作类型 | actions行动 | generate_uuid | Replaces a string parameter with a UUID.用 UUID 替换字符串参数。 |
|  | Action type动作类型 | actions行动 | prefill_current_user | Replaces a string parameter with the current user.将字符串参数替换为当前用户。 |
|  | Action type动作类型 | actions行动 | view_object_with_type | Shows the created/modified object in the success toast.在成功吐槽中显示已创建/修改的对象。 |
|  | Property财产 | analyzer分析仪 | not_analyzed | Prevents [Lucene ↗](https://lucene.apache.org/) from tokenizing the property; use for identifier properties that contain dashes, etc.阻止 Lucene ↗ 对该物业进行代币化;用于包含破折号等的标识符属性。 |
|  | Property财产 | analyzer分析仪 | simple / standard / whitespace / english / french / japanese / arabic / korean / german / combined_arabic_english简单/标准/空白/英语/法语/日语/阿拉伯语/韩语/德语/combined_arabic_english | Analyzers for specific languages and use cases. Most of these are implemented with Lucene built-in analyzers, but a few are custom plugins.针对特定语言和用例的分析器。大多数是用 Lucene 内置分析器实现的，但也有少数是自定义插件。
Korean and German are not supported in the legacy [Object Storage V1](/docs/foundry/object-databases/object-storage-v1/).在遗留的对象存储 V1 中，韩语和德语不被支持。 |
| Deprecated已弃用 | Property财产 | analyzer分析仪 | not_indexed | Prevents Lucene from indexing the property; use for properties that do not need to be searchable or aggregatable. 阻止卢塞恩对该物业进行索引;用于不需要可搜索或可聚合的属性。

 This type class is no longer used to manage whether a property should be indexed, as this functionality is now managed by the `searchable` [render hint](/docs/foundry/object-link-types/metadata-render-hints/).该类型类不再用于管理属性是否应被索引，因为该功能现在由可搜索的渲染提示管理。 |
| Deprecated已弃用 | Property财产 | multipass多重通行 | user_id | When applied to a property whose values contain Multipass UIDs, the property will be rendered as the users' username (comprised of the multipass and multipass attributes) in Object Explorer and Object Views. 当该属性的值包含多重通 UID 时，该属性将在对象资源管理器和对象视图中以用户用户名（由多重通和多重通属性组成）呈现。

This type class is no longer used to ensure a property is formatted as a username, and Multipass UIDs are now supported in the value formatting feature in the Ontology Manager.该类型类不再用于确保属性格式化为用户名，多重通道 UID 现已支持本体管理器的值格式化功能。 |
| Deprecated已弃用 | Property财产 | global全球 | <your_property_id> | Can be used to mark a property as global. This allows filtering of multiple object types by a common property as long as the properties have the same property_id and global type class on each object type that should be filtered by this property. 可以用来标记房产为全局。只要每个属性具有相同的 property_id 和全局类型类，就可以通过一个共同属性过滤多个对象类型。

This was only relevant in a previous version of Object Explorer.这只在之前的 Object Explorer 版本中出现过。 |
| Deprecated已弃用 | Property财产 | geo地理 | geojson | Indicates that the property contains GeoJSON data (e.g., polygons, lines, etc.). The [Map application](/docs/foundry/map/overview/) will render this GeoJSON on the map. Deprecated: use the `geoshape` property type instead.表示该属性包含 GeoJSON 数据（例如多边形、线条等）。 地图应用程序会在地图上渲染这个 GeoJSON。已弃用：改用 Geoshape 属性类型。 |
| Deprecated已弃用 | Property财产 | geo地理 | latitude纬度 | Indicates that the property contains a Latitude for use in the [Map application](/docs/foundry/map/overview/). Deprecated: use the `geopoint` property type instead.表示该属性包含用于地图应用的纬度。已弃用：改用 geopoint 属性类型。 |
| Deprecated已弃用 | Property财产 | geo地理 | longitude经度 | Indicates that the property contains a Longitude for use in the [Map application](/docs/foundry/map/overview/). Deprecated: use the `geopoint` property type instead.表示该属性包含用于地图应用的经度。已弃用：改用 geopoint 属性类型。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | geo地理 | altitude海拔 | Indicates that the property contains an altitude/elevation, in meters relative to sea level, for use in the [Map application](/docs/foundry/map/overview/) with 3D mode.表示该属性包含相对于海平面的高度/海拔，用于地图应用的 3D 模式。 |
|  | Property财产 | vertex顶点 | link_merge | For Vertex & Vortex Related Object Search Arounds, always treat this object as an intermediary - this object will no longer show up in Related Object list, but second-degree links from it will, and it will render as an edge on the graph. Place type class on the primary key of the object.对于顶点和涡旋相关对象搜索环节，始终将该对象视为中介——该对象将不再出现在相关对象列表中，但其二度链接会显示，并且它会被渲染为图中的一条边。在对象的主键上放置类型类。 |
|  | Relation关系 | vertex顶点 | link_merge_incoming | The same as `link_merge`, but only for this specific relation - the link merged object is the target/to side of this relation.和 link_merge 一样，但只针对这个特定关系——链接合并对象是该关系的目标/指向侧。 |
|  | Relation关系 | vertex顶点 | link_merge_outgoing | The same as `link_merge`, but only for this specific relation - the link merged object is the source/from side of this relation.和 link_merge 一样，但只针对这个特定关系——链接合并对象是该关系的源/来源端。 |
|  | Relation关系 | vertex顶点 | component组成部分 | For Vertex diagrams, indicates the objects linked to the base objects to be used in the diagram.对于顶点图，表示与图中基对象关联的对象。 |
|  | Property财产 | vertex顶点 | component_subtype | For Vertex, allows for finer-grained grouping than object type. Place type class on the primary key of the object.对于顶点，允许比对象类型更细粒度的分组。在对象的主键上放置类型类。 |
|  | Property财产 | vertex顶点 | event_intent.<intent_>event_intent。<intent_> | Set this on the primary key property of an Event to use it in Vertex & Vortex, where `intent` indicates the color/severity of the event/alert (danger, warning, primary, or success). For example: `event_intent.danger`在事件的主键属性上设置此项，以便在顶点和漩涡中使用，意图表示事件/警报的颜色/严重程度（危险、警告、主或成功）。例如：event_intent.危险 |
|  | Property财产 | vertex顶点 | event_value | Indicates the property representing the numeric value of the event.表示表示事件数值的属性。 |
|  | Property财产 | vertex顶点 | event_value_unit.<unit_>event_value_unit。<unit_> | Set this alongside `event_value`, where `unit` is the unit of measurement for numeric value of the event. For example: `event_value_unit.Kilograms`将此与 event_value 并列，其中单位是事件数值的计量单位。例如：event_value_unit。公斤 |
|  | Property财产 | vertex顶点 | event_property | Shows this property in the Vertex & Vortex event cards.在顶点与漩涡事件卡中显示该属性。 |
|  | Property财产 | vertex顶点 | min明 | For time series objects: Vertex will alert when series values fall below this minimum.对于时间序列对象：当序列值低于该最小值时，顶点会发出警报。 |
|  | Property财产 | vertex顶点 | max马克斯 | For time series objects: Vertex will alert when series values exceed this maximum.对于时间序列对象：当序列值超过该最大值时，顶点会发出警报。 |
|  | Property财产 | vertex顶点 | threshold_measure.<measure_>threshold_measure。<measure_> | For Vertex, set this on the primary key property of an object to indicate which measure to use for thresholding. For example: `threshold_measure.Temperature`对于 Vertex，将该指标设置为对象的主键属性，以指示阈值测量的测量。例如：threshold_measure。温度 |
|  | Property财产 | vertex顶点 | threshold_high_limit | Used in conjunction with `threshold_measure` to indicate which property represents the upper threshold bound.与 threshold_measure 结合使用，表示哪种性质代表上界。 |
|  | Property财产 | vertex顶点 | threshold_low_limit | Used in conjunction with `threshold_measure` to indicate which property represents the lower threshold bound.与 threshold_measure 结合使用，表示哪个性质代表下限阈值。 |
|  | Property财产 | vertex顶点 | threshold_exceed_intent.<intent_>threshold_exceed_intent。<intent_> | Set this on the primary key property of an object in conjunction with `threshold_measure`, where `intent` indicates the color/severity of the threshold breach (danger, warning, primary, or success). For example: `threshold_exceed_intent.danger`将此设置在对象的主键属性上，配合 threshold_measure，意图表示阈值突破的颜色/严重程度（危险、警告、主或成功）。例如： threshold_exceed_intent.danger |
|  | Property财产 | vertex顶点 | key_measure.<measure_>key_measure。<measure_> | Measures listed here will display on the Vertex home page. For example: `key_measure.Temperature`这里列出的度量将显示在顶点主页上。例如：key_measure。温度 |
| Deprecated已弃用 | Property财产 | vertex顶点 | enum_values | For time series objects: A JSON map from numeric values to string values. The type class is no longer supported.对于时间序列对象：一个从数值映射到字符串值的 JSON 映射。该类型类别已不再支持。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_id | When applied to the primary key of a timeseries object, this type class specifies the *series identifier* (`seriesId`) of that object. The property must be globally unique across all timeseries objects, and is the only type class that is required for your object to be discoverable in Quiver.当应用到时间序列对象的主键时，该类型类指定该对象的序列标识符 （seriesId）。该属性必须在所有时间序列对象之间全局唯一，并且是 Quiver 中唯一需要的类型类，才能让你的对象在 Quiver 中被发现。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_measure | The property specifying the [measure](/docs/foundry/quiver/timeseries-overview/) of a timeseries object. 指定时间序列对象度量的性质。

Note: The `timeseries.timeseries_sensor_type` type class was formerly used for the same purpose; this will continue to work, but use `timeseries.timeseries_measure` for consistency.注： timeseries.timeseries_sensor_type 类型类别过去也用于同样的目的;这方法会继续有效，但要保持一致性 timeseries.timeseries_measure。 |
| Deprecated已弃用 | Property财产 | timeseries时间序列 | timeseries_sensor_type | See `timeseries_measure` above.见上 timeseries_measure。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_units | The property specifying the *value* units of a timeseries object (e.g., a stock price timeseries might have `dollars` as a value unit).指定时间序列对象价值单位的属性（例如，股票价格时间序列可能以美元为价值单位）。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_internal_interpolation | The property specifying the default *internal interpolation* of a timeseries object. Internal interpolation is how Quiver infers series values between adjacent data points.指定时间序列对象默认内部插值的属性。内部插值是 Quiver 推断相邻数据点之间序列值的方式。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_root_object_id | The property specifying the [root object](/docs/foundry/quiver/timeseries-overview/) of a timeseries object. Each timeseries object can only have one root object.指定时间序列对象根对象的属性。每个时间序列对象只能有一个根对象。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_is_enum | A Boolean property which must be `true` for any timeseries that has enum values. 一个布尔属性， 必须对任何具有枚举值的时间序列成立。

Note: This requirement is temporary and may change in the future.注意：此要求为临时性，未来可能有所调整。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | timeseries_is_deprecated | A Boolean property which, when set to `true` for a timeseries, will filter it out of Object Explorer and Object View search results. 一个布尔属性，当时间序列设置为 true 时，会将其从对象浏览器和对象视图的搜索结果中过滤掉。

Note: This will only post-filter these timeseries out of results in Quiver. This will not affect search results in other applications.注意：这只会在 Quiver 中对这些时间序列进行后期过滤。这不会影响其他应用的搜索结果。 |
|  | Relation关系 | timeseries时间序列 | parent家长 | Describes the link between the timeseries object and each parent, similar to `hierarchy.parent`.描述时间序列对象与每个父节点之间的链接，类似于 hierarchy.parent。 |
|  | Property财产 | timeseries时间序列 | timeseries_is_value_inverted | When set to true, this boolean property will automatically invert the y-axis values of a timeseries in Quiver, such that values ascend going down. This is useful for plotting a time vs. depth series, such as when tracking the progress of an underground drilling operation over time.当设置为 true（真）时，该布尔属性会自动反转 Quiver 中时间序列的 y 轴值，使值向下递增。这对于绘制时间与深度序列很有用，比如追踪地下钻探作业随时间的进展。 |
|  | Property财产 | timeseries时间序列 | timeseries_depth_units | Place on the property containing the depth units of complex series (depth series, well completion series and fiber series). The regular `timeseries.timeseries_units` property is used for the value units of a depth series and well completion series.在物业上放置包含复杂级数（深度级数、井完井级数和纤维级数）深度单位的装置。正则 timeseries.timeseries_units 性质用于深度系列和井完井系列的值单位。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_id | The property specifying the *event identifier* (`eventId`) of an event object. Should be globally unique across all event objects.指定事件对象事件标识符 （eventId）的属性。应该在所有事件对象之间全局唯一。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_start_time | The property specifying the start time of an event object. This field should be a time value (e.g. a `TIMESTAMP)`.指定事件对象起始时间的属性。该字段应为时间值（例如时间戳）。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_end_time | The property specifying the end time of an event object. This field should be a time value (e.g. a `TIMESTAMP)`.指定事件对象结束时间的属性。该字段应为时间值（例如时间戳）。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_description | The property specifying the string description of an event object. This is required if the event object type will be used for [annotation writeback](/docs/foundry/quiver/timeseries-overview/).指定事件对象字符串描述的性质。如果事件对象类型将用于注释写回 ，这是必要的。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_root_object_id | The property specifying the [root object](/docs/foundry/quiver/timeseries-overview/) of an event object. Each event object can only have one root object.指定事件对象根对象的属性。每个事件对象只能有一个根对象。 |
| Configure in 配置
**Capabilities** page 能力页面
of object type对象类型 | Property财产 | timeseries时间序列 | event_linked_series_id | The property specifying the [series object](/docs/foundry/quiver/timeseries-overview/) to which an event object relates. String arrays as well as single strings are supported for this field.指定事件对象所关联的级数对象的属性。该字段支持字符串数组以及单字符串。 |
|  | Property财产 | schedules赛程表 | schedulable-start-time可预约开始时间 | Marks a timestamp property as the start time for schedule objects in dynamic scheduling widgets. Required for dynamic mode in the [Scheduling Calendar widget](/docs/foundry/dynamic-scheduling/scheduling-calendar-widget/) and Gantt chart widgets. The action parameter ID in your save handler action must match the property ID.在动态调度控件中，将时间戳属性标记为调度对象的起始时间。在排程日历小部件和甘特图小部件中，动态模式必备。你的存档处理程序中的动作参数 ID 必须与属性 ID 匹配。 |
|  | Property财产 | schedules赛程表 | schedulable-end-time可调度终点 | Marks a timestamp property as the end time for schedule objects in dynamic scheduling widgets. Required for dynamic mode in the [Scheduling Calendar widget](/docs/foundry/dynamic-scheduling/scheduling-calendar-widget/) and Gantt chart widgets. The action parameter ID in your save handler action must match the property ID.在动态调度控件中，将时间戳属性标记为调度对象的结束时间。在排程日历小部件和甘特图小部件中，动态模式必备。你的存档处理程序中的动作参数 ID 必须与属性 ID 匹配。 |
|  | Property财产 | schedules赛程表 | segment-by分段 | When applied to a property, enables segmentation in scheduling widgets, allowing pucks to be color-coded based on the property values using conditional formatting.应用于属性时，可以实现调度小部件的分割，允许根据属性值通过条件格式对节点进行颜色编码。 |
|  | Action type动作类型 | schedules赛程表 | schedulable-start-time可预约开始时间 | Marks an action parameter as the start time parameter for save handler actions in dynamic scheduling widgets. Must be applied to the same parameter that matches the start time property ID.在动态调度控件中，将动作参数标记为保存处理程序动作的开始时间参数。必须应用于与起始时间属性 ID 匹配的同一参数。 |
|  | Action type动作类型 | schedules赛程表 | schedulable-end-time可调度终点 | Marks an action parameter as the end time parameter for save handler actions in dynamic scheduling widgets. Must be applied to the same parameter that matches the end time property ID.在动态调度控件中，将动作参数标记为保存处理程序动作的结束时间参数。必须应用于与结束时间属性 ID 匹配的同一参数。 |

