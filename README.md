
# pnp_datetime
Simplified datetime functions for Plug and Play. 

## Repository structure
    pnp_datetime
    ├── LICENSE
    ├── pnp_datetime
    │   ├── __init__.py
    │   └── pnp_datetime.py
    ├── README.md
    └── test
        ├── __init__.py
        └── test_pnp_datetime.py

## Functions
> All methods return time default with timezone

* current_month_begin_time_of_tz(cls, pi_timezone:str) -> datetime
* datetime_minus_months(cls, pi_datetime:datetime, pi_months:int) -> datetime
* datetime_minus(cls, pi_datetime:datetime, **kwargs) -> datetime
* datetime_plus_months(cls, pi_datetime:datetime, pi_months:int) -> datetime
* datetime_plus(cls, pi_datetime:datetime, **kwargs) -> datetime
* datetime_to_str(cls, pi_datetime:datetime, out_format="ISO8601", sep="T") -> str
* is_local_daylight_saving(cls) -> bool
* local_current_month_begin_time(cls) -> datetime
* local_now(cls) -> datetime
* local_timezone_offset_seconds(cls)
* now_of_tz(cls, pi_timezone:str) -> datetime
* pytz_timezones(cls) -> list
* str_to_datetime(cls, pi_str_datetime:str) -> datetime
* utcnow(cls) -> datetime

## Automation Testing
	$ cd pnp_datetime
	$ python -m unittest -v
