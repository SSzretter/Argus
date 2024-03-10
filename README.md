<div style="text-align: center;">
<img src="resources/images/Argus Badge.png" alt="drawing" style="width:100%;"/>
</div>

<br>

<b>Disclaimer: Project <u>Not Maintained</u></b>

Setting up this bot is easy. Invite the bot account to your server first. Then keep note of the guild `id`.
Make sure the server is empty and has the community option enabled. You also have to give the bot admin and the highest role in the server (if you invited the bot with admin permission, drag the role to the top).

Finally make sure you set a rules channel named "rules" and a community updates channel called "community-updates".

Now we can truly begin.

First you have to create a `config.toml` in the root directory of this repository like this:

```toml
[bot]

# Bot Token
token = "OaA2MfMzMsgzMTg3MDA5YRE2.trjisg.sI0ds5dX3abh5acbqkLJUQOjseo"

# Whether you want to see more verbose logs.
debug = false

# When you'r ready to release.
# Logs will be larger and last longer in production.
production = true

[logs]

# Default Logging Level
level = "INFO"

# Sentry DSN
sentry = "https://5636365a78d3344a9b0445536b792440447a@o141345.ingest.sentry.io/4747464"


[database]

# This bot requires a URI from a MongoDB you set up.
uri = "mongodb+srv://argus:password123@argus-alpha.abcd.mongodb.net/argus?retryWrites=true&w=majority"

# Name of the database.
name = "argus"

[global]

# Name of the bot you want rendered.
name = "Argus"

# The Discord Snowflake for the guild the bot is in.
guild_id = 729148350156134416
```

Once this is done you can easily start this bot by installing the project locally using `pip`.

```bash
pip install -e .
```

To start the bot simply enter this:

```bash
argus
```

Sync commands to the server by sending this in any channel:

```
$sync
```

Finally initialize the server by doing:

```
/setup roles
/setup channels
```

If you server is Level 2 boosted then also do:

```
/setup icons
```

Once the channels, roles and icons are set up, you can enable the debating module with this command:

```
/global enable
```

The rest of the commands are self-explanatory, but you can find the [user manual here](https://wiki.opendebates.net/en/argus/manual).


---

WORK IN PROGRESS (DRAFT v1):

# in discord, create a new channel for this (left side of discord app, all the way down click plus button - community)
#  DO NOT DO THIS -- I believe when you create the community it will create these channels for you : create two public text channels: rules and community-updates
#  make sure you have 2fa enabled in discord!  (important) - settings, my account, enable authenticator app
#  enable developer mode in discord - go to settings (bottom) , advanced, turn on developer mode
#  go to server settings and enable community - get started - do let it create the rules and community updates channels 
# windows install
#  check add/remove programs, remove any versions of python other than 3.11.x
#  download and install python (3.11.8) 64bit (add to path/set enviornment variables if asked)  https://www.python.org/downloads/release/python-3118/  (do not install anything newer than 3.11.x)
#  install github desktop (or similar) ,  https://github.com/vivekjoshy/Argus   , clone (can use the green code button - open with github desktop)
#  open cmd as administrator, run pip install -e . in the Argus root directory , this will install the python dependencies
#  create config.toml in root of Argus folder, paste contents from readme.md  (it should be in the same directory as pyproject.toml)
#   go to: https://discordapp.com/developers/applications/ , create application , bot, create or reset - copy token replace value in config.toml
#      also in the bot settings page, enable presence, server members, message content intents and save
#   go to: sentry.io , sign in/create account, get started, python platform, configure sdk, skip framework, follow instructions on screen to install and copy / paste the url into sentry = in config.toml
#   go to: mongodb.com , start free, sign up, it will redirect to cloud.mongodb.com to finish the mongodb atlas signup process, select M0 (free) tier, (not sure if provider matters I used AWS), type a cluster name, create
#    at the next screen create a username/password
#    ??  connect from - I used my local enviornment and it automatically added my internet connection ip - not sure if cloud enviornment is a better choice or will work yet
#    finish / close , on overview screen click get connection string button
#    driver = python,  version = 3.11 or later, follow the on screen steps (run the install your driver command)
#    copy/paste the mongodb+srv url into the uri = in config.toml  (replace <password> with your actual password)
#  to get the guild_id, right click the server name at the top and choose 'copy id' and paste that into config.toml guild_id = 
# invite the bot - go to https://discordapp.com/developers/applications/ again , your application created earlier, oauth2 on left, use the oauth2 url generator - check 'bot', then 'administrator'
#  (you should be logged into discord in your browser as server owner) - go to the url you just generated and add the bot to the server (the bot should show as offline in the list of members)
#  DO NOT DO THIS ?? (the bot should appear as a role)  -- make sure the bot is an admin - go to server settings, roles, add a role for 'admin' and turn on Administrator permission and add the bot to manage members
#   I had issues with permissions when running the setup roles command and you have to also go to server settings - roles and drag the role named after the bot up above any other role so its at the top
# type argus in the argus to run the bot
# if it runs successfully and shows logged in and no 'errors' continue:
#  in discord in rules channel created by the community creation process type:
#   $sync
#   /setup roles      (and lots of roles should populate in your discord server settings - roles)
#   /setup channels   (and you will see the channels being configured on the left)
#  for level 2 boosted servers:  /setup icons
#   /global enable


# COMMANDS - you can type "/" in chat and press tab to see available commands


# SENTRY ERRORS - if sentry is configured and working errors will be sent there as well as to your email if configured that way
# DATABASE - view your data at cloud.mongodb.com


# one problem I ran into and resolved-
# run argus, produces error
    >argus
    pydantic.errors.PydanticImportError: `pydantic.datetime_parse:parse_datetime` has been removed in V2.
# poetry.lock refers to version 1.10.6 but reqs.txt is version 2.6.3 - chaning it to 1.10.6 , ran pip uninstall pydantic , then ran pip install pydantic==1.10.6, then re-run pip install -e .


# note: I was able to use vscode to run __main__.py , enabled the python debugger extension, edit debug configuration and add a second configuration block in launch.json , add these lines
# "request": "launch",
# "purpose": ["debug-test"],
# "justMyCode": false,
# "subProcess": true,
#
#  hint: in def main() you can add async.io around the bot.run line then you can step into it:  asyncio.run(bot.run(config["bot"]["token"], log_handler=None))

#  if you are having issues with pip commands, reboot then try removing these directories: (paths may be different on your system)
#    C:\Users\yourusername\AppData\Local\pip\cache
#    C:\Users\yourusername\AppData\Local\Temp
#    then run: pip freeze > reqs.txt   ,   pip uninstall -y -r reqs.txt
#    then run the pipinstall -e . and also run the mongodb and sentry pip installs


TODO:
 MANUAL - commands, use
 better error checking / trapping for invalid command parameters
