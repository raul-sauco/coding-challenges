-- Nice utiliiy to copy the name and URL from a problem.

vim.keymap.set("n", "<leader>cl", function()
	vim.fn.setreg("n", vim.fn.getline(1):sub(4))
	vim.fn.setreg("u", vim.fn.getline(4):sub(4))
	print("Copied name to 'n' and URL to 'u'")
end, { desc = "[C]opy [L]eetcode Data" })

-- vim: ts=2 sts=2 sw=2 et
