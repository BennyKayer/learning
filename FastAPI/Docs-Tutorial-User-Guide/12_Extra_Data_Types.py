"""https://fastapi.tiangolo.com/tutorial/extra-data-types/
this one has a list of various data types in a reference manner
"""
# Builtins
from datetime import datetime, time, timedelta
from typing import Optional
from uuid import UUID

# Third party
from fastapi import Body, FastAPI

app = FastAPI()


@app.put("/items/{item_id}")
async def read_items(
    item_id: UUID,
    start_datetime: Optional[datetime] = Body(None),
    end_datetime: Optional[datetime] = Body(None),
    repeat_at: Optional[time] = Body(None),
    process_after: timedelta = Body(...),
):
    """Demonstrates some Extra data types"""
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }
