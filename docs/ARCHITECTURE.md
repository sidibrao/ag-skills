# Production Distribution

`ag-skills` is the immutable approved source for the runtime skill catalog. Agents
receive only role-assigned skills. They discover metadata first and load full
instructions only when selected.

Skills call stable, namespaced capabilities through the centralized MCP service.
They do not contain MCP implementations or credentials. OpenBao supplies scoped
runtime secrets, and the coordinator records skill version, tool calls, approvals,
results, duration, and cost.
