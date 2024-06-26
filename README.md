**Overview** / [Setup](https://github.com/YumYummity/Guilded-Bot-Template/wiki/Setup) / [Cogs](https://github.com/YumYummity/Guilded-Bot-Template/wiki/Cogs) / [Logging](https://github.com/YumYummity/Guilded-Bot-Template/wiki/Logging) / [Examples](https://github.com/YumYummity/Guilded-Bot-Template/wiki/Examples)

# Guilded Bot Template
This is a Guilded bot template for Python.

> [!NOTE]
> If you are here for the provided example code, please see [Examples](https://github.com/YumYummity/Guilded-Bot-Template/wiki/Examples)
>
> Current Examples:
> - Command: Starting a User Info
> - Function: Fetching Channels from a Server

There is a good template here for `guilded.js` users: https://github.com/Rednexie/guilded-template

This template includes:
- Basic help command
- Cogs
- Developer commands
    - Eval/Exec
    - Cog load/reload/unload
- Advanced logging and error handling
    - Errors logging (when an error (traceback) occurs, it'll save to a txt file and tell the user the error ID)
    - Permission missing error handling (when a permission is missing, it'll tell the user exactly what permissions are missing)
- Config file
- Replies on ping
- Status changing in `tasks.py` cog
- Join/leave logging, join message
- Examples of commands, functions, and more!

> [!IMPORTANT]  
> This template uses the **experimental event style** provided by `guilded.py`.
> 
> As of 2024/02/08, `guilded.py`'s current master branch has deprecated the `experimental_event_style=True` and replaced it with `guilded.ClientFeatures(experimental_event_style=True)`. If you are using `guilded.py` from github (and not pypi), please use the commented code inside `main.py` at line 165 (and remove `experimental_event_style=True`)
>
> As of `guilded.py >= 1.13`, `experimental_event_style=True` has been deprecated and replaced. The code has been updated to include these changes.
> 
> An `on_message` event looks like this without it:
> ```python
> @bot.event
> async def on_message(message: guilded.ChatMessage):
>     message.content # do things with message
>     message.server_id # message's server id
>     message.server.name # message's server name
> ```
> An `on_message` event with experimental event style looks like this:
> ```python
> async def on_message(event: guilded.MessageEvent):
>     event.message.content # do things with message
>     event.server_id or event.message.server_id # event's server id
>     event.server.name or event.message.server.name # event's server name
> ```

### Final Comments
For more information, please see the jump links at the top of this README. (Please read Setup and Logging if you are familiar with Cogs, but if you aren't, you can read that as well.)

If you are having trouble with any of these steps (or understanding most of the code), `guilded.py` may be too advanced for you. Consider learning some more Python first.

For questions about `guilded.py`, consider reading https://guildedpy.readthedocs.io/ and asking questions in the official `guilded.py` support server https://guilded.gg/gpy.

If you have questions/feedback about this template (or something specific to this template), feel free to DM me on Guilded (I won't accept friend requests, but I respond to DMs). Please check the included information. Please use the issues tab for issues including errors, wrong information and suggestions.
