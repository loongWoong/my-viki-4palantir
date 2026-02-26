# [](#stub-object-searches-and-aggregations)Stub object searches and aggregationsStub 对象搜索和聚合


When writing unit tests you may want to create canned answers (also called "stubs") for object sets searches or object aggregations to dictate the responses to the calls your code is making when writing unit tests. You need to import `{ whenObjectSet }` from `"@foundry/functions-testing-lib"` to use stubs.在编写单元测试时，您可能希望为对象集搜索或对象聚合创建预定义的答案（也称为"存根"），以指定在编写单元测试时您的代码调用时的响应。您需要从 "@foundry/functions-testing-lib" 导入 { whenObjectSet } 才能使用存根。


#### [](#testing-filters-on-object-sets)Testing filters on object sets在对象集上测试过滤器


```
Copied!`1import { Objects } from "@foundry/ontology-api";
2
3const objectSet = Objects.search().objectType();
4
5expect(myFunctions.filterObjectSet(objectSet))
6        .toEqual(objectSet.filter(s => s.prop.range().gte(0)))`
```


#### [](#testing-aggregations-on-an-object-property-using-stubs)Testing aggregations on an object property using stubs使用存根在对象属性上测试聚合


You can define the response to aggregation calls using stubs.你可以使用存根来定义聚合调用的响应。


```
Copied!`1import { whenObjectSet } from "@foundry/functions-testing-lib"
2
3whenObjectSet(Objects.search().objectType().sum(s => s.property)).thenReturn(55);`
```


This means that whenever `Objects.search().objectType().sum(s => s.property))` is run, the result will be 55.这意味着每当运行 Objects.search().objectType().sum(s => s.property)) 时，结果将是 55。


#### [](#testing-objects-using-stubs)Testing objects using stubs使用存根测试对象


You can also define the response to certain object searches using stubs.你也可以使用存根来定义对某些对象搜索的响应。


```
Copied!`1import { whenObjectSet } from "@foundry/functions-testing-lib";
2
3whenObjectSet(Objects.search().objectType().orderBy().takeAsync(10)).thenReturn([employeeObj])
4await expect(myFunctions.aggregateSum(objectSet)).resolves.toEqual(65);`
```


This means that whenever this particular objects search aggregation is run, the property sum will resolve to 65.这意味着每当运行这个特定对象的搜索聚合时，属性总和将解析为 65。


#### [](#testing-different-object-sets-using-stubs)Testing different object sets using stubs使用存根测试不同的对象集


You can mock multiple specific object set searches by overloading the search constructor. You must give each object a `rid` property.你可以通过重载搜索构造函数来模拟多个特定对象集的搜索。你必须给每个对象一个 rid 属性。


```
Copied!`1import { whenObjectSet } from "@foundry/functions-testing-lib";
2
3const objA = Objects.create().objectType('a');
4const objB = Objects.create().objectType('b');
5
6objA.rid = 'ridA';
7objB.rid = 'ridB';
8
9whenObjectSet(Objects.search().ObjType([objA]).all()).thenReturn([objA]);
10whenObjectSet(Objects.search().ObjType([objB, objB]).all()).thenReturn([objA, objB]);`
```

