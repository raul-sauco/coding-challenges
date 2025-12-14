-- .nvim.lua
local dap = require("dap")

dap.configurations.rust = {
    {
        name = "Debug test part_one (bin 07)",
        type = "codelldb",
        request = "launch",
        program = vim.fn.getcwd() .. "/target/debug/07",
        args = { "compute_next_state", "--nocapture" },
        cwd = vim.fn.getcwd(),
    },
}
