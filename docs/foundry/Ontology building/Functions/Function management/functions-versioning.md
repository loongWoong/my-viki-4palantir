# [](#function-versioning)Function versioning功能版本控制


This document describes the versioning system used for functions. Versions for function releases are chosen by their publishers and are immutable after creation. Applying appropriate versions is critical to providing consumers of your functions with a stable and reliable experience.本文档描述了用于功能的版本控制系统。功能发布的版本由其发布者选择，创建后不可更改。应用适当的版本对于为您的功能消费者提供稳定可靠的体验至关重要。


## [](#backward-compatible-changes-vs-breaking-changes)Backward compatible changes vs. breaking changes向后兼容的变更与破坏性变更


The versioning system for functions distinguishes between backward compatible changes and breaking changes. *Backward compatible changes* are changes that do not disrupt existing consumers of your functions. A change that is not backward compatible can be referred to as a *backward incompatible* or a *breaking* change.功能的版本控制系统区分向后兼容的变更和破坏性变更。向后兼容的变更是指不会中断您功能现有消费者的变更。一个不向后兼容的变更可以称为向后不兼容的变更或破坏性变更。


Some examples of backward compatible changes are:向后兼容性变更的一些例子包括：


- Adding an optional input to a function’s signature.给函数的签名添加一个可选输入。
- Optimizing a function’s performance without changing its expected behavior.优化函数的性能而不改变其预期行为。
- Fixing a bug in your function without changing its expected behavior.修复函数中的错误而不改变其预期行为。


Some examples of breaking changes are:一些不兼容的变更示例包括：


- Adding a required input to a function’s signature.给函数签名添加一个必需的输入。
- Changing the output type of a function’s signature from an integer to a string.将函数签名的输出类型从整数更改为字符串。
- Deleting a function.删除一个函数。


When considering whether a change to an existing version is backward compatible, ask yourself if the change would cause disruption to or require explicit attention from a consumer of the existing version.在考虑对现有版本进行更改是否向后兼容时，问自己这个更改是否会对现有版本的消费者造成干扰或需要明确的关注。


Remember that you are ultimately in charge of dictating the expected consumption patterns of your functions.记住，你最终负责规定你的函数的预期使用模式。


## [](#the-semantic-versioning-system)The semantic versioning system语义版本系统


