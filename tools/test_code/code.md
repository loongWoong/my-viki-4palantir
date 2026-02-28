# [](#getting-started)Getting started入门


Tip提示The instructions below will guide you through a simple Python data transformation. If you are just getting started with data transformation, consider going through the batch pipeline tutorial for [Pipeline Builder](/docs/foundry/building-pipelines/create-batch-pipeline-pb/) or [Code Repositories](/docs/foundry/building-pipelines/create-batch-pipeline-cr/) first.以下说明将引导你完成简单的 Python 数据转换。如果你刚开始做数据转换，建议先看 Pipeline Builder 或 Code Repositories 的批处理流水线教程。


This tutorial walks through how you can use Python transforms to transform a spreadsheet of recent meteorite discoveries to a usable dataset ready for analysis.本教程将介绍如何使用 Python 变换，将最近陨石发现的电子表格转换为可用的数据集，供分析使用。


## [](#about-the-dataset)About the dataset关于数据集


This tutorial uses data from [NASA’s Open Data Portal ↗](https://data.nasa.gov/). You can follow along on your own code repository with this sample dataset:本教程使用了 NASA 开放数据门户↗ 网站的数据。你可以用这个示例数据集在自己的代码库中跟进：


[`Download meteorite_landings`](/docs/resources/foundry/transforms-python/meteorite_landings.csv)


This dataset contains data about meteorites that have been found on Earth. Note that the data has been cleaned to make it easier to work with.该数据集包含了在地球上发现的陨石数据。请注意，数据已被清理，以便使用。


The dataset includes name, mass, classification, and other identifying information for each meteorite, along with the year it was discovered and coordinates of where it was found. It is good practice to open the CSV to review the data before uploading it into Foundry.该数据集包含每颗陨石的名称、质量、分类及其他识别信息，以及发现年份和发现位置坐标。上传到 Foundry 之前，打开 CSV 查看数据是个好习惯。


## [](#set-up-a-python-code-repository)Set up a Python code repository建立一个 Python 代码仓库


Get started by creating a Python code repository.开始创建一个 Python 代码库。


1. Navigate to a project, and select **+ New > Code repository**.进入一个项目，选择 + 新的 > 代码仓库 。
2. In the **Repository type** section, select **Pipelines**.在仓库类型部分，选择管道 。
3. Select **Python** as the **Language**.选择 Python 作为语言 。
4. Choose to **Initialize repository**.选择初始化仓库 。


### [](#optional-use-a-local-python-repository)Optional: Use a local Python repository可选：使用本地 Python 仓库


Alternatively, you can copy your local Python repository into Code Repositories with the following steps:或者，您也可以通过以下步骤将本地的 Python 仓库复制到代码仓库中：


1. Create a new Python code repository, as described above.创建一个新的 Python 代码仓库，如上所述。
2. On your local repository, remove your previous Git origin (if you cloned it from GitHub, for example): `git remote remove origin`在你的本地仓库中，移除你之前的 Git 起源（比如你从 GitHub 克隆的话）：git remote remove origin
3. Add your code repository's Git remote URL: `git remote add origin <repository_url>`添加你代码仓库的 Git 远程网址： git remote add origin <repository_url>


You can find your code repository URL in the top right corner of the GitHub interface. Select the green **Clone** button, then copy the Git remote URL. Confirm this by running `git remote -v` to return the code repository URL.你可以在 GitHub 界面右上角找到你的代码仓库 URL。选择绿色克隆按钮，然后复制 Git 远程网址。通过运行 git remote -v 返回代码仓库 URL，确认这一点。
4. Merge the current `master` branch (or another branch of your choosing) in Code Repositories into your local branch: `git merge master`将代码仓库中的当前主分支（或你选择的其他分支）合并到本地分支：git merge master


If an error about `refusing to merge unrelated histories` occurs, run the command: `git merge master --allow-unrelated-histories`. This will remove the current Git history associated with your previous remote GitHub repository.如果发生关于的 refusing to merge unrelated histories 错误，执行命令： git merge master --allow-unrelated-histories 。这样会移除你之前远程 GitHub 仓库关联的当前 Git 历史记录。


This merge will bring essential files to your local repository that are required to make commits and changes in Code Repositories.合并后，这些文件将被带到本地仓库，这些文件对于在代码仓库中提交和更改至关重要。
5. Create a new branch and name it (`testbranch`, for example): `git checkout -b testbranch`.创建一个新分支并命名它（例如 testbranch）：git checkout -b testbranch。
6. Make your changes and commit them to your branch.做你的更改并提交给你的分支。
7. Perform `git push`, and confirm that the new branch appears in the Code Repositories interface. Verify that checks are successful.执行 git 推送 ，并确认新分支出现在代码仓库界面中。确认检查是否成功。


Learn more about [local development](/docs/foundry/transforms-python/local-development/) in Code Repositories.在代码仓库中了解更多关于本地开发的信息。


## [](#write-a-python-data-transformation)Write a Python data transformation编写一个 Python 数据转换


Navigate to your Python transforms repository. The default `examples.py` file contains example code to help you get started. Note that you can choose between pandas, Polars, and Spark compute engines. For more information on choosing a compute engine, refer to the [compute engine comparison](/docs/foundry/transforms-python/compute-engines/) documentation.
Start by creating a new file in `src/myproject/datasets`, and call it `meteor_analysis.py` to organize your analysis. Make sure you import the required functions and classes. Define a transformation that takes your `meteor_landings` dataset as input and creates `meteor_landings_cleaned` as its output:进入你的 Python 变换仓库。默认的 examples.py 文件包含示例代码，帮助你入门。注意你可以选择 pandas、Polars 和 Spark 计算引擎。有关选择计算引擎的更多信息，请参阅计算引擎比较文档。先在 src/myproject/datasets 创建一个新文件，并称之为 meteor_analysis.py，以便整理你的分析。确保导入所需的函数和类。定义一个转换，将你的 meteor_landings 数据集作为输入，输出 meteor_landings_cleaned：


Polars极地DuckDB鸭子数据库Pandas熊猫PySpark```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.using(
5    # Replace this with your output dataset path
6    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
7    # Replace this with your input dataset path
8    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
9)
10def clean(output, meteorite_landings):
11    df = meteorite_landings.polars()
12    # Your data transformation logic
13    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.using(
5    # Replace this with your output dataset path
6    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
7    # Replace this with your input dataset path
8    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
9)
10def clean(ctx, output, meteorite_landings):
11    conn = ctx.duckdb().conn
12    # Your data transformation logic using SQL
13    query = conn.sql("SELECT * FROM meteorite_landings")
14    output.write_table(query)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.using(
5    # Replace this with your output dataset path
6    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
7    # Replace this with your input dataset path
8    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
9)
10def clean(output, meteorite_landings):
11    df = meteorite_landings.pandas()
12    # Your data transformation logic
13    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.spark.using(
5    # Replace this with your output dataset path
6    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
7    # Replace this with your input dataset path
8    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
9)
10def clean(output, meteorite_landings):
11    df = meteorite_landings.dataframe()
12    # Your data transformation logic
13    output.write_dataframe(df)`
```


Now, suppose you want to filter your input dataset down to any “Valid” meteors that happened after the year 1950. Update your data transformation logic to filter the meteorites by `nametype` and `year`:现在，假设你想筛选出 1950 年以后发生的“有效”流星。更新你的数据转换逻辑，按名称类型和年份过滤陨石：


Polars极地DuckDB鸭子数据库Pandas熊猫PySpark```
Copied!`1import polars as pl
2from transforms.api import transform, Input, Output
3
4
5@transform.using(
6    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
7    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
8)
9def clean(output, meteorite_landings):
10    df = (
11        meteorite_landings.polars()
12        .filter(pl.col("nametype") == "Valid")
13        .filter(pl.col("year") >= 1950)
14    )
15    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3@transform.using(
4    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
5    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
6)
7def clean(ctx, output, meteorite_landings):
8    conn = ctx.duckdb().conn
9    query = conn.sql("""
10        SELECT *
11        FROM meteorite_landings
12        WHERE nametype = 'Valid' AND year >= 1950
13    """)
14    output.write_table(query)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.using(
5    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
6    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
7)
8def clean(output, meteorite_landings):
9    df = meteorite_landings.pandas()
10    df = df[
11        (df["nametype"] == "Valid") &
12        (df["year"] >= 1950)
13    ]
14    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.spark.using(
5    output=Output("/Users/jsmith/meteorite_landings_cleaned"),
6    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
7)
8def clean(output, meteorite_landings):
9    df = (
10        meteorite_landings.dataframe().filter(
11            meteorite_landings.dataframe().nametype == 'Valid'
12        ).filter(
13            meteorite_landings.dataframe().year >= 1950
14        )
15    )
16    output.write_dataframe(df)`
```


## [](#build-your-output-dataset)Build your output dataset构建你的输出数据集


To build your resulting dataset, commit your changes and select **Build** in the top right corner. For more information about building datasets in Code Repositories, review the [Create a simple batch pipeline](/docs/foundry/building-pipelines/create-batch-pipeline-cr/) tutorial.要构建你得到的数据集，提交你的更改后，在右上角选择 “构建 ”。想了解更多关于在代码仓库中构建数据集的信息，请查看 “创建简单批处理流水线 ”教程。


## [](#add-to-your-data-transformation)Add to your data transformation添加数据转换功能


With Python transforms, you can create multiple output datasets in a single Python file.通过 Python 转换，你可以在一个 Python 文件中创建多个输出数据集。


Let’s say you want to filter down even further to only meteors that were particularly large for their meteorite type. To do so, you will need to:假设你还想进一步筛选，只筛选出对于其陨石类型来说特别大的流星。为此，您需要：


1. Find the average mass for each meteorite type, and求每种陨石类型的平均质量，
2. Compare each meteor’s mass to the average mass for its meteor type.将每颗陨石的质量与其流星类型的平均质量进行比较。


First, add a data transformation to `meteor_analysis.py` that finds the average mass for each meteorite type. This transformation takes your `meteor_landings` dataset as input and creates `meteorite_stats` as its output:首先，在 meteor_analysis.py 中添加一个数据变换，以求出每种陨石类型的平均质量。这种转换以你的 meteor_landings 数据集为输入，输出为 meteorite_stats：


Polars极地Pandas熊猫PySpark```
Copied!`1import polars as pl
2from transforms.api import transform, Input, Output
3
4
5@transform.using(
6    # Output dataset name must be unique
7    output=Output("/Users/jsmith/meteorite_stats"),
8    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
9)
10def stats(output, meteorite_landings):
11    df = (
12        meteorite_landings.polars()
13        .groupby("class")
14        .agg(pl.col("mass").mean().alias("avg_mass_per_class"))
15    )
16    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.using(
5    # Output dataset name must be unique
6    output=Output("/Users/jsmith/meteorite_stats"),
7    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
8)
9def stats(output, meteorite_landings):
10    df = (
11        meteorite_landings.pandas()
12            .groupby("class", as_index=False)["mass"]
13            .mean()
14            .rename(columns={"mass": "avg_mass_per_class"})
15    )
16    output.write_table(df)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.spark.using(
5    # Output dataset name must be unique
6    output=Output("/Users/jsmith/meteorite_stats"),
7    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
8)
9def stats(output, meteorite_landings):
10    df = (
11        meteorite_landings.dataframe().groupBy("class").agg(
12            F.mean("mass").alias("avg_mass_per_class")
13        )
14    )
15    output.write_dataframe(df)`
```


Next, create a data transformation that compares each meteor’s mass to the average mass for its meteor type. The information needed for this transformation is spread across the `meteorite_landings` and `meteorite_stats` tables that you created in this tutorial. You must join the two datasets and filter the resulting dataset to find meteorites that have a greater-than-average mass, as shown below:接下来，创建一个数据转换，将每颗流星的质量与其流星类型的平均质量进行比较。完成这个转换所需的信息分布在你在本教程中创建的 meteorite_landings 表和 meteorite_stats 表中。你必须将这两个数据集合并，并筛选结果数据集，以找到质量大于平均值的陨石，如下所示：


Polars极地Pandas熊猫PySpark```
Copied!`1import polars as pl
2from transforms.api import transform, Input, Output
3
4
5@transform.using(
6    output=Output("/Users/jsmith/meteorite_enriched"),
7    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
8    meteorite_stats=Input("/Users/jsmith/meteorite_stats"),
9)
10def enriched(output, meteorite_landings, meteorite_stats):
11    df_landings = meteorite_landings.polars()
12    df_stats = meteorite_stats.polars()
13
14    enriched = df_landings.join(df_stats, on="class", how="inner")
15    enriched = enriched.with_columns(
16        (pl.col("mass") > pl.col("avg_mass_per_class")).alias("greater_mass")
17    )
18    result = enriched.filter(pl.col("greater_mass"))
19    output.write_table(result)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.spark.using(
5    output=Output("/Users/jsmith/meteorite_enriched"),
6    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
7    meteorite_stats=Input("/Users/jsmith/meteorite_stats"),
8)
9def enriched(output, meteorite_landings, meteorite_stats):
10    df_landings = meteorite_landings.pandas()
11    df_stats = meteorite_stats.pandas()
12
13    enriched = df_landings.merge(df_stats, on="class", how="inner")
14    enriched["greater_mass"] = enriched["mass"] > enriched["avg_mass_per_class"]
15    result = enriched[enriched["greater_mass"]]
16    output.write_table(result)`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4@transform.spark.using(
5    output=Output("/Users/jsmith/meteorite_enriched"),
6    meteorite_landings=Input("/Users/jsmith/meteorite_landings"),
7    meteorite_stats=Input("/Users/jsmith/meteorite_stats"),
8)
9def enriched(output, meteorite_landings, meteorite_stats):
10    df_landings = meteorite_landings.dataframe()
11    df_stats = meteorite_stats.dataframe()
12
13    enriched_together = df_landings.join(df_stats, "class")
14    greater_mass=enriched_together.withColumn(
15        'greater_mass', (enriched_together.mass > enriched_together.avg_mass_per_class)
16    )
17    result = greater_mass.filter("greater_mass")
18    output.write_dataframe(result)`
```


Now, you can further analyze the resulting `meteorite_enriched` dataset by exploring it in Contour.现在，您可以通过在 Contour 中进一步分析所得的 meteorite_enriched 数据集。


## [](#apply-your-data-transformation-to-multiple-inputs)Apply your data transformation to multiple inputs将数据转换应用于多个输入


So far, you created a dataset that contains meteorites of all types with a greater-than-average mass. The next step is to create separate datasets for each meteorite type. With Python transforms, you can use a for-loop to apply the same data transformation to each type of meteorite. For more information on applying the same data transformation to different inputs, refer to the section on [transform generation](/docs/foundry/transforms-python/transforms/#transform-generation).到目前为止，你创建了一个包含各种质量大于平均水平的陨石的数据集。下一步是为每种陨石类型创建独立数据集。通过 Python 转换，你可以用 for-loop 对每种陨石类型应用相同的数据转换。有关将相同数据转换应用于不同输入的更多信息，请参阅关于变换生成的部分。


Create a new file in `src/myproject/datasets` and name it `meteor_class.py`. Note that you can continue writing your data transformation code in the `meteor_analysis.py` file, but this tutorial uses a new file to separate the data transformation logic.在 src/myproject/datasets 创建一个新文件，并将其命名为 meteor_class.py。注意你可以继续在 meteor_analysis.py 文件中编写数据转换代码，但这个教程使用一个新文件来分离数据转换逻辑。


To create separate datasets for each meteorite type, filter the `meteorite_enriched` dataset by class. Then, define a `transform_generator` function that applies the same data transformation logic to each of the meteorite types you want to analyze:要为每种陨石类型创建独立数据集，请按类别过滤 meteorite_enriched 数据集。然后，定义一个 transform_generator 函数，将相同的数据转换逻辑应用于你想分析的每种陨石类型：


Polars极地Pandas熊猫PySpark```
Copied!`1import polars as pl
2from transforms.api import transform, Input, Output
3
4
5def transform_generator(sources):
6    transforms = []
7    for source in sources:
8        @transform.using(
9            output=Output(f'/Users/jsmith/meteorite_{source}'),
10            my_input=Input('/Users/jsmith/meteorite_enriched')
11        )
12        def filter_by_source(output, my_input, source=source):
13            df = my_input.polars()
14            result = df.filter(pl.col("class") == source)
15            output.write_table(result)
16        transforms.append(filter_by_source)
17    return transforms
18
19TRANSFORMS = transform_generator(["L6", "H5", "H4"])`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4def transform_generator(sources):
5    transforms = []
6    for source in sources:
7        @transform.using(
8            output=Output(f'/Users/jsmith/meteorite_{source}'),
9            my_input=Input('/Users/jsmith/meteorite_enriched')
10        )
11        def filter_by_source(output, my_input, source=source):
12            df = my_input.pandas()
13            result = df[df["class"] == source]
14            output.write_table(result)
15        transforms.append(filter_by_source)
16    return transforms
17
18TRANSFORMS = transform_generator(["L6", "H5", "H4"])`
```

```
Copied!`1from transforms.api import transform, Input, Output
2
3
4def transform_generator(sources):
5    transforms = []
6    for source in sources:
7        @transform.spark.using(
8            output=Output(f'/Users/jsmith/meteorite_{source}'),
9            my_input=Input('/Users/jsmith/meteorite_enriched')
10        )
11        def filter_by_source(output, my_input, source=source):
12            result = my_input.dataframe().filter(my_input["class"] == source)
13            output.write_table(result)
14        transforms.append(filter_by_source)
15    return transforms
16
17TRANSFORMS = transform_generator(["L6", "H5", "H4"])`
```


This will create a transformation that filters our meteorite dataset by class. Note that we must pass `source=source` into the `filter_by_source` function in order to capture the `source` parameter in the function’s scope.这将创建一个按类别过滤陨石数据集的变换。注意，我们必须将 source=source 传递到 filter_by_source 函数，才能在函数的作用域中捕获源参数。


Tip提示For the initial data transformation created in the `meteor_analysis.py` file, you did not have to do any additional configuration to add Transforms to your project’s pipeline. This is because the default Python project structure uses automatic registration to discover all transform objects within your `datasets` folder.在 meteor_analysis.py 文件中创建的初始数据转换中，无需额外配置即可将变换添加到项目的流水线中。这是因为默认的 Python 项目结构使用自动注册来发现数据集文件夹中的所有变换对象。

To add this final transformation to your project’s pipeline using automatic registration, you must add the generated transforms to a variable as a list. In the example above, we used the variable `TRANSFORMS`. For more information about automatic registration and transforms generators, refer to the section on [transforms generation](/docs/foundry/transforms-python/transforms/#transform-generation) in the Python transforms documentation.要通过自动注册将最终变换添加到项目流程中，必须将生成的变换添加到变量中作为列表。在上述示例中，我们使用了变量 TRANSFORMS。关于自动配准和变换生成器的更多信息，请参阅 Python 变换文档中关于变换生成的部分。

