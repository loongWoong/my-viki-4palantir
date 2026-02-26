# [](#version-range-dependencies-for-functions)Version range dependencies for functions函数的版本范围依赖


In addition to depending on a pinned version of a Function, some applications like Workshop and Actions allow you to depend on a Function at a version range. Doing so enables automatic upgrades at runtime, which can save you time in your development cycle and provide a downtime-less upgrade experience for [deployed functions](/docs/foundry/functions/functions-deployed/).除了依赖特定版本的函数外，一些应用如 Workshop 和 Actions 允许你依赖函数的版本范围。这样做可以在运行时自动升级，从而节省你的开发周期，并为已部署的函数提供无停机升级体验。


While version range dependencies are a powerful feature, they also carry certain risks (for example, there are [permissioning consequences specific to Actions](#permissions-and-provenance-in-actions)). This documentation explains the mechanics behind version range resolution so that you can better understand these risks and make an informed decision on whether version range dependencies are suitable for your application.虽然版本范围依赖是一个强大的功能，但它也伴随着一定的风险（例如，Actions 存在特定的权限管理后果）。本文档解释了版本范围解析的机制，以便你更好地理解这些风险，并就版本范围依赖是否适合你的应用做出明智的决策。


This documentation page assumes prior knowledge on topics like backward compatibility and the Semantic Versioning system. If you are not familiar with these topics, review our documentation on [functions versioning](/docs/foundry/functions/functions-versioning/).本文档页面假设你对向后兼容性和语义版本系统等主题已有先验知识。如果你不熟悉这些主题，请查阅我们关于函数版本化的文档。

You should also be familiar with the rules around version precedence as defined in the [Semantic Versioning specification ↗](https://semver.org/#spec-item-11). In other words, you should be able to determine, given two distinct versions, which one has lower precedence. For example, `1.0.0-rc.1` < `1.0.0` < `1.0.1` < `1.1.0` < `2.0.0`.你也应该熟悉语义版本规范（Semantic Versioning）中定义的版本优先级规则 ↗。换句话说，你应该能够根据两个不同的版本确定哪一个具有较低的优先级。例如， 1.0.0-rc.1 < 1.0.0 < 1.0.1 < 1.1.0 < 2.0.0 。


## [](#version-ranges)Version ranges版本范围


In its simplest form, a version range is a collection of version inequalities, and a version is said to "satisfy" a range if it satisfies all of its inequalities. For example, version `1.2.0` satisfies the range `>=1.0.0 <2.0.0`.最简单的形式中，版本范围是一组版本不等式，一个版本如果满足其所有不等式，则被认为“满足”该范围。例如，版本 1.2.0 满足范围 >=1.0.0 <2.0.0 。


Internally, the semantics of Function version ranges are adopted from NPM, a popular package manager for the JavaScript ecosystem. Review the [NPM documentation on version ranges ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#ranges) for a rigorous definition.内部上，Function 版本范围的语义借鉴自 JavaScript 生态系统中的流行包管理器 NPM。查阅 NPM 文档中关于版本范围的严格定义 ↗。


Applications like Workshop and Actions currently only allow version ranges that comprise backward compatible versions (that is, minor or patch upgrades).像 Workshop 和 Actions 这样的应用程序目前仅允许包含向后兼容版本的范围（即次要版本或补丁升级）。


The NPM equivalent of this backward compatible range used by Workshop and Actions is the [caret range ↗](https://docs.npmjs.com/cli/v6/using-npm/semver#caret-ranges-123-025-004).Workshop 和 Actions 使用的这种向后兼容范围在 NPM 中的等效项是尖头范围 ↗。


## [](#version-range-resolution)Version range resolution版本范围解析


With the exception of deployed functions, when you depend on a Function at a version range, a concrete version that satisfies the range will be chosen at runtime during execution. In particular, the *maximum* satisfying version will be chosen on an eventual basis (it can take a few minutes to pick up new releases).除已部署的函数外，当你依赖一个版本范围的函数时，在执行期间运行时将选择一个满足该范围的特定版本。特别是，最终将选择最满足的版本（选择新版本可能需要几分钟时间）。


### [](#deployed-functions)Deployed functions部署的函数


For deployed functions, a concrete version is instead resolved to the currently deployed version, if it satisfies the range. If the deployed version does not satisfy the range, an error will be returned.对于部署的函数，如果满足版本范围，则会解析到当前部署的版本。如果部署的版本不满足版本范围，将返回错误。


## [](#risks)Risks风险


While functions developers are guided towards the Semantic Versioning specification and general best practices, it is always possible for breaks to be accidentally introduced in non-major version releases.虽然函数开发者被引导遵循语义版本规范和一般最佳实践，但在非主要版本发布中仍有可能意外引入破坏。


If your application picks up a breaking change, it can manifest in any number of problems, like runtime failures or unexpected behavior.如果您的应用程序遇到破坏性变更，可能会表现为各种问题，如运行时失败或意外行为。


Upon noticing a breaking change, you should immediately contact the developer of the Function so that they can [release a fix](/docs/foundry/functions/functions-versioning/#accidentally-releasing-a-backward-incompatible-change-as-a-patch-or-minor-version), and in the meantime, you should pin your Function dependency to the last working version.在发现破坏性变更时，您应立即联系该 Function 的开发者，以便他们发布修复程序，同时您应将您的 Function 依赖项固定到最后一个可工作的版本。


With the caveat of deployed Function dependencies, if your application has strict uptime requirements and cannot tolerate any breaks, you should use pinned version dependencies.在部署 Function 依赖项的前提下，如果您的应用程序有严格的正常运行时间要求且无法容忍任何中断，您应使用固定版本依赖项。


### [](#permissions-and-provenance-in-actions)Permissions and provenance in ActionsActions 中的权限和来源


When using Function version ranges in [Function-backed Actions](/docs/foundry/action-types/function-actions-overview/), there are important considerations around permissions and provenance that can affect Action behavior. For more information about these implications, refer to the Actions documentation on [auto upgrades](/docs/foundry/action-types/function-actions-getting-started/#auto-upgrades).在使用基于函数的 Action 中的函数版本范围时，权限和来源等重要考虑因素会影响 Action 的行为。有关这些影响的信息，请参阅 Action 文档中关于自动升级的部分。