Functions are versioned according to the [Semantic Versioning ↗](https://semver.org/) system.函数按照语义版本系统 ↗ 进行版本控制。


In Semantic Versioning, versions take the form `X.Y.Z` where `X`, `Y`, and `Z`—known as the major, minor, and patch versions respectively—are non-negative integers (for instance, `1.2.3`). A version may also include a prerelease identifier comprised of alphanumeric characters by appending a hyphen immediately following the patch version (for example, `1.2.3-rc1`).在语义版本控制中，版本采用 X.Y.Z 的形式，其中 X 、 Y 和 Z 分别被称为主版本号、次版本号和修订版本号，它们是非负整数（例如 1.2.3 ）。版本还可以通过在修订版本号后立即附加一个连字符来包含一个由字母数字字符组成的预发布标识符（例如 1.2.3-rc1 ）。


This page provides a brief summary of Semantic Versioning. We encourage you to read the [full specification ↗](https://semver.org/) since adhering to the specification is an important aspect of publishing functions that can be reliably consumed in other applications.本页面简要介绍了语义版本控制。我们鼓励您阅读完整规范 ↗，因为遵循规范是发布可在其他应用程序中可靠使用功能的方面的重要组成部分。


### [](#choosing-a-release-version)Choosing a release version选择发布版本


When publishing a new version of a function, consider the following points from the Semantic Versioning specification:当发布函数的新版本时，请考虑语义版本控制规范中的以下要点：


- Major version `0` (`0.y.z`) is for initial development. During initial development, the function may change at any time and your functions should not be considered stable by consumers.主版本 0 （ 0.y.z ）用于初始开发。在初始开发期间，功能可能随时变更，因此你的功能不应被视为稳定版供消费者使用。
- The major version should be incremented when you make backward incompatible changes.当你进行向后不兼容的变更时，应增加主版本号。
- The minor version should be incremented when you add functionality in a backward compatible manner.当你以向后兼容的方式添加功能时，应增加次版本号。
- The patch version should be incremented when you make backward compatible bug fixes.当你进行向后兼容的补丁修复时，应增加修订版本号。
- A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version.一个预发布版本表示该版本不稳定，可能无法满足其相关正常版本所标明的预期兼容性要求。


### [](#backward-compatibility-checks)Backward compatibility checks向后兼容性检查


Backward compatibility checks are performed for your functions before you publish a new version. In particular, you will be warned about any of the following breaking changes:在您发布新版本之前，将为您执行向后兼容性检查。特别是，您将收到以下任何破坏性变更的警告：


- Dropping a function. This includes deleting a function in your Python or TypeScript function code repository.删除一个函数。这包括从您的 Python 或 TypeScript 函数代码库中删除一个函数。
- Dropping an input (even an optional one) on a function’s signature.在函数的签名上放置一个输入（即使是可选的）。
- Reordering an input on a function’s signature.在函数的签名上重新排序一个输入。
- Adding a required input to a function’s signature.向函数的签名添加一个必需的输入。
- Bad input type changes (such as integer to string). Note that widening a numeric input type (like integer to float) will result in a warning.不良的输入类型更改（例如整数到字符串）。注意，扩展数值输入类型（如整数到浮点数）将导致警告。
- Bad output type changes (such as string to optional string).错误的输出类型变更（如字符串到可选字符串）。


If these checks fail for any reason, it is recommended that you release a major version. However, this does not apply if you are still in the initial development phase (that is, you are still at major version `0`).如果因任何原因这些检查失败，建议你发布一个主版本。但是，如果你仍处于初始开发阶段（即你仍处于主版本 0 ），则不适用。


Palantir's built-in checks are not exhaustive of all types of breaking changes. For instance, breaking changes from your internal implementation may not be detected. It is not safe to release a minor or patch version based solely on a successful outcome from these checks.Palantir 的内置检查并非涵盖所有类型的破坏性变更。例如，来自您内部实现的破坏性变更可能无法被检测到。仅根据这些检查的成功结果来发布小版本或补丁版本是不安全的。


#### [](#caveat-custom-types)Caveat: Custom types注意事项：自定义类型


The internal functions data type representation currently lacks sufficient information regarding the optionality of custom type fields. As a result, you may notice that for custom type inputs and outputs, the backward compatibility checks will warn you when removing or adding any fields, including optional fields (such as `quantity?: Integer` in Typescript or `quantity: Integer = 0` in Python).当前内部函数数据类型表示方式在自定义类型字段的可选性方面缺乏足够信息。因此，您可能会发现对于自定义类型的输入和输出，在删除或添加任何字段（包括可选字段，例如 TypeScript 中的 quantity?: Integer 或 Python 中的 quantity: Integer = 0 ）时，向后兼容性检查会发出警告。


We are currently making changes so that going forward you will not be warned when removing an optional field on an output custom type or adding an optional field on an input custom type.我们目前正在对此进行修改，以便将来在删除输出自定义类型上的可选字段或在输入自定义类型上添加可选字段时，您将不再收到警告。


You will still receive a warning when removing an optional field on an input custom type. It is generally considered bad practice to ignore any fields provided by a consumer as they likely expect the provided fields to tell the behavior of your function.在移除输入自定义类型中的可选字段时，您仍然会收到一条警告。通常认为忽略消费者提供的任何字段是一种不良实践，因为它们很可能期望提供的字段能够说明您的函数的行为。


### [](#restrict-stable-version-tags)Restrict stable version tags限制稳定版本标签


Stable Semantic Version releases (non-prerelease versions) may be immediately consumed by downstream production applications if the applications have been configured to reference the Function by a version range (for example, `>=1.2.3 <2.0.0`). This makes it important to review and test code changes before releasing them in a new stable version.稳定语义版本发布（非预发布版本）如果应用程序已配置为通过版本范围引用函数（例如， >=1.2.3 <2.0.0 ），则可以立即被下游生产应用程序消费。这使得在发布新稳定版本之前审查和测试代码变更变得非常重要。


It is possible to enforce restrictions on the release of stable versions of your Functions by [enabling a toggle](/docs/foundry/code-repositories/branch-settings/#restrict-stable-version-tags) in the repository settings for protected branches.可以通过在受保护分支的存储库设置中启用一个开关来强制执行对您的函数稳定版本发布的限制。


## [](#frequently-asked-questions)Frequently asked questions常见问题


### [](#choosing-release-versions-in-the-0yz-initial-development-phase)Choosing release versions in the 0.y.z initial development phase在 0.y.z 初始开发阶段选择发布版本


It is common practice that any breaking changes be made in a minor release and any backward compatible changes be made in a patch release. This is an assumption made by consumers in many development spheres, such as the Node/NPM ecosystem, as demonstrated by their wide use of [caret ranges ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004).通常的做法是，任何破坏性变更都在次版本中发布，任何向后兼容的变更都在补丁版本中发布。这是许多开发领域（如 Node/NPM 生态系统）的消费者所做出的假设，这一点从他们广泛使用尖括号范围 ↗ 的做法中可以看出。


### [](#accidentally-releasing-a-backward-incompatible-change-as-a-patch-or-minor-version)Accidentally releasing a backward incompatible change as a patch or minor version意外将向后不兼容的变更作为补丁或小版本发布


As soon as you realize that you’ve released a breaking change, you should correct the problem and restore backward compatibility in a new minor version.一旦你意识到已经发布了一个破坏性变更，你应该修正问题并在新的小版本中恢复向后兼容性。


Consider the following example.考虑以下示例。


1. You have a function called `myFunction` at version `1.0.0` which takes a single string input.你有一个名为 myFunction 的函数，版本为 1.0.0 ，它接受一个字符串输入。
2. You add a new required input to `myFunction` and accidentally release this change in a minor version release `1.1.0`.您向 myFunction 添加了一个新的必需输入，并在次要版本发布 1.1.0 中意外发布了此更改。


To remediate this, you can revert the breaking change to the signature (that is, remove the new required input you added in `1.1.0`) and release this change in version `1.2.0`.为解决这个问题，您可以回滚破坏性更改到签名（即移除您在 1.1.0 中添加的新必需输入），并在版本 1.2.0 中发布此更改。


### [](#checking-backward-compatibility-when-a-release-fails-or-has-not-yet-been-published)Checking backward compatibility when a release fails or has not yet been published在发布失败或尚未发布时检查向后兼容性


In the case of TypeScript or Python functions, your functions may fail or take a few minutes to publish. In either of these cases, the built-in backward compatibility checks will be unable to run. If you want to see the results of these checks before making a new release, you have the following options:对于 TypeScript 或 Python 函数，您的函数可能会失败或需要几分钟才能发布。在这两种情况下，内置的向后兼容性检查将无法运行。如果您希望在发布新版本之前查看这些检查的结果，您有以下选项：


- If the last release failed, you should use the “custom tag” option to compare against the last successful tag.如果最后一次发布失败，你应该使用“自定义标签”选项来与最后一个成功的标签进行比较。
- If the last release has not been published yet, you should wait for it to finish.如果最后一个发布尚未完成，你应该等待它结束。

