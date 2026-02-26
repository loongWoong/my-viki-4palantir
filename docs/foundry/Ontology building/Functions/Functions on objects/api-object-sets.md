# [](#api-object-sets)API: Object setsAPI: 对象集


An **object set** represents an unordered collection of objects of a single type. You can use the functions APIs to filter object sets, perform Search Arounds to other object types based on defined link types, and compute aggregated values or retrieve the concrete objects. In addition to passing individual objects as inputs into a function, you can search for object sets at any time using the object search APIs.对象集表示一组单类型对象的无序集合。您可以使用函数 API 对对象集进行过滤，根据定义的链接类型在其他对象类型上执行搜索，并计算聚合值或检索具体对象。除了将单个对象作为输入传递给函数外，您还可以随时使用对象搜索 API 搜索对象集。


Filtering, ordering, and aggregations only work on properties that have the `Searchable` render hint enabled in the Ontology app. These properties have been indexed for search. [Learn how to enable the `Searchable` render hint.](/docs/foundry/object-link-types/metadata-render-hints/)过滤、排序和聚合仅适用于在本体应用中启用了 Searchable 渲染提示的属性。这些属性已被索引用于搜索。了解如何启用 Searchable 渲染提示。


Object sets are more efficient than object arrays for function inputs because they defer loading until needed. For best practices on using object sets efficiently, see [Optimize performance](/docs/foundry/functions/optimize-performance/).对象集比对象数组作为函数输入更高效，因为它们延迟加载直到需要时。有关高效使用对象集的最佳实践，请参阅优化性能。


## [](#object-search)Object search对象搜索


The `Objects.search()` interface allows you to initiate a search for any of the object types imported into your project. In this example, the function uses the given `airportCode` to find all flights that departed from that airport. Then, it finds all the distinct destinations of those flights and returns them.Objects.search() 接口允许你搜索项目导入的任何对象类型。在这个例子中，该函数使用给定的 airportCode 查找从该机场出发的所有航班。然后，它查找这些航班的所有不同目的地并返回它们。


```
Copied!`1import { Function } from "@foundry/functions-api";
2import { Objects } from "@foundry/ontology-api";
3
4export class FlightFunctions {
5    @Function()
6    public currentFlightDestinations(airportCode: string): Set<string> {
7        const flightsFromAirport = Objects.search()
8            .flights()
9            .filter(flight => flight.departureAirportCode.exactMatch(airportCode))
10            .all();
11
12        const destinations = flightsFromAirport.map(flight => flight.arrivalAirportCode!);
13
14        return new Set(destinations);
15    }
16}`
```


Object sets can also be created from a list of objects, list of object resource identifiers or an object set resource identifier by passing them as an argument to the searched object type. For example: `Objects.search().flights([flight])`.对象集也可以通过将它们作为参数传递给搜索的对象类型从对象列表、对象资源标识符列表或对象集资源标识符创建。例如： Objects.search().flights([flight]) 。


Once you have an object set of a given type, you can perform various operations on the set as documented below.一旦你获得给定类型的对象集，你就可以按照下文记录的方式对集合执行各种操作。


## [](#filtering)Filtering过滤


The `.filter()` method on an object set allows you to filter the object set based on the searchable properties of the objects. The filter method takes a filter definition, which is based on the type of the property you are filtering on.对象集上的 .filter() 方法允许您根据对象的可搜索属性过滤对象集。过滤方法需要一个基于您正在过滤的属性类型的过滤定义。


- All property types support the `.exactMatch()` filter, which filters to objects with an exact match on that property value. This is useful to filter for exact matches on strings (as in the example above), or to filter on the primary key of an object (for example,`.filter(object => object.primaryKey.exactMatch(PrimaryKey))`).
所有属性类型都支持 .exactMatch() 过滤，该过滤会筛选出在该属性值上完全匹配的对象。这对于筛选字符串的精确匹配（如上例所示）或筛选对象的主键（例如， .filter(object => object.primaryKey.exactMatch(PrimaryKey)) ）非常有用。- To check whether a property is `null` or `undefined`, use the `hasProperty()` method.要检查某个属性是否为 null 或 undefined ，请使用 hasProperty() 方法。
- To pass multiple values, use the spread operator `.exactMatch(...listVariable)`. If an empty array is passed in, the filter will be ignored.要传递多个值，使用展开运算符 .exactMatch(...listVariable) 。如果传递空数组，则过滤将不被忽略。
  - To check whether a property is `null` or `undefined`, use the `hasProperty()` method.要检查某个属性是否为 null 或 undefined ，请使用 hasProperty() 方法。
  - To pass multiple values, use the spread operator `.exactMatch(...listVariable)`. If an empty array is passed in, the filter will be ignored.要传递多个值，使用展开运算符 .exactMatch(...listVariable) 。如果传递空数组，则过滤将不被忽略。
  
  - String properties support several keyword filters. See the documentation on each method in Code Assist for full details.
