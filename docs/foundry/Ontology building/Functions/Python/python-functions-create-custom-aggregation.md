# [](#create-a-custom-aggregation)Create a custom aggregation创建自定义聚合


Functions can be used to compute custom aggregations based on data in the ontology, which can then be surfaced in a chart widget in Workshop. This guide walks through how to write custom aggregation logic that loads aggregated data from the ontology, manipulates the results to create a projection of future results, and returns the modified results.函数可用于基于本体中的数据计算自定义聚合，然后可以在 Workshop 中的图表小部件中显示这些聚合。本指南将介绍如何编写自定义聚合逻辑，该逻辑从本体加载数据聚合，操作结果以创建未来结果的投影，并返回修改后的结果。


These references may be useful while working through this section:在完成本节时，这些参考可能很有用：


- Reference for [Python aggregation types](/docs/foundry/functions/types-reference/#aggregation-types)Python 聚合类型参考


`.from_osdk()` in `TwoDimensionalAggregation` and `ThreeDimensionalAggregation` are only supported when using v2 of the Python OSDK..from_osdk() 在 TwoDimensionalAggregation 和 ThreeDimensionalAggregation 中仅在使用 Python OSDK v2 时才受支持。


## [](#loading-an-aggregation)Loading an aggregation加载聚合数据


In this example, assume you have an ontology consisting of expenses, with each `expense` object having properties for department name, expense `date`, and expense `amount`. If you want to estimate the monthly spend by department over the next six months, you can begin by loading the aggregated data for the monthly spend:在这个例子中，假设你有一个包含费用的本体，每个 expense 对象都有部门名称、费用 date 和费用 amount 的属性。如果你想要估算未来六个月的部门月度支出，你可以从加载月度支出的聚合数据开始：


```
Copied!`1client = FoundryClient()
2result: AggregateObjectsResponse = client.ontology.objects.Expense
3    .group_by(Expense.object_type.department_name.exact())
4    .group_by(Expense.object_type.date.exact())
5    .sum(Expense.object_type.amount)`
```


## [](#manipulating-aggregation-results)Manipulating aggregation results操作聚合结果


Next, you can extrapolate the spend for each department for the next six months. For this example, you can take a simple approach of using the final month's value as the estimate for the next six months.接下来，你可以推算出各部门未来六个月的支出。在这个例子中，你可以采用简单的方法，将最后一个月的数值作为未来六个月的估算值。


```
Copied!`1current_buckets = ThreeDimensionalAggregation.from_osdk(result, "departmentName", "date")
2modified_buckets: list[NestedBucket[str, Range[Date], Double]] = []
3date_format = "%Y-%m-%d"
4for bucket in current_buckets.buckets:
5    # Find the bucket corresponding to the most recent month
6    last_bucket: SingleBucket[Date, Double] = bucket[-1].value
7
8    next_six_months: list[SingleBucket[Range[Date], Double]] = []
9    # The `date` field has been converted to a string formatted YYYY-MM-DD.
10    # Convert to type `Date` from the string. Convert back to a string when
11    # creating a SingleBucket object for each month
12    current_month: Date = datetime.strptime(last_bucket.key, date_format).date()
13
14    # Loop six times
15    for _ in range(6):
16        # Construct the next month from the current month
17        next_month = current_month + relativedelta(months=1)
18        # Add a new bucket which uses the next month as the date range
19        # and the most recent months amount as the value
20        next_six_months.append(SingleBucket(Range(min=current_month, max=next_month), last_bucket.value))
21        current_month = next_month
22
23    # Append the modified results as a NestedBucket
24    modified_buckets.append(NestedBucket(bucket.key, next_six_months))`
```


## [](#returning-the-aggregation)Returning the aggregation返回聚合结果


Now that you have created an estimate for the next six months, you can return these estimated values as a `ThreeDimensionalAggregation`:现在你已经为未来六个月创建了估算值，你可以将这些估算值作为 ThreeDimensionalAggregation 返回：


```
Copied!`1return ThreeDimensionalAggregation(modified_buckets)`
```


The full example code for this function is as follows:这个函数的完整示例代码如下：


```
Copied!`1from dateutil.relativedelta import relativedelta
2from datetime import datetime
3
4from functions.api import (
5    Date,
6    Double,
7    NestedBucket,
8    SingleBucket,
9    String,
10    Range,
11    ThreeDimensionalAggregation,
12    function,
13)
14from ontology_sdk import FoundryClient
15from ontology_sdk.ontology.objects import Expense
16
17
18@function
19def estimated_department_expenses() -> ThreeDimensionalAggregation[str, Date, Double]:
20    client = FoundryClient()
21    result: AggregateObjectsResponse = client.ontology.objects.Expense
22        .group_by(Expense.object_type.department_name.exact())
23        .group_by(Expense.object_type.date.exact())
24        .sum(Expense.object_type.amount)
25
26    current_buckets = ThreeDimensionalAggregation.from_osdk(result, "departmentName", "date")
27    modified_buckets: list[NestedBucket[str, Range[Date], Double]] = []
28    date_format = "%Y-%m-%d"
29    for bucket in current_buckets.buckets:
30        # Find the bucket corresponding to the most recent month
31        last_bucket: SingleBucket[Date, Double] = bucket.buckets[-1]
32
33        next_six_months: list[SingleBucket[Range[Date], Double]] = []
34        # The `date` field has been converted to a string formatted YYYY-MM-DD.
35        # Convert to type `Date` from the string.
36        current_month: Date = datetime.strptime(last_bucket.key, date_format).date()
37
38        # Loop six times
39        for _ in range(6):
40            # Construct the next month from the current month
41            next_month = current_month + relativedelta(months=1)
42            # Add a new bucket which uses the next month as the date range
43            # and the most recent months amount as the value
44            next_six_months.append(SingleBucket(Range(min=current_month, max=next_month), last_bucket.value))
45            current_month = next_month
46
47        # Append the modified results as a NestedBucket
48        modified_buckets.append(NestedBucket(bucket.key, next_six_months))
49
50    return ThreeDimensionalAggregation(modified_buckets)`
```


The resulting aggregation can be used in a Workshop chart to show the monthly spend estimate for the next six months.由此产生的汇总可以在工作坊图表中使用，以显示未来六个月的月度支出估算。

