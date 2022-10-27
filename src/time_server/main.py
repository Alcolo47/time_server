import asyncio
from datetime import datetime
from typing import Optional

import typer
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"timestamp": datetime.now().timestamp()}


async def async_run(port: int):
    server = uvicorn.Server(uvicorn.Config(app=app, host="0.0.0.0", port=port))
    await server.serve()


def main():
    def run(port: Optional[int] = typer.Option(8123, envvar='PORT')):
        asyncio.run(async_run(port))

    typer.run(run)


if __name__ == '__main__':
    main()
