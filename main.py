import subprocess
import uuid
from pathlib import Path
from typing import Annotated

from fastapi import FastAPI, File
from fastapi.responses import PlainTextResponse


def lifespan(_):
    Path("/tmp/illuasion").mkdir(exist_ok=True)
    yield


app = FastAPI(lifespan=lifespan)


@app.post("/", response_class=PlainTextResponse)
def decompile(bytecode: Annotated[bytes, File()]) -> str:
    file = Path(f"/tmp/illuasion/{uuid.uuid4()}.luac")

    with file.open("wb") as f:
        f.write(bytecode)

    decompiler = subprocess.run(
        ["java", "-jar", "unluac.jar", file.absolute()],
        capture_output=True,
    )

    file.unlink()

    return decompiler.stdout.decode("utf-8")
