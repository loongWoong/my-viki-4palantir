# [](#action-monitoring)Action monitoring动作监控


Actions in Foundry can be monitored to track performance and reliability. This page explains the available monitoring capabilities for actions.在 Foundry 中可以监控动作以跟踪性能和可靠性。本页面解释了可用的动作监控功能。


## [](#available-monitoring-rules)Available monitoring rules可用的监控规则


Action monitoring in Foundry supports two key rule types:Foundry 中的动作监控支持两种关键规则类型：


1. **Action duration p95:** Alerts when the 95th percentile execution time exceeds thresholds.动作持续时间 p95：当 95 百分位执行时间超过阈值时发出警报。
2. **Number of action failures in window:** Alerts when failure count exceeds thresholds within a timeframe.窗口内的动作失败次数：当在特定时间段内失败计数超过阈值时发出警报。


For detailed configuration options and parameters, review our [monitoring rules reference documentation.](/docs/foundry/monitoring-views/rules-reference/#action-rules).有关详细的配置选项和参数，请查阅我们的监控规则参考文档。


## [](#set-up-action-monitoring)Set up action monitoring设置动作监控


To set up monitoring for your actions, follow the standard process for creating monitoring views and rules:要为您的操作设置监控，请遵循创建监控视图和规则的标准流程：


1. Create a monitoring view as described in the [monitoring views overview documentation](/docs/foundry/monitoring-views/overview/#create-a-new-monitoring-view).按照监控视图概述文档中的说明创建一个监控视图。
2. Add a monitoring rule for an action or action type as described in the section on [adding a monitoring rule](/docs/foundry/monitoring-views/overview/#add-a-monitoring-rule).按照添加监控规则部分中的说明为操作或操作类型添加一个监控规则。
3. Configure appropriate thresholds and severity levels.配置适当的阈值和严重程度级别。
4. Set up alert notifications following the [alert subscription guide](/docs/foundry/monitoring-views/overview/#subscribe-to-alerts).按照警报订阅指南设置警报通知。


![Example monitoring alert setup](monitoring-alerts.png)


## [](#related-documentation)Related documentation相关文档


- [Monitoring rules reference监控规则参考](/docs/foundry/monitoring-views/rules-reference/#action-rules)
- [Monitoring views overview监控视图概览](/docs/foundry/monitoring-views/overview/)