字符串属性支持多个关键字过滤器。有关每个方法的详细信息，请参阅代码辅助文档。- `.phrase()` splits the search query into tokens (usually individual words) and then filters values based on whether they contain all of the given tokens in order with no other tokens in between. Note that string values that are separated by underscores or periods will be treated as one token. For example, when searching for "banana", an object with the property value "banana_pudding" or "banana.pudding" will not be returned..phrase() 将搜索查询拆分为标记（通常是单个单词），然后根据它们是否按顺序包含所有给定标记且标记之间没有其他标记来过滤值。请注意，由下划线或点分隔的字符串值将被视为一个标记。例如，在搜索 "banana" 时，具有属性值 "banana_pudding" 或 "banana.pudding" 的对象不会被返回。
- `.phrasePrefix()` is almost identical to `phrase()`, but the last token will also match tokens starting with that token. For example, a `.phrasePrefix()` search for `fresh banana` would match the property value `fresh banana_pudding`, but not the property value `banana_pudding fresh`. A `.phrasePrefix()` search for `pudding` would not match the property value `banana_pudding`..phrasePrefix() 与 phrase() 非常相似，但最后一个标记也会匹配以该标记开头的标记。例如，一个 .phrasePrefix() 搜索 fresh banana 将匹配属性值 fresh banana_pudding ，但不会匹配属性值 banana_pudding fresh 。一个 .phrasePrefix() 搜索 pudding 不会匹配属性值 banana_pudding 。
- `.prefixOnLastToken()` splits the search query into tokens and then filters values based on whether they contain all of the given tokens, where the last token will also match tokens starting with that token. For example, `big app` would match `big apples` as well as `apples from the big tree`, though it would not match `apples from the biggest tree`..prefixOnLastToken() 将搜索查询分割成多个标记，然后根据它们是否包含所有给定的标记来过滤值，其中最后一个标记也会匹配以该标记开头的标记。例如， big app 会匹配 big apples ，但不会匹配 apples from the biggest tree 。
- `.matchAnyToken()`, `.fuzzyMatchAnyToken()` split the search query into tokens and then filter values based on whether they contain any of the given tokens. The `fuzzy` version allows approximate values to match..matchAnyToken() ， .fuzzyMatchAnyToken() 将搜索查询分割成多个标记，然后根据它们是否包含任何给定的标记来过滤值。 fuzzy 版本允许近似值匹配。
- `.matchAllTokens()`, `.fuzzyMatchAllTokens()` split the search query into tokens and then filter values based on whether they contain all of the given tokens. The `fuzzy` version allows approximate values to match.
.matchAllTokens() ， .fuzzyMatchAllTokens() 将搜索查询分割成多个标记，然后根据它们是否包含所有给定的标记来过滤值。 fuzzy 版本允许近似值匹配。- Fuzzy filters can take an optional `Fuzziness` parameter imported from `@foundry/functions-api`.模糊过滤器可以接受一个可选的 Fuzziness 参数，该参数来自 @foundry/functions-api 。
- Explanations of the available `Fuzziness` options can be found in the [ElasticSearch documentation ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness). More information can also be found below.关于可用的 Fuzziness 选项的解释可以在 ElasticSearch 文档中找到 ↗。更多信息也可以在下文中找到。
  - Fuzzy filters can take an optional `Fuzziness` parameter imported from `@foundry/functions-api`.模糊过滤器可以接受一个可选的 Fuzziness 参数，该参数来自 @foundry/functions-api 。
  - Explanations of the available `Fuzziness` options can be found in the [ElasticSearch documentation ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness). More information can also be found below.关于可用的 Fuzziness 选项的解释可以在 ElasticSearch 文档中找到 ↗。更多信息也可以在下文中找到。
  - `.phrase()` splits the search query into tokens (usually individual words) and then filters values based on whether they contain all of the given tokens in order with no other tokens in between. Note that string values that are separated by underscores or periods will be treated as one token. For example, when searching for "banana", an object with the property value "banana_pudding" or "banana.pudding" will not be returned..phrase() 将搜索查询拆分为标记（通常是单个单词），然后根据它们是否按顺序包含所有给定标记且标记之间没有其他标记来过滤值。请注意，由下划线或点分隔的字符串值将被视为一个标记。例如，在搜索 "banana" 时，具有属性值 "banana_pudding" 或 "banana.pudding" 的对象不会被返回。
  - `.phrasePrefix()` is almost identical to `phrase()`, but the last token will also match tokens starting with that token. For example, a `.phrasePrefix()` search for `fresh banana` would match the property value `fresh banana_pudding`, but not the property value `banana_pudding fresh`. A `.phrasePrefix()` search for `pudding` would not match the property value `banana_pudding`..phrasePrefix() 与 phrase() 非常相似，但最后一个标记也会匹配以该标记开头的标记。例如，一个 .phrasePrefix() 搜索 fresh banana 将匹配属性值 fresh banana_pudding ，但不会匹配属性值 banana_pudding fresh 。一个 .phrasePrefix() 搜索 pudding 不会匹配属性值 banana_pudding 。
  - `.prefixOnLastToken()` splits the search query into tokens and then filters values based on whether they contain all of the given tokens, where the last token will also match tokens starting with that token. For example, `big app` would match `big apples` as well as `apples from the big tree`, though it would not match `apples from the biggest tree`..prefixOnLastToken() 将搜索查询分割成多个标记，然后根据它们是否包含所有给定的标记来过滤值，其中最后一个标记也会匹配以该标记开头的标记。例如， big app 会匹配 big apples ，但不会匹配 apples from the biggest tree 。
  - `.matchAnyToken()`, `.fuzzyMatchAnyToken()` split the search query into tokens and then filter values based on whether they contain any of the given tokens. The `fuzzy` version allows approximate values to match..matchAnyToken() ， .fuzzyMatchAnyToken() 将搜索查询分割成多个标记，然后根据它们是否包含任何给定的标记来过滤值。 fuzzy 版本允许近似值匹配。
  - `.matchAllTokens()`, `.fuzzyMatchAllTokens()` split the search query into tokens and then filter values based on whether they contain all of the given tokens. The `fuzzy` version allows approximate values to match.
  .matchAllTokens() ， .fuzzyMatchAllTokens() 将搜索查询分割成多个标记，然后根据它们是否包含所有给定的标记来过滤值。 fuzzy 版本允许近似值匹配。- Fuzzy filters can take an optional `Fuzziness` parameter imported from `@foundry/functions-api`.模糊过滤器可以接受一个可选的 Fuzziness 参数，该参数来自 @foundry/functions-api 。
  - Explanations of the available `Fuzziness` options can be found in the [ElasticSearch documentation ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness). More information can also be found below.关于可用的 Fuzziness 选项的解释可以在 ElasticSearch 文档中找到 ↗。更多信息也可以在下文中找到。
    - Fuzzy filters can take an optional `Fuzziness` parameter imported from `@foundry/functions-api`.模糊过滤器可以接受一个可选的 Fuzziness 参数，该参数来自 @foundry/functions-api 。
    - Explanations of the available `Fuzziness` options can be found in the [ElasticSearch documentation ↗](https://www.elastic.co/guide/en/elasticsearch/reference/current/common-options.html#fuzziness). More information can also be found below.关于可用的 Fuzziness 选项的解释可以在 ElasticSearch 文档中找到 ↗。更多信息也可以在下文中找到。
    
    
  - Numbers, dates, and timestamp properties support `.range()` filters.
数字、日期和时间戳属性支持 .range() 过滤器。- Range filters have a set of `.lt()`, `.lte()`, `.gt()` and `gte()` methods for performing less than / less than or equal to / greater than / greater than or equal to (respectively) comparisons.范围过滤器有一组 .lt() 、 .lte() 、 .gt() 和 gte() 方法用于执行小于/小于或等于/大于/大于或等于（分别）的比较。
  - Range filters have a set of `.lt()`, `.lte()`, `.gt()` and `gte()` methods for performing less than / less than or equal to / greater than / greater than or equal to (respectively) comparisons.范围过滤器有一组 .lt() 、 .lte() 、 .gt() 和 gte() 方法用于执行小于/小于或等于/大于/大于或等于（分别）的比较。
  
  - Boolean properties support `.isTrue()` and `.isFalse()` filters.布尔属性支持 .isTrue() 和 .isFalse() 过滤器。
- Geopoint properties support `.withinDistanceOf()`, `.withinPolygon()`, and `.withinBoundingBox()` filters.地理点属性支持 .withinDistanceOf() 、 .withinPolygon() 和 .withinBoundingBox() 过滤器。
- GeoShape properties support `.withinBoundingBox()`, `.intersectsBoundingBox()`, `.doesNotIntersectBoundingBox()`, `.withinPolygon()`, `.intersectsPolygon()`, and `doesNotIntersectPolygon()` filters.地理形状属性支持 .withinBoundingBox() 、 .intersectsBoundingBox() 、 .doesNotIntersectBoundingBox() 、 .withinPolygon() 、 .intersectsPolygon() 和 doesNotIntersectPolygon() 过滤器。
- Link filters can be used to filter objects that do or do not have any linked objects of a specific type using the `.isPresent()` method.链接过滤器可以使用 .isPresent() 方法来过滤具有或不具有特定类型链接对象的物体。
- Array properties support the `.contains()` filter, which filters to objects whose array property values contain *any* of the given values.数组属性支持 .contains() 过滤器，该过滤器筛选出数组属性值包含所给值的对象。


### [](#combining-filters)Combining filters组合过滤器


You can compose filters together using the `Filters` API exported from `@foundry/functions-api`. The available methods are:您可以使用从 @foundry/functions-api 导出的 Filters API 将过滤器组合在一起。可用的方法有：


- `and()` filters the object set to objects that pass all the given filtersand() 将对象集过滤为通过所有给定过滤器的对象
- `or()` filters the object set to objects that pass any of the given filtersor() 将对象集过滤为通过任何给定过滤器的对象
- `not()` negates the given filternot() 否定给定的过滤器


In the example below, we can filter an object set of flights by flight destination using `and()`:在下面的示例中，我们可以使用 and() 通过航班目的地过滤航班对象集：


```
Copied!`1import { Filters } from "@foundry/functions-api";
2
3
4Objects.search()
5    .flights()
6    .filter(flight => Filters.or(
7        Filters.and(flight.destination.exactMatch("SFO"), flight.passengerCount.gt(100)),
8        Filters.and(flight.destination.exactMatch("LAX"), flight.passengerCount.gt(300)),
9    ))`
```


The above code would filter to flights that either arrived at SFO with more than 100 passengers or arrived at LAX with more than 300 passengers.上述代码将筛选出以下航班：抵达旧金山国际机场（SFO）的乘客数超过 100 人，或抵达洛杉矶国际机场（LAX）的乘客数超过 300 人。


Warning警告The `.filter()` method on an object set does not use the operators `&&` or `||`. To apply multiple filters, you must use one of the methods on `Filters` listed above (or call `.filter()` multiple times to achieve an `and` condition).对象集上的 .filter() 方法不使用 && 或 || 运算符。若要应用多个筛选条件，你必须使用上面列出的 Filters 方法之一（或多次调用 .filter() 以实现 and 条件）。


### [](#filtering-on-string-properties-with-fuzzy-search)Filtering on string properties with fuzzy search基于字符串属性进行模糊搜索


Specifying the optional `fuzziness` parameter can provide more fine-tuned control over Fuzzy matching behavior. If you do not specify fuzziness, then an automatic edit distance is allowed based on the length of the token you are searching for. You will need to import `Fuzziness` from `@foundry/functions-api` in order to specify edit distance.指定可选的 fuzziness 参数可以提供更精细的模糊匹配控制。如果你不指定模糊度，则允许基于你要搜索的标记长度自动编辑距离。你需要从 @foundry/functions-api 导入 Fuzziness 才能指定编辑距离。


#### [](#fuzzy-match-any-token)Fuzzy match any token模糊匹配任何标记


```
`Objects.search().employee().filter(employee => employee.firstName.fuzzyMatchAnyToken("Michael", { fuzziness: Fuzziness.LEVENSHTEIN_TWO })).all();
`
```


The code above returns any employees with a first name within two edits of the provided search term (with Levenshtein distance of two). In this example, that would include `Michael`, `Micheal`, `Mikhael`, `Michel`, `Mikhail`, `Mihail` (but not `Miguel` for example). If you have more certainty in the accuracy of your search term, you can search with a smaller edit distance (with different Levenshtein distances), refining your search results a little more.上述代码返回任何其名字与提供的搜索词在两个编辑距离内的员工（Levenshtein 距离为两个）。在这个例子中，这包括 Michael 、 Micheal 、 Mikhael 、 Michel 、 Mikhail 、 Mihail （但例如不包括 Miguel ）。如果你对搜索词的准确性更有把握，可以使用更小的编辑距离（使用不同的 Levenshtein 距离）来稍微细化你的搜索结果。


#### [](#fuzzy-match-all-tokens)Fuzzy match all tokens模糊匹配所有标记


```
`Objects.search().employee().filter(employee => employee.fullName.fuzzyMatchAllTokens("Michael Smith", { fuzziness: Fuzziness.LEVENSHTEIN_ONE })).all();
`
```


You can also use fuzzy filters on a multiple token phrase. The code above would match on employees whose full name contains **both** `Michael` and `Smith` with up to one edit in each token - for example, `Mikhael Smitt` (that is, each with a Levenshtein distance of one each). The ordering of tokens is not taken into account with a `fuzzyMatchAllTokens` or `fuzzyMatchesAllTokens` filter.你也可以对多个标记的短语使用模糊过滤器。上述代码会匹配那些全名包含 Michael 和 Smith 的员工，每个标记最多有一个编辑距离——例如 Mikhael Smitt （也就是说，每个标记的 Levenshtein 距离为一个）。使用 fuzzyMatchAllTokens 或 fuzzyMatchesAllTokens 过滤器时，标记的顺序不会被考虑。


#### [](#fuzzy-match-on-string-array-properties)Fuzzy match on string array properties字符串数组属性上的模糊匹配


All filters on array-based properties can use the methods available to their underlying type. For example, string array properties can be filtered based on any methods available to string properties, though the naming of the methods may differ slightly. Filtering on array properties requires a single match among the array elements in order for that object to be returned.基于数组的属性上的所有过滤器都可以使用其底层类型可用的方法。例如，字符串数组属性可以根据字符串属性可用的任何方法进行过滤，尽管方法名称可能略有不同。过滤数组属性需要数组元素中的单个匹配，以便返回该对象。


## [](#search-around)Search Around围绕搜索


Search around limits围绕搜索的限制Object sets loaded into memory `.all()` or `.allAsync()` are allowed to have a **maximum of 3 search arounds**. If more than 3 search arounds are used, an error is thrown. When performing a search around from object set A to object set B in Object Storage V2, the resulting object set B cannot have more than 10 million object instances, or an error will be thrown. For Object Storage V1, the limit is 100,000 object instances.加载到内存中的对象集 .all() 或 .allAsync() 允许最多有 3 次搜索。如果使用超过 3 次搜索，将抛出错误。在 Object Storage V2 中，从对象集 A 搜索到对象集 B 时，结果对象集 B 的对象实例数不能超过 1000 万，否则将抛出错误。对于 Object Storage V1，限制是 10 万个对象实例。


Based on the object type of your object set, *Search Around* methods are generated to enable traversing [links](/docs/foundry/object-link-types/link-types-overview/) based on the object type of your object set. In the below example, we filter to an object set of Flights based on the departure code, then Search Around to the passengers on those flights. This results in an object set of Passengers, which can be further filtered or searched around on.根据您的对象集的对象类型，将生成 Search Around 方法以实现基于对象集对象类型的链接遍历。在以下示例中，我们根据出发代码筛选到航班对象集，然后搜索这些航班上的乘客。这将生成乘客对象集，该对象集可以进一步筛选或搜索。


```
Copied!`1const passengersDepartingFromAirport = Objects.search()
2    .flights()
3    .filter(flight => flight.departureAirportCode.exactMatch(airportCode))
4    .searchAroundPassengers();`
```


Search Around methods will only be generated for link types that are imported into your project. Refer to [the tutorial](/docs/foundry/functions/foo-getting-started/#import-ontology-types) for details on how to import link types.Search Around 方法将仅为您导入到项目中的链接类型生成。有关如何导入链接类型的详细信息，请参阅教程。


Note that for performance reasons, the number of Search Around operations you can conduct in a single search is currently limited to 3. If you attempt to run a search with more than three levels of Search Around depth, the search will fail at runtime.请注意，出于性能考虑，单次搜索中可执行的搜索范围操作数量目前限制为 3。如果你尝试运行超过三个级别的搜索范围深度，搜索将在运行时失败。


## [](#k-nearest-neighbors-knn)K-nearest neighbors (KNN)K 近邻 (KNN)


KNN LimitsKNN 限制KNN is only supported on object types indexed into [OSv2](/docs/foundry/object-backend/overview/). The k value is limited to the range 0 < K <= 100. Also, the search vector must be the same size as the one used for indexing and has a 2048 dimension limit. An error will be thrown if any of these limits are exceeded.KNN 仅在索引到 OSv2 的对象类型上受支持。k 值限制在 0 < K <= 100 的范围内。此外，搜索向量的大小必须与索引时使用的大小相同，并且有 2048 维度的限制。如果超出这些限制，将抛出错误。


Object types with embedding properties will be available for KNN searches. These searches will return the k value objects that have an embedding property nearest to the provided embedding parameter. The following example returns the most similar movies to a provided movie script. Embeddings can be generated in transformation tools such as [Pipeline Builder](/docs/foundry/pipeline-builder/pipeline-builder-aip/#text-to-embeddings) ; or at function query time [using a Palantir-provided embedding model](language-models.md#embeddings) or [your own model in a function](/docs/foundry/functions/functions-on-models/).具有嵌入属性的物体类型将可用于 KNN 搜索。这些搜索将返回具有与提供的嵌入参数最近的嵌入属性的 k 值物体。以下示例返回与提供的电影剧本最相似的电影。嵌入可以在转换工具（如 Pipeline Builder）中生成；或使用 Palantir 提供的嵌入模型或您自己的模型在函数查询时生成。


Make sure that your functions repository's `functions.json` configuration file has the `enableVectorProperties` entry set to  `true`.确保您的函数仓库的 functions.json 配置文件已设置 enableVectorProperties 条目为 true 。


```
Copied!`1import { Objects } from "@foundry/ontology-api";
2
3const kValue: number = 2;
4// Vector can be generated from FML Live or come from an existing object
5const vector: Double[] = [0.7, 0.1, 0.3];
6const movies: Movies[] = Objects.search()
7        .movies()
8        .nearestNeighbors(obj => obj.vectorProperty.near(vector, { kValue }))
9        .orderByRelevance()
10        .take(kValue);`
```


For an example of a full semantic search workflow, review the [semantic search workflow guide](/docs/foundry/ontology/using-palantir-provided-models-to-create-a-semantic-search-workflow/).有关完整语义搜索工作流的示例，请查阅语义搜索工作流指南。


## [](#set-operations)Set operations集合运算


Object sets of the same object type can be combined in various ways using set operations:相同类型的对象集合可以通过集合运算以多种方式组合：


- `.union()` creates a new object set composed of objects present in any of the given object sets..union() 创建一个新的对象集合，包含在所给对象集合中的任意一个对象。
- `.intersect()` creates a new object set composed of objects present in all of the given object sets..intersect() 创建一个新的对象集合，包含在所有所给对象集合中的对象。
- `.subtract()` removes any objects present in the given object sets..subtract() 删除给定对象集中存在的任何对象。


## [](#retrieving-all-objects)Retrieving all objects检索所有对象


The `.all()` and `.allAsync()` methods retrieve all objects in the object set. Note that if you attempt to load too many objects at once, your function will fail to execute. Currently, the maximum number of objects you can load is 100,000. However, loading more than 10,000 objects may also cause your function execution to time out. [Learn more about time and space limits in functions.](/docs/foundry/functions/manage-functions/#enforced-limits).all() 和 .allAsync() 方法检索对象集中的所有对象。请注意，如果你一次性尝试加载太多对象，你的函数将无法执行。目前，你可以加载的最大对象数量是 100,000。然而，加载超过 10,000 个对象也可能导致你的函数执行超时。了解更多关于函数的时间和空间限制。


You can use the `.allAsync()` method to retrieve a Promise that resolves to all the objects in the object set. This can be useful for loading data from multiple object sets in parallel.你可以使用 .allAsync() 方法来获取一个 Promise，该 Promise 将解析为对象集中的所有对象。这对于并行从多个对象集加载数据很有用。


## [](#ordering-and-limiting)Ordering and limiting排序和限制


Instead of retrieving all objects, you can load a limited number by applying an ordering clause to your object set, then specifying a specific number of objects to load. To do this, you can use the following methods:您不必检索所有对象，而是可以通过对对象集应用排序子句，然后指定要加载的对象数量来加载有限数量的对象。为此，您可以使用以下方法：


- `.orderBy()` specifies a searchable property to order by, and allows you to specify an ordering direction. Only properties whose types can be ordered (numbers, dates, and strings) are available for selection in this method. You can call `.orderBy()` multiple times to sort by multiple properties..orderBy() 指定用于排序的可搜索属性，并允许您指定排序方向。在此方法中，只有可以排序的类型（数字、日期和字符串）的属性可供选择。您可以多次调用 .orderBy() 以按多个属性排序。
- `.orderByRelevance()` specifies that the objects should be returned in order of how well they match the provided filters, with the most relevant listed first. Relevance for a query term against a property value on a given object is a complex determination that takes into account the frequency of the term appearing in the property value, the frequency of the term appearing across all objects, and more. Relevance is less appropriate when performing only `.exactMatch()` filters or filtering on non-string properties. Note that only one of `.orderBy()` and `.orderByRelevance()` may be used in a single search..orderByRelevance() 指定对象应根据与提供的过滤器匹配的程度返回，最相关的对象将首先列出。查询项与给定对象属性值之间的相关性是一个复杂的确定过程，它考虑了该词在属性值中出现的频率、该词在所有对象中出现的频率等因素。当仅执行 .exactMatch() 过滤器或对非字符串属性进行过滤时，相关性不太适用。请注意，在单个搜索中， .orderBy() 和 .orderByRelevance() 只能使用其中之一。
- `.take()` and `.takeAsync()` enable you to retrieve a specified number of objects from the set. These methods are only available after you have specified an ordering..take() 和 .takeAsync() 可以让你从集合中检索指定数量的对象。这些方法只有在指定排序后才能使用。


For example, the following code would retrieve the ten employees with the earliest start dates:例如，以下代码将检索最早入职的十名员工：


```
Copied!`1Objects.search()
2    .employees()
3    .orderBy(e => e.startDate.asc())
4    .take(10)`
```


As another example, imagine an object type `claims` which contains text of accident claims for an insurance company. We'd like to find a specific claim involving a red car and a deer. Without the `.orderByRelevance()` line, any results containing any of the words `red`, `car`, `collision`, `with`, or `deer` may have been returned in the top 10 results. With the `.orderByRelevance()` line, the first 10 results will be the claims that contain the most search terms, so that the most relevant claims will appear first.再例如，假设有一个对象类型 claims ，其中包含某保险公司的事故索赔文本。我们想找到涉及红色汽车和鹿的特定索赔。如果没有 .orderByRelevance() 行，前 10 个结果中可能会返回包含 red 、 car 、 collision 、 with 或 deer 中的任何词语的结果。有了 .orderByRelevance() 行，前 10 个结果将是包含最多搜索词的索赔，以便最相关的索赔会首先显示。


```
Copied!`1const results = Objects.search()
2    .claims()
3    .filter(doc => doc.text.matchAnyToken("red car collision with deer"))
4    .orderByRelevance()
5    .take(10)`
```


## [](#computing-aggregations)Computing aggregations计算聚合


Aggregation limits聚合限制Aggregations returned from the Objects API are limited to **10,000 total buckets**. An error will be thrown if this limit is exceeded.从 Objects API 返回的聚合结果最多只能包含 10,000 个总桶。如果超出此限制，将抛出错误。

When bucketing using `.topValues()`, results will be approximate if the data has more than 1,000 distinct values. The list of top values may not be accurate in that case.使用 .topValues() 进行桶聚合时，如果数据包含超过 1,000 个不同值，结果将不精确。在这种情况下，顶级值列表可能不准确。


### [](#grouping-objects-by-properties)Grouping objects by properties按属性对对象进行分组


In many cases, it's unnecessary to load all of the objects in your object set. Instead, you can simply load a bucketed aggregation of values to conduct further analysis.在许多情况下，加载对象集中的所有对象是不必要的。相反，你可以直接加载一个桶聚合的值来进行进一步分析。


To begin computing an aggregation, call the `.groupBy()` method on an object set. This allows you to specify bucketing on one of the searchable properties of the object type in the object set. For example, this code groups employees by their start date:要开始计算聚合，请在对象集上调用 .groupBy() 方法。这允许您指定对象集中对象类型的可搜索属性之一进行分桶。例如，此代码按员工的开始日期进行分组：


```
Copied!`1Objects.search()
2    .employees()
3    .groupBy(e => e.startDate.byDays())`
```


When specifying which property to bucket by, you will have to provide additional information about how the bucketing should be done depending on the property type:在指定按哪个属性进行分桶时，您需要根据属性类型提供有关如何进行分桶的额外信息：


- For `boolean` properties, the only option is `.topValues()`. This returns two buckets, one for `true` and one for `false`.对于 boolean 属性，唯一选项是 .topValues() 。这会返回两个桶，一个用于 true ，一个用于 false 。
- For string properties, there are two options:
对于字符串属性，有两个选项：- `.topValues()`: For rapid response times and properties with a smaller cardinality. This buckets by the top 1,000 values for the string property. This limit is to ensure that the returned aggregation is not excessively large..topValues() : 用于快速响应时间以及基数较小的属性。此方法按字符串属性的前 1,000 个值进行分桶。此限制是为了确保返回的聚合结果不会过大。
- `.exactValues()`: For more exact aggregations and the possibility to consider up to 10,000 buckets for high cardinality properties. The amount of considered buckets can be specified via `.exactValues({"maxBuckets": numBuckets})` where `numBuckets` must be an integer value between 0 and 10,000. The response time for this method can take longer, as more results have to be considered..exactValues() : 用于更精确的聚合，并考虑高达 10,000 个分桶的可能性，适用于高基数属性。考虑的分桶数量可以通过 .exactValues({"maxBuckets": numBuckets}) 指定，其中 numBuckets 必须是一个介于 0 到 10,000 之间的整数值。此方法的响应时间可能较长，因为需要考虑更多结果。
  - `.topValues()`: For rapid response times and properties with a smaller cardinality. This buckets by the top 1,000 values for the string property. This limit is to ensure that the returned aggregation is not excessively large..topValues() : 用于快速响应时间以及基数较小的属性。此方法按字符串属性的前 1,000 个值进行分桶。此限制是为了确保返回的聚合结果不会过大。
  - `.exactValues()`: For more exact aggregations and the possibility to consider up to 10,000 buckets for high cardinality properties. The amount of considered buckets can be specified via `.exactValues({"maxBuckets": numBuckets})` where `numBuckets` must be an integer value between 0 and 10,000. The response time for this method can take longer, as more results have to be considered..exactValues() : 用于更精确的聚合，并考虑高达 10,000 个分桶的可能性，适用于高基数属性。考虑的分桶数量可以通过 .exactValues({"maxBuckets": numBuckets}) 指定，其中 numBuckets 必须是一个介于 0 到 10,000 之间的整数值。此方法的响应时间可能较长，因为需要考虑更多结果。
  
  - For numeric properties (e.g. `Integer`, `Long`, `Float`, `Double`), the two bucketing options are:
对于数值属性（例如 Integer 、 Long 、 Float 、 Double ），有两种分桶选项：- `.byRanges()` allows you to specify the exact ranges that should be used. For example, you could use `.byRanges({ min: 0, max: 50 }, { min: 50, max: 100 })` to bucket objects into the two ranges of [0, 50] and [50, 100] that you specify here. The `min` of the range is inclusive and the `max` is exclusive. You may omit either `min` or `max` to represent a bucket containing values from -∞ to `max` or `min` to ∞ respectively..byRanges() 允许你指定应使用的确切范围。例如，你可以使用 .byRanges({ min: 0, max: 50 }, { min: 50, max: 100 }) 将对象分桶到[0, 50]和[50, 100]这两个你在此处指定的范围内。范围的 min 是包含的，而 max 是排除的。你可以省略 min 或 max ，分别表示包含从-∞到 max 或 min 到∞的值的分桶。
- `.byFixedWidth()` specifies the width of each bucket. For example, you could use `.byFixedWidth(50)` to bucket objects into ranges that each have a width of 50..byFixedWidth() 指定了每个桶的宽度。例如，你可以使用 .byFixedWidth(50) 将对象分桶到每个宽度为 50 的范围内。
  - `.byRanges()` allows you to specify the exact ranges that should be used. For example, you could use `.byRanges({ min: 0, max: 50 }, { min: 50, max: 100 })` to bucket objects into the two ranges of [0, 50] and [50, 100] that you specify here. The `min` of the range is inclusive and the `max` is exclusive. You may omit either `min` or `max` to represent a bucket containing values from -∞ to `max` or `min` to ∞ respectively..byRanges() 允许你指定应使用的确切范围。例如，你可以使用 .byRanges({ min: 0, max: 50 }, { min: 50, max: 100 }) 将对象分桶到[0, 50]和[50, 100]这两个你在此处指定的范围内。范围的 min 是包含的，而 max 是排除的。你可以省略 min 或 max ，分别表示包含从-∞到 max 或 min 到∞的值的分桶。
  - `.byFixedWidth()` specifies the width of each bucket. For example, you could use `.byFixedWidth(50)` to bucket objects into ranges that each have a width of 50..byFixedWidth() 指定了每个桶的宽度。例如，你可以使用 .byFixedWidth(50) 将对象分桶到每个宽度为 50 的范围内。
  
  - For `LocalDate` properties, various convenience methods are provided for easy bucketing:
对于 LocalDate 属性，提供了各种方便的方法以便轻松分桶：- `.byYear()`
- `.byQuarter()`
- `.byMonth()`
- `.byWeek()`
- `.byDays()` buckets values into days. You may pass in a number of days to use for bucket widths..byDays() 将值分桶到天。你可以传入用于桶宽度的天数。
  - `.byYear()`
  - `.byQuarter()`
  - `.byMonth()`
  - `.byWeek()`
  - `.byDays()` buckets values into days. You may pass in a number of days to use for bucket widths..byDays() 将值分桶到天。你可以传入用于桶宽度的天数。
  
  - For `Timestamp` properties, the same bucketing options apply as for `LocalDate`, as well as the following additions:
对于 Timestamp 属性，与 LocalDate 相同的分桶选项适用，以及以下附加选项：- `.byHours()` buckets values by hours. You may pass in a number of hours to use for bucket widths..byHours() 按小时对值进行分组。您可以传入用于分组宽度的小时数。
- `.byMinutes()` buckets values by minutes. You may pass in a number of minutes to use for bucket widths..byMinutes() 按分钟对值进行分组。您可以传入用于分组宽度的分钟数。
- `.bySeconds()` buckets values by seconds. You may pass in a number of seconds to use for bucket widths..bySeconds() 按秒对值进行分组。您可以传入用于分组宽度的秒数。
  - `.byHours()` buckets values by hours. You may pass in a number of hours to use for bucket widths..byHours() 按小时对值进行分组。您可以传入用于分组宽度的小时数。
  - `.byMinutes()` buckets values by minutes. You may pass in a number of minutes to use for bucket widths..byMinutes() 按分钟对值进行分组。您可以传入用于分组宽度的分钟数。
  - `.bySeconds()` buckets values by seconds. You may pass in a number of seconds to use for bucket widths..bySeconds() 按秒对值进行分组。您可以传入用于分组宽度的秒数。
  
  - For `Array` properties, the bucketing options are determined by the type of the elements in the array. In particular, you get the same bucketing methods for `Array<PropertyType>` as you would get for the `PropertyType` (for example, `Array<boolean>` gets the same bucketing methods as `boolean`).
对于 Array 属性，分组选项由数组中元素的类型决定。特别是，您会得到与 Array<PropertyType> 相同的分组方法，就像您会得到 PropertyType 的分组方法一样（例如， Array<boolean> 得到与 boolean 相同的分组方法）。- For example, if you have an `Array<string>` called `employeeSet` consisting of Alice and Bob who have respectively worked in `["US", "UK"]` and `["US"]`. Then `employeeSet.groupBy(e => e.pastCountries.exactValue()).count()` will return `{ "US": 2, "UK": 1 }`.例如，如果你有一个名为 employeeSet 的 Array<string> ，其中 Alice 和 Bob 分别在 ["US", "UK"] 和 ["US"] 工作过。那么 employeeSet.groupBy(e => e.pastCountries.exactValue()).count() 将返回 { "US": 2, "UK": 1 } 。
  - For example, if you have an `Array<string>` called `employeeSet` consisting of Alice and Bob who have respectively worked in `["US", "UK"]` and `["US"]`. Then `employeeSet.groupBy(e => e.pastCountries.exactValue()).count()` will return `{ "US": 2, "UK": 1 }`.例如，如果你有一个名为 employeeSet 的 Array<string> ，其中 Alice 和 Bob 分别在 ["US", "UK"] 和 ["US"] 工作过。那么 employeeSet.groupBy(e => e.pastCountries.exactValue()).count() 将返回 { "US": 2, "UK": 1 } 。
  
  

After grouping by one property, you may optionally call the `.segmentBy()` method to perform further bucketing. This allows you to compute a three-dimensional aggregation bucketed by two searchable properties. For example, you could group employees by their start date as well as their role as follows:在按一个属性分组后，你可以选择调用 .segmentBy() 方法进行进一步的分桶操作。这允许你计算一个按两个可搜索属性分桶的三维聚合。例如，你可以按员工的开始日期以及他们的角色进行分组，如下所示：


```
Copied!`1Objects.search()
2    .employees()
3    .groupBy(e => e.startDate.byDays())
4    .segmentBy(e => e.role.topValues())`
```


### [](#choosing-an-aggregation-metric)Choosing an aggregation metric选择聚合指标


After grouping your object set, you can call various aggregation methods to compute aggregation metrics on each bucket. Methods that require a property only accept properties marked searchable. Possible aggregation methods are:在您将对象集分组后，可以调用多种聚合方法来计算每个桶的聚合指标。需要属性的方法仅接受标记为可搜索的属性。可能的聚合方法有：


- `.count()` simply returns the number of objects in each bucket.count() 仅返回每个桶中的对象数量
- `.average()` returns the average number for the given numeric, timestamp, date property.average() 返回给定数值、时间戳、日期属性的平均值
- `.max()` returns the maximum value for the given numeric, timestamp, date property.max() 返回给定数值、时间戳、日期属性的最大值
- `.min()` returns the minimum value for the given numeric, timestamp, date property.min() 返回给定数值、时间戳、日期属性的最小值
- `.sum()` returns the sum of values for the given numeric property.sum() 返回给定数值属性的总和
- `.cardinality()` returns the approximate number of distinct values for the given property.cardinality() 返回给定属性的大致不同值数量


Calling one of these methods returns either a `TwoDimensionalAggregation` or `ThreeDimensionalAggregation`. A `ThreeDimensionalAggregation` is returned if you called `.segmentBy()` before calling one of the final aggregation methods.调用这些方法之一会返回一个 TwoDimensionalAggregation 或 ThreeDimensionalAggregation 。如果你在调用最终聚合方法之前调用了 .segmentBy() ，则会返回一个 ThreeDimensionalAggregation 。


[Learn more about the structure of these aggregation types, including **valid bucketing types**.了解更多关于这些聚合类型结构的信息，包括有效的分桶类型。](/docs/foundry/functions/types-reference/#aggregation-types)


Note that the resulting aggregations are wrapped in a `Promise`, as computing the aggregation requires loading data from a remote service. You can use the [async/await ↗](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function) syntax to unwrap the `Promise` result.请注意，结果聚合被包装在一个 Promise 中，因为计算聚合需要从远程服务加载数据。你可以使用 async/await ↗ 语法来解包 Promise 结果。


Below is a full example of loading an aggregation and returning it as a result.下面是一个完整示例，展示如何加载聚合并将其作为结果返回。


```
Copied!`1import { Function, ThreeDimensionalAggregation } from "@foundry/functions-api";
2import { Objects } from "@foundry/ontology-api";
3
4export class AggregationFunctions {
5    @Function()
6    public async employeesByRoleAndOffice(): Promise<ThreeDimensionalAggregation<string, string>> {
7        return Objects.search()
8            .employee()
9            .groupBy(e => e.title.topValues())
10            .segmentBy(e => e.office.topValues())
11            .count();
12    }
13}`
```


Below is a full example of aggregating without groupBy statements:以下是聚合而不使用 groupBy 语句的完整示例：


```
Copied!`1import { Function } from "@foundry/functions-api";
2import { Objects } from "@foundry/ontology-api";
3
4export class AggregationFunctions {
5    @Function()
6    public async employeesStats(): Promise<Double> {
7        // Count of all employees, default to zero if count() returns undefined
8        return Objects.search().employee().count() ?? 0;
9    }
10}`
```


You can also perform other aggregations without groupBy by replacing the appropriate line in the code example above, such as:您也可以通过替换代码示例中相应的行来执行其他聚合操作，例如：


- Count of all employees: `Objects.search().employee().count();` (as seen in example above)所有员工的数量： Objects.search().employee().count(); （如上例所示）
- Average tenure of employees: `Objects.search().employee().average(e => e.tenure);`员工的平均任期： Objects.search().employee().average(e => e.tenure);
- Maximum tenure of employees: `Objects.search().employee().max(e => e.tenure);`员工的最高任期： Objects.search().employee().max(e => e.tenure);
- Minimum tenure of employees: `Objects.search().employee().min(e => e.tenure);`员工最低任期： Objects.search().employee().min(e => e.tenure);
- Sum of all employee salaries: `Objects.search().employee().sum(e => e.salary);`所有员工工资总和： Objects.search().employee().sum(e => e.salary);
- Number of offices: `Objects.search().employee().cardinality(e => e.office);`办公室数量： Objects.search().employee().cardinality(e => e.office);


For an example of manipulating aggregation results in memory, try the guide for [creating custom aggregations](/docs/foundry/functions/create-custom-aggregation/).若想了解如何在内存中操作聚合结果，可尝试查看创建自定义聚合的指南。

