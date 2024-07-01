# Commands

You will often interact with `Zentra` using its command-line interface (CLI). This chapter documents all the available commands `Zentra` has to offer.

!!! note
    All commands are configured with a `--help` flag that provides you with extra information about them. Simply add it to the command to read more information about it. For example:

    ```shell title=""
    zentra init --help
    ```

## Error Messages

We've designed the CLI to provide useful feedback when an `error` occurs. Our aim with `Zentra` is to allow users to focus on programming there project with minimal interference.

As such, our error messages will help you quickly fix issues yourself (if possible). We explain more about them in our [Error Handling Guide](../help/errors.md).

We encourage you to check this out when the time is right!

## Global Options

This section contains a list of flags that are applicable to every command.

- `--help` - displays help information

## zentra init

??? info "Noteworthy Features"

    - First use: configures the directory as a `Zentra` project
    - Additional uses: adds missing configuration files to the `zentra` directory

This command initialises the current directory as a `Zentra` project, configuring it with specific files required for using `Zentra`.

```shell title=""
zentra init
```

This requires confirmation to initialise the application and is the recommended approach to running the command.

### Init: Optional Flags

!!! warning
    When using `--reset-config` all its content is reset back to the default template. You will lose your existing content inside of it.

| Flag             | Description |
|------------------|-------------|
|`--force`         | removes confirmation requirement |
| `--reset-config` | hard resets the `zentra/models/__init__.py` file |

You can read more about the [`zentra init`](#zentra-init) command in our [Basic Usage Guide](basic_usage.md#creating-a-project).

## zentra generate

??? info "Noteworthy Features"

    - Manages all files in the `zentra/build` folder
    - Builds, updates, and removes `React` components dynamically

This is the main command you will run when using `Zentra`. It creates and updates your `React` components by reading the information in the `Zentra` app.

```shell title=""
zentra generate
```

You can read more about it in our [Basic Usage Guide](basic_usage.md#generating-components).
