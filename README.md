# tree-sitter-mojo

This project provides a [Tree-sitter](https://tree-sitter.github.io/tree-sitter/) grammar for the Mojo programming language. It is based on the grammar for Python, reflecting the similar syntax structures between Python and Mojo.

## Project Overview

The Mojo programming language shares a syntax that is nearly identical to Python. To accommodate the specifics of Mojo while leveraging existing robust solutions, this Tree-sitter grammar is derived from the official [tree-sitter-python](https://github.com/tree-sitter/tree-sitter-python) repository. Necessary modifications to the Python grammar to support Mojo-specific elements are integrated automatically on a weekly basis through GitHub Actions.

### Automation with GitHub Actions

The primary customization in this project resides in a single GitHub Actions workflow: [`tree_sitter_maker.yml`](.github/workflows/tree_sitter_maker.yml). This workflow is responsible for periodically updating the Tree-sitter grammar to adapt any changes from the Python grammar and apply Mojo-specific adjustments.

The updated grammar files are automatically generated and maintained through this automated process, ensuring that the Tree-sitter grammar for Mojo is always up-to-date with the latest syntactical standards of both Python and Mojo.

### Adding Mojo-Specific Keywords

You can add Mojo-specific keywords like `fn` to the grammar by including them in the `env:` section of the [`tree_sitter_maker.yml`](.github/workflows/tree_sitter_maker.yml). This allows for easy customization and expansion of the grammar to fit the evolving needs of the Mojo language.

## Setting Up Helix for Mojo

To use this Tree-sitter grammar with the Helix editor, follow the setup instructions below:

### 1. Configure Helix

First, create a `languages.toml` configuration file in your Helix setup located at `~/.config/helix`:

```toml
use-grammars = { only = [ "mojo" ] }

[language-server]
mojo = { command = "mojo-lsp-server" }

[[language]]
name = "mojo"
scope = "source.mojo"
roots = []
injection-regex = "mojo"
file-types = ["mojo", "🔥"]
comment-token = "#"
indent = { tab-width = 4, unit = "    " }
language-servers = [ "mojo" ]

[[grammar]]
name = "mojo"
source = { git = "https://github.com/garam-kim1/tree-sitter-mojo", rev = "2c069b8ee60641deaacd2f6a75d35e874faf79d9" }
```

### 2. Install the Grammar

After configuring, fetch, and build the grammar using the following commands in the Helix terminal:

```bash
hx --grammar fetch
cd ~/.config/helix
mkdir -p runtime/queries/mojo/
cp -r runtime/grammars/sources/mojo/runtime/queries/mojo/* runtime/queries/mojo/
hx --grammar build
```

These steps will integrate the Mojo language support into Helix, enabling syntax highlighting and other language-specific features.
