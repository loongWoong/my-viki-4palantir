# [](#create-a-custom-aggregation)Create a custom aggregation创建自定义聚合


Functions can be used to compute custom aggregations based on data in the ontology, which can then be surfaced in a chart widget in Workshop. This guide walks through how to write custom aggregation logic that loads aggregated data from the ontology, manipulates the results to create a projection of future results, and returns the modified results.函数可用于基于本体中的数据计算自定义聚合，然后可以在 Workshop 中的图表小部件中展示这些聚合结果。本指南将介绍如何编写自定义聚合逻辑，该逻辑从本体加载数据聚合结果，操作这些结果以创建未来结果的投影，并返回修改后的结果。


These references may be useful while working through this section:在完成本节时，这些参考资料可能很有用：


- Reference for [Object Set aggregations](/docs/foundry/functions/api-object-sets/#computing-aggregations)对象集聚合的参考资料
- Reference for [aggregation types](/docs/foundry/functions/types-reference/#aggregation-types)聚合类型的参考资料


## [](#loading-an-aggregation)Loading an aggregation加载聚合数据


In this example, assume you have an ontology consisting of expenses, with each `expense` object having properties for department name, expense `date`, and expense `amount`. If you want to estimate the monthly spend by department over the next six months, you can begin by loading the aggregated data for the monthly spend:在这个例子中，假设你有一个包含费用的本体，每个 expense 对象都有部门名称、费用 date 和费用 amount 的属性。如果你想要估算未来六个月的部门月度支出，你可以从加载月度支出的聚合数据开始：


```
Copied!`1const result = await Objects.search()
2    .expenses()
3    .groupBy(expense => expense.departmentName.topValues())
4    .segmentBy(expense => expense.date.byMonth())
5    .sum(expense => expense.amount);`
```


## [](#manipulating-aggregation-results)Manipulating aggregation results操作聚合结果


Next, you can extrapolate the spend for each department for the next six months. For this example, you can take a simple approach of using the final month's value as the estimate for the next six months.接下来，你可以预测每个部门未来六个月的支出。在这个例子中，你可以采用简单的方法，将最后一个月的值作为未来六个月的估算值。


```
Copied!`1const modifiedBuckets = result.buckets.map(bucket => {
2    // Find the bucket corresponding to the most recent month
3    const lastBucket = bucket.value[bucket.value.length - 1];
4
5    let nextSixMonths: IBaseBucket<IRange<Timestamp>, Double>[] = [];
6    let currentMonth = lastBucket.key.max!;
7    // Loop six times
8    for (let i = 0; i < 6; i++) {
9        // Find the end of this range (the following month)
10        const nextMonth = currentMonth.plusMonths(1);
11        // Add a new bucket which uses the next month as the date range
12        // and the most recent month as the value
13        nextSixMonths.push({
14            key: {
15                min: currentMonth,
16                max: nextMonth,
17            },
18            value: lastBucket.value,
19        });
20        currentMonth = nextMonth;
21    }
22
23    // Return the modified results
24    return { key: bucket.key, value: nextSixMonths };
25});`
```


## [](#returning-the-aggregation)Returning the aggregation返回聚合结果


Now that you have created an estimate for the next six months, you can return these estimated values:现在你已经为未来六个月创建了一个估算，你可以返回这些估算值：


```
Copied!`1return { buckets: modifiedBuckets };`
```


The full example code for this function is as follows:此函数的完整示例代码如下：


```
Copied!`1@Function()
2public async estimatedDepartmentExpenses(): Promise<ThreeDimensionalAggregation<string, IRange<Timestamp>>> {
3    const result = await Objects.search()
4        .expenses()
5        .groupBy(expense => expense.departmentName.topValues())
6        .segmentBy(expense => expense.date.byMonths())
7        .sum(expense => expense.amount);
8
9    const modifiedBuckets = result.buckets.map(bucket => {
10        // Find the bucket corresponding to the most recent month
11        const lastBucket = bucket.value[bucket.value.length - 1];
12
13        let nextSixMonths: IBaseBucket<IRange<Timestamp>, Double>[] = [];
14        let currentMonth = lastBucket.key.max!;
15        // Loop six times
16        for (let i = 0; i < 6; i++) {
17            // Find the end of this range (the following month)
18            const nextMonth = currentMonth.plusMonths(1);
19            // Add a new bucket which uses the next month as the date range
20            // and the most recent month as the value
21            nextSixMonths.push({
22                key: {
23                    min: currentMonth,
24                    max: nextMonth,
25                },
26                value: lastBucket.value,
27            });
28            currentMonth = nextMonth;
29        }
30
31        // Return the modified results
32        return { key: bucket.key, value: nextSixMonths };
33    });
34
35    return { buckets: modifiedBuckets };
36}`
```


The resulting aggregation can be used in a Workshop chart to show the monthly spend estimate for the next six months.由此产生的汇总可以在工作坊图表中使用，以显示未来六个月的月度支出估算。

