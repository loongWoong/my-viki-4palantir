# [](#configure-notifications)Configure notifications配置通知


Functions can be used to flexibly configure notifications that should be sent in the platform, including notifications that are sent externally to a user's email address.函数可用于灵活配置平台中应发送的通知，包括发送到用户电子邮件地址的外部通知。


Configuring a notification in a function makes use of the `Principal` (representing a `User` or `Group`) and `notification` types. These references may be useful while working through this section:在函数中配置通知会使用 Principal （代表 User 或 Group ）和 notification 类型。在处理本节内容时，这些引用可能很有用：


- Reference for [Principal, User, and Group types](/docs/foundry/functions/types-reference/#users-groups-and-principals)Principal、用户和组类型的参考
- Reference for [notification types](/docs/foundry/functions/types-reference/#notification)通知类型的参考


### [](#define-a-custom-notification)Define a custom notification定义自定义通知


Suppose that the ontology includes an `Issue` object that can be assigned to a `User`. You can create a function that defines the notification that should be sent to the given `User` with details about the `Issue`.假设本体包括一个可分配给 User 的 Issue 对象。您可以创建一个函数，该函数定义应发送给给定 User 的通知，其中包含关于 Issue 的详细信息。


TypeScript v1TypeScript v2Python```
Copied!`1import { EmailNotificationContent, Function, Notification, ShortNotification, User } from "@foundry/functions-api";
2import { Issue } from "@foundry/ontology-api";
3
4export class NotificationFunctions {
5    @Function()
6    public createIssueNotification(issue: Issue, user: User): Notification {
7        // Create a short notification that will be shown within the platform
8        const shortNotification = ShortNotification.builder()
9            .heading("New issue")
10            .content("A new issue has been assigned to you.")
11            // Link to the Issue object in the platform
12            .addObjectLink("Issue", issue)
13            .build();
14
15        // Define the email body. The email body may contain headless HTML, such as tables of data
16        // Note that you can access properties of both the user and the issue in the content
17        const emailBody = `Hello, ${user.firstName},
18
19A new issue has been assigned to you: ${issue.description}.`;
20
21        const emailNotificationContent = EmailNotificationContent.builder()
22            .subject("New issue")
23            .body(emailBody)
24            .addObjectLink("Issue", issue)
25            .build();
26
27        return Notification.builder()
28            .shortNotification(shortNotification)
29            .emailNotificationContent(emailNotificationContent)
30            .build();
31    }
32}`
```

```
Copied!`1import { NotificationLink, Notification, User } from "@osdk/functions";
2import { Issue } from "@ontology/sdk";
3import { type Osdk } from "@osdk/client";
4
5export default function createIssueNotification(issue: Osdk.Instance<Issue>): Notification {
6    // Link to the Issue object in the platform
7    const links: NotificationLink[] = [
8        {
9            label: "Issue",
10            linkTarget: {
11                type: "object",
12                object: issue
13            }
14        }
15    ]
16
17    const platformNotification = {
18        heading: "New issue",
19        content: "A new issue has been assigned to you.",
20        links: links
21    }
22
23    // Define the email body. The email body may contain headless HTML, such as tables of data
24    const emailBody = `Hello,
25
26A new issue has been assigned to you: ${issue.description}.`;
27
28    const emailNotification = {
29        subject: "New issue",
30        body: emailBody,
31        links: links
32    }
33
34    return {
35        platformNotification: platformNotification,
36        emailNotification: emailNotification
37    }
38}`
```

```
Copied!`1from functions.api import function, Notification, PlatformNotification, ShortNotification, NotificationLink, User
2from ontology_sdk.ontology.objects import Issue
3
4@function()
5def createIssueNotification(issue: Issue) -> Notification[Issue]:
6# If configuring a notification with an object link, you must declare the object type as part of the return type
7
8    # Link to the Issue object in the platform
9    links = [
10        NotificationObjectLink(label="Issue", objectTarget=issue)
11    ]
12
13    #Create a short notification that will be shown within the platform
14    platform_notification = PlatformNotification(
15        heading="New issue",
16        content="A new issue has been assigned to you.",
17        links=links
18    )
19
20    # Define the email body. The email body may contain headless HTML, such as tables of data
21    emailBody = f"Hello, \n A new issue has been assigned to you: {issue.description}."
22
23    email_notification = EmailNotification(
24            subject="New issue",
25            body=emailBody,
26            links=links
27        )
28
29    return Notification(platform_notification, email_notification)`
```


### [](#retrieve-users-and-groups)Retrieve users and groups检索用户和组


In addition to having a `User` passed into the function, you may retrieve a `User` or `Group` on demand. Suppose that the `Issue` object has an `assignee` field that contains a user ID. In the example below, the function returns a notification that reminds the user about the issue:除了在函数中传入 User 之外，您还可以按需检索 User 或 Group 。假设 Issue 对象有一个 assignee 字段，其中包含用户 ID。在下面的示例中，函数返回一条提醒用户注意问题的通知：


TypeScript v1TypeScript v2Python```
Copied!`1import { EmailNotificationContent, Function, Notification, ShortNotification, User, Users } from "@foundry/functions-api";
2import { Issue } from "@foundry/ontology-api";
3
4export class NotificationFunctions {
5    @Function()
6    public async createIssueReminderNotification(issue: Issue): Promise<Notification> {
7        if (!issue.assignee) {
8            throw new UserFacingError("Cannot create notification for issue without an assignee.");
9        }
10
11        const user = await Users.getUserByIdAsync(issue.assignee);
12
13        const emailBody = `Hello, ${user.firstName},
14
15This is a reminder to investigate the following issue: ${issue.description}`.
16
17        // You can also use this structure to build the entire notification inline
18        return Notification.builder()
19            .shortNotification(ShortNotification.builder()
20                .heading("Issue reminder")
21                .content("Investigate this issue.")
22                .addObjectLink("Issue", issue)
23                .build())
24            .emailNotificationContent(EmailNotificationContent.builder()
25                .subject("New issue")
26                .body(emailBody)
27                .addObjectLink("Issue", issue)
28                .build())
29            .build();
30    }
31}`
```

```
Copied!`1import { Users } from "@osdk/foundry.admin";
2import { Issue } from "ontology_sdk";
3import { Client } from "@osdk/client";
4
5export default async function createIssueReminderNotification(client: Client, issue: Issue): Promise<Notification> {
6    const user = await Users.get(client, issue.assignee);
7
8    const emailBody = `Hello, ${user.firstName},
9
10This is a reminder to investigate the following issue: ${issue.description}`.
11
12    // You can also use this structure to build the entire notification inline
13    const links: NotificationLink[] = [
14        {
15            label: "Issue",
16            linkTarget: {
17                type: "object",
18                object: issue
19            }
20        }
21    ]
22
23    // You can also use this structure to build the entire notification inline
24    return {
25        shortNotification: {
26            heading: "Issue reminder",
27            content: "Investigate this issue.",
28            links:  links
29        }
30        emailNotification: {
31            subject: "New issue",
32            body: emailBody,
33            links: links
34        }
35    }
36}`
```

```
Copied!`1from functions.api import function, Notification, PlatformNotification, ShortNotification, NotificationLink
2from ontology_sdk.ontology.objects import Issue
3from foundry_sdk import FoundryClient
4import foundry_sdk
5
6@function()
7def createIssueReminderNotification(client: Client, issue: Issue) -> Notification:
8    client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
9
10    user = client.admin.User.get(user_id)
11
12    emailBody = f"Hello, {user.firstName}, \n A new issue has been assigned to you: {issue.description}."
13
14    # Link to the Issue object in the platform
15    links = [
16        NotificationObjectLink(label="Issue", objectTarget=issue)
17    ]
18
19    #Create a short notification that will be shown within the platform
20    platform_notification = PlatformNotification(
21        subject="New issue",
22        body="A new issue has been assigned to you.",
23        links=links
24    )
25
26    # Define the email body. The email body may contain headless HTML, such as tables of data
27    # Note that you can access properties of both the user and the issue in the content
28    emailBody = f"Hello, {user.firstName}, \n A new issue has been assigned to you: {issue.description}."
29
30    email_notification = EmailNotification(
31            subject="New issue",
32            body=emailbody,
33            links=links
34        )
35
36    return Notification(platform_notification, email_notification)`
```


### [](#return-recipients)Return recipients返回接收者


The `Notification` API documented above allows you to return custom notification content. Another way you can use functions to configure notifications is by returning a list of recipients for the notification. To do so, create a function that returns one or more `Principal` objects, such as `User` or `Group` objects.上述文档中提到的 Notification API 允许您返回自定义通知内容。另一种使用函数配置通知的方式是返回通知的接收者列表。为此，创建一个返回一个或多个 Principal 对象的函数，例如 User 或 Group 对象。


In the example below, the function returns both the user who reported the issue and the user who is currently assigned to the issue:在下面的示例中，该函数返回了报告问题的用户和当前分配给问题的用户：


TypeScript v1TypeScript v2Python```
Copied!`1import { Function, User, Users } from "@foundry/functions-api";
2import { Issue } from "@foundry/ontology-api";
3
4export class NotificationFunctions {
5    /**
6     * Given an Issue, returns users representing the current assignee for the Issue and the user
7     * who originally reported the issue.
8     */
9    @Function()
10    public async getIssueAssigneeAndReporter(issue: Issue): Promise<User[]> {
11        if (!issue.assignee || !issue.reporter) {
12            throw new UserFacingError("Cannot create notification for issue without an assignee or reporter.");
13        }
14
15        const user = await Users.getUserByIdAsync(issue.assignee);
16        const issueReporter = await Users.getUserByIdAsync(issue.reporter);
17
18        return [user, issueReporter];
19    }
20}`
```

```
Copied!`1import { UserId, Principal } from "@osdk/functions";
2import { Users, Groups } from "@osdk/foundry.admin";
3import { Issue } from "ontology_sdk";
4import { Client } from "@osdk/client";
5
6/**
7 * Given an Issue, returns users representing the current assignee for the Issue and the user
8 * who originally reported the issue.
9 */
10async function getIssueAssigneeAndReporter(client: Client, issue: Issue): Promise<UserId[]> {
11    const user = await Users.get(client, issue.assignee);
12    const issueReporter = await Users.get(client, issue.reporter);
13
14    return [user.id, issueReporter.id];
15}
16
17/**
18 * Given an Issue, returns the user who is the current assignee of the issue and the group that issue belongs to.
19 */
20async function getIssueAssigneeAndGroups(client: Client, issue: Issue): Promise<Principal[]> {
21    // To return both groups and users, return the Principal type.
22
23    const user = await Users.get(client, issue.assignee);
24    const group = await Groups.get(client, issue.group);
25
26    return [{type: "user", id: user.id}, {type: "group", id: group.id}];
27}`
```

```
Copied!`1from functions.api import Array, function, Principal, UserId
2from ontology_sdk.ontology.objects import Issue
3from foundry_sdk import FoundryClient
4import foundry_sdk
5
6# Given an Issue, returns users representing the current assignee for the Issue and the user
7# who originally reported the issue.
8@function()
9def getIssueAssigneeAndReporter(issue: Issue) -> Array[UserId]:
10    client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
11
12    user = client.admin.User.get(issue.assignee)
13    issueReporter = client.admin.User.get(issue.assignee)
14
15    return [user.id, issueReporter.id]
16
17# Given an Issue, returns the user who is the current assignee of the issue and the group that issue belongs to.
18@function()
19def getIssueAssigneeAndGroup(issue: Issue) -> Array[Principal]:
20    # To return both groups and users, return the Principal type.
21    client = FoundryClient(auth=foundry_sdk.UserTokenAuth(...), hostname="example.palantirfoundry.com")
22
23    user = client.admin.User.get(issue.assignee)
24    group = client.admin.Group.get(issue.group)
25
26    return [Principal.user(user.id), Principal.group(group.id)]`
```

