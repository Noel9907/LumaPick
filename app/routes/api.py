from fastapi import APIRouter
from services.album import album
from services.album import GetImage
router = APIRouter()

router.add_api_route("/album",album,methods=['GET'])
router.add_api_route("/image",GetImage,methods=['GET'])