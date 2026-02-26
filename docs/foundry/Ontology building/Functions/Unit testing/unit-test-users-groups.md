# [](#mock-users-and-groups)Mock users and groups模拟用户和组


### [](#user-mocks)User mocks用户模拟


You are able to create partial mock of a user using `createUser`, where all properties besides `id` and `username` are optional. You need to import `{ createUser }` from `"@foundry/functions-testing-lib"`.您可以使用 createUser 创建用户的部分模拟，其中 id 和 username 之外的所有属性都是可选的。您需要从 "@foundry/functions-testing-lib" 导入 { createUser } 。


```
Copied!`1import { MyFunctions } from ".."
2
3import { verifyOntologyEditFunction, createGroup, createUser } from "@foundry/functions-testing-lib";
4
5describe("example test suite", () => {
6    const myFunctions = new MyFunctions();
7    test("test users and groups", async () => {
8        const group = createGroup({
9            id: "groupId",
10        });
11        const user = createUser({
12            id: "userId",
13            username: "username",
14        });
15        await expect(myFunctions.searchUsers("userId", "groupId")).resolves.toEqual([user, group]);
16    });
17});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Users, Group, Principal } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public async searchUsers(userId: string, groupId: string): Promise<Principal[]> {
6        const existingPrincipals = await Promise.all([
7            Users.getUserByIdAsync(userId),
8            Users.getGroupByIdAsync(groupId),
9        ]);
10        return existingPrincipals.filter(r => !!r).map(r => r!);
11    }
12}`
```


### [](#group-mocks)Group mocks组模拟


You are also able to create partial mock of a group using `createGroup`, where all properties besides `id` are optional. You need to import `{ createGroup }` from `"@foundry/functions-testing-lib"`.您还可以使用 createGroup 创建一个组的部分模拟，其中除了 id 之外的所有属性都是可选的。您需要从 "@foundry/functions-testing-lib" 导入 { createGroup } 。


```
Copied!`1import { MyFunctions } from ".."
2
3import { verifyOntologyEditFunction, createGroup } from "@foundry/functions-testing-lib";
4
5describe("example test suite", () => {
6    const myFunctions = new MyFunctions();
7    test("test groups", async () => {
8        const group = createGroup({
9            id: "groupId",
10        });
11        await expect(myFunctions.searchGroups("groupId")).resolves.toEqual([group]);
12    });
13});`
```


This can be used to test the following function:这可以用来测试以下功能：


```
Copied!`1import { Function, OntologyEditFunction, Users, Group, Principal } from "@foundry/functions-api";
2
3export class MyFunctions {
4    @Function()
5    public async searchGroups(groupId: string): Promise<Principal[]> {
6        const existingPrincipals = await Promise.all([
7            Users.getGroupByIdAsync(groupId),
8        ]);
9        return existingPrincipals.filter(r => !!r).map(r => r!);
10    }
11}`
```

