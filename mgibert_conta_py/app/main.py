from fastapi import FastAPI

from mgibert_conta_py.app.periods.adapters.http import period_controller
from mgibert_conta_py.app.projects.adapters.http import project_controller

app = FastAPI()


app.include_router(period_controller.router)
app.include_router(project_controller.router)
