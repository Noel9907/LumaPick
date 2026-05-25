from fastapi import APIRouter
from services.album import home
router = APIRouter()

router.add_api_route("/",home,methods=['GET'])
