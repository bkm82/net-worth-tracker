import os

from dynaconf import Dynaconf

HERE = os.path.dirname(os.path.abspath(__file__))

settings = Dynaconf(
    envvar_prefix="net_worth_tracker",
    preload=[os.path.join(HERE, "default.toml")],
    settings_files=["settings.toml", ".secrets.toml"],
    environments=["development", "production", "testing"],
    env_switcher="net_worth_tracker_env",
    load_dotenv=False,
)


"""
# How to use this application settings

```
from net_worth_tracker.config import settings
```

## Acessing variables

```
settings.get("SECRET_KEY", default="sdnfjbnfsdf")
settings["SECRET_KEY"]
settings.SECRET_KEY
settings.db.uri
settings["db"]["uri"]
settings["db.uri"]
settings.DB__uri
```

## Modifying variables

### On files

settings.toml
```
[development]
KEY=value
```

### As environment variables
```
export net_worth_tracker_KEY=value
export net_worth_tracker_KEY="@int 42"
export net_worth_tracker_KEY="@jinja {{ this.db.uri }}"
export net_worth_tracker_DB__uri="@jinja {{ this.db.uri | replace('db', 'data') }}"
```

### Switching environments
```
net_worth_tracker_ENV=production net_worth_tracker run
```

Read more on https://dynaconf.com
"""
