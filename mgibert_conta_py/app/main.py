from fastapi import FastAPI

from mgibert_conta_py.app.periods.adapters.http import period_controller

app = FastAPI()


app.include_router(period_controller.router)
